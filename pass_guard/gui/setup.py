import customtkinter

class Setup(customtkinter.CTkFrame):
    password_visible = False

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.setup_label = customtkinter.CTkLabel(
            master=self,
            text="Enter a password to unlock the application in the future",
            font=("Segue UI", 15, "bold")
        )
        self.setup_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.set_password_entry = customtkinter.CTkEntry(
            master=self,
            placeholder_text="abc123",
            width=400,
            height=35,
        )
        self.set_password_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.set_password_entry.configure(show="*", justify="center")

        self.toggle_password_button = customtkinter.CTkButton(
            master=self,
            text="Toggle Password Visibility",
            width=195,
            height=40,
            command=self.toggle_password_visibility
        )
        self.toggle_password_button.grid(row=2, column=0, padx=10, pady=5)

        self.submit_password_button = customtkinter.CTkButton(
            master=self,
            text="Submit",
            width=195,
            height=40,
        )
        self.submit_password_button.grid(row=2, column=1, padx=10, pady=5)


    def toggle_password_visibility(self):
        if self.password_visible:
            self.set_password_entry.configure(show="*")
            self.password_visible = False
        else:
            self.set_password_entry.configure(show="")
            self.password_visible = True