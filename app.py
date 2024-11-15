import os;
from routes import routes_setup
from flask import Flask

app = Flask(__name__)   



routes_setup(app)
if __name__ == '__main__':  
     app.run(debug=True, host="0.0.0.0", port=8000)




