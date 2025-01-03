import customtkinter
from enum import Enum
from pass_guard.gui import Login, Setup

class CTKFrames(Enum):
    LOGIN = 0,
    SETUP = 1,

class FrameController():
    @staticmethod
    def set_frame(app: customtkinter.CTk, next_frame: CTKFrames,
                  previous_frame: CTKFrames=None):
        if previous_frame:
            previous_frame.pack_forget()
        frame = FrameController._get_frame(app, next_frame)
        frame.pack(padx=10, pady=150)

    @staticmethod
    def _get_frame(master: customtkinter.CTk, frame: CTKFrames) ->customtkinter.CTkFrame:
        match (frame):
            case CTKFrames.LOGIN:
                return Login(master)
            case CTKFrames.SETUP:
                return Setup(master)
