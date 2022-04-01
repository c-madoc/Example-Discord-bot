from helpers.database.connection import *


class Users:
    """ The entire Users collection in the database. """
    class User(DynamicDocument):
        """ An individual user within the Users collection. """
        timestamp = datetime.now()
        entry_created = DateTimeField(required=True, default=timestamp)
        entry_modified = DateTimeField(required=True, default=timestamp)
        uid = DynamicField(required=True)
        name = DynamicField(required=True)
        discriminator = DynamicField(required=True)

    def add(self, _id: int, name: str, discriminator: str) -> bool:
        """ Adds a new user to the database. """
        return add(self.User(uid=_id, name=name, discriminator=discriminator))

    def get(self, _id: str) -> User:
        """ Gets an existing user from the database. """
        with switch_collection(self.User, find_collection(self)) as Collection:
            return Collection.objects(uid=_id).first()

    def get_all(self) -> User:
        """ Gets all users from the database. """
        with switch_collection(self.User, find_collection(self)) as Collection:
            return Collection.objects.all()
