

class FileHandler:
    def __init__(self, path: str):
        self.path = path

    def read_from_file(self):
        try:
            with open(self.path, "r") as opened_file:
                return opened_file.read()
        except FileNotFoundError:
            return ""

    def write_to_file(self, text):
        with open(self.path, "a") as opened_file:
            opened_file.write(text)
            return "written successfully"
