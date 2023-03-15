from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify
import os
from werkzeug.utils import secure_filename
import mysql.connector
import datetime
app = Flask(__name__)
#con = mysql.connector.connect(user="root", database="imman")
UPLOAD_FOLDER = "static/upload"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def getconnection():
    return mysql.connector.connect(user="root", database="imman")

@app.route("/")
def header():
    return render_template("header.html")

@app.route("/dashboard")
def dashboard():
    con = getconnection()
    cursor = con.cursor()
    total_student_query = "SELECT COUNT(*) AS registration_count FROM enquiry"
    pc_query = "SELECT COUNT(*) AS registration_count FROM enquiry WHERE course IN ('Python','React','Java','C++','C')"
    ac_query = "SELECT COUNT(*) AS registration_count FROM enquiry WHERE course IN ('Tally','Excel','Gst plus','Income tax','Tally prime','Tally guru')"
    mmc_query = "SELECT COUNT(*) AS registration_count FROM enquiry WHERE course IN ('Photoshop','Graphics','Design')"
    total_course_query = "SELECT COUNT(course) FROM enquiry"
    pc1_query = "SELECT COUNT(course) FROM enquiry WHERE course IN ('Python','React','Java','C++','C')"
    ac1_query = "SELECT COUNT(course) FROM enquiry WHERE course IN ('Tally','Excel','Gst plus','Income tax','Tally prime','Tally guru')"
    mmc1_query = "SELECT COUNT(course) FROM enquiry WHERE course IN ('Photoshop','Graphics','Design')"
    result = []
    result1 = []
    cursor.execute(total_student_query)
    result.append(list(cursor.fetchone())[0])

    cursor.execute(pc_query)
    result.append(list(cursor.fetchone())[0])

    cursor.execute(ac_query)
    result.append(list(cursor.fetchone())[0])

    cursor.execute(mmc_query)
    result.append(list(cursor.fetchone())[0])

    cursor.execute(total_course_query)
    result1.append(list(cursor.fetchone())[0])

    cursor.execute(pc1_query)
    result1.append(list(cursor.fetchone())[0])

    cursor.execute(ac1_query)
    result1.append(list(cursor.fetchone())[0])

    cursor.execute(mmc1_query)
    result1.append(list(cursor.fetchone())[0])

    return render_template("dashboard.html", total=result[0], pc=result[1], ac=result[2], mmc=result[3], total1=result1[0], pc1=result1[1], ac1=result1[2], mmc1=result1[3])

@app.route("/graph")
def graph():
    con = getconnection()
    cur = con.cursor()
    addmission_graph = cur.execute("SELECT SUBSTR(dateofadd,6,2) AS month_of_admission,COUNT(slno) AS registration_count FROM enquiry GROUP BY month_of_admission")
    result = cur.fetchall()
    res = []
    for row in result:
        dto = datetime.datetime.strptime(row[0], "%m")
        res.append([dto.strftime("%B"), row[1]])
    fees_graph = cur.execute("SELECT fees.transmonth AS fees_paid_month, SUM(fees.transamount) AS fees_count FROM fees GROUP BY fees_paid_month")
    result1 = cur.fetchall()
    res1 = []
    for row1 in result1:
        dto1 = datetime.datetime.strptime(row1[0], "%m")
        res1.append([dto1.strftime("%B"), row1[1]])
    cur.close()
    return render_template("graph.html", data=res, data1=res1)

@app.route("/footer")
def footer():
    return render_template("footer.html")

@app.route("/backgroundvideo")
def background_video():
    return render_template("backgroundvideo.html")

@app.route("/enquiry")
def enquiry():
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from enquiry")
    result = cur.fetchall()
    cur.close()
    return render_template("enquiry.html", data=result)

@app.route("/enquiryentry")
def enquiryentry():
    course = request.args.get("course")
    return render_template("enquiryentry.html" , course=course)

@app.route("/extradetails", methods=['POST'])
def extradetails():
    reg_num = request.get_json(force = True)
    print(reg_num['slno'])
    con = getconnection()
    cur = con.cursor()
    cur.execute("SELECT `slno`, `name`, `regno`, `fname`, `dob`, `gender`, `eduqua`, `clg`, `dateofadd`, `course`, `addofcom`, `email`, `phnoc`, `phnop`, `fees` FROM `enquiry` WHERE slno=%s",(reg_num['slno'],))
    result = cur.fetchone()
    data_column = [x[0] for x in cur.description]
    res = dict(zip(data_column, list(result)))
    print(res)
    cur.close()
    return make_response(res, 200)

@app.route("/enquirysave", methods = ["POST","GET"])
def enquiry_save():
      if request.method == "POST":
        a = request.form["slno"]
        b = request.form["username"]
        c = request.form["regno"]
        d = request.form["fname"]
        e = request.form["dob"]
        f = request.form["gender"]
        g = request.form["eduqua"]
        h = request.form["college"]
        i = request.form["doa"]
        j = request.form["course"]
        k = request.form["aoc"]
        l = request.form["email"]
        m = request.form["phnoc"]
        n = request.form["phnop"]
        o = request.form["fees"]
        con = getconnection()
        cur = con.cursor()
        cur.execute("insert into enquiry values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"','"+i+"','"+j+"','"+k+"','"+l+"','"+m+"','"+n+"','"+o+"')")
        con.commit()
        return redirect(url_for("enquiry"))

@app.route("/course")
def course():
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from course")
    result = cur.fetchall()
    cur.close()
    return render_template("course.html", data=result)

@app.route("/coursesave", methods = ["POST","GET"])
def course_save():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filename = secure_filename((file.filename))
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        a = request.form["name"]
        b = file.filename
        c = request.form["duration"]
        d = request.form["fees"]
        con = getconnection()
        cur = con.cursor()
        cur.execute("insert into course values('"+a+"','"+b+"','"+c+"','"+d+"')")
        con.commit()
        return redirect(url_for("course"))

@app.route("/courseentry")
def course_entry():
    return render_template("courseentry.html")

# @app.route("/coursedelete",methods = ["Post","Get"])
# def course_delete():
#         name = request.args.get("RN")
#         con = getconnection()
#         cur = con.cursor()
#         cur.execute("delete from course where name = '"+name+"'")
#         con.commit()
#         cur.close()
#         return redirect(url_for("course"))

@app.route("/studentreg")
def studentreg():
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from studentregister")
    result = cur.fetchall()
    cur.close()
    return render_template("studentreg.html", data=result)

@app.route("/studentregentry")
def studentreg_entry():
    return render_template("studentregentry.html")

@app.route("/studentregsave", methods = ["POST","GET"])
def studentreg_save():
      if request.method == "POST":
        a = request.form["name"]
        b = request.form["dob"]
        c = request.form["email"]
        d = request.form["phnoc"]
        e = request.form["gender"]
        f = request.form["eduqua"]
        g = request.form["slno"]
        h = request.form["course"]
        i = request.form["doa"]
        j = request.form["aadhar"]
        k = request.form["idate"]
        l = request.form["edate"]
        m = request.form["address"]
        n = request.form["pincode"]
        o = request.form["state"]
        p = request.form["city"]
        q = request.form["fname"]
        r = request.form["mname"]
        s = request.form["phnop"]
        t = request.form["religion"]
        u = request.form["nation"]
        con = getconnection()
        cur = con.cursor()
        cur.execute("insert into studentregister values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"','"+h+"','"+i+"','"+j+"','"+k+"','"+l+"','"+m+"','"+n+"','"+o+"','"+p+"','"+q+"','"+r+"','"+s+"','"+t+"','"+u+"')")
        con.commit()
        return redirect(url_for("studentreg"))

@app.route("/staffreg")
def staffreg():
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from staffregister")
    result = cur.fetchall()
    cur.close()
    return render_template("staffreg.html", data=result)

@app.route("/staffregentry")
def staffreg_entry():
    return render_template("staffregentry.html")

@app.route("/staffregsave", methods = ["POST","GET"])
def staffreg_save():
      if request.method == "POST":
        a = request.form["id"]
        b = request.form["name"]
        c = request.form["address"]
        d = request.form["subject"]
        con = getconnection()
        cur = con.cursor()
        cur.execute("insert into staffregister values('"+a+"','"+b+"','"+c+"','"+d+"')")
        con.commit()
        return redirect(url_for("staffreg"))

@app.route("/fees")
def fees():
    con = getconnection()
    cur = con.cursor()
    cur.execute("select e.slno, e.regno, e.name, e.dateofadd, e.course, e.email, e.fees, sum(f.transamount),e.fees-sum(f.transamount) from enquiry as e, fees as f where e.regno = f.transid group by e.regno")
    result = cur.fetchall()
    cur.close()
    return render_template("fees.html", data=result)

@app.route("/feesentry")
def fees_entry():
    return render_template("feesentry.html")

@app.route("/feessave", methods = ["POST","GET"])
def fees_save():
      if request.method == "POST":
        a = request.form["slno"]
        b = request.form["id"]
        c = request.form["tdate"]
        d = request.form["tmonth"]
        e = request.form["tyear"]
        f = request.form["tamount"]
        con = getconnection()
        cur = con.cursor()
        cur.execute("insert into fees values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"')")
        con.commit()
        return redirect(url_for("fees"))

# @app.route("/feesedit")
# def fees_edit():
#     slno = request.args.get("RN")
#     con = getconnection()
#     cur = con.cursor()
#     cur.execute("select * from fees where slno = '" + slno + "'")
#     result = cur.fetchall()
#     cur.close()
#     return render_template("feesedit.html", data=result)
#
#
# @app.route("/feesupdate", methods = ["POST","GET"])
# def fees_update():
#     if request.method == "POST":
#         a = request.form["slno"]
#         b = request.form["id"]
#         c = request.form["tdate"]
#         d = request.form["tmonth"]
#         e = request.form["tyear"]
#         f = request.form["tamount"]
#         con = getconnection()
#         cur = con.cursor()
#         cur.execute("update fees set transid='"+b+"', transdate='"+c+"', transmonth='"+d+"', transyear='"+e+"', transamount='"+f+"' where slno='"+a+"'")
#         con.commit()
#         return redirect(url_for("fees"))

@app.route("/feesdelete",methods = ["Post","Get"])
def fees_delete():
        slno = request.args.get("RN")
        con = getconnection()
        cur = con.cursor()
        cur.execute("delete from fees where slno = '"+slno+"'")
        con.commit()
        cur.close()
        return redirect(url_for("fees"))

@app.route("/enquiryedit")
def enquiry_edit():
    slno = request.args.get("RN")
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from enquiry where slno = '" + slno + "'")
    result = cur.fetchall()
    cur.close()
    return render_template("enquiryedit.html", data=result)


@app.route("/studentregedit")
def studentreg_edit():
    name = request.args.get("RN")
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from studentregister where name = '" + name + "'")
    result = cur.fetchall()
    cur.close()
    return render_template("studentregedit.html", data=result)

@app.route("/staffregedit")
def staffreg_edit():
    id = request.args.get("RN")
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from staffregister where id = '" + id + "'")
    result = cur.fetchall()
    cur.close()
    return render_template("staffregedit.html", data=result)

          # Enquiry Save,Update,Delete
          # ==========================


@app.route("/enquiryupdate", methods=["POST", "GET"])
def enquiry_update():
    if request.method == "POST":
        a = request.form["slno"]
        b = request.form["username"]
        c = request.form["regno"]
        d = request.form["fname"]
        e = request.form["dob"]
        f = request.form["gender"]
        g = request.form["eduqua"]
        h = request.form["college"]
        i = request.form["doa"]
        j = request.form["course"]
        k = request.form["aoc"]
        l = request.form["email"]
        m = request.form["phnoc"]
        n = request.form["phnop"]
        o = request.form["fees"]
        con = getconnection()
        cur = con.cursor()
        cur.execute("update enquiry set name='" + b + "', regno='" + c + "', fname='" + d + "', dob='" + e + "',gender='" + f + "',eduqua='" + g + "',clg='" + h + "',dateofadd='" + i + "',course='" + j + "',addofcom='" + k + "',email='" + l + "',phnoc='" + m + "',phnop='" + n + "',fees='" + o + "' where slno='" + a + "'")
        con.commit()
        return redirect(url_for("enquiry"))

@app.route("/enquiryview")
def enquiry_view():
    slno = request.args.get("RN")
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from enquiry where slno = '" + slno + "'")
    result = cur.fetchall()
    cur.close()
    return render_template("enquiryview.html", data=result)

@app.route("/studentregview")
def studentreg_view():
    name = request.args.get("RN")
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from studentregister where name = '" + name + "'")
    result = cur.fetchall()
    cur.close()
    return render_template("studentregview.html", data=result)

@app.route("/feesview")
def fees_view():
    slno = request.args.get("RN")
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from fees where slno = '" + slno + "'")
    result = cur.fetchall()
    cur.close()
    return render_template("feesview.html", data=result)


@app.route("/enquirydelete",methods = ["Post","Get"])
def enquiry_delete():
        slno = request.args.get("RN")
        con = getconnection()
        cur = con.cursor()
        cur.execute("delete from enquiry where slno = '"+slno+"'")
        con.commit()
        cur.close()
        return redirect(url_for("enquiry"))

# ==========================
# StudentRegister Save,Update,Delete
# ==========================

@app.route("/studentregupdate", methods = ["POST","GET"])
def studentreg_update():
    if request.method == "POST":
        a = request.form["name"]
        b = request.form["dob"]
        c = request.form["email"]
        d = request.form["phnoc"]
        e = request.form["gender"]
        f = request.form["eduqua"]
        g = request.form["slno"]
        h = request.form["course"]
        i = request.form["doa"]
        j = request.form["aadhar"]
        k = request.form["idate"]
        l = request.form["edate"]
        m = request.form["address"]
        n = request.form["pincode"]
        o = request.form["state"]
        p = request.form["city"]
        q = request.form["fname"]
        r = request.form["mname"]
        s = request.form["phnop"]
        t = request.form["religion"]
        u = request.form["nation"]
        con = getconnection()
        cur = con.cursor()
        cur.execute("update studentregister set name='"+a+"',dob='"+b+"', email='"+c+"', phnoc='"+d+"',gender='"+e+"',eduqua='"+f+"',course='"+h+"',doa='"+i+"',aadhar='"+j+"',issdate='"+k+"',expdate='"+l+"',address='"+m+"',pincode='"+n+"',state='"+o+"',city='"+p+"',fname='"+q+"',mname='"+r+"',phnop='"+s+"',religion='"+t+"',nation='"+u+"' where slno='"+g+"'")
        con.commit()
        return redirect(url_for("studentreg"))

@app.route("/studentregdelete",methods = ["Post","Get"])
def studentreg_delete():
        slno = request.args.get("RN")
        con = getconnection()
        cur = con.cursor()
        cur.execute("delete from studentregister where slno = '"+slno+"'")
        con.commit()
        cur.close()
        return redirect(url_for("studentreg"))

@app.route("/staffregupdate", methods = ["POST","GET"])
def staffreg_update():
    if request.method == "POST":
        a = request.form["id"]
        b = request.form["name"]
        c = request.form["address"]
        d = request.form["subject"]
        con = getconnection()
        cur = con.cursor()
        cur.execute("update staffregister set name='"+b+"', address='"+c+"', majorsub='"+d+"' where id='"+a+"'")
        con.commit()
        return redirect(url_for("staffreg"))

@app.route("/staffregdelete",methods = ["Post","Get"])
def staffreg_delete():
        id = request.args.get("RN")
        con = getconnection()
        cur = con.cursor()
        cur.execute("delete from staffregister where id = '"+id+"'")
        con.commit()
        cur.close()
        return redirect(url_for("staffreg"))

if __name__ == '__main__':
    app.run(port=8000, debug=True)