
-- WHERE u.id ='9829b44c-9a2b-4f48-9eda-73b726321b10';
-- and v.created_at BETWEEN переданная_дата_начала  AND переданная_дата_конца;


-- 1. Охват
-- 
-- SELECT count(DISTINCT v.user_id) uniq_users_views_current
-- FROM feed.views v
-- INNER JOIN feed.posts p on p.id = v.post_id
-- WHERE p.author_id = UUID_TO_BIN('4b963742-99b2-494c-bdd6-d6a4176e954a') AND
-- 	  v.created_at BETWEEN переданная_дата_начала  AND переданная_дата_конца
-- 
-- 2. Вовлеченность
-- 
-- 2.1 Лайки
-- 
-- with count_like_posts as (
-- 	SELECT COUNT(l.post_id) posts_likes
-- 	FROM feed.likes l
-- 	INNER JOIN feed.posts p on p.id = l.post_id 
-- 	WHERE p.author_id  = UUID_TO_BIN(переданный_user_id) AND
-- 		  l.created_at BETWEEN переданная_дата_начала AND переданная_дата_конца
-- ), count_like_comments as (
-- 	SELECT COUNT(cl.comment_id) comments_likes
-- 	FROM feed.comment_likes cl
-- 	INNER JOIN comments c on c.id = cl.comment_id
-- 	WHERE c.author_id  = UUID_TO_BIN(переданный_user_id) AND
-- 		  cl.created_at BETWEEN переданная_дата_начала AND переданная_дата_конца
-- )
-- SELECT (posts_likes + comments_likes) count_all_likes
-- FROM count_like_posts, count_like_comments
-- 
-- 2.2 Комментарии
-- 
-- 	SELECT COUNT(c.id) comments
-- 	FROM feed.comments c
--  	INNER JOIN feed.posts p on p.id = c.post_id
-- 	WHERE p.author_id  = UUID_TO_BIN(переданный_user_id) AND
-- 		  c.created_at BETWEEN переданная_дата_начала AND переданная_дата_конца
-- 		  
-- 2.3 Подписчики
-- 
-- 	SELECT COUNT(s.subscriber_id) subscriptions
-- 	FROM feed.subscriptions s
-- 	WHERE s.publisher_id  = UUID_TO_BIN(переданный_user_id) AND s.created_at <= переданная_дата_конца


-- 5. Новые подписчики
-- 
-- SELECT COUNT(e.id)  
-- FROM feed.events e 
-- INNER JOIN feed.posts p on p.id = e.post_id 
-- WHERE e.event_type = 2 AND p.author_id = UUID_TO_BIN(переданный_id) AND
-- 	  e.created_atBETWEEN переданная_дата_начала AND переданная_дата_конца
-- 	  
-- 6. Отписки
-- 
-- SELECT COUNT(e.id)  
-- FROM feed.events e 
-- INNER JOIN feed.posts p on p.id = e.post_id 
-- WHERE e.event_type = 3 AND p.author_id = UUID_TO_BIN(переданный_id) AND
-- 	  e.created_atBETWEEN переданная_дата_начала AND переданная_дата_конца

