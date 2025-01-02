class File():
    @staticmethod
    def create_file(file_name: str) -> bool:
        try:
            f = open("credential.enc", "x")
            return True
        except FileExistsError:
            return False

    @staticmethod
    def read_file(file_path: str) -> tuple[str, bool]:
        try:
            f = open(file_path, "r")
            return f.read(), True
        return "", False
    
    @staticmethod
    def check_file_exists(file_path: str) -> bool:
        return False
