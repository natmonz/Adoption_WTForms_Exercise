from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL, Length, NumberRange


class addPetForm(FlaskForm):
    """Form to List pet up for Adoption"""
    name = StringField('Pet Name', 
                       validators=[InputRequired()])
    
    species = SelectField("Species",
        choices=[("cat", "Cat"), ("dog", "Dog")],)
    
    photo_url = StringField('Photo URL', 
                            validators=[Optional(), 
                                        URL()])
    
    age = IntegerField('Age', 
                     validators=[Optional(), 
                                NumberRange(min=0, max=30)])
    
    notes = StringField('Notes', 
                        validators=[Optional(), 
                                    Length(min=10)])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],)

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],)

    available = BooleanField("Available?")