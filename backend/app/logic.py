def generate_recommendations(team_data):
    players = team_data["players"]

    # Captain logic: highest form among non-injured players
    healthy_players = [p for p in players if p["injury_risk"] == 0.0]
    captain = max(healthy_players, key=lambda p: p["form"], default={"name": "N/A"})

    # Transfer logic: players with low form or injury risk
    transfers = [
        p for p in players
        if p["form"] < 2.0 or p["injury_risk"] > 0.5
    ]

    # Chip logic: naive activation if 3+ injuries
    num_injured = len([p for p in players if p["injury_risk"] > 0])
    chip = "Wildcard" if num_injured >= 3 else "None"

    return {
        "captain": captain["name"],
        "transfers": [p["name"] for p in transfers],
        "chip": chip
    }