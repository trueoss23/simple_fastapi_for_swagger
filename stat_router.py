from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class Stat(BaseModel):
    profile_reach: int
    profile_engagement: float
    profile_searched: int
    profile_views: int
    profile_subscribers: int
    profile_unsubscribers: int
    post_follow_link_post: int
    profile_follow_link_profile: int


new = Stat(profile_reach=100,
           profile_engagement=35,
           profile_searched=20,
           profile_views=400,
           profile_subscribers=10,
           profile_unsubscribers=30,
           post_follow_link_post=10,
           profile_follow_link_profile=100,)

old = Stat(profile_reach=10,
           profile_engagement=0,
           profile_searched=20,
           profile_views=400,
           profile_subscribers=10,
           profile_unsubscribers=0,
           post_follow_link_post=10,
           profile_follow_link_profile=100,)


r = APIRouter()


@r.get('/account/{user_id}/all/')
async def read_all_stat(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                        date_from: datetime = datetime.utcnow(),
                        date_to: datetime = datetime.utcnow()
                        ):
    """"This function returns statistics on a user with 'user_id'(UUID format)
      for the period from 'date_from' to 'date_to'"""
    return {'new': new,
            'old': old}


@r.get('/account/{user_id}/profile_reach')
async def read_reach(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                     date_from: datetime = datetime.utcnow(),
                     date_to: datetime = datetime.utcnow()):
    """"The function returns the number of unique users who viewed
    at least one post by user with 'user_id'(UUID format)
    for the period from 'date_from' to 'date_to'"""
    return {'new_profile_reach': new.profile_reach,
            'old_profile_reach': old.profile_reach,}


@r.get('/account/{user_id}/profile_engagement')
async def read_engagement(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                          date_from: datetime = datetime.utcnow(),
                          date_to: datetime = datetime.utcnow(),
                          ):
    """"This function returns profile_engagement statistics on a user with
    'user_id'(UUID format) for the period day, week, month or year
    Engagement = ((like + comments) / subscribers) * 100
    subscribers in the moment!
    like and comment for the period from 'date_from' to 'date_to'"""
    return {'new_profile_engagement': new.profile_engagement,
            'old_profile_engagement': old.profile_engagement,}


@r.get('/account/{user_id}/profile_searched')
async def read_searched(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                        date_from: datetime = datetime.utcnow(),
                        date_to: datetime = datetime.utcnow()):
    """The function returns the number of times a user with
    'user_id'(UUID format) was displayed in search results, in 20 results,
    for the period from 'date_from' to 'date_to'"""
    return {'new_profile_searched': new.profile_searched,
            'old_profile_searched': old.profile_searched,}


@r.get('/account/{user_id}/profile_views')
async def read_views(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                     date_from: datetime = datetime.utcnow(),
                     date_to: datetime = datetime.utcnow()):
    """The function returns the number of profile_views of
    a user profile with 'user_id'(UUID format)
    for the period from 'date_from' to 'date_to'"""
    return {'new_profile_views': new.profile_views,
            'old_profile_views': old.profile_views,}


@r.get('/account/{user_id}/profile_subscribers')
async def read_subscribers(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                            date_from: datetime = datetime.utcnow(),
                            date_to: datetime = datetime.utcnow()):
    """the function returns the number of users who clicked
    'Subscribe'
    in the profile of the user with 'user_id'(UUID format)
    for the period from 'date_from' to 'date_to'"""
    return {'new_profile_subscribers': new.profile_subscribers,
            'old_profile_subscribers': old.profile_subscribers,}


@r.get('/account/{user_id}/profile_unsubscribers')
async def read_unsubscribers(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                            date_from: datetime = datetime.utcnow(),
                            date_to: datetime = datetime.utcnow()):
    """the function returns the number of users who clicked
    'You are subscribed'
    in the profile of the user with 'user_id'(UUID format)
    for the period from 'date_from' to 'date_to'"""
    return {'new_profile_unsubscribers': new.profile_unsubscribers,
            'old_profile_unsubscriberss': old.profile_unsubscribers,}


@r.post('/post/{post_id}/post_follow_link_post')
async def hit_follow_link_post(post_id: int):
    """The function increases the number of users who followed the link from the post
    of the user who owns the post with 'post_id'(BigInt format)"""
    new.post_follow_link_post += 1
    return


@r.post('/account/{user_id}/profile_follow_link_profile')
async def hit_follow_link_profile(user_id: UUID):
    """The function increases the number of users who followed the link from the profile
    of the user with 'user_id'(UUId format)"""
    new.profile_follow_link_profile += 1
    return
