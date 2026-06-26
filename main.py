import json
import html
from urllib.parse import urlparse, parse_qs

import requests
from bs4 import BeautifulSoup

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0"
})


def get_json_proxies(urls):
    proxies = []

    for url in urls:
        try:
            data = session.get(url, timeout=10).json()
            proxies.extend(
                item["link"]
                for item in data
                if isinstance(item, dict) and "link" in item
            )
        except Exception as e:
            print(f"JSON Error: {url} -> {e}")

    return proxies


def get_telegram_proxies(url):
    try:
        response = session.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        proxies = []

        for a in soup.find_all("a", href=True):
            link = html.unescape(a["href"]).strip()

            # فقط پروکسی واقعی
            if (
                link.startswith("https://t.me/proxy?")
                or link.startswith("tg://proxy?")
            ):
                proxies.append(link)

        return proxies

    except Exception as e:
        print(f"Telegram Error: {url} -> {e}")
        return []


def save_as_json(proxy_list):
    result = []

    for proxy in proxy_list:
        try:
            q = parse_qs(urlparse(proxy).query)

            result.append({
                "server": q.get("server", [""])[0],
                "port": q.get("port", [""])[0],
                "secret": q.get("secret", [""])[0],
                "url": proxy
            })
        except:
            pass

    with open("proxy.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


# منابع JSON
json_urls = [
    # "https://example.com/proxies.json"
]

# کانال‌های تلگرام
telegram_urls = [
    "https://t.me/s/iMTProto",
    "https://t.me/s/iRoProxy",
    "https://t.me/s/darkproxy",
    "https://t.me/s/proxymtprotoj",
    "https://t.me/s/MTProxyStar",
    "https://t.me/s/MTProxyStar",
    "https://t.me/s/ProxyMTProto_tel",
    "https://t.me/s/MTP_roto",
    "https://t.me/s/ProxyMTProto",
    "https://t.me/s/proxymtprotoir",
    "https://t.me/s/MTProxyStar"
    "https://t.me/s/Proxy_Qavi"
    "https://t.me/s/TelMTProto"

]

# جمع‌آوری
proxies = []

proxies.extend(get_json_proxies(json_urls))

for url in telegram_urls:
    proxies.extend(get_telegram_proxies(url))

# حذف تکراری‌ها و مرتب‌سازی
proxies = sorted(set(proxies))

print(f"TOTAL: {len(proxies)}")

# TXT
with open("proxy.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(proxies))

# JSON
save_as_json(proxies)

print("proxy.txt saved")
print("proxy.json saved")
