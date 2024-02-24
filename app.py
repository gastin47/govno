from flask import Flask, render_template, request, jsonify
import sys
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    code = request.json['code']
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    
    try:
        exec(code)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        sys.stdout = old_stdout

    return jsonify({'result': redirected_output.getvalue()})

if __name__ == '__main__':
    app.run(debug=True)
