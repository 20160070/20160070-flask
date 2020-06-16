from flask import Flask, request, render_template, redirect, url_for, abort, session

import game
import json
import testdb

from flask import Flask, request, render_template, redirect, url_for, abort, session

import game
import json
import testdb


app = Flask(__name__) 


app.secret_key = b'aaa!111/'

@app.route('/')
def hello():
    return '메인페이지!'


#@app.route('/hello/<name>')
#def hellovar(name):
 #  return render_template("gamestart.html", data = user)

##@app.route('/game')
#def game():
 #   with open("static/save.txt", "r", encoding='utf-8') as f:
   #    data = f.read()
      ## print(user)
    #return "{0}님 숫자를 맞춰보세요. ({1}승{2}패 입니다.)".format(user["name"], user["win"], user["lose"])



#@app.route('/getinfo')
#def getinfo():
 #   ret = testdb.select_all()
  #  print(ret[1])
   # return render_template('getinfo.html', data = ret)



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
            return "안녕하세요~ {}님".format(ret[2])
        else:
            return "아이디 또는 패스워드를 확인 하세요."

# 로그아웃(session 제거)
@app.route('/logout') 
def logout():
    session.pop('user', None)
    return redirect(url_for('form'))

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
