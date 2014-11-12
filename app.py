import flask
from flask import Flask, render_template, request, redirect, session, url_for, escape, flash
import urllib2, json

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main():
    if request.method == "POST":
        query = request.form['search']
        url = "https://www.healthcare.gov/api/index.json"
        json_blob = urllib2.urlopen(url)
        text = json_blob.read()
        data = json.loads(text) #this is a list
    
        results = []

        for d in data:
            if not type(d) == bool:
                if query in d['bite'] or query in d['title']:
                    results.append(d)

        #print data
        #return render_template("main.html")
        print results

        return redirect(url_for("results", data=results))

    return render_template("main.html")


@app.route('/results')
def results(data):
    return render_template("results.html", data=data)
    
if __name__ == "__main__":
    app.debug = True
    app.run(port = 5005) #when everyone in class tests their projects we avoid 5000"
