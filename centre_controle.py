#Task 1

# 1 & 2
with open("mission_data/journal_bord.txt", "r", encoding="utf-8") as f:
    total_lines = len(f.readlines())

print( f"Journal de bord : {total_lines} entrées")

# 3
