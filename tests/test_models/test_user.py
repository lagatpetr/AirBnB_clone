import unittest
import os
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    # Set up and tear down methods
    def setUp(self):
        pass

    def tearDown(self):
        self.resetStorage()

    def resetStorage(self):
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    # Test cases for User class
    def test_instantiation(self):
        # Test instantiation of User class
        user_instance = User()
        self.assertEqual(str(type(user_instance)),
                         "<class 'models.user.User'>")
        self.assertIsInstance(user_instance, User)
        self.assertTrue(issubclass(type(user_instance), BaseModel))

    # Other test methods...

    def test_attributes(self):
        # Test the attributes of User class
        attributes = storage.attributes()["User"]
        user_instance = User()
        for attribute_name, attribute_type in attributes.items():
            self.assertTrue(hasattr(user_instance, attribute_name))
            self.assertEqual(type(getattr(user_instance, attribute_name,
                                          None)), attribute_type)


if __name__ == "__main__":
    unittest.main()
