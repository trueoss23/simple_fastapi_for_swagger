from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from uuid import UUID


class Duration(Enum):
    DAY: str = 'day'
    WEEK: str = 'week'
    MONTH: str = 'mounth'
    YEAR: str = 'year'


class Stat(BaseModel):
    reach: int
    engagement: float
    searched: int
    views: int
    subscriptions: int
    unsubscriptions: int
    follow_link_post: int
    follow_link_profile: int


db = Stat(reach=100,
          engagement=10.3,
          searched=20,
          views=400,
          subscriptions=10,
          unsubscriptions=30,
          follow_link_post=10,
          follow_link_profile=100,)


r = APIRouter(prefix='/stat')


@r.get('/get_all/acc/{user_id}/{duration}')
async def read_all_stat_to_fix_duration(id: UUID,
                                        duration: Duration) -> Stat:
    """"This function returns statistics on a user with 'user_id'(UUID format)
      for the period day, week, month or year"""
    return db


@r.get('/get_all')
async def read_all_stat(id: UUID,
                        date_from: datetime,
                        date_to: datetime = datetime.utcnow()
                        ) -> Stat:
    """"This function returns statistics on a user with 'user_id'(UUID format)
      for the period from 'date_from' to 'date_to'"""
    return db


@r.get('/reach/acc/{user_id}/{duration}')
async def read_reach_to_fix_duration(id: UUID,
                                     duration: Duration) -> int:
    """"The function returns the number of unique users who viewed
    at least one post by user with 'user_id'(UUID format)
    for the period: day, week, month or year"""
    return db.reach


@r.get('/reach/acc/{user_id}')
async def read_reach(id: UUID,
                     date_from: datetime,
                     date_to: datetime = datetime.utcnow()) -> int:
    """"The function returns the number of unique users who viewed
    at least one post by user with 'user_id'(UUID format)
    for the period from 'date_from' to 'date_to'"""
    return db.reach


@r.get('/engagement/acc/{user_id}/{duration}')
async def read_engagement_to_fix_duration(id: UUID,
                                          duration: Duration) -> float:
    """"This function returns engagement statistics on a user with
    'user_id'(UUID format) for the period day, week, month or year
    Engagement = ((like + comments) / subscribers) * 100
    subscribers in the moment!
    like and comment for the period: day, week, month or year"""
    return db.engagement


@r.get('/engagement/acc/{user_id}')
async def read_engagement(id: UUID,
                          date_from: datetime,
                          date_to: datetime = datetime.utcnow(),
                          ) -> float:
    """"This function returns engagement statistics on a user with
    'user_id'(UUID format) for the period day, week, month or year
    Engagement = ((like + comments) / subscribers) * 100
    subscribers in the moment!
    like and comment for the period from 'date_from' to 'date_to'"""
    return db.engagement


@r.get('/searched/acc/{user_id}/{duration}')
async def read_searched_to_fix_duration(id: UUID,
                                        duration: Duration) -> int:
    """The function returns the number of times a user with
    'user_id'(UUID format) was displayed in search results, in 20 results
    for the period: day, week, month or year"""
    return db.searched


@r.get('/searched/acc/{user_id}')
async def read_searched(id: UUID,
                        date_from: datetime,
                        date_to: datetime = datetime.utcnow()) -> int:
    """The function returns the number of times a user with
    'user_id'(UUID format) was displayed in search results, in 20 results,
    for the period from 'date_from' to 'date_to'"""
    return db.searched


@r.get('/views/acc/{user_id}/{duration}')
async def read_views_to_fix_duration(id: UUID,
                                     duration: Duration) -> int:
    """The function returns the number of views of
    a user profile with 'user_id'(UUID format)
    for the period: day, week, month or year"""
    return db.views


@r.get('/views/acc/{user_id}')
async def read_views(id: UUID,
                     date_from: datetime,
                     date_to: datetime = datetime.utcnow()) -> int:
    """The function returns the number of views of
    a user profile with 'user_id'(UUID format)
    for the period from 'date_from' to 'date_to'"""
    return db.views


@r.get('/subscribers/acc/{user_id}/{duration}')
async def read_subscribers_to_fix_duration(id: UUID,
                                           duration: Duration) -> int:
    """the function returns the number of users who clicked
    'Subscribe'
    in the profile of the user with 'user_id'(UUID format)
    for the period: day, week, month or year"""
    return db.subscribers


@r.get('/subscribers/acc/{user_id}')
async def read_subscriberss(id: UUID,
                            date_from: datetime,
                            date_to: datetime = datetime.utcnow()) -> int:
    """the function returns the number of users who clicked
    'Subscribe'
    in the profile of the user with 'user_id'(UUID format)
    for the period from 'date_from' to 'date_to'"""
    return db.subscribers


@r.get('/unsubscribers/acc/{user_id}/{duration}')
async def read_unsubscribers_to_fix_duration(id: UUID,
                                             duration: Duration) -> int:
    """the function returns the number of users who clicked
    'You are subscribed'
    in the profile of the user with 'user_id'(UUID format)
    for the period: day, week, month or year"""
    return db.unsubscriptions


@r.get('/unsubscribers/acc/{user_id}')
async def read_usubscribers(id: UUID,
                            date_from: datetime,
                            date_to: datetime = datetime.utcnow()) -> int:
    """the function returns the number of users who clicked
    'You are subscribed'
    in the profile of the user with 'user_id'(UUID format)
    for the period from 'date_from' to 'date_to'"""
    return db.unsubscriptions


@r.post('post/{post_id}follow_link_post')
async def hit_follow_link_post(post_id: int) -> None:
    """The function increases the number of users who followed the link from the post
    of the user who owns the post with 'post_id'(BigInt format)"""
    db.follow_link_post += 1


@r.post('acc/{user_id}/follow_link_profile')
async def hit_follow_link_profile(user_id: UUID) -> None:
    """The function increases the number of users who followed the link from the profile
    of the user with 'user_id'(UUId format)"""
    db.follow_link_profile += 1
