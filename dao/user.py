from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(User).all()

    def get_user_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    #def delete(self, username):
        #user = self.get_user_by_id(username)
        #self.session.delete(user)
        #self.session.commit()

    def update(self, user_d):
        email = user_d.get('email')
        self.session.query(User).filter(User.email == email).update(user_d)
        self.session.commit()
        return self.get_user_by_email(email)

    def get_user_by_id(self, uid):
        return self.session.query(User).filter(User.id == uid).first()
