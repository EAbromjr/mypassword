import csv


class Password:
    def __init__(self) -> None:
        pass

    def read_csv(self, file_path: str):
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            return reader
