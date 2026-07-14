from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    player_id = ""

    if request.method == "POST":
        player_id = request.form.get("player_id", "").strip()

        if player_id:
            prediction = []
            for i in range(7):
                row = random.randint(1, 5)
                prediction.append(row)

    return render_template(
        "index.html",
        prediction=prediction,
        player_id=player_id
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
