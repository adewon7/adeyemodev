from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

comments = []

@app.route('/')
def home():
    return "Server is running and ready to receive comments!"

@app.route('/add_comment', methods=['POST'])
def add_comment():
    data = request.get_json()
    name = data.get('name')
    comment = data.get('comment')
    
    if not name or not comment:
        return jsonify({'error': 'Name and comment are required!'}), 400
    
    comments.append({'name': name, 'comment': comment})
    return jsonify({'message': 'Comment added successfully!', 'comments': comments})

@app.route('/get_comments', methods=['GET'])
def get_comments():
    return jsonify(comments)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
