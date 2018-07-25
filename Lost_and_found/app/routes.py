# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 23:06:55 2018

@author: Cristina
"""

from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LostForm, FoundForm

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/lost", methods=["GET", "POST"])
def search():
    #get data from LostForm
    form = LostForm()
    #if valid data, redirect to main page and show the contents of form
    #as a flash message (for testing purposes).
    #To be changed later on when database is introduced
    if form.validate_on_submit():
        flash("Search requested for item {}, colour {} and {}, last seen in {}, on {}"
              .format(form.item.data, form.colour1.data, form.colour2.data,
                form.location.data, form.date.data))
        return redirect(url_for("index"))
    return render_template("lost.html", form=form)


@app.route("/found", methods=["GET", "POST"])
def add():
    #get data from FoundForm
    form = FoundForm()
    #if valid data, redirect to main page and show the contents of form
    #as a flash message (for testing purposes).
    #To be changed later on when database is introduced
    if form.validate_on_submit():
        flash("Add requested for item {}, colour {} and {}, last seen in {}, on {}"
              .format(form.item.data, form.colour1.data, form.colour2.data,
                form.location.data, form.date.data))
        return redirect(url_for("index"))
    return render_template("found.html", form=form)