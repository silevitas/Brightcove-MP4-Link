from flask import Flask, request
from markupsafe import escape
import yaml, json, requests

app = Flask(__name__)

config = yaml.safe_load(open("config.yml"))

@app.route("/")
def index():
    return 'No arguments supplied. Use /video/VIDEO_ID'

@app.route('/video/<int:video_id>')
def return_mp4_link(video_id):

    account_id = request.args.get('account', '')
    policy_key = request.args.get('key', '')

    if account_id == "":
        account_id = config["defaultAccountId"]
        app.logger.info("No account ID set, using %s", account_id)

    if policy_key == "":
        policy_key = config["defaultPolicyKey"]
        app.logger.info("No policy key set, using %s", policy_key)

    app.logger.info("Video ID: %s", video_id)
    app.logger.info("Account ID: %s", account_id)
    app.logger.info("Policy Key: %s", policy_key)

    try:      
        response = requests.get(
            url=(f"https://edge.api.brightcove.com/playback/v1/accounts/{escape(account_id)}/videos/{escape(video_id)}"),
            headers={
                "Content-Type": "application/json",
                "Accept": f"application/json;pk={escape(policy_key)}",
            },
        )
        app.logger.info("Response: %s", response.status_code)

        if response.status_code == 200:
            full_sources = json.loads(response.content)
            sources = full_sources['sources']

            for item in sources:
                app.logger.info("Current Item: %s", item)
                if "container" in item:
                    app.logger.info("Item Found: %s", item)
                    return(item['src'].replace("http:", "https:"))
        elif response.status_code == 404:
            return("Video not found.")
        elif response.status_code == 403:
            return("Unauthorised. Have you used the right account and policy key combination?")
        else:
            return("Error. I don't know what the problem is.")
                
    except requests.exceptions.RequestException:
        return('HTTP Request failed')

    
    

