# Retrieve MP4 links via the Brightcove Playback API

## What is it?
Access the publc Playback API, parses the JSON and returns just the MP4 link. This does not do anything that isn't possible today, it just makes it a bit easier.

In other words it turns something like this:   
```
curl "https://edge.api.brightcove.com/playback/v1/accounts/123456789001/videos/987654321001" \
-H 'Content-Type: application/json' \
-H 'Accept: application/json;pk=LONG_POLICY_KEY_GOES_HERE' \
| jq -r '.sources[] | select(.container=="MP4") | .src'
```

To:   
```
https://server.com/video/987654321001
```

Why would you want this? A good use case would be to provide non-technical end-users with an MP4 link.

## Requirements
An active Brightcove account.
Requires Python 3, Flask, Pyyaml, and some modules listed in the file.

## Configuration
Create a "config.yml" file (use the sampleConfig.yml file as a template) to set a default account ID and policy key for when they're not passed.

## Usage
Once running, access the URL like this:
https://server.com/video/1234567001

...where "1234567001" is a video ID in your account defined in the config.yml file.

And then you'll get back an MP4 link if one's available for that video. Nothing special.

You can also pass a different account ID and policy key using the "account" and "key" query string parameters like so:

https://server.com/video/1234567001?account=98765432001&key=BCpkADthisIsALongPolicyKeyString

That's it, easy peasy!

## To Do
1. Code comments
2. Maybe some tweaks like sorting the response if there is more than one MP4* 
3. But that's about all I'm gonna do with this. It's a POC.
9. Learn Python cos I'm bad at it.


*It's unlikely unless you have some very specific requirements in your ingest profile.
