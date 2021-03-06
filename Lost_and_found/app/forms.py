# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 19:27:16 2018

@author: Cristina
"""

#Login form


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators
from wtforms.fields.html5 import DateField


class LostForm(FlaskForm):
    """
    Class object: lost item form
    Attributes: item, colour1, colour2, location, date
    """
    colours = [("", ""), ("black", "Black"), ("blue", "Blue"), ("brown", "Brown"),
               ("green", "Green"), ("grey", "Grey"), ("orange", "Orange"), 
               ("pink", "Pink"), ("purple", "Purple"), ("red", "Red"), 
               ("white", "White"), ("yellow", "Yellow")]
    locations = [("", ""), ("cafeteria", "Cafeteria"), ("class01", "Classroom01"),
                 ("class02", "Classroom02"), ("library", "Library"), 
                 ("restroom", "Restroom")]
    item = StringField("Lost item")
    colour1 = SelectField("Colour 1", choices=colours)
    colour2 = SelectField("Colour 2", choices=colours)
    location = SelectField("Last known location", choices=locations)
    date = DateField("Date lost", format="%Y-%m-%d", 
                     validators=[validators.Optional(),] )
    submit = SubmitField("Search")

    
class FoundForm(FlaskForm):
    """
    Class object: found item form
    Attributes: item, colour1, colour2, location, date
    """
    item = StringField("Found item")
    colours = [("", ""), ("black", "Black"), ("blue", "Blue"), ("brown", "Brown"),
               ("green", "Green"), ("grey", "Grey"), ("orange", "Orange"), 
               ("pink", "Pink"), ("purple", "Purple"), ("red", "Red"), 
               ("white", "White"), ("yellow", "Yellow")]
    locations = [("", ""), ("cafeteria", "Cafeteria"), ("class01", "Classroom01"),
                 ("class02", "Classroom02"), ("library", "Library"), 
                 ("restroom", "Restroom")]
    colour1 = SelectField("Colour 1", choices=colours)
    colour2 = SelectField("Colour 2", choices=colours)
    location = SelectField("Location", choices=locations)
    date = DateField("Date found", format="%Y-%m-%d", 
                     validators=[validators.Optional(),] )
    submit = SubmitField("Add")
    