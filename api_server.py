from flask import Flask, request
import json, requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/github/<owner>/<repo>/deployments", methods=['GET'])
def deploy(owner, repo):
    branch = request.args.get("branch")
    token = request.args.get("token")

    headers = { "Authorization": f"token {token}", "Accept": "application/vnd.github.ant-man-preview+json" }  
    body = { "ref": branch, "description" : "deploy from api" }
    response = requests.post(f"https://api.github.com/repos/{owner}/{repo}/deployments", headers=headers, data=json.dumps(body))
    return response.json()


host_addr = "0.0.0.0"
host_port = 8080
if __name__ == "__main__":
    app.run(host=host_addr, port=host_port)
