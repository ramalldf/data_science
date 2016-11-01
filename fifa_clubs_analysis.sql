SELECT team_record.*, team_attributes.*
FROM (
SELECT team, SUM(goals_for) AS total_goals_for, SUM(goals_against) AS total_goals_against, SUM(win) AS total_wins, SUM(loss) AS total_losses, SUM(draw) AS total_draws
FROM (SELECT *,
	CASE WHEN diff <0 THEN 1 ELSE 0 END as loss, 
	CASE WHEN diff = 0 THEN 1 ELSE 0 END as draw,
	CASE WHEN diff > 0 THEN 1 ELSE 0 END as win 

FROM (SELECT date, home_team_api_id AS team, home_team_goal AS goals_for, away_team_goal AS goals_against, home_team_goal-away_team_goal AS diff 
FROM Match
UNION
SELECT date, away_team_api_id AS team, away_team_goal AS goals_for, home_team_goal AS goals_against, away_team_goal-home_team_goal AS diff 
FROM Match
ORDER BY team) 
)

GROUP BY team) team_record
JOIN team_attributes
ON team_record.team = team_attributes.team_api_id
WHERE date > 2015
ORDER BY team

