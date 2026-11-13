# Multiplication Board (1 to 20)

size = 20

# Print header row
print(f"{'×':>4}", end="")
for col in range(1, size + 1):
    print(f"{col:>5}", end="")
print()

# Print separator line
print("-" * (5 * (size + 1)))

# Print multiplication table
for row in range(1, size + 1):
    print(f"{row:>4}", end="")

    for col in range(1, size + 1):
        print(f"{row * col:>5}", end="")

    print()