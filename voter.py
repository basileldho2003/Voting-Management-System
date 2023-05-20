from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import os

app = Flask("__name__")

app.config['MYSQL_HOST'] = '' #hostname
app.config['MYSQL_USER'] = '' #mysql/mariadb username
app.config['MYSQL_PASSWORD'] = '' #mysql/mariadb password
app.config['MYSQL_DB'] = 'VOTERDB'
mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("voter/index.html")


@app.route("/registration", methods=["POST", "GET"])
def registration():
    try:
        if request.method == "POST":
            vname = request.form["name"]
            aadhar = request.form["aadhar"]
            dob = request.form["dob"]
            age = request.form["age"]
            gender = request.form["flexRadioGender"]
            qualification = request.form["qualification"]
            passwd = request.form["passwd"]
            if "cand" not in request.form:
                mycur = mysql.connection.cursor()
                mycur.execute(
                    f"INSERT INTO VOTER_DETAILS VALUES({aadhar}, '{vname.title()}', '{dob}', {age}, '{gender}', '{qualification}', NULL)")
                mycur.execute(
                    f"INSERT INTO LOGIN_DETAILS VALUES({aadhar}, '{passwd}')")
                mysql.connection.commit()
                mycur.close()
            else:
                cid = request.form["cand"]
                mycur = mysql.connection.cursor()
                mycur.execute(
                    f"INSERT INTO VOTER_DETAILS VALUES({aadhar}, '{vname}', '{dob}', {age}, '{gender}', '{qualification}', '{cid}')")
                mycur.execute(
                    f"INSERT INTO LOGIN_DETAILS VALUES({aadhar}, '{passwd}')")
                mysql.connection.commit()
                mycur.close()
            return """<script> alert('Successfully submitted! Proceed to login...');
            window.close();</script>"""
    except Exception:
        return """<script> alert('Invalid entries received... Try again!');
        window.location.href='/registration'</script>"""
    return render_template("voter/register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        aadhar = int(request.form['aadhar'])
        passwd = request.form['passwd']
        session["aadhar"] = aadhar
        mycur = mysql.connection.cursor()
        mycur.execute(
            f"SELECT * FROM LOGIN_DETAILS WHERE AADHAR_ID={aadhar}")
        data = mycur.fetchall()
        if len(data) > 0:
            saadhar = data[0][0]
            spasswd = data[0][1]
            if aadhar == saadhar and passwd == spasswd:
                return redirect(url_for("dashboard"))
            if aadhar == saadhar and passwd != spasswd:
                flash("Incorrect or blank password!")
                return redirect(url_for("login"))
        else:
            flash("Invalid account!")
            return redirect(url_for("login"))
    return render_template("voter/login.html")


@app.route("/dashboard")
def dashboard():
    mycur = mysql.connection.cursor()
    aadhaar = session.get("aadhar", None)
    mycur.execute(
        f"SELECT VOTED FROM VOTED WHERE AADHAR_ID={aadhaar}")
    voted = mycur.fetchall()
    if voted == ():
        voted = ((0,),)
    voted_val = voted[0][0]
    mycur.execute(
        f"SELECT VNAME FROM VOTER_DETAILS WHERE AADHAR_ID={aadhaar}")
    vname = mycur.fetchall()
    voter_name = vname[0][0]
    mycur.execute("SELECT * FROM CANDIDATE_LIST")
    cand_details = mycur.fetchall()
    mycur.execute("SELECT CL.CID, CL.CNAME, CL.PARTY, CL.SYMBOL, COUNT(CV.CID) AS TOTAL FROM CANDIDATE_LIST CL, CANDIDATE_VOTED CV WHERE CL.CID=CV.CID GROUP BY CV.CID ORDER BY TOTAL DESC")
    vote_results = mycur.fetchall()
    mycur.execute(f"SELECT * FROM VOTER_DETAILS WHERE AADHAR_ID={aadhaar}")
    vdetails = mycur.fetchall()
    return render_template("voter/dashboard.html", cand_details=cand_details, voter_name=voter_name, vote_results=vote_results, voted_val=voted_val, vdetails=vdetails)


@app.route("/voted/<string:cid>", methods=["POST", "GET"])
def voted(cid):
    aadhaar = session.get("aadhar", None)
    mycur = mysql.connection.cursor()
    mycur.execute(f"INSERT INTO VOTED VALUES({aadhaar}, 1)")
    mysql.connection.commit()
    mycur.execute(f"INSERT INTO CANDIDATE_VOTED VALUES('{cid}', 1)")
    mysql.connection.commit()
    return redirect(url_for("dashboard"))


@app.route("/edit_voter/details", methods=["POST"])
def edit_voter_details():
    try:
        aadhaar = session.get("aadhar", None)
        mycur = mysql.connection.cursor()
        mycur.execute(f"SELECT * FROM VOTER_DETAILS WHERE AADHAR_ID={aadhaar}")
        rvdetails = mycur.fetchall()
        cdob = rvdetails[0][2]
        cage = rvdetails[0][3]
        cgender = rvdetails[0][4]
        cqual = rvdetails[0][5]
        nvname = request.form.get('vname')
        naadhaar = request.form.get('aadhaar')
        ndob = request.form.get('ndob')
        cage = request.form.get('cage')
        nage = request.form.get('nage')
        ngender = request.form.get('flexRadioGender')
        nqual = request.form.get('nqualification')
        if ndob == "":
            ndob = cdob
        if nage == "":
            nage = cage
        if ngender == None:
            ngender = cgender
        if nqual == "":
            nqual = cqual
        mycur.execute(
            f"UPDATE VOTER_DETAILS SET AADHAR_ID={naadhaar}, VNAME='{nvname}', DOB='{ndob}', AGE={nage}, GENDER='{ngender}', EDUCATION='{nqual}' WHERE AADHAR_ID={aadhaar}")
        mysql.connection.commit()
        mycur.close()
        return """<script>window.close();</script>"""
    except Exception:
        return """<script> alert('Failed to submit... Try again!');
        window.location.href='/dashboard'</script >"""


@app.route("/change_password", methods=["POST"])
def change_voter_password():
    try:
        aadhaar = session.get("aadhar", None)
        passwd = request.form.get("passwd")
        mycur = mysql.connection.cursor()
        mycur.execute(
            f"UPDATE LOGIN_DETAILS SET PASSWORD='{passwd}' WHERE AADHAR_ID={aadhaar}")
        mysql.connection.commit()
        mycur.close()
        return """<script>window.close();</script>"""
    except Exception:
        return """<script> alert('Failed to update password... Try again');
        window.location.href='/dashboard'</script >"""


@app.route("/logout")
def logout():
    session.pop("aadhar", None)
    return "<script>window.close()</script>"


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, port=5001)
