from fastapi import FastAPI, Query
from .logic import generate_recommendations
from .fpl_data import fetch_team_picks, fetch_bootstrap_data

app = FastAPI()

@app.get("/recommend")
def recommend_team(fpl_id: int = Query(...), gw: int = Query(...)):
    # Fetch player metadata
    bootstrap = fetch_bootstrap_data()
    player_map = {player["id"]: player for player in bootstrap["elements"]}

    # Fetch user picks
    picks_data = fetch_team_picks(fpl_id, gw)
    picks = picks_data["picks"]

    # Map to enriched player data
    enriched_players = []
    for pick in picks:
        player_id = pick["element"]
        player_info = player_map.get(player_id, {})
        enriched_players.append({
            "name": player_info.get("web_name", "Unknown"),
            "form": float(player_info.get("form", 0)),
            "injury_risk": 1.0 if player_info.get("status") == "i" else 0.0
        })

    # Run AI logic
    result = generate_recommendations({"players": enriched_players})
    return result