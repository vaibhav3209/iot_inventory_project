'''THIS IS BASIC CODE FOR FIRST FLASK WEB SERVER'''


from flask import Flask, render_template,jsonify

# flask == module hai
# Flask = class hai

vaibhav = Flask(__name__)               #app ka naam

# @vaibhav.route("/")                    #route provide kiya
# def hello():
#     return  "hello world"

lst = [
    {
        'student':1,
        'name':"vaibhav",
        'age': 22
    },
    {
        'student':2,
        'name':"malav",
        'age': 22
    }

]
@vaibhav.route("/")
def html_code():
    return  render_template("home.html",jobs_variable = lst)
#therfore a parameter can also be passed
#use f;ask syntax {{}}

@vaibhav.route("/api/students")        #port k baad ye likhenge to json mein dikhega
def show_students():
    return jsonify(lst)



if __name__ == "__main__":
    vaibhav.run(host="0.0.0.0",debug=True)               #if isi file ko terminal mein chalaya
                                                        #then app chalega