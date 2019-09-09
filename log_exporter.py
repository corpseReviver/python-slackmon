import slackmon
import json


def lambda_function():
	token = ""
	logs = slackmon.get_all_messages(token=token, frequency=3600)
	formatted_logs = format_logs(json.loads(logs))
	if formatted_logs:
		import_to_sumo(formatted_logs)
	else:
		print('--> No new logs')

def format_logs(logs):
	format_string = ''
	for channel_type, data in logs.items():
		if data:
			for channel_id, message_data in data.items():
				for item in message_data.get('data'):
					format_string += "{}\n".format(item)

	return format_string

def import_to_sumo(logs):
	print(logs)


if __name__ == '__main__':
	lambda_function()