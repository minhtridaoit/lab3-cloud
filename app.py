from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bài thực hành 3: Triển khai PaaS trên Render - Đào Minh Trí - 2324802010142'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)