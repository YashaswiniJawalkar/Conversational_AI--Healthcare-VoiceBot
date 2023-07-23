# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import rasa.core.tracker_store
from rasa.shared.core.trackers import DialogueStateTracker
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pymongo import MongoClient
from random import randint
#from flask import Flask, session
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient('mongodb://localhost:27017/healfavor')
db=client.healfavor


class ActionSaveConversation(Action):

    def name(self) -> Text:

        return "action_save_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conversation=tracker.events
        import os
        if not os.path.isfile('chats.csv'):
            with open('chats.csv','w') as file:
                file.write("intent,user_input,entity_name,entity_value,action,bot_reply\n")
        chat_data=''
        chat=''
        count=0
        for i in conversation:
            if i['event'] == 'user':
                chat_data+=i['parse_data']['intent']['name']+','+i['text']+','
                print('user: {}'.format(i['text']))
                chat+='user: {}'.format(i['text'])
                chat+='\n'
                count+=1
                if len(i['parse_data']['entities']) > 0:
                    chat_data+=i['parse_data']['entities'][0]['entity']+','+i['parse_data']['entities'][0]['value']+','
                    print('extra data:', i['parse_data']['entities'][0]['entity'], '=',
                          i['parse_data']['entities'][0]['value'])
                    count+=1
                else:
                    chat_data+=",,"
            elif i['event'] == 'bot':
                print('Bot: {}'.format(i['text']))
                chat+='Bot: {}'.format(i['text'])
                chat+='\n'
                count+=1
                try:
                    chat_data+=i['metadata']['utter_action']+','+i['text']+'\n'
                except KeyError:
                    pass
        else:
            with open('chats.csv','a') as file:
                file.write(chat_data)
        db.chats.insert({'chat': chat, 'count': count})
        dispatcher.utter_message(text="All Chats saved.")
        return []