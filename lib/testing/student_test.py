 #!/usr/bin/env python3


import unittest
from student import Student, ChattyStudent  # Import your classes from student.py

class TestStudent(unittest.TestCase):
    def test_default_hello(self):
        student = Student()
        self.assertEqual(student.hello(), "Hey there! I'm so excited to learn stuff.")

    def test_set_hello(self):
        student = Student()
        self.assertIsNone(student.set_hello("Hello, world!"))
        self.assertEqual(student.hello(), "Hello, world!")

    def test_raise_hand(self):
        student = Student()
        self.assertEqual(student.raise_hand(), "Pick me!")

class TestChattyStudent(unittest.TestCase):
    def test_default_hello(self):
        chatty_student = ChattyStudent()
        expected = "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."
        self.assertEqual(chatty_student.hello(), expected)

    def test_set_hello(self):
        chatty_student = ChattyStudent()
        expected = "Hey there! How's your day going? If you need a chat, some info, or just want to share something cool, I'm all ears (or, well, text!)."
        self.assertEqual(chatty_student.set_hello("Hello, everyone!"), expected)
        self.assertEqual(chatty_student.hello(), expected)

    def test_raise_hand(self):
        chatty_student = ChattyStudent()
        expected = "Pick me!" * 10
        self.assertEqual(chatty_student.raise_hand(), expected)

if __name__ == '__main__':
    unittest.main()
