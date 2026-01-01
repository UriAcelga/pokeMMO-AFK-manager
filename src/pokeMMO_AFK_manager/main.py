from view import AppView
from controller import AppController

def main():
    app = AppView()
    controller = AppController(app)
    app.run()

if __name__ == "__main__":
    main()