from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from uuid import UUID


class Stat(BaseModel):
    reach: int
    engagement: str
    searched: int
    views: int
    subscriptions: int
    unsubscriptions: int
    follow_link_post: int
    follow_link_profile: int


db = Stat(reach=100,
          engagement='+35%',
          searched=20,
          views=400,
          subscriptions=10,
          unsubscriptions=30,
          follow_link_post=10,
          follow_link_profile=100,)


r = APIRouter()


@r.get('/account/{user_id}/all/')
async def read_all_stat(id: UUID,
                        date_from: datetime,
                        date_to: datetime = datetime.utcnow()
                        ) -> Stat:
    """"This function returns statistics on a user with 'user_id'(UUID format)
      for the period from 'date_from' to 'date_to'"""
    return db


@r.get('/account/{user_id}/reach')
async def read_reach(id: UUID,
                     date_from: datetime,
                     date_to: datetime = datetime.utcnow()) -> int:
    """"The function returns the number of unique users who viewed
    at least one post by user with 'user_id'(UUID format)
    for the period from 'date_from' to 'date_to'"""
    return db.reach


@r.get('/account/{user_id}/engagement')
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


@r.get('/account/{user_id}/searched')
async def read_searched(id: UUID,
                        date_from: datetime,
                        date_to: datetime = datetime.utcnow()) -> int:
    """The function returns the number of times a user with
    'user_id'(UUID format) was displayed in search results, in 20 results,
    for the period from 'date_from' to 'date_to'"""
    return db.searched


@r.get('/account/{user_id}/views')
async def read_views(id: UUID,
                     date_from: datetime,
                     date_to: datetime = datetime.utcnow()) -> int:
    """The function returns the number of views of
    a user profile with 'user_id'(UUID format)
    for the period from 'date_from' to 'date_to'"""
    return db.views


@r.get('/account/{user_id}/subscribers')
async def read_subscriberss(id: UUID,
                            date_from: datetime,
                            date_to: datetime = datetime.utcnow()) -> int:
    """the function returns the number of users who clicked
    'Subscribe'
    in the profile of the user with 'user_id'(UUID format)
    for the period from 'date_from' to 'date_to'"""
    return db.subscribers


@r.get('/account/{user_id}/unsubscribers')
async def read_usubscribers(id: UUID,
                            date_from: datetime,
                            date_to: datetime = datetime.utcnow()) -> int:
    """the function returns the number of users who clicked
    'You are subscribed'
    in the profile of the user with 'user_id'(UUID format)
    for the period from 'date_from' to 'date_to'"""
    return db.unsubscriptions


@r.post('/post/{post_id}/follow_link_post')
async def hit_follow_link_post(post_id: int) -> None:
    """The function increases the number of users who followed the link from the post
    of the user who owns the post with 'post_id'(BigInt format)"""
    db.follow_link_post += 1


@r.post('/account/{user_id}/follow_link_profile')
async def hit_follow_link_profile(user_id: UUID) -> None:
    """The function increases the number of users who followed the link from the profile
    of the user with 'user_id'(UUId format)"""
    db.follow_link_profile += 1
