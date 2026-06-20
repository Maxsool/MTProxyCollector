import requests
from bs4 import BeautifulSoup

session = requests.Session()


def get_json_proxies(urls):
    proxies = []

    for url in urls:
        try:
            proxies += [item["link"] for item in session.get(url, timeout=10).json()]
        except Exception as e:
            print(f"JSON Error ({url}): {e}")

    return proxies


def get_telegram_proxies(url):
    try:
        soup = BeautifulSoup(session.get(url, timeout=10).text, "html.parser")
        return [a["href"] for a in soup.find_all("a", string="پروکسی")]
    except Exception as e:
        print(f"Telegram Error ({url}): {e}")
        return []


json_urls = [
    "",
]

telegram_urls = [
    "https://t.me/s/iporoto",
    "https://t.me/s/HiProxy",
    "https://t.me/s/iproxy",
    "https://t.me/s/iRoProxy",
    "https://t.me/s/proxyforopeta",
    "https://t.me/s/IRN_Proxy",
    "https://t.me/s/MProxy_ir",
    "https://t.me/s/ProxyHagh",
    "https://t.me/s/PyroProxy",
]

proxies = (
    get_json_proxies(json_urls)
    + [p for url in telegram_urls for p in get_telegram_proxies(url)]
)

with open("proxy.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(proxies))

print(f"{len(proxies)} proxies saved.")

#####

import json

def save_as_json(proxy_list):
    data = {"proxies": proxy_list}

    with open("proxies.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

###############

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Proxy List</title>

<style>
body {
    font-family: Arial;
    background: #111;
    color: #fff;
}

.container {
    max-width: 700px;
    margin: auto;
    padding: 20px;
}

.proxy {
    background: #222;
    padding: 10px;
    margin: 10px 0;
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

a {
    color: #4fc3f7;
    text-decoration: none;
    word-break: break-all;
}

button {
    background: #4caf50;
    border: none;
    color: white;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 5px;
}
</style>
</head>

<body>

<div class="container">
<h2>Telegram Proxies</h2>

<div id="list"></div>
</div>

<script>
fetch("proxies.json")
.then(res => res.json())
.then(data => {
    const list = document.getElementById("list");

    data.proxies.forEach(proxy => {
        const div = document.createElement("div");
        div.className = "proxy";

        div.innerHTML = `
            <a href="${proxy}" target="_blank">${proxy}</a>
            <button onclick="copyText('${proxy}')">Copy</button>
        `;

        list.appendChild(div);
    });
});

function copyText(text) {
    navigator.clipboard.writeText(text);
    alert("Copied!");
}
</script>

</body>
</html>
####################
