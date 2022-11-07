"""Print mario half-pyramid of a specified height"""

# Try to get the height
while True:
    height = input("Height: ")
    if height.isnumeric() and 0 < int(height) < 9:
        height = int(height)
        break

# Print the pyramid
for i in range(1, height + 1):
    print(f"{' ' * (height - i)}{'#' * i}")
