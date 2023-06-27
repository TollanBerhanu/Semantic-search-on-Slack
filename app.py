from peft import PeftModel
from transformers import LLaMATokenizer, LLaMAForCausalLM, GenerationConfig
import textwrap

import os
import pandas as pd

import glob
import json

slack_data = './slack-data/'
# cwd = os.path.join (os.getcwd(), slack_data)  # join with current_working_directory just in case

df = pd.read_json(slack_data + 'channels.json')

channel_ids = [id for id in df['id']]
channel_names = [ name for name in df['name']]

channels = pd.DataFrame({ 'channel_id': channel_ids, 'channel_name': channel_names } )

# Return the metadata of each message in the channel
def extract_channel_data(channel_name):
  # use glob to get all the json files in the folder
  daily_json_files = glob.glob(slack_data + channel_name +'/*.json')

  # just return if the channel doesn't exist (or hasn't been exported yet)
  if not daily_json_files:
    return

  metadata = pd.DataFrame(columns = ['message', 'channel', 'date', 'time', 'user_id', 'user_name'])

  # loop over the list of json files (each json file includes every post in that channel for a single day)
  for f in daily_json_files:
    # read the json file
    # today_data = pd.read_json(f)
    with open(f, 'r') as file:
        # Read the contents
        data = file.read()
        # Parse the JSON data
        today_data = json.loads(data)

    today_date = f.split("/")[-1]  # 'f' is the full file path and file name
    print('Extracting...', today_date) # the file name is the date

    # iterate through all the messages of the day
    for msg_data in today_data:
      # Skip if its a "channel_join" type message or if the actual message content is empty
      if ('subtype' in msg_data) or (msg_data['text'] == '') or (msg_data['type'] != 'message'):
        continue
        # TODO: filter out any links, stickers, and other junk
        # TODO: replace @Member references by their real names

      metadata.loc[len(metadata)] = {
            'message': msg_data['text'],
            'channel': channel_name,
            'date': today_date.split(".json")[0], # omit the file extension '.json'
            'time': msg_data['ts'],
            'user_id': msg_data['user'],
            'user_name': msg_data['user_profile']#['first_name'] # We can also use 'real_name' if we wanted the full name of the user
      }

  return metadata

print(extract_channel_data('general').to_json(orient="records"))