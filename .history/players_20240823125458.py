players = [
    {"name": "Mykhalo Mudryk", "club": "Chelsea"},
    {"name": "Dominic Solanke", "club": "Spurs"},
    {"name": "Savinho", "club": "Man City"}
]

#Lambda function
players.sort(key=lambda players:players["club"])

print(players)