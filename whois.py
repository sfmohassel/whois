import requests
from bs4 import BeautifulSoup


def check_domain_availability(domain) -> dict:
    domain_url = f"https://who.is/whois/{domain}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        # Fetch the WHOIS page for the domain
        response = requests.get(domain_url, headers=headers, timeout=10)
        if response.status_code != 200:
            return {"domain": domain, "available": None, "error": "Could not fetch"}

        soup = BeautifulSoup(response.text, "html.parser")

        tags = soup.select(".queryResponseBodyRow > .queryResponseBodyValue")
        if not tags:
            return {"domain": domain, "available": False, "error": None}

        empty_text_count = 0
        for tag in tags:
            text = tag.text.strip().lower().replace("\n", " ")
            if not text:
                empty_text_count += 1

        if empty_text_count > 5:
            return {"domain": domain, "available": True, "error": None}

        return {"domain": domain, "available": False, "error": None}

    except Exception as e:
        return {"domain": domain, "available": None, "error": str(e)}
