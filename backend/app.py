from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="database",
    database="capstone",
    user="admin",
    password="password"
)

@app.route("/assignments", methods=["GET"])
def get_assignments():
    cur = conn.cursor()
    cur.execute("SELECT * FROM assignments")
    rows = cur.fetchall()
    cur.close()
    return jsonify(rows)

@app.route("/assignments", methods=["POST"])
def add_assignment():
    data = request.json
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO assignments (course,title,deadline) VALUES (%s,%s,%s)",
        (data["course"], data["title"], data["deadline"])
    )
    conn.commit()
    cur.close()
    return {"message": "Assignment added"}

@app.route("/assignments/<int:id>", methods=["DELETE"])
def delete_assignment(id):
    cur = conn.cursor()
    cur.execute("DELETE FROM assignments WHERE id=%s",(id,))
    conn.commit()
    cur.close()
    return {"message":"Deleted"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)