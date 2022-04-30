import random

from authomatic.adapters import WerkzeugAdapter
from flask import (
    Blueprint,
    flash,
    make_response,
    redirect,
    render_template,
    request,
    url_for, )
from flask_login import current_user, login_required, login_user, logout_user
from jinja2 import TemplateNotFound
from werkzeug.debug import console
from werkzeug.security import generate_password_hash

from root.users.forms import LoginForm, RegistrationForm, SettingsForm, QuizForm
from root.users.models import User, Questions
from root.users.oauth_config import authomatic

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    """Registers the user with username, email and password hash in database"""
    logout_user()
    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = generate_password_hash(form.password.data)
        user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            username=form.username.data,
            email=form.email.data,
            city=form.city.data,
            school=form.school.data,
            age=form.age.data,
            password_hash=password_hash,
        )
        user.save()
        flash("Thanks for registering!", category="success")
        return login_and_redirect(user)
    return render_template("users/register.html", form=form), 200


@users.route("/login", methods=["GET", "POST"])
def login():
    """Logs the user in through username/password"""
    logout_user()
    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from a user model lookup
        username_or_email = form.username_or_email.data
        if "@" in username_or_email:
            user = User.objects(email=username_or_email).first()
        else:
            user = User.objects(username=username_or_email).first()
        if user is not None and user.check_password(form.password.data):
            # User validates (user object found and password for that
            # user matched the password provided by the user)
            return login_and_redirect(user)
        else:
            flash(
                "(email or username)/password combination not found", category="error"
            )
    return render_template("users/login.html", form=form), 200


@users.route("/logout")
@login_required
def logout():
    """Log out the current user"""
    logout_user()
    flash("You have logged out.", category="success")
    return redirect(url_for("users.login"))


@users.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    """Update user settings"""
    form = SettingsForm()
    if form.validate_on_submit():
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.city = form.city.data
        current_user.school = form.school.data
        current_user.age = form.age.data
        if form.new_pass.data:
            new_hash = generate_password_hash(form.new_pass.data)
            current_user.password_hash = new_hash
        current_user.save()
        flash("User Account Updated", category="success")
        return redirect(url_for("core.index"))
    elif request.method == "GET":
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.city.data = current_user.city
        form.school.data = current_user.school
        form.age.data = current_user.age

    return render_template(
        "users/settings.html", form=form, can_disconnect=can_oauth_disconnect()
    )


@users.route("/quiz")
@login_required
def quiz():
    form = QuizForm()
    used_questions = []
    score = current_user.score
    question_number = 0
    while True:
        if form.validate_on_submit():
            right_answer = form.choosed_answer.data
            question = Questions.objects(number=question_number)
            if question.answer == right_answer:
                score += 5
        elif request.method == "GET":
            if score < 30:
                difficulty_nivel = "low"
            elif 30 <= score < 60:
                difficulty_nivel = "medium"
            else:
                difficulty_nivel = "high"
            #     take all the possible questions with wanted difficulty
            possible_questions = Questions.objects(difficulty=difficulty_nivel)
            # take all ids for those questions
            questions_id = [question.number for question in possible_questions]
            question_number = random.choice(questions_id)
            tries = 0
            # search for a questions who wasn't asked
            while question_number in used_questions and tries <= 3:
                question_number = random.choice(questions_id)
                tries += 1
            if tries == 3:
                current_user.score = score
                return
            next_question = Questions.objects(number__gt=2)
            print("question number: ", question_number)
            for q in Questions.objects:
                if q.number == question_number:
                    print(q.question)
                    form.question.data = q.question
                    form.option1.data = q.options[0]
                    form.option2.data = q.options[1]
                    form.option3.data = q.options[2]
            used_questions.append(question_number)
        return render_template(
            "users/quiz.html", form=form
        )
    # questions = Questions.objects(difficulty="low").first()
    # return jsonify(questions.number), 200


@users.route("/map")
@login_required
def maps():
    flash("You opened the map.", category="success")
    return render_template(
        "users/map.html", can_disconnect=can_oauth_disconnect()
    )


@users.route('/<template>')
@login_required
def route_template(template):
    print("1")
    try:
        if not template.endswith('.html'):
            template += '.html'
        print("2")
        # Detect the current page
        segment = get_segment(request)
        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template)
        print("3")
    except TemplateNotFound:
        print("4")
        return render_template("home/page-404.html"), 404

    except:
        print("5")
        return render_template("home/page-500.html"), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:

        segment = request.path.split('/')[-1]
        print("6")
        if segment == '':
            segment = '/index'
        print("7")
        return segment
    except:
        print("8")
        return None


@users.route("/delete_account")
@login_required
def delete_account():
    """Delete current user's account"""
    current_user.delete()
    flash("Account deleted!", category="success")
    return redirect(url_for("core.index"))


@users.route("/facebook_oauth")
def facebook_oauth():
    """Perform facebook OAuth operations"""
    return oauth_generalized("Facebook")


@users.route("/google_oauth")
def google_oauth():
    """Perform google OAuth operations"""
    return oauth_generalized("Google")


@users.route("/facebook_oauth_disconnect")
def facebook_oauth_disconnect():
    """Disconnect facebook OAuth"""
    return oauth_disconnect("Facebook")


@users.route("/google_oauth_disconnect")
def google_oauth_disconnect():
    """Disconnect google OAuth"""
    return oauth_disconnect("Google")


# ----------------------------------------------------------------------------
# HELPER METHODS
def can_oauth_disconnect():
    """Test to determine if OAuth disconnect is allowed"""
    has_gg = True if current_user.google_id else False
    has_fb = True if current_user.facebook_id else False
    has_email = True if current_user.email else False
    has_pw = True if current_user.password_hash else False

    oauth_count = [has_gg, has_fb].count(True)
    return bool(oauth_count > 1 or (has_email and has_pw))


def oauth_disconnect(oauth_client):
    """Generalized OAuth disconnect"""
    if not current_user.is_authenticated:
        return redirect(url_for("users.login"))

    db_oauth_key = str(oauth_client).lower() + "_id"

    current_user[db_oauth_key] = None
    current_user.save()

    flash(f"Disconnected from {oauth_client}!")
    return redirect(url_for("users.settings"))


def oauth_generalized(oauth_client):
    """Perform OAuth registration, login, or account association"""
    # Get response object for the WerkzeugAdapter.
    response = make_response()
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), oauth_client)
    # If there is no LoginResult object, the login procedure is still pending.
    if not result:
        return response
    # If there is no result.user something went wrong
    if not result.user:
        flash("Login failed, try again with another method.", category="error")
        return redirect(url_for("users.login"))

    # Update user to retrieve data
    result.user.update()

    db_oauth_key = str(oauth_client).lower() + "_id"

    client_name = result.user.name
    client_oauth_id = result.user.id

    # Check if user in database with this OAuth login already exists
    lookup = {db_oauth_key: client_oauth_id}
    user = User.objects(**lookup).first()

    # Should only enter this block if adding another OAuth to the account
    # in user settings
    if current_user.is_authenticated:
        # OAuth method is already linked to an account, do nothing
        if user:
            flash(
                f"That {oauth_client} account is already linked with an account. "
                f"Please log in to that account through {oauth_client} and un-link "
                "it from that account to link it to this account.",
                category="danger",
            )
        # Add this OAuth method to current user
        else:
            current_user[db_oauth_key] = client_oauth_id
            current_user.save()
        # Should only get here from "settings" so return there
        return redirect(url_for("users.settings"))

    # Register a new user with this OAuth authentication method
    if not user:
        # Generate a unique username from client's name found in OAuth lookup
        base_username = client_name.lower().split()[0]
        print(base_username)
        username = base_username
        attempts = 0
        while True:
            user = User.objects(username=username).first()
            if user:
                attempts += 1
                username = base_username + str(attempts)
            else:
                break
        # Create user and save to database
        user_data = {
            "username": username,
            "firstname": client_name,
            db_oauth_key: client_oauth_id,
        }
        user = User(**user_data)
        user.save()
        flash("Thanks for registering!", category="success")

    # Else user was found and is now authenticated
    # Log the found-or-created user in
    return login_and_redirect(user)


def login_and_redirect(user):
    """Logs in user, flashes welcome message and redirects to index"""
    login_user(user)
    flash(f"Welcome {user.username}!", category="success")
    return redirect(url_for("core.index"))
