from flask import Flask, render_template

app = Flask(__name__)

dashboard_url = "https://public.tableau.com/views/Dashboard_17874002499910/Dashboard1?:showVizHome=no&:embed=true"
story_url = "https://public.tableau.com/views/story_17874001467400/Story1?:showVizHome=no&:embed=true"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard1_page():
    return render_template(
        "dashboard.html",
        tableau_url=dashboard_url
    )

@app.route("/story")
def story_page():
    return render_template(
        "story.html",
        tableau_url=story_url
    )

if __name__ == "__main__":
    app.run(debug=True)
