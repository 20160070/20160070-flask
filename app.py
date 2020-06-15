from flask import Flask, request, render_template, redirect, url_for, abort


app = Flask(__name__) 

@app.route('/hello/<name>')
def hellovar(name):
    game.MainStart(name)
    return "메인페이지"


@app.route('/form')
def form(): 
    return render_template("test.html")   


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return "!@#!@#!@$!@$!@$!@$@!$!@"
 

    elif request.method == 'GET':
        a = request.args.get('num')
        b = request.args.get('name')
        if a == 'abc' and b == '1234':
            return " 로그인 성공"
        else:
            return "로그인 실패"


@app.route('/move/naver')
def naver():
    return render_template("naver.html")


@app.route('/move/daum')
def daum(): 
    return redirect("https://www.daum.net/")

if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('daum'))

    app.run(debug=True)
