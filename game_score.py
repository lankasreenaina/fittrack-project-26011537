name = input("Enter player name: ")
games = int(input("Enter games played: "))
total_score = int(input("Enter total score: "))

average = total_score / games

print(f"Player: {name}")
print(f"Games Played: {games}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average}")
