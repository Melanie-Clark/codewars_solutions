/*
Imagine you are working for a dating app. Users of the app can "like" other users, and these interactions 
are stored in a database table called user_likes. The app's key feature is matching users when there is a mutual like, 
meaning both users have liked each other.

user_likes table has the following structure:

id (int): primary key
liker_id (int): The ID of the user who sent the like.
liked_id (int): The ID of the user who received the like.
Your task is to write a query to identify mutual likes from the user_likes table. A mutual like exists when:

User A likes User B, and
User B likes User A
Additionally, you must ensure that each pair is reported only once, regardless of the order in which the users liked each other. 
You should always assign the smaller ID to the first column and the larger ID to the second column.

Output Columns:

user1_id: The smaller ID in the pair
user2_id: The larger ID in the pair.
Output should be sorted firstly by user1_id and secondy user2_id: both in ascending order.

Notes:

Self-likes (e.g., a user liking themselves) are not logical in the context of a dating app and do not exist in the system.
It is possible to have duplicates recorded multiple times. Your query must handle this and ensure that each match is returned only once.
*/

SELECT DISTINCT(a.liker_id) AS user1_id, a.liked_id AS user2_id
FROM user_likes AS a
JOIN user_likes AS b
ON a.liker_id = b.liked_id 
AND a.liked_id = b.liker_id 
WHERE a.liker_id < a.liked_id