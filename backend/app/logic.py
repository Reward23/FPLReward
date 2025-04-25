def generate_recommendations(team_data):
    # Dummy logic
    captain = max(team_data["players"], key=lambda p: p["form"])
    transfers = [p for p in team_data["players"] if p["injury_risk"] > 0.5]

    return {
        "captain": captain["name"],
        "transfers": [p["name"] for p in transfers],
        "chip": "None"
    }