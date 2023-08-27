class Student:
     def __init__(self):
         self._hello = "Hey there! I'm so excited to learn stuff."
         self._raise_hand = "Pick me!"

     def set_hello(self, hello):
         if hello == "":
            self._hello = "Hey there everyone!"
            return self._hello
         else:
            self._hello = hello
            return None
   
     def hello(self):
        return self._hello
    
     def raise_hand(self):
       return self._raise_hand
  
        
class ChattyStudent(Student):
     def __init__(self):
        super().__init__()
        self._hello = "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."
    
     def set_hello(self, hello):
        super().set_hello(hello)
        self._hello = "Hey there! How's your day going? If you need a chat, some info, or just want to share something cool, I'm all ears (or, well, text!)."
        return self._hello
     
     def hello(self):
        return self._hello
     
     
     def raise_hand(self):
        chatty_phrase = super().raise_hand()
        annoying_phrase = chatty_phrase * 10
        print (annoying_phrase)
        return annoying_phrase
     
    
student = Student()
print(student.hello())
print(student.raise_hand())
print(student.set_hello(""))

chatty_student =  ChattyStudent()
print(chatty_student.hello())
print(chatty_student.raise_hand())
print(chatty_student.set_hello("Hello everyone! I'm really chatty!"))
        
