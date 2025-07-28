from flask import Flask,request, render_template


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/template')
def template_page():
    return render_template('template.html')

    

if __name__ == "__main__":
    print("👌 Aplicatia ruleaza !!")
    app.run(debug=True, port=5000, host='0.0.0.0')
