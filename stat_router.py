from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class RequestBodyWithClicker(BaseModel):
	profileID: UUID
	clickerID: UUID

	class Config:
		json_schema_extra = {
            "example": {
                "profileID": "4b963742-99b2-494c-bdd6-d6a4176e954a",
                "clickerID": "5f963742-99b2-494c-bdd9-d6a4176e954a",
            }
        }


class RequestBodyForSearch(BaseModel):
	profileID: UUID
	clickerID: UUID
	searchValue: str

	class Config:
		json_schema_extra = {
            "example": {
                "profileID": "4b963742-99b2-494c-bdd6-d6a4176e954a",
                "clickerID": "5f963742-99b2-494c-bdd9-d6a4176e954a",
                "searchValue": "psina",
            }
        }


class StatPoint(BaseModel):
    profileReach: int
    profileEngagement: float
    profileViews: int
    profileSubscribers: int
    profileUnsubscribers: int
    allFollowsLink: int
    allSearch: int

    class Config:
        json_schema_extra = {
            "example": {
                "profileReach": 5,
                "profileEngagement": 35.4,
                "profileViews": 2,
                "profileSubscribers": 1,
                "profileUnsubscribers": 3,
                "allFollowsLink": 100,
                "allSearch": 20,
            }
        }


class Stat(BaseModel):
    Curr: StatPoint
    Prev: StatPoint


Curr = StatPoint(profileReach=100,
           profileEngagement=35.4,
           searcheded=0,
           profileViews=400,
           profileSubscribers=10,
           profileUnsubscribers=30,
		   allFollowsLink=100,
           allSearch=200,)

Prev = StatPoint(profileReach=0,
           profileEngagement=12.4,
           searcheded=20,
           profileViews=400,
           profileSubscribers=10,
           profileUnsubscribers=0,
		   allFollowsLink=10,
           allSearch=230,)


r = APIRouter()


@r.get('/profile/{userID}/allStats/')
async def readAllStat(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                      start: datetime = datetime.utcnow(),
                      end: datetime = datetime.utcnow()) -> Stat:
    """"This function returns statistics on a user with 'userID'(UUID format)
      for the period from 'start' to 'end'"""
    return {'Curr': Curr,
            'Prev': Prev}


@r.get('/profile/{userID}/reach')
async def read_reach(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                     start: datetime = datetime.utcnow(),
                     end: datetime = datetime.utcnow()):
    """"returns the number of unique users who viewed
    at least one post by user with 'userID'(UUID format)
    for the period from 'start' to 'end'"""
    return {'CurrReach': Curr.profileReach,
            'PrevReach': Prev.profileReach}


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
    return {'CurrEngagement': Curr.profileEngagement,
            'PrevEngagement': Prev.profileEngagement}


@r.get('/profile/{userID}/views')
async def read_views(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                     start: datetime = datetime.utcnow(),
                     end: datetime = datetime.utcnow()):
    """returns the number of profileViews of
    a user profile with 'userID'(UUID format)
    for the period from 'start' to 'end'"""
    return {'CurrViews': Curr.profileViews,
            'PrevViews': Prev.profileViews}


@r.get('/profile/{userID}/subscribers')
async def read_subscribers(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                           start: datetime = datetime.utcnow(),
                           end: datetime = datetime.utcnow()):
    """returns the number of users who clicked
    'Subscribe'
    in the profile of the user with 'userID'(UUID format)
    for the period from 'start' to 'end'"""
    return {'CurrSubscribers': Curr.profileSubscribers,
            'PrevSubscribers': Prev.profileSubscribers}


@r.get('/profile/{userID}/unsubscribers')
async def read_unsubscribers(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                             start: datetime = datetime.utcnow(),
                             end: datetime = datetime.utcnow()):
    """returns the number of users who clicked
    'You are subscribed'
    in the profile of the user with 'userID'(UUID format)
    for the period from 'start' to 'end'"""
    return {'CurrUnsubscribers': Curr.profileUnsubscribers,
            'PrevUnsubscriberss': Prev.profileUnsubscribers}


@r.get('/profile/{userID}/followsLinkFromPosts')
async def readFollowsLinkFromPosts(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                                   start: datetime = datetime.utcnow(),
                                   end: datetime = datetime.utcnow()):
    """returns the number of users who clicked
    links from posts in the profile of the user with 'userID'(UUID format)
    for the period from 'start' to 'end'"""
    return {'CurrFollowsLinkFromPosts': Curr.followsLinkFromPost,
            'PrevFollowsLinkFromPosts': Prev.followsLinkFromPost}


@r.get('/profile/{userID}/followsLinkFromProfile')
async def readFollowsLinkFromProfile(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                                     start: datetime = datetime.utcnow(),
                                     end: datetime = datetime.utcnow()):
    """returns the number of users who clicked
    links from profile of the user with 'userID'(UUID format)
    for the period from 'start' to 'end'"""
    return {'CurrFollowsLinkFromProfile': Curr.followsLinkFromProfile,
            'PrevFollowsLinkFromProfile': Prev.followsLinkFromProfile}


@r.get('/profile/{userID}/clicksFromSubscribers')
async def readClickFromSubscribers(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                                     start: datetime = datetime.utcnow(),
                                     end: datetime = datetime.utcnow()):
    return {'CurrClicksSubscribers': Curr.clicksFromSubscribers,
            'PrevClicksSubscribers': Prev.clicksFromSubscribers}


@r.get('/profile/{userID}/profileClicksFromSubscriptions')
async def readClickFromSubscriptions(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                                     start: datetime = datetime.utcnow(),
                                     end: datetime = datetime.utcnow()):
    return {'CurrClicksSubscriptions': Curr.clicksFromSubscriptions,
            'PrevClicksSubscriptions': Prev.clicksFromSubscriptions}


@r.get('/profile/{userID}/clicksFromKvad')
async def readClickFromKvad(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                            start: datetime = datetime.utcnow(),
                            end: datetime = datetime.utcnow()):
    return {'CurrClicksKvad': Curr.clicksFromKvad,
            'PrevClicksKvad': Prev.clicksFromKvad}


@r.get('/profile/{userID}/searched')
async def read_searched(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                        start: datetime = datetime.utcnow(),
                        end: datetime = datetime.utcnow()):
    """returns the number of times a user with
    'userID'(UUID format) was displayed in search results, in 20 results,
    for the period from 'start' to 'end'"""
    return {'CurrSearched': Curr.searched,
            'PrevSearched': Prev.searched}


@r.get('/profile/{userID}/searchedInHashtag')
async def read_searchedInHashtag(id: UUID = '006e40e7-8749-44d1-90bf-1f9027dcdd02',
                        start: datetime = datetime.utcnow(),
                        end: datetime = datetime.utcnow()):
    """returns the number of times a user with
    'userID'(UUID format) was displayed in search results, in 20 results,
    for the period from 'start' to 'end'"""
    return {'CurrSearchedInHashtag': Curr.searchedInHashtag,
            'PrevSearchedInHashtag': Prev.searchedInHashtag}


@r.post('/post/followsLinkFromPost')
async def createFollowsLinkFromPost(profileID: UUID, visitorID: UUID):
    """adds to the database a user with an visitorID(UUID format)
    who followed the link from the post of the user with an profileID(UUID format)"""
    Curr.allFollowsLink += 1
    return


@r.post('/profile/followsLinkFromProfile')
async def createFollowsLinkFromProfile(profileID: UUID, visitorID: UUID):
    """adds to the database a user with an visitorID(UUID format)
    who followed the link from the profile of the user with an profileID(UUID format)"""
    Curr.allFollowsLink += 1
    return


@r.post('/profile/click/subscribers')
async def createClickFromSubscribers(profileID: UUID, clickerID: UUID):
    """adds to the database a clickerID(UUID format) who clicked on a profile
    with an profileID(UUID format) in their subscribers
    """
    Curr.allSearch += 1
    return


@r.post('/profile/click/subscriptions')
async def createClickFromSubscriptions(profileID: UUID, clickerID: UUID):
    """adds to the database a clickerID(UUID format) who clicked on a profile
    with an profileID(UUID format) in their Subscruptions
    """
    Curr.allSearch += 1
    return


@r.post('/profile/click/kvad')
async def createClickFromKvad(profileID: UUID, clickerID: UUID):
    """adds to the database a clickerID(UUID format) who clicked on a profile
    with an profileID(UUID format) in kvad
    """
    Curr.allSearch += 1
    return


@r.post('/profile/search')
async def createProfileSearch(profileIDList: list[RequestBodyForSearch]):
    """adds to the database a user with an ID who was looking for
    a list of profiles with an ID(UUID format) in searchValue
    """
    Curr.allSearch += 1
    return


@r.post('/profile/searchInHashtag')
async def createProfileSearchInHashtag(profileIDList: list[RequestBodyWithClicker]):
    """adds to the database a user with an ID who was looking for
    a list of profiles with an ID(UUID format) in hashtag
    """
    Curr.allSearch += 1
    return
