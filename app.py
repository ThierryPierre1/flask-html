from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('WhatWeDoing_noCSS.html')

@app.route('/styled')
def homepage_styles():
    return render_template('WhatImDoing_withCSS.html')
    # import to note that it is going to look for the .html files in a folder called templates

@app.route('/styled_layout')
def homepage_styles_layout():
    return render_template('WhatYouDoing_withCSS_layout.html')
    # import to note that it is going to look for the .html files in a folder called templates

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
