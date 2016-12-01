from flask import Flask, render_template, request

app = Flask(__name__)  

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/newyork") 
def newyork(): 
    return render_template('newyork.html')

@app.route("/miami") 
def miami(): 
    return render_template('miami.html')

@app.route("/neworleans") 
def neworleans(): 
    return render_template('neworleans.html')

@app.route("/nashville") 
def nashville(): 
    return render_template('nashville.html')
	
@app.route("/stlouis") 
def stlouis(): 
    return render_template('stlouis.html')
	
@app.route("/chicago") 
def chicago(): 
    return render_template('chicago.html')

if __name__ == "__main__":     
    app.run()