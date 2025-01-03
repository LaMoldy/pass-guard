import customtkinter
import os
from pass_guard.gui import App
from pass_guard.controllers import File, CTKFrames, FrameController

CREDENTIAL_FILE_NAME = "credentials.enc"
PASSWORD_FILE_NAME = "passwords.enc"


def ensure_password_files_exist():
    if not File.exists(CREDENTIAL_FILE_NAME):
        File.create(CREDENTIAL_FILE_NAME)
    if not File.exists(PASSWORD_FILE_NAME):
        File.create(PASSWORD_FILE_NAME)


def start_first_frame(app: customtkinter.CTk):
    if os.path.getsize(CREDENTIAL_FILE_NAME) > 0:
        FrameController.set_frame(app, CTKFrames.LOGIN)
    else:
        FrameController.set_frame(app, CTKFrames.SETUP)
    
  
def main():
    ensure_password_files_exist()
    app = App()
    start_first_frame(app)
    app.mainloop()


if __name__ == "__main__":
    main()
