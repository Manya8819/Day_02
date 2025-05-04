football_players = {"Alice", "Bob", "David"}
cricket_players = {"Bob", "Charlie", "Eve"}

both = football_players & cricket_players
only_one = football_players ^ cricket_players
all_students = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank"}
none = all_students - (football_players | cricket_players)

print("\nSports Participation:")
print(f"Students who play both: {both}")
print(f"Students who play only one: {only_one}")
print(f"Students who play none: {none}")
