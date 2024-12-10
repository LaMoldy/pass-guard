import customtkinter

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("PassGuard")
        self.geometry("800x600")
        self.resizable(False, False)

        self._create_widgets()

    def _create_widgets(self):
        header_label = customtkinter.CTkLabel(self, text="Welcome", font=("Arial", 16))
        header_label.pack(pady=20)

if __name__ == "__main__":
    main_window = MainWindow()