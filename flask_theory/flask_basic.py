'''THIS IS BASIC CODE FOR FIRST FLASK WEB SERVER'''
# flask == module hai
# Flask = class hai
from flask import Flask, render_template,jsonify,request
vaibhav = Flask(__name__)                               #app ka naam

# ......................................................

#
# # @vaibhav.route("/")                    #route provide kiya
# # def hello():
# #     return  "hello world"
#
# lst = [
#     {
#         'student':1,
#         'name':"vaibhav",
#         'age': 22
#     },
#     {
#         'student':2,
#         'name':"malav",
#         'age': 22
#     }
#
# ]
#
#
# @vaibhav.route("/")
# def html_code():
#     return  render_template("index.html")
#                             # ,jobs_variable = lst)
# #therfore a parameter can also be passed
# #use f;ask syntax {{}}
#
# @vaibhav.route("/api/students")        #port k baad ye likhenge to json mein dikhega
# def show_students():
#     return jsonify(lst)
#
#
# @vaibhav.route("")
# if __name__ == "__main__":
#     vaibhav.run(host="0.0.0.0",debug=True)               #if isi file ko terminal mein chalaya
#                                                         #then app chalega
# ..........................................................................


@vaibhav.route("/")
def home_page():
    return  render_template("index.html")

@vaibhav.route("/#register",methods=["GET","POST"])
def login_page():
    if request.method == "POST":
        return ("success dending data")
    else: return ("ruk j athoda")


if __name__ == "__main__":
    vaibhav.run(host="0.0.0.0",debug=True)