import uuid
import datetime
from passlib.hash import sha256_crypt
from db import db


class UserModel(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.String(36), primary_key=True, default=str(
        uuid.uuid4()), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), nullable=False, onupdate=datetime.datetime.now())

    def __init__(self, name, birth_date, email, cpf, password, admin):
        self.name = name
        self.birth_date = birth_date
        self.email = email
        self.cpf = cpf
        self.password = password
        self.admin = admin

    def encryptPassword(self, password):
        pswencrypt = sha256_crypt.encrypt(password)
        return pswencrypt

    def checkPassword(self, password):
        return sha256_crypt.verify(password, self.password)

    def saveUser(self):
        self.password = self.encryptPassword(self.password)
        db.session.add(self)
        db.session.commit()

    def updateUser(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def deleteUser(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth_date': self.birth_date.strftime('%d/%m/%Y'),
            'email': self.email,
            'cpf': self.cpf,
            'admin': self.admin,
            'created_at': self.created_at.strftime('%d/%m/%Y %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%d/%m/%Y %H:%M:%S')
        }

    @staticmethod
    def getOneUser(id):
        return UserModel.query.filter_by(id=id).first()

    @staticmethod
    def getAllUsers():
        return UserModel.query.all()

    @staticmethod
    def getUserByEmail(email):
        return UserModel.query.filter_by(email=email).first()

    @staticmethod
    def login(email, password):
        try:
            user = UserModel.getUserByEmail(email)
        except:
            return None
        if user.checkPassword(password):
            return user.json()
        return None
