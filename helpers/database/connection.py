from datetime import datetime

from mongoengine import *
from mongoengine.context_managers import *

from helpers.tools.logger import Logger
from settings import Settings

log = Logger(__name__)


def _is_plural(collection: str) -> bool:
    """Determines if an object type is in its plural form or not."""
    if collection.endswith('s'):
        return True
    return False


def _make_plural(collection: str) -> str:
    """Returns a plural form of an object's `__name__` attribute if it is singular."""
    return f"{collection}s"


def find_collection(obj: object) -> type(object):
    """Returns the actual type name of the provided object formatted for MongoDB collection queries."""
    collection = type(obj).__name__.lower()
    if _is_plural(collection):
        return collection
    else:
        return _make_plural(collection)


def add(obj) -> bool:
    """Allows the creation of a new database object document given an object."""
    try:
        obj.switch_collection(find_collection(obj))  # Make sure we insert our document in the proper collection.
        obj.save()
        return True
    except Exception as e:
        if Settings.log_verbosity >= Logger.Verbosity.debug:
            log.error(f"Error: {e}")
        return False


def save(obj) -> bool:
    """Updates the provided object's document within the database if it exists."""
    try:
        obj.switch_collection(find_collection(obj))
        obj.entry_modified = datetime.now()
        result = obj.update(**obj.to_mongo())
        return result
    except OperationError:
        return False


def remove(obj) -> bool:
    """Removes the provided object's document from the database."""
    try:
        obj.switch_collection(find_collection(obj))
        obj.delete()
        return True
    except Exception as e:
        if Settings.log_verbosity >= Logger.Verbosity.debug:
            log.error(f"Error: {e}")
        return False
