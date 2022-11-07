# Simulate a sports tournament
import random
import sys
from csv import DictReader
from typing import TypedDict

# Number of simulations to run
N = 1000


class Team(TypedDict):
    team: str
    rating: int


def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams: list[Team] = []

    # Read all the teams
    with (open(sys.argv[1], "r") as f):
        reader: DictReader[dict[str, str]] = DictReader(f)
        for team in reader:
            teams.append({"team": team["team"], "rating": int(team["rating"])})

    counts: dict[str, int] = {}

    # Simulate N tournaments and keep track of win counts
    for i in range(0, N):
        winner = simulate_tournament(teams)

        if winner not in counts:
            counts[winner] = 0

        counts[winner] += 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1: Team, team2: Team) -> bool:
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))

    return random.random() < probability


def simulate_round(teams: list[Team]) -> list[Team]:
    """Simulate a round. Return a list of winning teams."""
    winners: list[Team] = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams: list[Team]) -> str:
    """Simulate a tournament. Return name of winning team."""
    winners = teams

    while True:
        winners = simulate_round(winners)
        if len(winners) == 1:
            return winners[0]["team"]


if __name__ == "__main__":
    main()
