

class FileHandler:
    def __init__(self, path: str):
        self.path = path

    def read_from_file(self):
        try:
            file = open(self.path, "r")
            return file.read()
        except FileNotFoundError:
            return ""

    def write_to_file(self, text):
        try:
            file = open(self.path, "a")
            file.write(text)
            file.close()
            return "written successfully"
        except FileNotFoundError:
            return "no such file"
