from abc import ABC, abstractmethod


class Encryption(ABC):

    def __init__(self):
        self.lookup = {}

    @abstractmethod
    def encrypt(self, text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, text: str) -> str:
        raise NotImplementedError

    def encrypt_lookup(self, text: str) -> str:
        encrypted_text = ""
        for character in text:
            encrypted_text += self.lookup.get(character, character)
        return encrypted_text

    def decrypt_symetric(self, text: str) -> str:
        return self.encrypt(text)

    @staticmethod
    def shift_in_range(num: int, shift: int, low: int, high: int) -> int:
        if num > high or num < low:
            return num+0
        return ((num-low)+shift) % (high-low+1) + low


class Rot47(Encryption):
    ASCII_RANGE = (33, 126) # ASCII 36 - ASCII 126
    SHIFT = 47

    def __init__(self):
        super().__init__()
        self.lookup = {}
        for i in range(Rot47.ASCII_RANGE[0], Rot47.ASCII_RANGE[1]+1):
            self.lookup[chr(i)] = chr(self.shift_in_range(i, Rot47.SHIFT, Rot47.ASCII_RANGE[0], Rot47.ASCII_RANGE[1]))

    def encrypt(self, text: str) -> str:
        return self.encrypt_lookup(text)

    def decrypt(self, text: str) -> str:
        return self.decrypt_symetric(text)


class Rot13(Encryption):
    ASCII_RANGES = [(65, 95), (97, 122)]  # A-Z, a-z
    SHIFT = 13

    def __init__(self):
        super().__init__()
        self.lookup = {}
        for ascii_range in Rot13.ASCII_RANGES:
            for i in range(ascii_range[0], ascii_range[1]+1):
                self.lookup[chr(i)] = chr(self.shift_in_range(i, Rot13.SHIFT, ascii_range[0], ascii_range[1]))

    def encrypt(self, text: str) -> str:
        return self.encrypt_lookup(text)

    def decrypt(self, text: str) -> str:
        return self.decrypt_symetric(text)


class EncryptionFactory:
    ENCRYPTION_OBJECTS = {0: Rot47(), 1: Rot13()}
    ENCRYPTION_NAMES = {0: "Rot47", 1: "Rot13"}

    def __init__(self):
        pass

    @staticmethod
    def get_encryption_object(index: int) -> Encryption:
        return EncryptionFactory.ENCRYPTION_OBJECTS.get(index)
