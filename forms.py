from flask_wtf import FlaskForm;
from wtforms import StringField, PasswordField, TextAreaField, RadioField, IntegerField, FloatField, BooleanField, SelectField;
from wtforms.validators import InputRequired, Optional, Length, EqualTo, Email, NumberRange;

# General Field Length Constants
MAX_URL_LENGTH = 150;
DESCRIPTION_MAX_LENGTH = 512;
MESSAGE_MAX_LENGTH = 5000;

# User Field Constants
GENERAL_FIELD_MAX_LENGTH = 16;
USERNAME_LENGTH = [4, 32];  # username between 4 and 32 characters.
PASSWORD_LENGTH = [6, 16];  # password between 6 and 16 characters.

# Pet Field Constants
VALID_PET_AGES = [0, 50];       # between 0 and 50.
VALID_PET_WEIGHT = [0, 500];    # between 0 and 500.

class LoginForm(FlaskForm):
    
    username = StringField('Username', 
        validators=[InputRequired(), Length(min=USERNAME_LENGTH[0], max=USERNAME_LENGTH[1], message=f'Username must be between {USERNAME_LENGTH[0]} and {USERNAME_LENGTH[1]} characters.')
            ]);
    encrypted_password = PasswordField('Password', 
        validators=[
            InputRequired(), 
            Length(min=PASSWORD_LENGTH[0], max=PASSWORD_LENGTH[1], message=f'Enter a password between {PASSWORD_LENGTH[0]} and {PASSWORD_LENGTH[1]} characters.')
            ]);

class RegisterForm(LoginForm):
    
    confirm_password = PasswordField('Confirm Password', 
        validators=[
            Length(min=PASSWORD_LENGTH[0], max=PASSWORD_LENGTH[1]),
            EqualTo('encrypted_password', message='Passwords must match.')
        ]);

    first_name = StringField('First Name', validators=[InputRequired(), Length(max=GENERAL_FIELD_MAX_LENGTH, message=f'Enter the first {GENERAL_FIELD_MAX_LENGTH} characters of your first name.')]);
    last_name = StringField('Last Name', validators=[InputRequired(), Length(max=GENERAL_FIELD_MAX_LENGTH, message=f'Enter the first {GENERAL_FIELD_MAX_LENGTH} characters of your last name.')]);
    email = StringField('Email', validators=[InputRequired(), Length(max=MAX_URL_LENGTH), Email()]);
    
class EleveatedMessageForm(FlaskForm):
    '''Send a message to request a Rescue Agency Account.'''
    
    first_name = StringField('First Name', validators=[InputRequired(), Length(max=GENERAL_FIELD_MAX_LENGTH, message=f'Enter the first {GENERAL_FIELD_MAX_LENGTH} characters of your first name.')]);
    last_name = StringField('Last Name', validators=[InputRequired(), Length(max=GENERAL_FIELD_MAX_LENGTH, message=f'Enter the first {GENERAL_FIELD_MAX_LENGTH} characters of your last name.')]);
    agency_name = StringField('Agency Name', validators=[InputRequired(), Length(max=GENERAL_FIELD_MAX_LENGTH, message=f'Enter the first {GENERAL_FIELD_MAX_LENGTH} characters of your organization\'s name.')]);
    agency_type = SelectField('Agency Type', validators=[InputRequired()], 
        choices=[
            (1, 'Public, Government'),
            (2, 'Private, 501\(c2\)'),
            (3, 'Private, 501\(c3\)'),
            (4, 'Private, None of the above'),
            (5, 'Mixed')
        ],
        coerce=int);
    email = StringField('Email', validators=[InputRequired(), Length(max=MAX_URL_LENGTH), Email()]);
    message = TextAreaField(f'Message \(Optional, {MESSAGE_MAX_LENGTH} Characters\)', 
        validators=[Optional(), Length(max=MESSAGE_MAX_LENGTH, message=f'Max message length: {MESSAGE_MAX_LENGTH} characters.')]);

class EditUserForm(FlaskForm):
    
    username = StringField('Username',
        render_kw={'readonly': True});  # disabled
        # ... = ...(label, ..., render_kw={'readonly': True});
            # Make a form element read-only: https://stackoverflow.com/a/43215676
    first_name = StringField('First Name', 
        validators=[InputRequired(), Length(max=GENERAL_FIELD_MAX_LENGTH, message=f'Enter the first {GENERAL_FIELD_MAX_LENGTH} characters of your first name.')]);
    last_name = StringField('Last Name',
        validators=[InputRequired(), Length(max=GENERAL_FIELD_MAX_LENGTH, message=f'Enter the first {GENERAL_FIELD_MAX_LENGTH} characters of your last name.')]);
    email = StringField('Email',
        render_kw={'readonly': True});  # disabled
    description = TextAreaField('Description', 
        validators=[InputRequired(), Length(max=DESCRIPTION_MAX_LENGTH, message='Describe yourself in {DESCRIPTION_MAX_LENGTH} charactesr or less.')]);

    password = PasswordField('Password', 
        validators=[
            InputRequired(), 
            Length(min=PASSWORD_LENGTH[0], max=PASSWORD_LENGTH[1], message=f'Enter a password between {PASSWORD_LENGTH[0]} and {PASSWORD_LENGTH[1]} characters.')
            ]);

class AddEditPetForm(FlaskForm):

    pet_name = StringField('Pet Name',
        validators=[
            InputRequired(),
            Length(max=GENERAL_FIELD_MAX_LENGTH, message=f'Enter the first {GENERAL_FIELD_MAX_LENGTH} characters of your first name.')
        ]);
    description = TextAreaField('Description', 
        validators=[InputRequired(), Length(max=DESCRIPTION_MAX_LENGTH, message='Pet description in {DESCRIPTION_MAX_LENGTH} charactesr or less.')]);
    image_url = StringField('Pet Image (file upload not available)', validators=[InputRequired(), Length(max=MAX_URL_LENGTH)]);
    
    gender = RadioField('Gender',
        validators=[InputRequired()], 
        choices=[
            (True, 'Male'),
            (False, 'Female')
        ],
        render_kw={
            'class':''
        });
    sterilized = BooleanField('Sterilized (Spayed / Neutered)?', 
        false_values=False,
        render_kw={
            'class':''
        });
    
    estimated_age = IntegerField('Pet Age', 
        validators=[
            InputRequired(), 
            NumberRange(min=VALID_PET_AGES[0], max=VALID_PET_AGES[1], message=f'Valid Pet Age between: {VALID_PET_AGES[0]} and {VALID_PET_AGES[1]}')
            ]);
    age_certainty = BooleanField('Certain of Age?')
    weight = FloatField('Pet Weight',
        validators=[
            InputRequired(),
            NumberRange(min=VALID_PET_WEIGHT[0], max=VALID_PET_WEIGHT[1], message=f'Valid Pet Age between: {VALID_PET_WEIGHT[0]} and {VALID_PET_WEIGHT[1]}')
        ]);

    pet_classification = SelectField('Pet Classficiation', validators=[InputRequired()], coerce=int);
    primary_breed = SelectField('Pet Breed', validators=[InputRequired()], coerce=int);
        # null the selection in new pet logic (models.py) if the pet_classificatino is not dog or cat. doesn't need to be that polished.
        # manually set it to required if pet_classificatino is dog or cat.

    coat_hair = SelectField('Coat Hair Type', validators=[InputRequired()], coerce=int);
    coat_pattern = SelectField('Coat Pattern', validators=[Optional()], coerce=int);

    primary_light_shade = SelectField('Primary Light Shade', validators=[InputRequired()], coerce=int);
    primary_dark_shade = SelectField('Primary Dark Shade', validators=[InputRequired()], coerce=int);

    trained = BooleanField('Trained?',
        false_values=False,
        render_kw={
            'class':''
        });
    medical_records_uptodate = BooleanField('Up to Date Medical Records?',
        false_values=False,
        render_kw={
            'class':''
        });

    special_needs = TextAreaField('Special Needs', validators=[Optional(), Length(max=DESCRIPTION_MAX_LENGTH, message=f'Max Length is {DESCRIPTION_MAX_LENGTH}')])

