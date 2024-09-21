import random
import shutil
from typing import Optional, List
from bson import ObjectId
from pydantic import BaseModel, Field
from src.anty.actions.login import Login
from src.anty.browser.browser import Browser
from src.anty.actions.video import Video
from src.config import PATH_TO_PROFILES
from src.db.db import account_collection, proxy_collection
from src.models.proxy import Proxy
from src.models.pyobject_id import PyObjectId


class Account(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    mail: str
    password: str
    recovery_mail: str
    proxy_id: Optional[PyObjectId] = Field(default=None)
    country: str
    broken: bool = Field(default=False)

    def create_account(self):
        self.country = self.country.replace("\r", "")
        proxy = list(proxy_collection.find({"country": str(self.country)}))
        r = random.Random()
        proxy = r.choice(proxy)
        self.proxy_id = proxy["_id"]
        created = account_collection.insert_one(self.model_dump())
        self.id = str(created.inserted_id)
        p = Proxy.model_validate(proxy)
        browser = Browser(self.id, p).get_browser()
        login = Login(browser, self.mail, self.password, self.recovery_mail)
        result = login.login()
        if not result:
            account_collection.update_one({"_id": ObjectId(self.id)}, {"$set": {"broken": True}})
        browser.close()

    def video_like(self, url):
        video = self.get_video(url)
        is_working = video.check_auth()
        if is_working:
            video.video_like()
            video.close()
            return True
        else:
            video.close()
            account_collection.update_one({"_id": ObjectId(self.id)}, {"$set": {"broken": True}})
            return False

    def shorts_like(self, url):
        video = self.get_video(url)
        is_working = video.check_auth()
        if is_working:
            video.shorts_like()
            video.close()
            return True
        else:
            video.close()
            account_collection.update_one({"_id": ObjectId(self.id)}, {"$set": {"broken": True}})
            return False

    def video_comment(self, url, comment):
        video = self.get_video(url)
        is_working = video.check_auth()
        if is_working:
            video.video_comment(comment)
            video.close()
            return True
        else:
            video.close()
            account_collection.update_one({"_id": ObjectId(self.id)}, {"$set": {"broken": True}})
            return False

    def video_comment_reply(self, url, comment):
        video = self.get_video(url)
        is_working = video.check_auth()
        if is_working:
            video.video_comment_reply(comment)
            video.close()
            return True
        else:
            video.close()
            account_collection.update_one({"_id": ObjectId(self.id)}, {"$set": {"broken": True}})
            return False

    def video_comment_like(self, url):
        video = self.get_video(url)
        is_working = video.check_auth()
        if is_working:
            video.comment_like()
            video.close()
            return True
        else:
            video.close()
            account_collection.update_one({"_id": ObjectId(self.id)}, {"$set": {"broken": True}})
            return False

    def community_like(self, url):
        video = self.get_video(url)
        is_working = video.check_auth()
        if is_working:
            video.community_like()
            video.close()
            return True
        else:
            video.close()
            account_collection.update_one({"_id": ObjectId(self.id)}, {"$set": {"broken": True}})
            return False

    def community_comment(self, url, comment):
        video = self.get_video(url)
        is_working = video.check_auth()
        if is_working:
            video.community_comment(comment)
            video.close()
            return True
        else:
            video.close()
            account_collection.update_one({"_id": ObjectId(self.id)}, {"$set": {"broken": True}})
            return False

    def community_comment_reply(self, url, comment):
        video = self.get_video(url)
        is_working = video.check_auth()
        if is_working:
            video.community_comment_reply(comment)
            video.close()
            return True
        else:
            video.close()
            account_collection.update_one({"_id": ObjectId(self.id)}, {"$set": {"broken": True}})
            return False

    def community_comment_like(self, url):
        video = self.get_video(url)
        is_working = video.check_auth()
        if is_working:
            video.community_comment_like()
            video.close()
            return True
        else:
            video.close()
            account_collection.update_one({"_id": ObjectId(self.id)}, {"$set": {"broken": True}})
            return False


    def delete(self):
        deleted = account_collection.delete_one({"_id": ObjectId(self.id)})
        if deleted.deleted_count and self.id:
            shutil.rmtree(f"{PATH_TO_PROFILES}/{self.id}")

    def get_video(self, url):
        proxy = Proxy.model_validate(proxy_collection.find_one({"_id": ObjectId(self.proxy_id)}))
        browser = Browser(self.id, proxy).get_browser()
        return Video(url, browser)

    def reply_vote(self, url, option_id):
        video = self.get_video(url)
        is_working = video.check_auth()
        if is_working:
            video.community_vote(option_id)
            video.close()
            return True
        else:
            video.close()
            account_collection.update_one({"_id": ObjectId(self.id)}, {"$set": {"broken": True}})
            return False



class AccountList(BaseModel):
    accounts: Optional[List[Optional[Account]]]

def accounts_quantity(country=None, is_broken=None):
    query = {}
    if country:
        query.update({"country": country})
    if type(is_broken) is bool:
        query.update({"broken": is_broken})
    query.update({})
    return len(list(account_collection.find(query)))

def get_good_accounts(country, quantity):
    collection = account_collection.aggregate([
        {"$match": {"country": country, "broken": False}},
        {"$sample": { "size": quantity} }
    ])
    return AccountList(accounts=list(collection)).accounts

def get_broken_accounts():
    return AccountList(accounts=list(account_collection.find({"broken": True}))).accounts

def accounts_countries():
    return list(account_collection.distinct("country"))
