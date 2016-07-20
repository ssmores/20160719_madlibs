from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Connecting to correct template dependant on desire to play game."""
    
    user_response = request.args.get("is_game_ready")

    if user_response:
        #If the user checked the box, use the madlibs.html template.
        return render_template("game.html")
    else: 
        #If the user did not check the box, go to the goodbye.html template.
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Creates a madlib story based on user input values. """
    text_name = request.args.get("character")

    color_type = request.args.get("color_option")

    noun_type = request.args.get("favnoun")

    adj_type = request.args.get("favadjective")

    likes_fish = request.args.get("likes_fish")

    votes = request.args.get("vote")
    print votes

    return render_template("madlibs.html", color=color_type, 
        noun=noun_type, person=text_name, adjective=adj_type, likes_fish=likes_fish, votes=votes)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
