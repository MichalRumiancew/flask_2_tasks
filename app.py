from flask import Flask, render_template
from in_memory_data import user_stories

app = Flask(__name__)


@app.route('/')
def index():
    table_headers = ["Id", "Story Title", "User Story", "Acceptance Criteria", "Business Value", " Estimation", "Status"]
    return render_template("inedx.html", table_headers=table_headers)


if __name__ == '__main__':
    app.run()
