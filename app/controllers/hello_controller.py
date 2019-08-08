from flask import render_template
from app import app
from app.helpers import common_helpers

# I used jsonify in helpers. uncomment below line if needed in controllers
# from flask import jsonify

@app.route('/')
@app.route('/hello')
def hello_world():
    message = "Hello World!!"

    # I like using common helpers to generate JSON data
    # Feel free to jsonify API response here in controller, if needed, as below :)
    # resp = jsonify(message)
    # resp.status_code = 200
    # return resp
    return common_helpers.req_completed(message)


@app.route('/ui/hello')
def hello_world_ui():
    message = "Hello World from controller!"
    return render_template('hello.html', message=message)


