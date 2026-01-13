names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

totals = [sum(s) for s in steps]

# Display totals
for name, total in zip(names, totals):
    print(f"{name}: {total} steps")

max_index = totals.index(max(totals))
min_index = totals.index(min(totals))

print(f"\nHighest: {names[max_index]} ({totals[max_index]} steps)")
print(f"Difference: {totals[max_index] - totals[min_index]} steps")
