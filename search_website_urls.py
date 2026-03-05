def clean_website(url):
    if not url:
        return ""
    url = str(url).strip()
    if not url.startswith("http"):
        url = "http://" + url
    return url
