from main import db
from flask import Blueprint

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("richardsWisdom")
def wisdom():
    print("Hello World")