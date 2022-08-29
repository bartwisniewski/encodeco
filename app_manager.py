from dataclasses import dataclass
from menu import ConsoleMenu
from encryption import EncryptionFactory
from file_handler import FileHandler


class AppManager:
    SELECTIONS = ["encrypt", "decrypt", "peek buffer", "save to file", "exit"]
    ENCRYPTION_FACTORY = EncryptionFactory()

    def __init__(self) -> None:
        self.buffer = Buffer("")
        self.menu = ConsoleMenu()
        self.is_running = True

    def main_menu(self) -> None:
        while self.is_running:
            selection = self.menu.select(description="What would you like to do?", selections=AppManager.SELECTIONS)
            self.__call_selection(selection)

    def __call_selection(self, selection: int) -> None:
        sel_methods = [self.__encrypt, self.__decrypt, self.__peek_buffer, self.__save_to_file, self.__exit]
        sel_methods[selection]()

    def __encrypt(self) -> None:
        selection = self.menu.select("Select encryption", AppManager.ENCRYPTION_FACTORY.ENCRYPTION_NAMES)
        encryptor = AppManager.ENCRYPTION_FACTORY.get_encryption_object(index=selection)
        text = self.menu.get_text("Enter text to encrypt")
        print(encryptor.__class__.__name__)
        encrypted_text = encryptor.encrypt(text)
        self.buffer.write(encrypted_text)

    def __decrypt(self) -> None:
        selection = self.menu.select("Select encryption", AppManager.ENCRYPTION_FACTORY.ENCRYPTION_NAMES)
        decryptor = AppManager.ENCRYPTION_FACTORY.get_encryption_object(index=selection)
        path = self.menu.get_text("give path to the file")
        file_handler = FileHandler(path)
        text = file_handler.read_from_file()
        print("decrypted text:")
        print(decryptor.decrypt(text))

    def __peek_buffer(self) -> None:  # TEST
        print(self.buffer)

    def __save_to_file(self) -> None:
        path = self.menu.get_text("give path to the file")
        file_handler = FileHandler(path)
        file_handler.write_to_file(self.buffer.buffer)
        self.buffer.clear()

    def __exit(self) -> None:
        print("Bye bye")
        self.is_running = False


@dataclass
class Buffer:
    buffer: str

    def write(self, text: str) -> None:
        self.buffer += text

    def clear(self) -> None:
        self.buffer = ""

    def __str__(self) -> str:
        return self.buffer
