from pass_guard.gui import App, Login

def main():
    app = App()
    login_frame = Login(app)
    login_frame.pack(padx=0, pady=100)
    app.mainloop()

if __name__ == "__main__":
    main()
