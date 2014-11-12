import flask
from flask import Flask, render_template, request, redirect, session, url_for, escape, flash
import urllib2, json

app = Flask(__name__)

#Simple 2 pages: search page, results page.

@app.route('/',methods=["GET","POST"])
def main():
    if request.method == "POST":
        query = request.form['search']
        url = "https://www.healthcare.gov/api/index.json"
        json_blob = urllib2.urlopen(url)
        text = json_blob.read()
        data = json.loads(text) #this is a list of dicts
    
        results = [] #all of the matched result dicts will be in here. Basically another list of dicts

        for d in data:
            if not type(d) == bool:
                if query in d['bite'] or query in d['title']:
                    results.append(d)

        #print results
        
        session['data'] = results #stores the results in the session data. You might want to pop it later, but eh.
        return redirect(url_for("results"))

    return render_template("main.html")


@app.route('/results')
def results():
    return render_template("results.html", data=session['data'])
    #takes that list and uses it in the site to create search results

app.secret_key="Try_to_break_this_herpderpherpderpherpderp"

if __name__ == "__main__":
    app.debug = True
    app.run(port = 5005) #when everyone in class tests their projects we avoid 5000"
