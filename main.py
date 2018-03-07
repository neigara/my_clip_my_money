import json, re, pycurl, argparse
from io import BytesIO

GQL_PAYLOAD = "gql_payload"
# Only thumbnailURL and title. No 
# GQL_PAYLOAD = "gql_payload_shortened"

# YOUR CLIENT ID. You get this by pressing F12 on the clips page.
# Maybe hit F5 to refresh to reload the request.
# You can see your client-id under 'gql' thing (refer to the video)
# then it's under 'request headers'. Copy the id and paste into
# YOUR_CLIENT_ID.
# 
# Mine starts with 'kim' and ends with 'ko', and was 30 digits long.
CLIENT_ID = "client-id:YOUR_CLIENT_ID"

def main():
  # Argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('login_id', type=str)
  parser.add_argument('--filter-type', type=str, default='LAST_WEEK')
  parser.add_argument('--limit', type=int, default=20)
  parser.add_argument('--download-clips', action='store_true', default=False)
  parser.add_argument('--verbose', action='store_true', default=False)
  parser.add_argument('--url', action='store_true', default=False)
  args = parser.parse_args()

  # Get 'details' based on 'gql_payload' file to download clips from
  details = getDetails(args)

  # argparse option to print out this details.
  if args.verbose:
    print(details)
   
  # get only clips url 
  if args.url:
    for clips in details:
      print (clips['url']
    
  # Don't download if this option wasn't set.
  if not args.download_clips:
    print("Do download clips, use `--download-clips` option")
    exit()

  # Start downloading. You can quit with 'Ctrl + c'.
  # Downloads under 'clips/' folder. Make sure the folder exists.
  c = pycurl.Curl()
  for a in details:
    u = re.sub(r'-preview.*', ".mp4", a["thumbnailURL"])
    t = a["title"]
    f = open("clips/" + t, 'wb')
    print("Downloading " + t)
    c.setopt(c.URL, u)
    c.setopt(c.WRITEDATA, f)
    c.perform()
    f.close()
  c.close()

# Send requests to the server as if you are scrolling down the clips page
# and collects data into 'nodes'.
# 
# The target data is under `[0]["data"]["user"]["clips"]["edges"]`, i.e.,
# thumbnailURLs, titles, clip uploader, etc.
def getDetails(args):
  nodes = []
  cursor = ""

  print("Getting response. 'Ctrl + c' to quit.")
  while args.limit > 0:
    response = getHTTPResponse(args,cursor)

    # [{"data": {"user": {"clips": {"edges": [HERE]}}}}]
    r = json.loads(response)

    try :
      d = r[0]["data"]["user"]["clips"]["edges"]
    except TypeError:
      print(r)
      print("Check your parameters")
      print("exiting program")
      exit()

    nodes = nodes + list(map(lambda a: a['node'], d))
    cursor = list(filter(lambda a: a['cursor'] is not None, d))[0]['cursor']
    args.limit = args.limit - 100

  return nodes

# Change the fucking annoying pycurl to `request` or something
# I see why people on SO suggest using `request`.
def getHTTPResponse(args, cursor=""):
  url = "https://gql.twitch.tv/gql"
  
  file = open(GQL_PAYLOAD)
  content = json.load(file)[0]

  # Streamer id
  content["variables"]["login"] = args.login_id

  # One of "LAST_WEEK" or "ALL_TIME".
  content["variables"]["criteria"]["filter"] = args.filter_type

  # 1 ~ 100
  content["variables"]["limit"] = min(args.limit, 100)

  # Cursor. E.g., if limit is greater than 100
  content["variables"]["cursor"] = cursor

  # Following the pycurl quickstart [doc][1].
  # [1]: http://pycurl.io/docs/latest/quickstart.html
  b = BytesIO()

  c = pycurl.Curl()
  c.setopt(c.URL, url)
  # c.HEADER ... doesn't work.
  c.setopt(c.HTTPHEADER, [CLIENT_ID])
  # Weird SHIT. Can't just `content` or `json.dumps(content)`
  c.setopt(c.POSTFIELDS, "[" + json.dumps(content) + "]")
  # Following the pycurl quickstart
  c.setopt(c.WRITEDATA, b)
  c.perform()
  c.close()

  # Following the pycurl quickstart
  response = b.getvalue().decode('utf-8')
  return response

if __name__=="__main__":
  main()
