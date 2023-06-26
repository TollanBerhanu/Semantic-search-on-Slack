import os
import pandas as pd
import numpy as np

slack_data = './slack-data/'

df = pd.read_json(slack_data + 'channels.json')

# channel_ids = [id for id in df['id']]
channel_names = [ name for name in df['name']]

channel_names
#channel_info --> (key: channel_id , value: channel_name)

# Helper functions
def lookup_channel(channel_id):
  channel_name = ''
  return channel_name

# import necessary libraries
import glob

def extract_channel_data(channel_name):
  # use glob to get all the json files in the folder
  daily_json_files = glob.glob(slack_data + channel_name +'/*.json')

  # just return if the channel doesn't exist (or hasn't been exported yet)
  if not daily_json_files:
    return

  # loop over the list of json files (each json file includes every post in that channel for a single day)
  for f in daily_json_files:
    # read the json file
    data = pd.read_json(f) 
    
    # print the filename getting extracted (it is also the messages were posted)
    today = f.split("/")[-1]  # 'f' is the location of the file
    print('Extracting...', today)

    # Skip if its a "channel_join" type message or if the actual message content is empty
    # if data['subtype'] or data['type'] == "":
    #   return
      # We should also remove any links, stickers, and other junk
      # We should replace @Member references by their actual names
    
    return {
            'message': data['text'],
            'channel': channel_name,
            'date': today,
            'time': data['ts'],
            'user_id': data['user'],
            'user_name': data['user_profile'].first_name # We can also use 'real_name' if we wanted the full name of the user
          }

print (extract_channel_data('general'))