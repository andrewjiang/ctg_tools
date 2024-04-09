import json
import sys
import os

def main(file_name):
    # Load the JSON data from the file
    with open(file_name, 'r') as file:
        data = json.load(file)

    # Initialize a dictionary to count messages for each sender
    sender_message_count = {}

    # Iterate through the messages and count them for each sender
    for message in data['messages']:
        if 'from' in message:
            sender = message['from']
            if sender in sender_message_count:
                sender_message_count[sender] += 1
            else:
                sender_message_count[sender] = 1

    # Export the results to a new JSON file
    summary_file_name = os.path.splitext(file_name)[0] + '_summary.json'
    with open(summary_file_name, 'w', encoding='utf-8') as summary_file:
        json.dump(sender_message_count, summary_file, indent=4, ensure_ascii=False)

    print(f'Summary saved to {summary_file_name}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script.py <json_file_name>")
        sys.exit(1)
    main(sys.argv[1])
