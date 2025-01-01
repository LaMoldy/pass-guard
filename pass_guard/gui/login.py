import customtkinter

class Login(customtkinter.CTkFrame):
    password_visible = False

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.password_label = customtkinter.CTkLabel(
            master=self,
            text="Please enter your password to unlock the app",
            font=("Segoe UI", 16, "bold")
        )
        self.password_label.pack(padx=10, pady=7)
        
        self.password_entry = customtkinter.CTkEntry(
            master=self,
            placeholder_text="Password",
            width=400,
            height=40,
            font=("Segoe UI", 14)
        )
        self.password_entry.configure(show="*", justify="center")
        self.password_entry.pack(padx=10, pady=2)

        self.toggle_password_button = customtkinter.CTkButton(
            master=self,
            text="Toggle Password Visibility",
            width=400,
            height=40,
            command=self.toggle_password_visibility
        )
        self.toggle_password_button.pack(padx=10, pady=5)


    def toggle_password_visibility(self):
        if self.password_visible:
            self.password_entry.configure(show="*")
            self.password_visible = False
        else:
            self.password_entry.configure(show="")
            self.password_visible = True
        
