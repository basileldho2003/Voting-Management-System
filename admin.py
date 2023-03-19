from flask import Flask, render_template, request, session, flash, redirect, url_for
from flask_mysqldb import MySQL
import os

app = Flask("__name__")
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'bepma'
app.config['MYSQL_PASSWORD'] = 'bepma#2003'
app.config['MYSQL_DB'] = 'VOTERDB'
mysql = MySQL(app)

@app.route("/dashboard")
def home():
    mycur = mysql.connection.cursor()
    mycur.execute("SELECT * FROM VOTER_DETAILS")
    voter = mycur.fetchall()
    mycur.execute("SELECT * FROM CANDIDATE_LIST")
    cand = mycur.fetchall()
    mycur.execute("SELECT CL.CID, CL.CNAME, CL.PARTY, CL.SYMBOL, COUNT(CV.CID) AS TOTAL FROM CANDIDATE_LIST CL, CANDIDATE_VOTED CV WHERE CL.CID=CV.CID GROUP BY CV.CID ORDER BY TOTAL DESC")
    voted = mycur.fetchall()
    mycur.close()
    return render_template("admin/dashboard.html", voter=voter, cand=cand, voted=voted)

@app.route("/", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        try:
            passwd = request.form["password"]
            mycur = mysql.connection.cursor()
            mycur.execute("SELECT * FROM ADMIN_CREDENTIALS")
            dbpasswd = mycur.fetchall()
            rpasswd = dbpasswd[0][0]
            session["logged_in"] = passwd
            if passwd == rpasswd:
                return redirect("/dashboard")
            elif passwd == "":
                flash("Please enter your password!")
                return redirect("/")
            else:
                flash("Wrong password!")
                return redirect("/")
        except Exception:
            flash("Invalid input!")
            return redirect("/")
    return render_template("admin/login.html")

@app.route("/new_candidate", methods=["GET", "POST"])
def insert_cand():
    try:
        if request.method == "POST":
            cid = request.form['cid']
            cname = request.form['cname']
            party = request.form['party']
            logo = request.form['logo']
            mycur = mysql.connection.cursor()
            mycur.execute(
                f"INSERT INTO CANDIDATE_LIST VALUES('{cid}', '{cname.title()}', '{party}', '{logo}')")
            mysql.connection.commit()
            mycur.close()
            return """<script> alert('Successfully submitted!'); 
                        window.close();</script >"""
    except Exception:
        return """<script>alert('Failed to submit... Try again!');window.location.href='/new_candidate';</script >"""
    return render_template("admin/insert_cand.html")

@app.route("/edit_candidate", methods=["GET", "POST"])
def edit_cand():
    mycur = mysql.connection.cursor()
    mycur.execute("SELECT CID FROM CANDIDATE_LIST")
    cid = mycur.fetchall()
    cid_data = tuple(cid)
    mycur.close()
    return render_template("admin/edit_cand.html", cid_data=cid_data)

@app.route("/edit_candidate/details", methods=["GET", "POST"])
def edit_candidate_details():
    mycur = mysql.connection.cursor()
    mycidval = request.form.get('cid')
    mycur.execute(f"SELECT * FROM CANDIDATE_LIST WHERE CID='{mycidval}'")
    cand_data = mycur.fetchall()
    cand_data2 = tuple(cand_data)
    cid = cand_data2[0][0]
    cname = cand_data2[0][1]
    party = cand_data2[0][2]
    logo = cand_data2[0][3]
    mycur.close()
    return render_template("admin/edit_cand_details.html", cid=cid, cname=cname, party=party, logo=logo)

@app.route("/edit_candidate/update", methods=["POST"])
def update_details():
    try:
        mycur = mysql.connection.cursor()
        cid = request.form.get('cid')
        ncname = request.form.get('cname')
        oparty = request.form.get('cparty')
        ologo = request.form.get('clogo')
        nparty = request.form.get('nparty')
        nlogo = request.form.get('nlogo')
        if nparty == "":
            nparty = oparty
            nlogo = ologo
        mycur.execute(
            f"UPDATE CANDIDATE_LIST SET CNAME='{ncname.title()}', PARTY='{nparty}', SYMBOL='{nlogo}' WHERE CID='{cid}'")
        mysql.connection.commit()
        mycur.close()
        return """<script>alert('Successfully updated!');
            window.close();</script>"""
    except Exception:
        return """<script> alert('Failed to submit... Try again!');
        window.location.href='/edit_candidate/update'</script >"""


@app.route("/delete_candidate/<string:cid>", methods=["GET", "POST"])
def delete_details(cid):
    mycur = mysql.connection.cursor()
    mycur.execute(f"DELETE FROM CANDIDATE_LIST WHERE CID='{cid}'")
    mysql.connection.commit()
    mycur.close()
    flash("Successfully deleted!")
    return redirect(url_for('home'))

@app.route("/logout")
def admin_logout():
    session.pop("logged_in", None)
    return redirect("/")

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
