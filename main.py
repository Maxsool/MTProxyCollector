import requests
from bs4 import BeautifulSoup

session = requests.Session()


def get_json_proxies(urls):
    proxies = []
    for url in urls:
        try:
            data = session.get(url, timeout=10).json()
            proxies += [item["link"] for item in data if "link" in item]
        except:
            pass
    return proxies


def get_telegram_proxies(url):
    try:
        html = session.get(url, timeout=10).text
        soup = BeautifulSoup(html, "html.parser")

        return [
            a["href"]
            for a in soup.find_all("a", href=True)
            if "proxy" in a["href"]
        ]
    except:
        return []


json_urls = [
    # اگر داشتی اینجا بذار
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

proxies = list(set(
    get_json_proxies(json_urls) +
    [p for url in telegram_urls for p in get_telegram_proxies(url)]
))

print("TOTAL:", len(proxies))

with open("proxy.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(proxies) if proxies else "NO PROXIES")

save_as_json(proxies)
