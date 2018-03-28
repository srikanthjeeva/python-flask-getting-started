from flask import jsonify

# success handing
def req_completed(data):
    message = {
            'success': True,
            'result': data
    }
    resp = jsonify(message)
    resp.status_code = 200
    return resp
