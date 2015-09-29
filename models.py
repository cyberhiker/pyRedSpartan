from mongoengine import *

connect('redspartan', username='chris', password='nothing', host='localhost')

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    password = StringField(max_length=200)

class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
    meta = {'allow_inheritance': True}

class AssessmentRoles(DynamicDocument):
    role = StringField(required=True)
    description = StringField(required=True)
    type = StringField(required=True)
    meta = {'collection': 'AssessmentRoles'}

'''
class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()
'''
