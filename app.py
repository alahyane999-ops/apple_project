from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    player_id = ""
    error = ""

    if request.method == "POST":
        player_id = request.form.get("player_id", "").strip()

        # يقبل فقط ID مكون من 10 أرقام
        if not player_id.isdigit():
            error = "❌ يجب إدخال أرقام فقط."
        elif len(player_id) != 10:
            error = "❌ يجب أن يكون الـ ID مكونًا من 10 أرقام."
        else:
            prediction = []
            for _ in range(7):
                prediction.append(random.randint(1, 5))

    return render_template(
        "index.html",
        prediction=prediction,
        player_id=player_id,
        error=error
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
