import requests
import string
import random
import time

digits = string.ascii_lowercase + string.digits
def generate_url():
    _id = ''.join(random.sample(digits, 6))
    return f"http://tabbycats.club/cat/{_id}"

while True:
    url = generate_url()
    # url = "http://tabbycats.club/cat/5vio47" # good
    # url = "http://tabbycats.club/cat/5vio45" # 404
    res = requests.get(url, timeout=10)
    if "Lil 404" not in res.text:
        print(url)
        with open("links.txt", 'a+') as f:
            f.write(url + '\n')
    else:
        print(f"Lil 404, {url}")

    time.sleep(0.2)
