from flask import Flask
app=Flask(__name__)

#@app.route('/hi/<name>')
#def index(name):
 #   return 'Hello' + name

@app.route('/hi/<float:n>')
def index(n):
    return 'Hello %f' % n             


if __name__=="__main__":
    app.run(debug=True)
    
