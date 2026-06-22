from app import app
from flask import render_template, session, redirect, request, url_for
import os

from app.settings_manager import load_settings, save_settings
from app.statistics_manager import load_statistics
from app.profiles_manager import load_profiles, save_profiles
from app.math_generator import generate_example


@app.route("/")
def index():
    session["correct"] = 0
    session["wrong"] = 0
    return render_template("index.html")


@app.route("/select/<mode>")
def select(mode):
    session["mode"] = mode
    return redirect(url_for("game"))


@app.route("/game")
def game():

    example = generate_example(session["mode"])

    session["answer"] = example["answer"]

    message=message,
    success=success

    return render_template(
        "game.html",
        num1=example["num1"],
        num2=example["num2"],
        operation=example["operation"],
        correct=session["correct"],
        wrong=session["wrong"],
        stars=session["stars"]
    )


@app.route("/check", methods=["POST"])
def check():

    user_answer = int(request.form["answer"])

    if user_answer == session["answer"]:
        session["correct"] += 1
        session["stars"] += 1

        session["message"] = "🎉 Молодец!"
        session["success"] = True

    else:
        session["wrong"] += 1

        session["message"] = "🙂 Попробуй ещё"
        session["success"] = False

    return redirect(url_for("game"))


@app.route("/settings")
def settings():

    settings = load_settings()

    images = os.listdir("app/static/backgrounds")

    return render_template(
        "settings.html",
        settings=settings,
        images=images
    )


@app.route("/save_settings", methods=["POST"])
def save_settings_route():

    settings = load_settings()

    settings["background_color"] = request.form["background_color"]

    settings["background_image"] = request.form["background_image"]

    settings["theme"] = request.form["theme"]

    save_settings(settings)

    return redirect(url_for("settings"))


@app.route("/profiles")
def profiles():

    profiles = load_profiles()

    return render_template(
        "profiles.html",
        profiles=profiles
    )


@app.route("/add_profile", methods=["POST"])
def add_profile():

    profiles = load_profiles()

    profiles.append(
        {
            "name": request.form["name"],
            "stars": 0,
            "correct": 0,
            "wrong": 0,
            "record": 0
        }
    )

    save_profiles(profiles)

    return redirect(url_for("profiles"))


@app.route("/select_profile/<int:index>")
def select_profile(index):

    session["profile_index"] = index

    return redirect(url_for("index"))


@app.context_processor
def inject_profile():

    profiles = load_profiles()

    current = None

    if "profile_index" in session:
        current = profiles[session["profile_index"]]

    return dict(current_profile=current)


@app.route("/statistics")
def statistics():

    stat = load_statistics()

    return render_template(
        "statistics.html",
        stat=stat
    )