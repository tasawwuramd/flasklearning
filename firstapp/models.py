from firstapp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), index=True)
    lname = db.Column(db.String(100), index=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return "<User : {}>".format(self.fname+' '+self.lname)

#   The User class is inherited from db.Model.
#   It also defines four fields as instances of db.Column Class.
#   The db.Column class takes field type as an argument and other optional arguments.
