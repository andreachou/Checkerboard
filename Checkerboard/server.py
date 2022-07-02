from flask import Flask, render_template

app = Flask(__name__)


# 1. http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def main():
    return render_template('index.html', col=4, row=8, color1='black', color2='red')


# 2. http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/<int:y>')
def set_row(y):
    return render_template('index.html', col=4, row=y, color1='black', color2='red')

# 3. NINJA BONUS: Have another route accept 2 parameters (i.e. "/<x>/<y>") and render a checkerboard with x rows and y columns, with alternating colors
@app.route('/<int:x>/<int:y>')
def set_col_row(x, y):
    return render_template('index.html', col=x, row=y, color1='black', color2='red')

# 4. SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def set_all(x, y, color1, color2):
    return render_template('index.html', col=x, row=y, color1=color1, color2=color2)


if __name__ == "__main__":
    app.run(debug=True)