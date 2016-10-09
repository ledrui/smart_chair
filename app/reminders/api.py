from app import application
from flask import jsonify, request
from app.reminders import reminder_manager


@application.route('/reminders/<username>', methods=['GET'])
def get_user_reminders(username):
    print "Fetching User Reminders"
    reminders = reminder_manager.get_user_reminders(username)
    print "Reminders: " + str(reminders)
    return jsonify(
        should_send_sitting_alert=reminders['sitting'],
        should_send_posture_alert=reminders['posture']
    )


@application.route('/reminders/send', methods=['POST'])
def send_user_reminder():
	json = request.get_json()
	print "Received request " + str(json)
	username = json["username"]
	reminder_type = json["reminder_type"]
	reminder_manager.send_reminder(username)
	return jsonify(
		status="SUCCESS"
	)