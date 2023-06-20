from flask import Flask, render_template, flash, redirect, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, connect_db, db
from forms import addPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
toolbar= DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
app.app_context().push()


@app.route('/')
def list_pets():
    pets = Pet.query.all()
    return render_template('listing.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    '''Add Pet Form Handler'''
    form = addPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f'{new_pet.name} successfully added.')
        return redirect(url_for('list_pets'))
    else:
       return render_template('add_pet_form.html', form=form)
    
@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Edit selected Pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name}'s information has been updated.")
        return redirect(url_for('list_pets'))
    else:
        return render_template('pet_edit_form.html', form=form, pet=pet)
    
@app.route('/api/pets/<int:pet_id>', methods=['GET'])
def api_get_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)