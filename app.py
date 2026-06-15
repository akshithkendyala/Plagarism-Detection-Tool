from flask import Flask, request, jsonify
from flask_cors import CORS
from plagiarism import calculate_similarity
from file_reader import extract_text
from db import connection, cursor

app = Flask(__name__)
CORS(app)

@app.route('/check', methods=['POST'])
def check():

    file1 = request.files['file1']
    file2 = request.files['file2']

    text1 = extract_text(file1)
    text2 = extract_text(file2)

    score = calculate_similarity(text1, text2)

    if score < 20:
        risk = "LOW"
    elif score < 50:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    cursor.execute(
    "INSERT INTO reports(similarity, risk) VALUES(%s, %s)",
    (score, risk)
    )

    connection.commit()
    
    return jsonify({
        "similarity": score,
        "risk": risk
    })
    
@app.route('/stats')
def stats():

    cursor.execute("SELECT COUNT(*) FROM reports")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT AVG(similarity) FROM reports")
    avg = cursor.fetchone()[0]

    return jsonify({
        "total": total,
        "average": round(avg, 2)
    })
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )

    user = cursor.fetchone()

    if user:
        return jsonify({
            "success": True
        })
    else:
        return jsonify({
            "success": False
        })
if __name__ == "__main__":
    app.run(debug=True)