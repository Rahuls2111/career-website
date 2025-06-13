from flask import Flask, render_template, request, redirect, url_for


app=Flask(__name__)  # create a new flask app created an object of the flask class


@app.route('/')  # this is the route

#below is the function that will be called when the route is accessed

def hello_world():
  return ("Hello World! Rahul this is your first flask app")
  
if(__name__=="__main__"):
  app.run(host='0.0.0.0',debug=True)
  # app.run(debug=True)
