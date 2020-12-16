import scan
import location
import portscanner, shodan_api
from nmaputils import nmap as nm
from flask import Flask, render_template, request, redirect, escape


app = Flask(__name__)
keys = ('IP', 'City', 'Country', 'Organization', 'Lat', 'Long')


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/about")
def aboutPage():
    return render_template("about.html")

@app.route("/fetch", methods=["POST", "GET"])
def fetching():
    if request.method == "POST":
        host = str(request.form['host'])
        lo = location.findLocation(host)
        # sh = shodan_api.scanHost(host)
        cr = scan.fullScan(host)
        # details = ['del11s07-in-f14.1e100.net', {'Port': [80, 443], 'State': ['open', 'open'], 'Name': ['http', 'https'], 'Version': ['', '']}, 'OpenBSD 4.0', '89']
    return render_template("results.html", 
    ip=host,
    hostname=cr[0],
    portsInfo=cr[1],
    osName=cr[2],
    accuracy=cr[3],
    contentLength=len(cr[1]['Port']),
    Lat=lo[0],
    Long=lo[1]
    )

app.run(debug=True)