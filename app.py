from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret_key"

gifts = []


@app.route("/", methods=["GET", "POST"])
def index():
    search_result = None

    if request.method == "POST":
        gift = request.form.get("gift", "").strip()

        if not gift:
            flash("Порожній подарунок не можна додати!")
        else:
            gifts.append(gift)
            flash("Подарунок додано!")

        return redirect(url_for("index"))

    search = request.args.get("search")

    if search is not None:
        if search.strip() in gifts:
            search_result = "Такий подарунок вже є у списку"
        else:
            search_result = "Такого подарунка ще немає у списку"

    return render_template(
        "index.html",
        gifts=gifts,
        search_result=search_result
    )


if __name__ == "__main__":
    app.run(debug=True)
