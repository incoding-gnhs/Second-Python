from flask import Flask, request, render_template_string
import subprocess
import os
import sys

app = Flask(__name__)

HTML = '''
<h2>학번별 코드 실행</h2>
<form method="POST">
  학번 입력: <input name="student_id">
  <input type="submit" value="실행">
</form>
<pre>{{ output }}</pre>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        student_id = request.form.get("student_id", "").strip()
        filename = f"{student_id}.py"
        if os.path.isfile(filename):
            result = subprocess.run([sys.executable, filename], capture_output=True, text=True)
            output = result.stdout + result.stderr
        else:
            output = f"⚠️ {filename} 파일이 존재하지 않습니다."
    return render_template_string(HTML, output=output)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
