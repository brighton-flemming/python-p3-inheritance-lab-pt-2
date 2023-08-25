class Student:
    def __init__(self, hello, raise_hand):
        self._hello = hello
        self._raise_hand = raise_hand

    def hello(self, hello):
        if hello == "":
            print("Hey there! I'm so excited to learn stuff.")
        else:
            self._hello = hello
        
    
    def raise_hand(self):
        attention_seeker = "Pick me!"
        print(attention_seeker)
        return attention_seeker
        
        
class ChattyStudent(Student):
    def __init__(self, hello, raise_hand):
        super().__init__(hello, raise_hand)
    
    def hello(self, hello):
        super()._hello(hello)
        hello = "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."
        print(hello)
        return hello
    
    def raise_hand(self):
        chatty_phrase = super().raise_hand()
        annoying_phrase = chatty_phrase * 10
        print (annoying_phrase)
        return annoying_phrase
        
