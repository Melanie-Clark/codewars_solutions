/*
Choose those with tegil appearing anywhere in their first name, as they are likely to be good calligraphers, OR those with astar anywhere in their last name, who will be faithful to the role.

Elves table:

firstname
lastname
all names are in lowercase

To aid the scribes, return the firstname and lastname column concatenated, separated by a space, into a single shortlist column, and capitalise the first letter of each name.


*/

# PostgreSQL
SELECT CONCAT(INITCAP(firstname), ' ', INITCAP(lastname)) AS shortlist
FROM Elves
WHERE firstname LIKE '%tegil%' OR lastname LIKE '%astar%'