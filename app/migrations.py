from app import create_app, db
from app.models.user import User, VeggieEntry

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'VeggieEntry': VeggieEntry}