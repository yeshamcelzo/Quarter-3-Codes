steps = [
    [4500, 5200, 4800, 5500, 5300],   # Yesha
    [4000, 4100, 3900, 4200, 4600],   # Jia
    [6000, 5800, 5900, 6100, 6200]    # Nicole
]

print("---- Output ----")

for i in range(len(steps)):
    total = sum(steps[i])
    average = total / len(steps[i])
    minimum = min(steps[i])
    maximum = max(steps[i])

    print(f"Friend {i+1} - Total Steps: {total} | Average: {average:.1f} | Min: {minimum} | Max: {maximum}")
