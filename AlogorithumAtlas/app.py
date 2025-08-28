from flask import Flask, request

app = Flask(__name)

@app.route('/run-python', methods=['POST'])
def execute_python():
    code = request.json.get('code')
    try:
        result = exec(code)
        return str(result)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
