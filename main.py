from flask import Flask

# app = Flask(__name__) #__name__ is just a convenient way to get the import name of the place the app is defined.
app = Flask(__name__)

# I have @app.rout(#this where I need this info in the web too)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/super_simple')
def super_simple():
    return 'Hello this is HR, Boo yah ,Let gooo'

if __name__ == '__main__':
    app.run()