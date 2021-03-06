from flask import Flask, request, render_template, redirect, url_for, abort, session

import json
import game
import testdb


app = Flask(__name__) 


app.secret_key = b'aaa!111/'
# 메인페이지
@app.route('/')
def hello():
    return render_template('main.html')


@app.route('/hello/<name>')
def hellovar(name):
    
    return render_template("gamestart.html", data = "철준")
# 게임
@app.route('/game')
def game():
    with open("static/save.txt", "r", encoding='utf-8') as f:
        data = f.read()
        user = json.loads(data)
    return "{0}님 숫자를 맞춰보세요. ({1}승{2}패 입니다.)".format(user["name"], user["win"], user["lose"])


# 회원정보
@app.route('/getinfo')
def getinfo():
    if 'user' in session:
        ret = testdb.select_all()
        print(ret[1]) 
        return render_template('getinfo.html', data = ret)
        
    return redirect(url_for('login'))



# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        ret = testdb.select_user(id, pw)
        if ret != None:
            session['user'] = id
            return redirect(url_for('login'))
        else:
            return redirect(url_for('login'))

# 로그아웃(session 제거)
@app.route('/logout') 
def logout():
    session.pop('user', None)
    return redirect(url_for('hello'))

# 로그인 사용자만 접근 가능으로 만들면
@app.route('/form')
def form():
    if 'user' in session:
        return render_template('test.html')
    return redirect(url_for('login'))



@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET 으로 전송이다.'
    else:
        num = request.form["id"]
        name = request.form["pw"]
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

# 회원가입
@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'GET':
        return render_template('reg.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        name = request.form['nname']
        ret = testdb.check_id(id)
        if ret != None:
            return '''
                    <script>
                    alert('다른 아이디를 사용하세요');
                    location.href='/reg';
                    </script>
                    '''
        testdb.insert_user(id, pw, name)
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
