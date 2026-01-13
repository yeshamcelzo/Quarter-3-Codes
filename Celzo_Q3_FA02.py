steps = [
    [4500, 5200, 4800, 5000, 5300],   # Yesha
    [4000, 4100, 3900, 4200, 4600],   # Jia
    [6000, 5800, 5900, 6100, 6200]    # Nicole
]

# Names list to match row indexes
names = ["Yesha", "Jia", "Nicole"]

# Print Jia's steps on Wednesday
print("Jia's steps on Thursday:", steps[1][3])

#Print my (Yesha) steps for the whole week
print("Yesha's steps...", steps[0])

# Update my Thursday steps to 5500
print("Updating Yesha's Friday steps to 3600.")
steps[0][4] = 3600

# 4. Print updated steps
print(" updated steps:", steps[0])
