from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)

# Positions, sizes, and links for art in galleries
artwork = {
    "room1": [],
    "room2": [],
    "room3": [],
    "room4": [],
    "room5": [],
    "room6": [],
    "room7": [],
    "room8": []
}

@app.route('/')
@app.route('/<id>')
def gallery(id=1):
    return render_template('gallery.html', title=f"Room {id}", page = int(id), totalpages = 8, background=f"../static/galleries/room {id}.jpg", artwork=artwork[f"room{id}"])

@app.route('/artists')
def artists():
    return render_template('about.html', title="Artists")

@app.route('/<art>')
def art():
    return

if __name__ == '__main__':
    app.run(debug=True)
