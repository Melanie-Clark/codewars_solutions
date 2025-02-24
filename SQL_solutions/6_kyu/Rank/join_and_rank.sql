/*
For this challenge you need to create a simple SELECT statement that will return all columns from the people table, and join to the sales table so that you can return the COUNT of all sales and RANK each person by their sale_count.

people table schema
id
name
sales table schema
id
people_id
sale
price
You should return all people fields as well as the sale count as "sale_count" and the rank as "sale_rank".
*/

SELECT
  p.*,
  COUNT(s.id) as sale_count,
  RANK() OVER (ORDER BY COUNT(s.id) DESC) as sale_rank
FROM people p
JOIN sales s
ON p.id = s.people_id
GROUP BY p.id