from typing import Optional
from src.anty.browser.proxy import add_proxy
from pydantic import BaseModel, Field
from src.db.db import proxy_collection
from src.models.pyobject_id import PyObjectId


class Proxy(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias="_id")
    scheme: str
    host: str
    port: str
    username: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    country: str

    def record_proxy(self):
        i = proxy_collection.insert_one(self.model_dump())
        if self.username and self.password:
            add_proxy(self.scheme, self.host, self.port, self.username, self.password, str(i.inserted_id))


def proxy_quantity(country=None):
    query = {}
    if country:
        query = {"country": country}
    return len(list(proxy_collection.find(query)))

def proxy_countries():
    return list(proxy_collection.distinct("country"))

