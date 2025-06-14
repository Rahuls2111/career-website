from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import engine, load_jobs_from_db



app=Flask(__name__)  # create a new flask app created an object of the flask class

# JOBS = [
#   {
#       'id':1,
#       'title':'Data Analyst',
#       'location':'Bengaluru,India',
#       'salary':'Rs. 10,00,000'
#   },
#   {
#       'id':2,
#       'title':'Data Scientist',
#       'location':'Delhi,India',
#       'salary':'Rs. 15,00,000'
#   },
#   {
#       'id':3,
#       'title':'Frontend Engineer',
#       'location':'Remote',
#       'salary':'Rs. 12,00,000'
#   },
#   {
#       'id':4,
#       'title':'Backend Engineer',
#       'location':'San Francisco,USA',
#       'salary':'$120,000'
#   },
#   {
#       'id':5,
#       'title':'Full Stack Engineer',
#       'location':'Remote',
#       'salary':'Rs. 12,00,000'
#   },
#   {
#       'id':5,
#       'title':'Full Stack Engineer',
#       'location':'Remote',
      
#   }
# ]
# def load_jobs_from_db():
#     with engine.connect() as conn:
#         result = conn.execute(text("select * from jobs limit 10"))
#         jobs = []
#         for row in result.all():
#             jobs.append(dict(row._mapping))
#        # print(jobs)
#         return jobs
        
@app.route('/')  # this is the route
#below is the function that will be called when the route is accessed



def hello_world():
    jobs = load_jobs_from_db()
  #return ("Hello World! Rahul this is your first flask app")
    return render_template('home.html',jobs=jobs,company_name='Rahul')
  

@app.route("/jobs")  # this is the route

def list_jobs():
  return jsonify(JOBS)

if(__name__=="__main__"):
  app.run(host='0.0.0.0',debug=True) # app.run(debug=True)