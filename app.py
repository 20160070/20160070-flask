from flask import Flask, request, render_template, redirect, url_for, abort

import game
import json
import testdb

app = Flask(__name__) 

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/hello/<name>')
def hellovar(name):
    user = game.set_user(name)
    return render_template("gamestart.html", data = user)

##@app.route('/game')
#def game():
 #   with open("static/save.txt", "r", encoding='utf-8') as f:
   #    data = f.read()
      ## print(user)
    #return "{0}님 숫자를 맞춰보세요. ({1}승{2}패 입니다.)".format(user["name"], user["win"], user["lose"])


@app.route('/form')
def form(): 
    return render_template("test.html")

@app.route('/getinfo')
def getinfo():
    # 파일 입력
    with open("static/save.txt", "r", encoding='utf-8') as file:
        student = file.read().split(',')  # 쉽표로 잘라서 student 에 배열로 저장
    return '번호 : {}, 이름 : {}'.format(student[0], student[1])


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return "!@#!@#!@$!@$!@$!@$@!$!@"
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        with open("static/save.txt", "w", encoding='utf-8') as f:
            f.write("%s %s" % (num, name))
        return 'POST 이다. 학번은 : {} 이름은 : {}'.format(num, name)
 



if __name__ == '__main__':
    app.run(debug=True)
