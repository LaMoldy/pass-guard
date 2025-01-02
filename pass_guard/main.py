from pass_guard.gui import App, Setup

def main():
    app = App()
    setup_frame = Setup(app)
    setup_frame.pack(padx=10, pady=150)
    app.mainloop()

if __name__ == "__main__":
    main()
