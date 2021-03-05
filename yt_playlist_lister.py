# Must have google-api-python-client installed
# pip3 install --upgrade google-api-python-client

import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "")

url = 'https://www.youtube.com/playlist?list=PLHoPanaLuJVA6iHc_XHFFuyaikhnrCk9d'
query = parse_qs(urlparse(url).query)

playlist_query = query["list"][0]

request = youtube.playlistItems().list(
    playlistId = playlist_query,
    part = "snippet",
)

playlist_info = []
while request is not None:
    response = request.execute()
    playlist_info += response["items"]
    request = youtube.playlistItems().list_next(request, response)

playlist_output = open('ytplaylist.txt','w')

for i in playlist_info:
    playlist_output.write(f'{i["snippet"]["title"]}\n')
    playlist_output.write(f'https://www.youtube.com/watch?v={i["snippet"]["resourceId"]["videoId"]}\n')

