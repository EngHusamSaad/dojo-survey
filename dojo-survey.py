from flask import Flask,render_template, request, redirect,url_for
from datetime import datetime


app=Flask(__name__)


class Item:
   def __init__(self,name,location,lang,comment):
      self.name=name
      self.location=location
      self.lang=lang
      self.comment=comment

items=[]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/addnew" , methods=['POST'])
def addnew():
   # item=Item(**request.form)
   item2=Item(name=request.form["name"],location=request.form["location"],lang=request.form["lang"],comment=request.form["comment"])
   items.append(item2)
   return redirect("/result")

# @app.route("/addnew" , methods=['POST'])
# def addnew():
#    # item=Item(**request.form)
#    item2=Item(name=request.form["name"],location=request.form["location"],lang=request.form["lang"],comment=request.form["comment"])
#    items.append(item2)
#    return render_template("result.html.j2",items=items)


@app.route("/result" , methods=['get'])
def result():
   return render_template("result.html.j2",items=items)
      







if __name__ == '__main__':
  app.run()


