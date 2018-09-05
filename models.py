from app import db


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    client_ip = db.Column(db.String())
    created_at = db.Column(db.DateTime())

    def __init__(self, text, client_ip, created_at):
        self.text = text
        self.client_ip = client_ip
        self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)