from dataclasses import dataclass
from menu import ConsoleMenu
from encryption import EncryptionFactory
from file_handler import FileHandler


class AppManager:
    selections = ["encrypt", "decrypt", "peek buffer", "save to file", "exit"]
    encryption_types = ["ROT47", "ROT13"]

    def __init__(self):
        self.buffer = Buffer("")
        self.encryption_factory = EncryptionFactory()
        self.menu = ConsoleMenu()
        self.main_menu()

    def main_menu(self):
        selection = self.menu.select(description="What would you like to do?", selections=self.selections)
        self.call_selection(selection)

    def call_selection(self, selection: int):
        sel_methods = [self. encrypt, self.decrypt, self.peek_buffer, self.save_to_file, self.exit]
        sel_methods[selection]()

    def encrypt(self):
        selection = self.menu.select("Select encryption", self.encryption_types)
        encryptor = self.encryption_factory.create(index=selection)
        text = self.menu.get_text("Enter text to encrypt")
        print(encryptor.__class__.__name__)
        encrypted_text = encryptor.encrypt(text)
        self.buffer.write(encrypted_text)
        self.main_menu()

    def decrypt(self):
        selection = self.menu.select("Select encryption", self.encryption_types)
        decryptor = self.encryption_factory.create(index=selection)
        path = self.menu.get_text("give path to the file")
        file_handler = FileHandler(path)
        text = file_handler.read_from_file()
        print("decrypted text:")
        print(decryptor.decrypt(text))
        self.main_menu()

    def peek_buffer(self):
        print(self.buffer)
        self.main_menu()

    def save_to_file(self):
        path = self.menu.get_text("give path to the file")
        file_handler = FileHandler(path)
        file_handler.write_to_file(self.buffer.buffer)
        self.buffer.clear()
        self.main_menu()

    @staticmethod
    def exit():
        print("Bye bye")


@dataclass
class Buffer:
    buffer: str

    def write(self, text: str):
        self.buffer += text

    def clear(self):
        self.buffer = ""

    def __str__(self):
        return self.buffer
