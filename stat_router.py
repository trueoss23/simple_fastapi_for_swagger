from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class Stat(BaseModel):
    profileReach: int
    profileEngagement: float
    profileViews: int
    profileSubscribers: int
    profileUnsubscribers: int
    followsLinkFromPosts: int
    followsLinkFromProfile: int
    profileClicksFromSubscribers: int
    profileClikcsFromSubscriptions: int
    profileClicksFromKvad: int = None
    profileSearchedInHashtag: int
    profileSearched: int


new = Stat(profileReach=100,
           profileEngagement=35.4,
           profileSearcheded=0,
           profileViews=400,
           profileSubscribers=10,
           profileUnsubscribers=30,
           followsLinkFromPosts=10,
           followsLinkFromProfile=100,
           profileClicksFromSubscribers=2,
           profileClikcsFromSubscriptions=3,
           profileClicksFromKvad=1,
           profileSearchedInHashtag=3,
           profileSearched=0,)

old = Stat(profileReach=0,
           profileEngagement=12.4,
           profileSearcheded=20,
           profileViews=400,
           profileSubscribers=10,
           profileUnsubscribers=0,
           followsLinkFromPosts=0,
           followsLinkFromProfile=100,
           profileClicksFromSubscribers=20,
           profileClikcsFromSubscriptions=33,
           profileClicksFromKvad=0,
           profileSearchedInHashtag=31,
           profileSearched=100,)


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


@r.get('/profile/{userID}/profileClicksFromSubscribers')
async def readClickFromSubscribers(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                                     start: datetime = datetime.utcnow(),
                                     end: datetime = datetime.utcnow()):
    return {'newProfileClickFromSubscribers': new.profileClicksFromSubscribers,
            'oldProfileClickFromSubscribers': old.profileClicksFromSubscribers}


@r.get('/profile/{userID}/profileClickFromSubscriptions')
async def readClickFromSubscriptions(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                                     start: datetime = datetime.utcnow(),
                                     end: datetime = datetime.utcnow()):
    return {'newProfileClickFromSubscriptions': new.profileClikcsFromSubscriptions,
            'oldProfileClickFromSubscriptions': old.profileClikcsFromSubscriptions}


@r.get('/profile/{userID}/profileClicksFromKvad')
async def readClickFromKvad(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                            start: datetime = datetime.utcnow(),
                            end: datetime = datetime.utcnow()):
    return {'newProfileClickFromKvad': new.profileClicksFromKvad,
            'oldProfileClickFromKvad': old.profileClicksFromKvad}


@r.get('/profile/{userID}/searched')
async def read_searched(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                        start: datetime = datetime.utcnow(),
                        end: datetime = datetime.utcnow()):
    """returns the number of times a user with
    'userID'(UUID format) was displayed in search results, in 20 results,
    for the period from 'start' to 'end'"""
    return {'newProfileSearched': new.profileSearched,
            'oldProfileSearched': old.profileSearched}


@r.get('/profile/{userID}/searchedInHashtag')
async def read_searchedInHashtag(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                        start: datetime = datetime.utcnow(),
                        end: datetime = datetime.utcnow()):
    """returns the number of times a user with
    'userID'(UUID format) was displayed in search results, in 20 results,
    for the period from 'start' to 'end'"""
    return {'newProfileSearchedInHashtag': new.profileSearchedInHashtag,
            'oldProfileSearchedInHashtag': old.profileSearchedInHashtag}


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


@r.post('/profile/click/subscribers')
async def createClickFromSubscribers(profileID: UUID, clickerID: UUID):
    """adds to the database a clickerID(UUID format) who clicked on a profile
    with an profileID(UUID format) in their subscribers
    """
    new.profileClicksFromSubscribers += 1
    return


@r.post('/rofile/click/subscriptions')
async def createClickFromSubscriptions(profileID: UUID, clickerID: UUID):
    """adds to the database a clickerID(UUID format) who clicked on a profile
    with an profileID(UUID format) in their Subscruptions
    """
    new.profileClikcsFromSubscriptions += 1
    return


@r.post('/profile/click/kvad')
async def createClickFromKvad(profileID: UUID, clickerID: UUID):
    """adds to the database a clickerID(UUID format) who clicked on a profile
    with an profileID(UUID format) in kvad
    """
    new.profileClicksFromKvad += 1
    return


@r.post('/profile/search')
async def createProfileSearch(profileIDList: list[UUID],
                              finderID: UUID,
                              searchValue: str):
    """adds to the database a user with an ID who was looking for
    a list of profiles with an ID(UUID format) in searchValue
    """
    new.profileSearched += 1
    return


@r.post('/profile/searchInHashtag')
async def createProfileSearchInHashtag(profileIDList: list[UUID],
                                       finderID: UUID,
                                       hashtag: str):
    """adds to the database a user with an ID who was looking for
    a list of profiles with an ID(UUID format) in hashtag
    """
    new.profileSearchedInHashtag += 1
    return
