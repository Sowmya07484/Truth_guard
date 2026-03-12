def check_source(url):

    trusted_sources = [
        "bbc.com",
        "reuters.com",
        "thehindu.com",
        "ndtv.com"
    ]

    for source in trusted_sources:
        if source in url:
            return "Trusted Source"

    return "Unknown / Unverified Source"