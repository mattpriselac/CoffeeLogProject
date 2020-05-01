from app import app, db
from app.models import User, GreenCoffee, RoastSession, RoastedCoffee

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'GreenCoffee': GreenCoffee, 'RoastSession': RoastSession, 'RoastedCoffee': RoastedCoffee}
