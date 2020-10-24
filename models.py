# -*- coding utf-8 -*-
from mongoengine import Document, StringField, ListField, IntField, DateTimeField
import datetime


class Super(Document):
    alias = StringField(required=True, max_length=30)
    real_name = StringField(required=True, default="Unknown", max_length=30)
    abilities = ListField(StringField(max_length=30))
    createdAt = DateTimeField(required=True, default=datetime.datetime.now)


if __name__ == "__main__":
    super = Super(
        alias="Batman",
        real_name="Bruce Wayne",
        abilities=["strength", "martial arts", "super intelligence"]
    )
    data = super.to_json()
    print(data)
