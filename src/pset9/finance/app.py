import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure an API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    portfolio = []
    for row in db.execute("SELECT symbol, shares FROM portifolio WHERE user_id = ?", user_id):
        stock = lookup(row["symbol"])
        portfolio.append(
            {**row, "name": stock["name"], "price": stock["price"], "total": row["shares"] * stock["price"]})

    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    total = sum([p["total"] for p in portfolio]) + cash

    return render_template("portifolio/index.jinja2", portfolio=portfolio, cash=cash, total=total)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("login/login.jinja2")

    # User reached route via POST (as by submitting a form via POST)
    username = request.form.get("username")
    password = request.form.get("password")

    # Ensure username was submitted
    if not username:
        return apology("must provide username", 403)

    # Ensure password was submitted
    elif not password:
        return apology("must provide password", 403)

    # Query database for username
    rows = db.execute("SELECT * FROM users WHERE username = ?", username)

    # Ensure username exists and password is correct
    if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
        return apology("invalid username and/or password", 403)

    # Remember which user has logged in
    session["user_id"] = rows[0]["id"]

    # Redirect user to home page
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("login/register.jinja2")

    # User reached route via POST (as by submitting a form via POST)
    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")

    # Ensure username was submitted
    if not username:
        return apology("must provide username", 400)

    # Ensure password was submitted
    elif not password:
        return apology("must provide password", 400)

    # Ensure password was confirmed
    elif not confirmation:
        return apology("must confirm password", 400)

    # Ensure password and confirmation match
    elif password != confirmation:
        return apology("passwords do not match", 400)

    # Query database for username
    rows = db.execute("SELECT * FROM users WHERE username = ?", username)

    # Ensure username does not exist
    if len(rows) == 1:
        return apology("username already exists", 400)

    # Insert new user into database
    db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username,
               generate_password_hash(password))

    # Redirect user to home page
    return redirect("/login")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to log in a form
    return redirect("/login")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote/quote.jinja2")

    symbol = request.form.get("symbol")
    if not symbol:
        return apology("must provide symbol", 400)

    quote = lookup(symbol)
    if not quote:
        return apology("invalid symbol", 400)

    return render_template("quote/quoted.jinja2", name=quote["name"], symbol=quote["symbol"], price=quote["price"])


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("transaction/buy.jinja2")

    # Get form data
    user_id = session["user_id"]

    symbol = request.form.get("symbol").upper()
    if not symbol:
        return apology("must provide symbol", 400)

    quote = lookup(symbol)
    if not quote:
        return apology("invalid symbol", 400)

    shares = request.form.get("shares")
    if not shares:
        return apology("must provide shares", 400)

    try:
        shares = int(shares)
        assert shares > 0
    except (ValueError, AssertionError):
        return apology("invalid shares", 400)

    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
    price = quote["price"]
    total = price * shares

    if cash < total:
        return apology("insufficient funds", 400)

    try:
        db.execute("INSERT INTO portifolio (user_id, symbol, shares) VALUES(?, ?, ?)", user_id, symbol, shares)
    except ValueError:
        db.execute("UPDATE portifolio SET shares = shares + ? WHERE user_id = ? AND symbol = ?", shares, user_id,
                   symbol)

    db.execute("INSERT INTO history (user_id, symbol, shares, price) VALUES(?, ?, ?, ?)", user_id, symbol, shares,
               price)
    db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total, user_id)

    return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]

    if request.method == "GET":
        symbols = [row["symbol"] for row in db.execute("SELECT symbol FROM portifolio WHERE user_id = ?", user_id)]
        return render_template("transaction/sell.jinja2", symbols=symbols)

    symbol = request.form.get("symbol").upper()
    if not symbol:
        return apology("must provide symbol", 400)

    quote = lookup(symbol)
    if not quote:
        return apology("invalid symbol", 400)

    shares = request.form.get("shares")
    if not shares:
        return apology("must provide shares", 400)

    try:
        shares = int(shares)
        assert shares > 0
    except (ValueError, AssertionError):
        return apology("invalid shares", 400)

    portfolio = db.execute("SELECT shares FROM portifolio WHERE user_id = ? AND symbol = ?", user_id, symbol)
    if not portfolio:
        return apology("symbol not in portfolio", 400)

    portfolio_shares = portfolio[0]["shares"]
    if shares > portfolio_shares:
        return apology("insufficient shares", 400)

    price = quote["price"]
    total = price * shares

    if portfolio_shares == shares:
        db.execute("DELETE FROM portifolio WHERE user_id = ? AND symbol = ?", user_id, symbol)
    else:
        db.execute("UPDATE portifolio SET shares = shares - ? WHERE user_id = ? AND symbol = ?", shares, user_id,
                   symbol)

    db.execute("INSERT INTO history (user_id, symbol, shares, price) VALUES(?, ?, ?, ?)", user_id, symbol, -shares,
               price)
    db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total, user_id)

    return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    user_id = session["user_id"]
    row = db.execute("SELECT * FROM history WHERE user_id = ?", user_id)
    return render_template("portifolio/history.jinja2", history=row)


if __name__ == "__main__":
    app.run()
