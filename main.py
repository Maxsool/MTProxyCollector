import requests
from bs4 import BeautifulSoup
import json

session = requests.Session()


# 🔹 JSON sources (اختیاری)
def get_json_proxies(urls):
    proxies = []
    for url in urls:
        try:
            data = session.get(url, timeout=10).json()
            proxies += [item["link"] for item in data if "link" in item]
        except:
            pass
    return proxies


# 🔹 Telegram scraping (FIXED + CLEAN FILTER)
def get_telegram_proxies(url):
    try:
        html = session.get(url, timeout=10).text
        soup = BeautifulSoup(html, "html.parser")

        proxies = []

        for a in soup.find_all("a", href=True):
            link = a["href"]

            # ❌ حذف پست‌ها و لینک‌های اضافی
            if "/mproxy_ir/" in link:
                continue
            if "t.me/" in link and "proxy?" not in link:
                continue

            # ✔️ فقط MTProto proxy
            if "t.me/proxy?" in link or "tg://proxy?" in link:
                proxies.append(link)

        return proxies

    except:
        return []


# 🔹 JSON save
def save_as_json(proxy_list):
    with open("proxies.json", "w", encoding="utf-8") as f:
        json.dump({"proxies": proxy_list}, f, ensure_ascii=False, indent=2)


# 🔹 sources
json_urls = []

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


# 🔹 collect
proxies = list(set(
    get_json_proxies(json_urls) +
    [p for url in telegram_urls for p in get_telegram_proxies(url)]
))


print("TOTAL:", len(proxies))


# 🔹 save TXT
with open("proxy.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(proxies) if proxies else "NO PROXIES")


# 🔹 save JSON
save_as_json(proxies)
