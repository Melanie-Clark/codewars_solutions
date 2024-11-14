/*
Return name, won, and lost columns displaying the name, total number of wins and total number of losses. Group by the fighter's name.
Do not count any wins or losses where the winning move was Hadoken, Shouoken or Kikoken.
Order from most-wins to least
Return the top 6. Don't worry about ties.
*/

SELECT name, SUM(won) AS won, SUM(lost) AS lost
FROM fighters f
JOIN winning_moves w
ON f.move_id = w.id
WHERE move NOT IN('Hadoken', 'Shouoken', 'Kikoken')
GROUP BY f.name
ORDER BY SUM(won) desc
LIMIT 6;