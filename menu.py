
class ConsoleMenu:
    def __init__(self):
        pass

    @staticmethod
    def select(description: str, selections: list) -> int:
        index = 0
        print(description)
        for selection in selections:
            print(f"{index} - {selection}")
            index += 1

        input1 = int(input("your selection:"))
        return input1

    @staticmethod
    def get_text(description) -> str:
        print(description)
        input1 = input("enter:")
        return input1
