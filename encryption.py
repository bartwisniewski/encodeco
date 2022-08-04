from abc import ABC, abstractmethod


class Encryption(ABC):

    def __init__(self):
        self.lookup = {}

    @abstractmethod
    def encrypt(self, text: str):
        pass

    def decrypt(self, text: str):
        pass

    @staticmethod
    def shift_in_range(num, shift, low, high):
        if num > high or num < low:
            return num+0
        return ((num-low)+shift) % (high-low+1) + low


class Rot47(Encryption):

    def __init__(self):
        super().__init__()
        self.lookup = {}
        for i in range(33, 126):
            self.lookup[chr(i)] = chr(self.shift_in_range(i, 47, 33, 126))

    def encrypt(self, text: str):
        encrypted_text = ""
        for character in text:
            encrypted_text += self.lookup.get(character, character)
        return encrypted_text

    def decrypt(self, text: str):
        return self.encrypt(text)


class Rot13(Encryption):

    def __init__(self):
        super().__init__()
        self.lookup = {}
        for i in range(65, 90):
            self.lookup[chr(i)] = chr(self.shift_in_range(i, 13, 65, 90))
        for i in range(97, 122):
            self.lookup[chr(i)] = chr(self.shift_in_range(i, 13, 97, 122))

    def encrypt(self, text: str):
        encrypted_text = ""
        for character in text:
            encrypted_text += self.lookup.get(character, character)
        return encrypted_text

    def decrypt(self, text: str):
        return self.encrypt(text)

