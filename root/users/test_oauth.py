"""A file for testing OAuth setup"""
from authomatic.adapters import WerkzeugAdapter
from flask import Flask, make_response, request

from oauth_config import authomatic

app = Flask(__name__)


@app.route("/")
def index():
    """Landing page for our OAuth test with hyperlinks to each OAuth test"""
    return """
    <p><a href="/users/facebook_oauth">Go to Facebook</a></p>
    <p><a href="/users/google_oauth">Go to Google</a></p>
    """


@app.route("/users/facebook_oauth")
def facebook_oauth():
    """Ask for Facebook OAuth data"""
    return oauth_generalized("Facebook")


@app.route("/users/google_oauth")
def google_oauth():
    """Ask for Google OAuth data"""
    return oauth_generalized("Google")


def oauth_generalized(oauth_client):
    """Generalized OAuth data retrieval"""
    # Get response object for the WerkzeugAdapter.
    response = make_response()
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), oauth_client)
    # If there is no LoginResult object, the login procedure is still pending.
    if not result:
        return response
    # If there is no result.user something went wrong
    if not result.user:
        return "Failed to retrieve OAuth user"

    # Update user to retrieve data
    result.user.update()

    # Return a dictionary containing the user data
    # Flask automatically converts the dictionary to JSON
    return result.user.data


if __name__ == "__main__":
    # Initiate app
    app.run()
