import customtkinter

class Login(customtkinter.CTkFrame):
    password_visible = False

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.password_label = customtkinter.CTkLabel(
            master=self,
            text="Please enter your password to unlock the app login",
            font=("Segoe UI", 16, "bold")
        )
        self.password_label.grid(row=0, column=0, columnspan=2, padx=10, pady=7)

        self.password_entry = customtkinter.CTkEntry(
            master=self,
            placeholder_text="Password",
            width=400,
            height=40,
            font=("Segoe UI", 14)
        )
        self.password_entry.configure(show="*", justify="center")
        self.password_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=2)

        self.error_label = customtkinter.CTkLabel(
            master=self,
            text="",
            font=("Segoe UI", 14, "bold"),
            text_color="red"
        )
        self.error_label.grid(row=2, column=0, columnspan=2, padx=10, pady=3)

        self.toggle_password_button = customtkinter.CTkButton(
            master=self,
            text="Toggle Password Visibility",
            width=195,
            height=40,
            command=self._toggle_password_visibility
        )
        self.toggle_password_button.grid(row=3, column=0, padx=10, pady=5)

        self.submit_password_button = customtkinter.CTkButton(
            master=self,
            text="Submit",
            width=195,
            height=40,
        )
        self.submit_password_button.grid(row=3, column=1, padx=10, pady=5)

    def _toggle_password_visibility(self):
        show_character = "*" if self.password_visible else ""
        self.password_entry.configure(show=show_character)
        self.password_visible = not self.password_visible

