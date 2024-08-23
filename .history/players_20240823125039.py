players = {
    "name": "Mykhalo Mudryk", "club": "Chelsea",
    "name": "Dominic Solanke", "club": "Spurs",
    "name": "Savinho", "club": "Man City"
}

players.sort(key=lambda players:players["name"])

print(players)