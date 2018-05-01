#from flask_login import UserMixin
#from werkzeug.security import generate_password_hash, check_password_hash

from app import db

class Word(db.Model):
    """
    Create the words table
    """

    __tablename__ = 'rijeci'

    rijec = db.Column(db.Unicode(60, collation='utf8_bin'),
                      primary_key=True)
    konkretnost_m = db.Column(db.Float, index=True)
    konkretnost_std = db.Column(db.Float, index=True)
    predocivost_m = db.Column(db.Float, index=True)
    predocivost_std = db.Column(db.Float, index=True)
    dob_usvajanja_m = db.Column(db.Float, index=True)
    dob_usvajanja_std = db.Column(db.Float, index=True)
    subj_frekvencija_m = db.Column(db.Float, index=True)
    subj_frekvencija_std = db.Column(db.Float, index=True)

    def __repr__(self):
        return u'<Word: {}>'.format(self.rijec)
