from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    name=['asd','addf','ddd']
    dict1={
        1:'aarti',
        2:'komal',
        3:'harshita'
        }
    return render_template('index.html',result=dict1)
 
if __name__=="__main__":
    app.run(debug=True)
