from flask import Flask,render_template, jsonify

app=Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Intern wealthsimple, Software Development (Summer 2024)',
    'location':'Toronto',
    'salary':'$50,000'
  },
  {
    'id':2,
    'title':'Snowflake, SOFTWARE ENGINEER INTERN (TORONTO) - SUMMER 2024',
    'location':'Toronto',
    'salary':'$50,000'
  },
  {
    'id':3,
    'title':'Velocity - Software Engineer Internship/Co-Op - Summer 2024',
    'location':'Toronto',
    'salary':'$50,000'
  }
    ]
@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=JOBS,
                        company_name="IndeKedIn")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)