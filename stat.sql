-- ✅1.Охват
-- Хороший запрос. 63 миллисекунды. 
SELECT count(DISTINCT v.user_id) uniq_users_views_current
FROM feed.views v
INNER JOIN feed.posts p on p.id = v.post_id
WHERE p.author_id = UUID_TO_BIN('828e4905-b154-4f51-ad31-1448b31a522c') 
AND v.created_at BETWEEN '2023-07-01 00:00:00'  AND '2023-08-01 00:00:00';

-- ✅ 2.1. Лайки на посты и на комменты
-- Тоже хороший запрос.  112-190 мс
with count_like_posts as (
  SELECT COUNT(l.post_id) posts_likes
  FROM feed.likes l
  INNER JOIN feed.posts p on p.id = l.post_id 
  WHERE p.author_id  = UUID_TO_BIN('94414adb-f84a-499a-b252-b3beb6c5c5cf') AND
      l.created_at BETWEEN '2023-01-01 00:00:00'  AND '2023-09-01 00:00:00'
), count_like_comments as (
  SELECT COUNT(cl.comment_id) comments_likes
  FROM feed.comment_likes cl
  INNER JOIN comments c on c.id = cl.comment_id
  WHERE c.author_id  = UUID_TO_BIN('94414adb-f84a-499a-b252-b3beb6c5c5cf') AND
      cl.created_at BETWEEN '2023-01-01 00:00:00'  AND '2023-09-01 00:00:00'
     )
SELECT (posts_likes + comments_likes) count_all_likes
FROM count_like_posts, count_like_comments;

-- ✅2.2 Комменты
-- Хороший запрос 60 мс
  SELECT COUNT(c.id) comments
  FROM feed.comments c
  INNER JOIN feed.posts p on p.id = c.post_id
  WHERE p.author_id  = UUID_TO_BIN('94414adb-f84a-499a-b252-b3beb6c5c5cf') AND
      c.created_at BETWEEN  '2023-01-01 00:00:00'  AND '2023-09-01 00:00:00';


-- ✅2.3. Подписчики
-- 60 мс, гуд
  SELECT COUNT(s.subscriber_id) subscriptions
  FROM feed.subscriptions s
  WHERE s.publisher_id  = UUID_TO_BIN('94414adb-f84a-499a-b252-b3beb6c5c5cf') AND s.created_at <= '2023-09-01 00:00:00';

-- ✅4. Просмотры профиля
-- Хороший запрос 55 мс
  SELECT COUNT(DISTINCT ug.guest_uid) as cnt
FROM auth.user_guests ug 
WHERE ug.user_uid = '94414adb-f84a-499a-b252-b3beb6c5c5cf'  AND ug.created_at BETWEEN '2023-01-01 00:00:00'  AND '2023-09-01 00:00:00'; 


-- ✅5. Новые подписчики
-- 50 мс
SELECT COUNT(e.id) as cnt 
FROM feed.events e 
INNER JOIN auth.users u on  UUID_TO_BIN(u.id) = e.profile_id
WHERE e.event_type = 2 AND e.profile_id = UUID_TO_BIN('0643e689-8ac9-4351-9545-3523322bc536') AND
    e.created_at BETWEEN '2023-01-01 00:00:00'  AND '2023-09-01 00:00:00';

-- ✅6.Отписки
-- 50 мс
SELECT COUNT(e.id) as cnt 
FROM feed.events e 
INNER JOIN auth.users u on  UUID_TO_BIN(u.id) = e.profile_id
WHERE e.event_type = 3 AND e.profile_id = UUID_TO_BIN('0643e689-8ac9-4351-9545-3523322bc536') AND
    e.created_at BETWEEN '2023-01-01 00:00:00'  AND '2023-09-01 00:00:00';
