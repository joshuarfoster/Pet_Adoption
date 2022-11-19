from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional
class AddPet(FlaskForm):
    """Form for adding Pets"""

    name = StringField("Name",
                        validators=[InputRequired()])
    species = SelectField("Species", 
                        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", 
                        validators=[Optional(),URL()])
    age = IntegerField("Age", 
                        validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes",
                        validators=[Optional(), Length(min=10)])