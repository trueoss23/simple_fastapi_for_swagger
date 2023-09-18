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


@r.get('/profile/{userID}/allStats/')
async def readAllStat(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                      start: datetime = datetime.utcnow(),
                      end: datetime = datetime.utcnow()):
    """"This function returns statistics on a user with 'userID'(UUID format)
      for the period from 'start' to 'end'"""
    return {'new': new,
            'old': old}


@r.get('/profile/{userID}/reach')
async def read_reach(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                     start: datetime = datetime.utcnow(),
                     end: datetime = datetime.utcnow()):
    """"returns the number of unique users who viewed
    at least one post by user with 'userID'(UUID format)
    for the period from 'start' to 'end'"""
    return {'newProfileReach': new.profileReach,
            'oldProfileReach': old.profileReach}


@r.get('/profile/{userID}/engagement')
async def read_engagement(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                          start: datetime = datetime.utcnow(),
                          end: datetime = datetime.utcnow(),
                          ):
    """"This function returns profileEngagement statistics on a user with
    'userID'(UUID format) for the period day, week, month or year
    Engagement = ((like + comments) / subscribers) * 100
    subscribers in the moment!
    like and comment for the period from 'start' to 'end'"""
    return {'newProfileEngagement': new.profileEngagement,
            'oldProfileEngagement': old.profileEngagement}


@r.get('/profile/{userID}/searched')
async def read_searched(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                        start: datetime = datetime.utcnow(),
                        end: datetime = datetime.utcnow()):
    """returns the number of times a user with
    'userID'(UUID format) was displayed in search results, in 20 results,
    for the period from 'start' to 'end'"""
    return {'newProfileSearched': new.profileSearched,
            'oldProfileSearched': old.profileSearched}


@r.get('/profile/{userID}/views')
async def read_views(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                     start: datetime = datetime.utcnow(),
                     end: datetime = datetime.utcnow()):
    """returns the number of profileViews of
    a user profile with 'userID'(UUID format)
    for the period from 'start' to 'end'"""
    return {'newProfileViews': new.profileViews,
            'oldProfileViews': old.profileViews}


@r.get('/profile/{userID}/subscribers')
async def read_subscribers(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                           start: datetime = datetime.utcnow(),
                           end: datetime = datetime.utcnow()):
    """returns the number of users who clicked
    'Subscribe'
    in the profile of the user with 'userID'(UUID format)
    for the period from 'start' to 'end'"""
    return {'newProfileSubscribers': new.profileSubscribers,
            'oldProfileSubscribers': old.profileSubscribers}


@r.get('/profile/{userID}/unsubscribers')
async def read_unsubscribers(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                             start: datetime = datetime.utcnow(),
                             end: datetime = datetime.utcnow()):
    """returns the number of users who clicked
    'You are subscribed'
    in the profile of the user with 'userID'(UUID format)
    for the period from 'start' to 'end'"""
    return {'newProfileUnsubscribers': new.profileUnsubscribers,
            'oldProfileUnsubscriberss': old.profileUnsubscribers}


@r.get('/profile/{userID}/followsLinkFromPosts')
async def readFollowsLinkFromPosts(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                                   start: datetime = datetime.utcnow(),
                                   end: datetime = datetime.utcnow()):
    """returns the number of users who clicked
    links from posts in the profile of the user with 'userID'(UUID format)
    for the period from 'start' to 'end'"""
    return {'newFollowsLinkFromPostss': new.followsLinkFromPosts,
            'oldFollowsLinkFromPosts': old.followsLinkFromPosts}


@r.get('/profile/{userID}/followsLinkFromProfile')
async def readFollowsLinkFromProfile(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                                     start: datetime = datetime.utcnow(),
                                     end: datetime = datetime.utcnow()):
    """returns the number of users who clicked
    links from profile of the user with 'userID'(UUID format)
    for the period from 'start' to 'end'"""
    return {'newFollowsLinkFromProfile': new.followsLinkFromProfile,
            'oldFollowsLinkFromProfile': old.followsLinkFromProfile}


@r.post('/post/followsLinkFromPost')
async def createFollowsLinkFromPost(profileID: UUID, visitorID: UUID):
    """adds to the database a user with an visitorID(UUID format)
    who followed the link from the post of the user with an profileID(UUID format)"""
    new.followsLinkFromPosts += 1
    return


@r.post('/profile/followsLinkFromProfile')
async def createFollowsLinkFromProfile(profileID: UUID, visitorID: UUID):
    """adds to the database a user with an visitorID(UUID format)
    who followed the link from the profile of the user with an profileID(UUID format)"""
    new.followsLinkFromProfile += 1
    return
