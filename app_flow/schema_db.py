from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app_flow.db import db


class Company(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    type_company = db.Column(db.String, nullable=False)
    company_name = db.Column(db.String, nullable=False)
    company_email = db.Column(db.String, unique=True, nullable=False)
    tax_identification_number = db.Column(db.Integer,
                                          unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def set_password(self, password: str) -> str:
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return "Company {}, id - {}".format(self.company_name, self.id)


class Employee(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(
        db.Integer, db.ForeignKey(
            'company.id', ondelete='CASCADE'
        ), nullable=False)
    last_name = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    patronymic = db.Column(db.String, nullable=False)
    employee_email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def set_password(self, password: str) -> str:
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return "User {} {} {}, id - {}".format(
            self.last_name, self.first_name, self.patronymic,
            self.id)
