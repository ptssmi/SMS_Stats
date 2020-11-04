import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from datetime import date
from emoji import UNICODE_EMOJI
from collections import Counter
import time

#filters out any 
UNICODE_EMOJI_FILTERED = list(filter(lambda x: 'sign' not in UNICODE_EMOJI.get(x) and 'tone' not in UNICODE_EMOJI.get(x), UNICODE_EMOJI))

#constants
contact_number = input("Input the contact name: ")
print("Calculating...")

#initial states
message_sent_count = 0
message_received_count = 0
sundaycount = 0
mondaycount = 0
tuesdaycount = 0
wednesdaycount = 0
thursdaycount = 0
fridaycount = 0
saturdaycount = 0
picture_counter = 0
sent_emoji_counter = 0
received_emoji_counter = 0

twelve_am_count = 0
one_am_count = 0
two_am_count = 0
three_am_count = 0
four_am_count = 0
five_am_count = 0
six_am_count = 0
seven_am_count = 0
eight_am_count = 0
nine_am_count = 0
ten_am_count = 0
eleven_am_count = 0
twelve_pm_count = 0
one_pm_count = 0
two_pm_count = 0
three_pm_count = 0
four_pm_count = 0
five_pm_count = 0
six_pm_count = 0
seven_pm_count = 0
eight_pm_count = 0
nine_pm_count = 0
ten_pm_count = 0
eleven_pm_count = 0

total_message_sent = []
total_message_received = []
emoji_sent = []
emoji_received = []



def phone_number_condencer(number):
    number = number.replace('-','').replace(' ','').replace(')','').replace('(','')
    number = number[-10:]
    return number

root = ET.parse('data.xml').getroot()

#for sms messages
for type_tag in root.findall('sms'):
    phone_number = type_tag.get('address')
    phone_number = phone_number_condencer(phone_number)

    contact_name = type_tag.get("contact_name")
    
    # if phone_number == contact_number:
    if contact_name == contact_number:

        #Gather data and assign to variables
        message_type = type_tag.get('type')
        message_content = type_tag.get('body')
        string_time = type_tag.get('date')

        message_content_split = message_content.split()
        
        #Adds up total messages sent
        if message_type == '2':
            message_sent_count = message_sent_count + 1
            total_message_sent.extend(message_content_split)

            #adds up emojis sent
            for emoji in UNICODE_EMOJI_FILTERED:
                for char in message_content:
                    if(emoji in char):
                        emoji_sent.extend(char)
                        sent_emoji_counter = sent_emoji_counter + 1

        #Adds up total messages recieived
        elif message_type == '1':
            message_received_count = message_received_count + 1
            total_message_received.extend(message_content_split)

            #adds up emojis recieved
            for emoji in UNICODE_EMOJI_FILTERED:
                for char in message_content:
                    if(emoji in char):
                        emoji_received.extend(char)
                        received_emoji_counter = received_emoji_counter + 1
        
        #Adds up messages sent on each day of the week
        weekday = date.fromtimestamp(int(string_time[0:10])).weekday()
        if weekday == 0:
            mondaycount = mondaycount + 1
        elif weekday == 1:
            tuesdaycount = tuesdaycount + 1
        elif weekday == 2:
            wednesdaycount = wednesdaycount + 1
        elif weekday == 3:
            thursdaycount = thursdaycount + 1
        elif weekday == 4:
            fridaycount = fridaycount + 1
        elif weekday == 5:
            saturdaycount = saturdaycount + 1
        elif weekday == 6:
            sundaycount = sundaycount + 1

        #Counts messages during each time of the day
        hold = time.localtime(int(string_time[0:10]))
        
        if hold.tm_hour == 0:
            twelve_am_count = twelve_am_count + 1
        elif hold.tm_hour == 1:
            one_am_count = one_am_count + 1
        elif hold.tm_hour == 2:
            two_am_count = two_am_count + 1
        elif hold.tm_hour == 3:
            three_am_count = three_am_count + 1
        elif hold.tm_hour == 4:
            four_am_count = four_am_count + 1
        elif hold.tm_hour == 5:
            five_am_count = five_am_count + 1
        elif hold.tm_hour == 6:
            six_am_count = six_am_count + 1
        elif hold.tm_hour == 7:
            seven_am_count = seven_am_count + 1
        elif hold.tm_hour == 8:
            eight_am_count = eight_am_count + 1
        elif hold.tm_hour == 9:
            nine_am_count = nine_am_count + 1
        elif hold.tm_hour == 10:
            ten_am_count = ten_am_count + 1
        elif hold.tm_hour == 11:
            eleven_am_count = eleven_am_count + 1
        elif hold.tm_hour == 12:
            twelve_pm_count = twelve_pm_count + 1
        elif hold.tm_hour == 13:
            one_pm_count = one_pm_count + 1
        elif hold.tm_hour == 14:
            two_pm_count = two_pm_count + 1
        elif hold.tm_hour == 15:
            three_pm_count = three_pm_count + 1
        elif hold.tm_hour == 16:
            four_pm_count = four_pm_count + 1
        elif hold.tm_hour == 17:
            five_pm_count = five_pm_count + 1
        elif hold.tm_hour == 18:
            six_pm_count = six_pm_count + 1
        elif hold.tm_hour == 19:
            seven_pm_count = seven_pm_count + 1
        elif hold.tm_hour == 20:
            eight_pm_count = eight_pm_count + 1
        elif hold.tm_hour == 21:
            nine_pm_count = nine_pm_count + 1
        elif hold.tm_hour == 22:
            ten_pm_count = ten_pm_count + 1
        elif hold.tm_hour == 23:
            eleven_pm_count = ten_pm_count + 1

# print(total_message)
count_sent = Counter(total_message_sent)
count_received = Counter(total_message_received)
emoji_count_received = Counter(emoji_received)
emoji_count_sent = Counter(emoji_sent)
print(count_sent.most_common(10))
print(count_received.most_common(10))
print(emoji_count_received.most_common(10))
print(emoji_count_sent.most_common(10))

#for mms messages
for type_tag in root.findall('mms'):
    contact_name = type_tag.get("contact_name")
    if contact_name == contact_number:
        picture_counter = picture_counter + 1


#Displays bar graph of weekday breakdown
objects = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
data = [mondaycount,tuesdaycount,wednesdaycount,thursdaycount,fridaycount,saturdaycount,sundaycount]
plt.bar(objects,data)
plt.xlabel("Day of the Week") 
plt.ylabel("Text Messages Sent") 
plt.title('Weekday Breakdown')
plt.show()

#Displays bar graph of time breakdown
times = ['12AM','1AM','2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM','10AM','11AM','12PM','1PM','2PM','3PM','4PM','5PM','6PM',"7PM","8PM","9PM","10PM","11PM"]
stats = [twelve_am_count,one_am_count,two_am_count,three_am_count,four_am_count,five_am_count,six_am_count,seven_am_count,eight_am_count,nine_am_count,ten_am_count,eleven_am_count,twelve_pm_count,one_pm_count,two_pm_count,three_pm_count,four_pm_count,five_pm_count,six_pm_count,seven_pm_count,eight_pm_count,nine_pm_count,ten_pm_count,eleven_pm_count]
plt.bar(times,stats)
plt.xlabel("Time") 
plt.ylabel("Text Messages Sent") 
plt.title('Time Breakdown')
plt.show()

#pi chart
datalabel = ['Messages Received','Messages Sent']
data = [message_received_count,message_sent_count]
plt.pie(data,labels = datalabel,autopct='%1.1f%%')
plt.show()

#calculates the total amount of messages sent
totalmessages_count = message_received_count + message_sent_count
total_emojis = sent_emoji_counter + received_emoji_counter

#prints out data
print("Total messages sent: {}".format(totalmessages_count))
print("Messages recieved: {}".format(message_received_count))
print("Messages sent: {}".format(message_sent_count))

print("Total Pictures Sent: {}".format(picture_counter))

print("Number of Emojis Sent: {}".format(sent_emoji_counter))
print("Number of Emojis Received: {}".format(received_emoji_counter))
print("Total Number of Emojis: {}".format(total_emojis))








