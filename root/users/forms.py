from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

from root.users.custom_form_validators import safe_string, unique_or_current_user_field


class RegistrationForm(FlaskForm):
    """Register a new user with email, username, and password"""
    firstname = StringField(
        "John",
        description="John",
        validators=[Length(min=4, max=80)],
    )
    lastname = StringField(
        "Deep",
        description="Deep",
        validators=[Length(min=1, max=80)],
    )
    username = StringField(
        "Username",
        description="Username",
        validators=[
            DataRequired(),
            unique_or_current_user_field("Username is already taken."),
            safe_string(),
            Length(min=3, max=40),
        ],
    )
    email = StringField(
        "Email",
        description="my@email.com",
        validators=[
            DataRequired(),
            Email(),
            unique_or_current_user_field("Email is already registered."),
        ],
    )
    city = StringField(
        "City",
        description="Iasi",
    )
    school = StringField(
        "School",
        description="Scoala Generala nr.6",
    )
    age = StringField(
        "Age",
        description="9 ani",
    )
    password = PasswordField(
        "Password",
        description="Old password",
        validators=[DataRequired(), Length(min=5, max=40)],
    )
    pass_confirm = PasswordField(
        "Confirm password",
        description="Password confirm",
        validators=[
            DataRequired(),
            EqualTo("pass_confirm", message="Passwords Must Match!"),
        ],
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    """Allow users to log in with username or email compared against a pw"""

    username_or_email = StringField(
        "Username or email",
        description="Username or email",
        validators=[DataRequired()],
    )
    password = PasswordField(
        "Password", description="Password", validators=[DataRequired()]
    )
    submit = SubmitField("Log In")


class SettingsForm(FlaskForm):
    """Allow users to update their name, username, email, and password"""
    firstname = StringField(
        "Firstname", description="John", validators=[Optional(), Length(max=80)],
    )
    lastname = StringField(
        "Name", description="Smith", validators=[Optional(), Length(max=80)],
    )
    username = StringField(
        "Username",
        description="Username",
        validators=[
            DataRequired(),
            unique_or_current_user_field("Username already exists."),
            safe_string(),
            Length(min=3, max=40),
        ],
    )
    email = StringField(
        "Email",
        description="my@email.com",
        validators=[
            DataRequired(),
            Email(),
            unique_or_current_user_field("Email is already registered."),
        ],
    )
    city = StringField(
        "City", description="Iasi", validators=[Optional(), Length(max=80)],
    )
    school = StringField(
        "School", description="Scoala Generala nr.6", validators=[Optional(), Length(max=80)],
    )
    age = StringField(
        "Age", description="11", validators=[Optional(), Length(max=80)],
    )
    new_pass = PasswordField(
        "New Password",
        description="New password",
        validators=[Optional(), Length(min=8, max=30)],
    )
    pass_confirm = PasswordField(
        "Confirm password",
        description="Confirm password",
        validators=[Optional(), EqualTo("new_pass", message="Passwords Must Match!")],
    )
    submit = SubmitField("Update")


class QuizForm(FlaskForm):
    """Handle the questions for the quiz"""
    question = StringField(
        "Question tralala", description="Question", validators=[Optional(), Length(max=80)],
    )
    option1 = StringField(
        "Option1", description="Option1", validators=[Optional(), Length(max=80)],
    )
    option2 = StringField(
        "Option2", description="Option2", validators=[Optional(), Length(max=80)],
    )
    option3 = StringField(
        "Option3", description="Option3", validators=[Optional(), Length(max=80)],
    )
    submit = SubmitField("Next")
