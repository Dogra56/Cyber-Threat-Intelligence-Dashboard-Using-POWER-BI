import feedparser
import csv

# ✅ Compatible CVE RSS Feed (NVD)
feed_url = "https://nvd.nist.gov/feeds/xml/cve/misc/nvd-rss-analyzed.xml"

feed = feedparser.parse(feed_url)

if feed.entries:
    print(f"✅ Total CVEs found: {len(feed.entries)}\n")
    for entry in feed.entries[:5]:  # sirf pehle 5 CVEs print
        print(f"📌 Title   : {entry.title}")
        print(f"🗓️  Date    : {entry.published}")
        print(f"🔗 Link    : {entry.link}")
        print("-" * 50)

    # ✅ Save to CSV
    with open('latest_cves.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Published Date', 'Link'])
        for entry in feed.entries:
            writer.writerow([entry.title, entry.published, entry.link])
    print("📁 CVEs saved to latest_cves.csv")

else:
    print("❌ No CVEs found or feed could not be parsed.")
