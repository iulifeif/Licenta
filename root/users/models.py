"""User model"""
from flask_login import UserMixin
from werkzeug.security import check_password_hash

from root.globals import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    """Load the user object from the user ID stored in the session"""
    return User.objects(pk=user_id).first()


class User(db.Document, UserMixin):
    """User model

    When sparse=True combined with unique=True and required=False
    means that uniqueness won't be enforced for None values
    """

    # User editable fields
    username = db.StringField(required=True, unique=True, max_length=40, index=True)
    firstname = db.StringField(required=False, max_length=80, index=True)
    lastname = db.StringField(required=False, max_length=80, index=True)
    email = db.EmailField(
        unique=True, required=False, sparse=True, max_length=80, index=True
    )
    city = db.StringField(required=False, max_length=10, index=True)
    school = db.StringField(required=False, max_length=80, index=True)
    age = db.StringField(required=False, max_length=10, index=True)
    score = db.IntField(required=True, max_length=10, index=True, default=0)
    password_hash = db.StringField(required=False, index=True)

    # OAuth stuff
    facebook_id = db.StringField(unique=True, required=False, sparse=True, index=True)
    google_id = db.StringField(unique=True, required=False, sparse=True, index=True)

    def __repr__(self):
        """Define what is printed for the user object"""
        return f"Username: {self.username} id: {self.id}"

    def check_password(self, password):
        """Checks that the pw provided hashes to the stored pw hash value"""
        return check_password_hash(self.password_hash, password)


class Questions(db.Document, UserMixin):
    number = db.IntField(required=True, )
    classe = db.StringField(required=True, max_length=10, index=True)
    difficulty = db.StringField(required=True, max_length=10, index=True)
    question = db.StringField(required=True, unique=True, max_length=40, index=True)
    answer = db.StringField(required=True, max_length=80, index=True)
    options = db.StringField(required=True, max_length=80, index=True)

    def __repr__(self):
        """Define what is printed for the questions object"""
        return f"Question: {self.question} id: {self.id}"
