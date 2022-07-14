import flask
from flask import request, jsonify,render_template
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

data={
        'pin': 4,
        'value': 0
    }
 #   {
 #       'pin': '2',
 #       'value': '0',
 #   }
#]
@app.route("/", methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'ON':
            #pass # do something
            val='1'
            conn = sqlite3.connect('database.db')
            sql = "INSERT INTO data(pin,value) VALUES(4,?)"
            cur = conn.cursor()
            cur.execute(sql,val)
            conn.commit()
            data['value']=int(val)
            #create_table(conn,val)
            
        elif  request.form.get('action2') == 'OFF':
            #pass # do something else
            val='0'
            conn = sqlite3.connect('database.db')
            sql = "INSERT INTO data(pin,value) VALUES(4,?)"
            cur = conn.cursor()
            cur.execute(sql,val)
            conn.commit()
            data['value']=int(val)
            #create_table(conn,val)
            
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html', data=data)
    
    return render_template("index.html",data=data)


@app.route('/iottestwebapp', methods=['GET'])
def api_all():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data WHERE ID = (SELECT MAX(ID) FROM data);")
    rows = cur.fetchall()
    #print(rows)
    for row in rows:
        print(row)
    #data['value']=row[2]
    #data['value']=
    return jsonify(data)

######################################## DATABASE Begins ############################################### 
db_file = 'database.db'

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def insert_data(conn,val):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = "INSERT INTO data(pin,value) VALUES(4,?)"
    cur = conn.cursor()
    cur.execute(sql,val)
    conn.commit()
    return cur.lastrowid
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def delete_all_tasks(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    #sql = 'DROP TABLE data'
    sql = 'DELETE FROM data WHERE pin=4'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
#app.run()
conn=create_connection(db_file)
#insert_data(conn,3)
select_all_tasks(conn)
#delete_all_tasks(conn)
######################################## DATABASE ENDS ############################################### 

app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
