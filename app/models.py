from app import db

class Note(db.Model):

    __tablename__ = "note"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    
    def __init__(self, text):
        self.text = text

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Note.query.all()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Note: {}>".format(self.text)