from flask_sqlalchemy import SQLAlchemy;
from flask_bcrypt import Bcrypt;
from datetime import datetime;              # timestamp for datetime.utcnow

db = SQLAlchemy();
bcrypt = Bcrypt();

def connectDatabase(app):
    db.app = app;
    db.init_app(app);

''' =============USER MODEL=============
'''
class User(db.Model):
    # seeded, injected, and api_created
    
    __tablename__ = 'users';

    username = db.Column(db.Text, nullable = False, unique = True, primary_key = True);
        # limit to 32 in Form
    encrypted_password = db.Column(db.Text, nullable = False);
    first_name = db.Column(db.Text, nullable = False);
        # if is_elevated, String(128), in `forms.py` make it Length(max=32) 
    last_name = db.Column(db.Text, nullable = True);
        # limit to 32 in Form
        # if is_elevated, it is Null, in `forms.py` make it InputRequired() because normal user cannot get elevated priviledges
    email = db.Column(db.Text, nullable = False);
    description = db.Column(db.Text, nullable = True);
        # limit to 512 in Form
    image_url = db.Column(db.Text, nullable = False, default='_defaultUser.jpg')
    is_elevated = db.Column(db.Boolean, nullable = False, default = False, server_default='false'); # do not show on `forms.py` to register

    # insert foreignkey rel, roletable

    def __repr__(self):
        '''Self-representation for a User instance.'''
        return f'<User {self.username}: {self.first_name}>';
    
    @classmethod
    def cleanRequestData(cls, requestData, method='CreateUser'):
        '''Clean request data.'''

        mutableRequestData = dict(requestData);

        if mutableRequestData.get('csrf_token'):
            mutableRequestData.pop('csrf_token');

        if method == 'EditUser':
            mutableRequestData.pop('username');
            mutableRequestData.pop('email');
            mutableRequestData.pop('password');

        return mutableRequestData;

    @classmethod
    def returnUserbyUsername(cls, username):
        ''''''
        userObject = cls.query.get_or_404(username);

        return userObject;

    @classmethod
    def createUser(cls, requestData):
        '''Register a user. Create and insert a new User into the database.'''

        cleanedData = cls.cleanRequestData(requestData);

        password = cleanedData.get('encrypted_password');
        hashedPassword = bcrypt.generate_password_hash(password).decode('UTF-8');

        cleanedData['encrypted_password'] = hashedPassword;
        
        db.session.add(cls(**cleanedData));
        db.session.commit();
        return;

    @classmethod
    def authentication(cls, username, password):
        '''Authentication, either for login or an extra authentication key. The entered credentials.'''

        UserObject = cls.returnUserbyUsername(username);

        if UserObject and bcrypt.check_password_hash(UserObject.encrypted_password, password):
            return UserObject;
        
        else:
            return False;
    
    def updateUser(self, requestData):
        '''Update the user object. Update an entry in User by primary key ("username").'''

        cleanedData = User.cleanRequestData(requestData, method='EditUser');
            # check the password in `app.py`
        db.session.query(User).filter(User.username == self.username).update(cleanedData);
        db.session.commit();
        return;


    def deleteUser(self):
        '''Delete the user. Delete the record from the table.'''
        # Todo.
        
        # dangerousConfirmation = User.;

        # if dangerousConfirmation:
        #     db.session.delete(self);
        #     db.session.commit();
        
        return;


    # ADMIN METHODS
    @classmethod
    def returnAllUsers(cls):
        ''''''

        return cls.query.all();

    @classmethod
    def deleteUserByUsername(cls, username):
        ''''''

        selectedUser = db.session.get_or_404(username);

        cls.userNotFound(selectedUser);

        if not selectedUser:
            
        # confirmation logic in routes
        # db.session.query()
            return;

        return;
    
    
class Role(db.Model):
    # seeded and db edit only.

    __tablename__ = 'role';

    id = db.Column(db.SmallInteger, primary_key = True);
    role_name = db.Column(db.String(16), nullable = False);
        # admin, rescueAgency, user
    
    def __repr__(self):
        '''Self-representation for a Role instance.'''
        return f'<Role {self.id}: {self.role_name}>';

class RoleTable(db.Model):
    # seeded and db edit only.

    __tablename__ = 'userrole_join';

    user_username = db.Column(
        db.String(32), 
        db.ForeignKey(User.username, ondelete='CASCADE', onupdate='CASCADE'),
        primary_key = True);
    role_id = db.Column(db.SmallInteger, 
        db.ForeignKey(Role.id, ondelete='CASCADE', onupdate='CASCADE'),
        primary_key = True);

    userReference = db.relationship('User', backref=db.backref('userAlias', cascade='all, delete'));
    roleReference = db.relationship('Role', backref=db.backref('roleJoinAlias', cascade='all, delete'));

    def __repr__(self):
        '''Self-representation for a RoleTable instance.'''
        return f'<RoleTable {self.user_username}: {self.role_id}>';

''' =============PET MODEL=============
'''
class Pet(db.Model):
    # seeded, injected, and api_created
    
    __tablename__ = 'pet';

    id = db.Column(db.BigInteger, autoincrement = True, primary_key = True);
        # Todo.
    pet_name = db.Column(db.Text, nullable = False);
        # limit the character in form (32)
    description = db.Column(db.Text, nullable = True);
        # limit the character in form (512)
    image_url = db.Column(db.Text, nullable = True, default = 'default_pet.png');
    publish_time = db.Column(db.DateTime, nullable = False, default = datetime.utcnow());
    gender = db.Column(db.Boolean, nullable = False);
        # F => Female, T => Male,
    sterilized = db.Column(db.Boolean, nullable = False);
    estimated_age = db.Column(db.Integer, nullable = False, default = 0)
    age_certainty = db.Column(db.Boolean, nullable = False, default = False);
        # F => Unsure, T => Sure
    weight = db.Column(db.Integer, nullable = False, default = 0);
    pet_classification = db.Column(db.SmallInteger, db.ForeignKey());
    coat_hair = db.Column(db.SmallInteger, db.ForeignKey());
    coat_pattern = db.Column(db.SmallInteger, db.ForeignKey());
    primary_light_shade = db.Column(db.SmallInteger, db.ForeignKey(), default = 0);
    primary_dark_shade = db.Column(db.SmallInteger, db.ForeignKey(), default = 0);
    trained = db.Column(db.Boolean, nullable = False, default = False);
    medical_record_uptodate = db.Column(db.Boolean, nullable = False, default = False);
    special_needs = db.Column(db.Text, nullable = True);

    def __repr__(self):
        '''Self-representation for a PetUserJoin instance.'''
        return f'<Pet {self.id}: {self.pet_name}>';
    
    @classmethod
    def cleanRequestData(cls, requestData):
        '''Clean request data.'''

        mutableRequestData = dict(requestData);

        if mutableRequestData.get('csrf_token'):
            mutableRequestData.pop('csrf_token');

        return mutableRequestData;

    @classmethod
    def createPet(cls,requestData):
        # Todo.
        pass;

    @classmethod
    def updatePet(cls,requestData):
        # Todo.
        pass;
    
    def removePet(self):
        # Todo. Requires authorization.
        pass;


class PetUserJoin(db.Model):
    # seeded and injected

    __tablename__ = 'petuser_join';

    user_id = db.Column(db.String(32), db.ForeignKey(User.username, ondelete='CASCADE', onupdate='CASCADE'), primary_key = True);
    pet_id = db.Column(db.BigInteger, db.ForeignKey(Pet.id, ondelete='CASCADE', onupdate='CASCADE'), primary_key = True);

    userReference = db.relationship('User', backref=db.backref('userJoinAlias', cascade='all, delete'));
    petReference = db.relationship('Pet', backref=db.backref('petJoinAlias', cascade='all, delete'));
        # Todo: through relationship unnecessary?

    def __repr__(self):
        '''Self-representation for a PetUserJoin instance.'''
        return f'<Pet-User {self.pet_id}-{self.user_id}>';

    @classmethod
    def returnPetUserByPrimaryKey(cls, username, petID):
        '''Probably unused but here by default.'''
        return cls.query.get_or_404((username, petID));

    @classmethod
    def returnPetUserByUsername(cls, username):
        '''Return all pets uploaded by a specified User.'''
        return cls.query.filter(cls.user_id == username).all();

''' =============PET CATEGORIES=============
'''
class PetSpecie(db.Model):
    # seeded; parent model = Pet

    __tablename__ = 'petspecie';

    id = db.Column(db.SmallInteger, primary_key = True);    # not smallserial
    specie_name = db.Column(db.String(16), nullable = False);
    specie_fa = db.Column(db.Text, nullable = False);
        # 0-100 common_mammals:
        #   0   dog (<i class="fa-duotone fa-dog"></i>)
        #   1   cat (<i class="fa-solid fa-cat"></i>)
        # 101 else
        #   101 bird (<i class="fa-duotone fa-bird"></i>);
        #   102 reptile (<i class="fa-duotone fa-snake"></i>); 
        #   103 fish (<i class="fa-duotone fa-fish-fins"></i>)
        #   104 amphibia (<i class="fa-duotone fa-frog"></i>)
        #   999 plant ()

    def __repr__(self):
        '''Self-representation for a PetSpecie instance.'''
        return f'<PetSpecie {self.id}: {self.specie_name}>';

class CoatDescription(db.Model):
    # seeded; parent model = Pet

    __tablename__ = 'coatdescription';
    
    id = db.Column(db.SmallInteger, primary_key = True);    # smallint
    coat_description = db.Column(db.Text, nullable = False);
        #   0: Unknown
        #   1: Straight
        #   2: Mixed
        #   3: Curly
        #   4: Bald
        #   Coat Patterns: 100+

    def __repr__(self):
        '''Self-representation for a CoatDescription instance.'''
        return f'<CoatDescription {self.id}: {self.coat_description}>';

class Color(db.Model):
    # seeded; parent model = Pet

    __tablename__ = 'color';

    id = db.Column(db.SmallInteger, primary_key = True);    # not smallserial
        #   Null: 0
        #   Light Colors: 1 - 100
        #   Dark Colors: 101 - 200
    color_name = db.Column(db.String(16), nullable = False);
    color_hex = db.Column(db.String(7), nullable = False);

    def __repr__(self):
        '''Self-representation for a Color instance.'''
        return f'<Color {self.id}: {self.color_name} ({self.color_hex})>';

class Breed(db.Model):
    # seeded
    # only enable this for "cats" and "dogs"

    __tablename__ = 'breed';

    id = db.Column(db.SmallInteger, primary_key = True);    # not smallserial
        # Unknown: 0
        # Cat Breeds: 1 - 1000
        # Dog Breeds: 1001 - 2000
        # Plants: 2001 - 3000 (really just: decorative tree, fruit tree, indoor non-tree, outdoor non-tree)
        # Birds, Amphibians, etc. are not given categorization
    breed_name = db.Column(db.Text, nullable = False);
    breed_image = db.Column(db.Text, nullable = True, default = 'default_pet.png');

    def __repr__(self):
        '''Self-representation for a Breed instance.'''
        return f'<Breed {self.id}: {self.breed_name}>';

class PrimaryBreedTable(db.Model):
    '''Only for dogs and cats.'''
    # seeded, injected, and api_created

    __tablename__ = 'primarybreed_join';
    
    pet_id = db.Column(db.BigInteger, db.ForeignKey(Pet.id, ondelete='CASCADE', onupdate='CASCADE'), primary_key = True);
    breed_id = db.Column(db.SmallInteger, db.ForeignKey(Breed.id, ondelete='CASCADE', onupdate='CASCADE'), primary_key = True);

    petReference = db.relationship('Pet', backref=db.backref('petJoinAlias', cascade='all, delete'));
    primaryBreedReference = db.relationship('Breed', backref=db.backref('primaryBreedJoinAlias', cascade='all, delete'));

    def __repr__(self):
        '''Self-representation for a Pet-Breed Join instance.'''
        return f'<PrimaryBreedTable {self.pet_id}: {self.breed_id}>';

    @classmethod
    def createBreedJoinEntry(cls, requestData):
        # Todo.
        
        # if breed == none, set to unknown

        return;
    
    @classmethod
    def updateBreedEntry(self):
        ''''''
        # Todo.
        return;

    def resetBreedEntry(self):
        ''''''
        # Todo.
        return;