from flask import Flask, request, render_template_string

app = Flask(__name__)

# In-memory storage for submitted data per name
stored_data = {}

@app.route("/")
def home():
    return "Hello DevOps! Running on Flask 🚀"

@app.route("/health")
def health():
    return {"status": "UP"}
@app.route('/page')
def page():
                return "Welcome to the DevOps Application!"
@app.route('/app/<name>', methods=["GET", "POST"])
def app_name(name):
    if request.method == "POST":
        value = request.form.get("value")
        if name not in stored_data:
            stored_data[name] = []
        if value:
            stored_data[name].append(value)
    data_list = stored_data.get(name, [])
    return render_template_string('''
        <h2>App: {{ name }}</h2>
        <form method="post">
            <input type="text" name="value" placeholder="Enter data" required>
            <input type="submit" value="Submit">
        </form>
        <h3>Stored Data:</h3>
        <ul>
        {% for item in data_list %}
            <li>{{ item }}</li>
        {% endfor %}
        </ul>
        <a href="/">Back to Home</a>
    ''', name=name, data_list=data_list)
                

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
