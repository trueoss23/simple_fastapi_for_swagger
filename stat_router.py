from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class Stat(BaseModel):
    profileReach: int
    profileEngagement: float
    profileSearched: int
    profileViews: int
    profileSubscribers: int
    profileUnsubscribers: int
    followsLinkFromPosts: int
    followsLinkFromProfile: int


new = Stat(profileReach=100,
           profileEngagement=35.4,
           profileSearched=0,
           profileViews=400,
           profileSubscribers=10,
           profileUnsubscribers=30,
           followsLinkFromPosts=10,
           followsLinkFromProfile=100,)

old = Stat(profileReach=0,
           profileEngagement=12.4,
           profileSearched=20,
           profileViews=400,
           profileSubscribers=10,
           profileUnsubscribers=0,
           followsLinkFromPosts=0,
           followsLinkFromProfile=100,)


r = APIRouter()


@r.get('/profile/{userId}/allStats/')
async def readAllStat(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                      start: datetime = datetime.utcnow(),
                      end: datetime = datetime.utcnow()):
    """"This function returns statistics on a user with 'userId'(UUID format)
      for the period from 'start' to 'end'"""
    return {'new': new,
            'old': old}


@r.get('/profile/{userId}/reach')
async def read_reach(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                     start: datetime = datetime.utcnow(),
                     end: datetime = datetime.utcnow()):
    """"returns the number of unique users who viewed
    at least one post by user with 'userId'(UUID format)
    for the period from 'start' to 'end'"""
    return {'newProfileReach': new.profileReach,
            'oldProfileReach': old.profileReach}


@r.get('/profile/{userId}/engagement')
async def read_engagement(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                          start: datetime = datetime.utcnow(),
                          end: datetime = datetime.utcnow(),
                          ):
    """"This function returns profileEngagement statistics on a user with
    'userId'(UUID format) for the period day, week, month or year
    Engagement = ((like + comments) / subscribers) * 100
    subscribers in the moment!
    like and comment for the period from 'start' to 'end'"""
    return {'newProfileEngagement': new.profileEngagement,
            'oldProfileEngagement': old.profileEngagement}


@r.get('/profile/{userId}/searched')
async def read_searched(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                        start: datetime = datetime.utcnow(),
                        end: datetime = datetime.utcnow()):
    """returns the number of times a user with
    'userId'(UUID format) was displayed in search results, in 20 results,
    for the period from 'start' to 'end'"""
    return {'newProfileSearched': new.profileSearched,
            'oldProfileSearched': old.profileSearched}


@r.get('/profile/{userId}/views')
async def read_views(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                     start: datetime = datetime.utcnow(),
                     end: datetime = datetime.utcnow()):
    """returns the number of profileViews of
    a user profile with 'userId'(UUID format)
    for the period from 'start' to 'end'"""
    return {'newProfileViews': new.profileViews,
            'oldProfileViews': old.profileViews}


@r.get('/profile/{userId}/subscribers')
async def read_subscribers(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                           start: datetime = datetime.utcnow(),
                           end: datetime = datetime.utcnow()):
    """returns the number of users who clicked
    'Subscribe'
    in the profile of the user with 'userId'(UUID format)
    for the period from 'start' to 'end'"""
    return {'newProfileSubscribers': new.profileSubscribers,
            'oldProfileSubscribers': old.profileSubscribers}


@r.get('/profile/{userId}/unsubscribers')
async def read_unsubscribers(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                             start: datetime = datetime.utcnow(),
                             end: datetime = datetime.utcnow()):
    """returns the number of users who clicked
    'You are subscribed'
    in the profile of the user with 'userId'(UUID format)
    for the period from 'start' to 'end'"""
    return {'newProfileUnsubscribers': new.profileUnsubscribers,
            'oldProfileUnsubscriberss': old.profileUnsubscribers}


@r.get('/profile/{userId}/followsLinkFromPosts')
async def readFollowsLinkFromPosts(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                                   start: datetime = datetime.utcnow(),
                                   end: datetime = datetime.utcnow()):
    """returns the number of users who clicked
    links from posts in the profile of the user with 'userId'(UUID format)
    for the period from 'start' to 'end'"""
    return {'newFollowsLinkFromPostss': new.followsLinkFromPosts,
            'oldFollowsLinkFromPosts': old.followsLinkFromPosts}


@r.get('/profile/{userId}/followsLinkFromProfile')
async def readFollowsLinkFromProfile(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                                     start: datetime = datetime.utcnow(),
                                     end: datetime = datetime.utcnow()):
    """returns the number of users who clicked
    links from profile of the user with 'userId'(UUID format)
    for the period from 'start' to 'end'"""
    return {'newFollowsLinkFromProfile': new.followsLinkFromProfile,
            'oldFollowsLinkFromProfile': old.followsLinkFromProfile}


@r.post('/post/{postId}/followsLinkFromPost')
async def hit_follow_link_post(post_id: int):
    """increases the number of users who followed the link from the post
    of the user who owns the post with 'post_id'(BigInt format)"""
    new.followsLinkFromPosts += 1
    return


@r.post('/profile/{userId}/followsLinkFromProfile')
async def hit_follow_link_profile(userId: UUID):
    """increases the number of users who followed the link from the profile
    of the user with 'userId'(UUId format)"""
    new.followsLinkFromProfile += 1
    return
