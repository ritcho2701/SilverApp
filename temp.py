from flask import Flask, request, jsonify

app = Flask(__name__)

groups = {}  # Dictionary to store user groups and their messages

@app.route("/send_message", methods=["POST"])
def send_message():
    group_name = request.form.get("group")
    message = request.form.get("message")

    if group_name and message:
        if group_name not in groups:
            groups[group_name] = []

        groups[group_name].append(message)
        return "Message sent successfully!"
    else:
        return "Failed to send message"

@app.route("/get_messages", methods=["GET"])
def get_messages():
    group_name = request.args.get("group")

    if group_name in groups:
        return jsonify({"group": group_name, "messages": groups[group_name]})
    else:
        return "Group not found"

if __name__ == "__main__":
    # Method 1: Using Flask's built-in development server
    #app.run()

    # Method 2: Using Gunicorn as the WSGI server
    from waitress import serve
    serve(app, host='0.0.0.0', port=8000)


    # Method 3: Using uWSGI as the WSGI server
    # Run with: uwsgi --http :5000 --wsgi-file app.py --callable app
    # app.run()
