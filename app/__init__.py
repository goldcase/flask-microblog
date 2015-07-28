from flask import Flask

# Assign to app the Flask instance.
app = Flask(__name__)
# Import the views module that we will write.
from app import views
