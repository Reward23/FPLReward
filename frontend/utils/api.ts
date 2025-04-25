export async function fetchTeamData(fplId: string, gameweek: number) {
  const res = await fetch(`/api/team?fplId=${fplId}&gw=${gameweek}`);
  return res.json();
}

export async function getRecommendations(teamData) {
  const res = await fetch('http://localhost:8000/recommend', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(teamData),
  });
  return res.json();
}