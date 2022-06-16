from flask import Flask, render_template
from ppp import get_data 

app = Flask('app')

@app.route('/')
def hello_world():
  data_list,data_list1,data_list2,data_list3= get_data()
  #print(type(data))
  return render_template("index.html",data_list=data_list, data_list1=data_list1,data_list2=data_list2,data_list3=data_list3)

app.run(host='0.0.0.0', port=8080)
