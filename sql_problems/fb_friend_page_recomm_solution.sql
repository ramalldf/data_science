--Problem: "Write a SQL query that makes recommendations using the pages that your friends liked. Assume you have two tables: a two-column table of users and their friends, and a two-column table of users and the pages they liked. It should not recommend pages you already like."

SELECT DISTINCT C.*
FROM (SELECT DISTINCT A.user AS mainUser, A.friend AS origFriend, B.page AS recommPage
		  FROM (SELECT user, friend
					FROM friends
					UNION
					SELECT friend, user
					FROM friends) A
		 JOIN pages B
		 ON origFriend = B.user ) C
ORDER BY mainUser
