from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('port.html')

@app.route('/fine-arts')
def fine_arts():
    return render_template('indexs.html')

@app.route('/career-hub')
def career_hub():
    return render_template('Test1.html')

@app.route('/calculator')
def calculator():
    return render_template('Team1_Task3.html')

@app.route('/movie-ticket')
def movie_ticket():
    return render_template('entry.html')

@app.route('/ai-enigma')
def ai_enigma():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        
        # Here you can add email sending logic
        # For now, we'll just return success
        return jsonify({
            'status': 'success',
            'message': 'Message sent successfully!'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 