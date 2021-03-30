from flask import Flask, request, jsonify 
from utilise import conn_db

app = Flask(__name__)

global l
l=[]
conn,cur = conn_db()
cur.execute('''select email from details1''')
email_check=cur.fetchall()
print(email_check)
print(type(email_check))

@app.route('/', methods=['POST','GET'])
def indata():
    if request.method == 'POST':
        data= request.get_json()
        ids=data['id']
        first_name=data['first_name']
        last_name=data['last_name']
        email=data['email']
        password=data['password']
        for i in email_check:
            j=str(i[0])
            l.append(j)

        if email in l:
            print('email already exit')
            return 'email already exit'
        else:
            kam = "INSERT INTO details1(ids,first_name,last_name,email,password)VALUES(%s,%s,%s,%s,%s)"
            nav = (ids,first_name,last_name,email,password)

            cur.execute(kam,nav)
            conn.commit()
            return 'success'

    if request.method == 'GET':
        cur.execute('''select * from details1''')
        details=cur.fetchall()
       
    return str(details)

@app.route('/<int:id>',methods=['GET'])
def required(id):
    if request.method == 'GET':
        cur.execute('''select * from details1 where ids = %s'''%id)
        req=cur.fetchall()
    return str(req)

@app.route('/<name>/<int:id>', methods=['PATCH'])
def update(name,id):
    if request.method == 'PATCH':
        har='''UPDATE details1 SET last_name = %s where ids = %s'''
        ish=(name,id)
        cur.execute(har,ish)
        conn.commit()
        #up=cur.fetchall()
    return 'modified'

@app.route('/dele/<int:id>', methods=['DELETE'])
def dele(id):
    if request.method == 'DELETE':
        cur.execute('''DELETE from details1 where ids = %s'''%id)
        conn.commit()
    return 'deleted'

@app.route('/hello')

def hello():
    return 'hello world'

if __name__=='__main__':
    app.run(debug=True, port=5690)