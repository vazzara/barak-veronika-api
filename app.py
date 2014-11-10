import flask
from flask import Flask, render_template, request, redirect, session, url_for, escape, flash

app = Flask(__name__)


if __name__ == "__main__":
    app.debug = True
    app.run(port = 5005) #when everyone in class tests their projects we avoid 5000"
