# Generate MP4 links via the Brightcove Playback API!

Requires Flask, Python 3, some modules listed in the file.

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
2. Maybe some tweaks like sorting the response if there is more than one MP4*, 
3. But that's about all I'm gonna do with this. It's a POC.
9. Learn Python cos I'm bad at it.


*It's unlikely unless you have some very specific requirements in your ingest profile.
