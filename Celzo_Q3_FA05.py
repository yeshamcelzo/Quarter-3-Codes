names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]


numdays = len(steps[0])


dailytotals = []


for day in range(numdays):
    total = 0
    for person in steps:
        total += person[day]
    dailytotals.append(total)
    print(f"Total steps for Day {day+1}: {total}")


max_steps = max(dailytotals)
most_active_day = dailytotals.index(max_steps) + 1
print(f"The most active day overall is Day {most_active_day} with {max_steps} steps.")
