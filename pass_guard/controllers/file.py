class File():
    @staticmethod
    def create(file_name: str) -> bool:
        try:
            f = open(file_name, "x")
            return True
        except FileExistsError:
            return False

    @staticmethod
    def read(file_path: str) -> tuple[str, bool]:
        try:
            f = open(file_path, "r")
            return f.read(), True
        except:
            return "", False

    @staticmethod
    def exists(file_path: str) -> bool:
        return False
