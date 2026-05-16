import urllib.request
import re

try:
    # 1. Fetch the raw HTML of CP24's live video player page
    url = "https://www.cp24.com/video/live/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')

    # 2. Use Regex to find the hidden master .m3u8 stream token in the page source
    match = re.search(r'(https://.*?\.m3u8.*?)"', html)
    
    if match:
        stream_url = match.group(1)
        
        # 3. Format it into an IPTV-compatible M3U layout
        m3u_content = f"#EXTM3U\n#EXTINF:-1 tvg-id=\"cp24\" tvg-name=\"CP24 News\" group-title=\"News\",CP24 Live\n{stream_url}\n"
        
        # 4. Save it as a playlist file
        with open("cp24_live.m3u", "w") as f:
            f.write(m3u_content)
        print("Successfully updated CP24 cloud link!")
    else:
        print("Could not locate live stream token on page source.")
except Exception as e:
    print(f"Error executing scraper: {e}")