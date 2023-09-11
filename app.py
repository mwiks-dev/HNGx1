from flask import Flask, request, jsonify
from datetime import datetime, timedelta, timezone

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if slack_name is None or track is None:
        return jsonify({'error': 'Both slack_name and track are required'}), 400

    # Get the current day of the week
    current_day = datetime.utcnow().strftime('%A')

    # Get the current datetime in UTC
    current_datetime = datetime.now(timezone.utc)

    # Calculate the offset from UTC in minutes
    timezone_offset_minutes = current_datetime.utcoffset().total_seconds() // 60

    # Create a new datetime object with the offset added
    utc_datetime = current_datetime + timedelta(minutes=timezone_offset_minutes)

    # Convert the datetime to ISO8601 format with 'Z'
    utc_time = utc_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
    # Construct the response JSON
    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': 'https://github.com/mwiks-dev/HNGx1/blob/main/app.py',  # Replace with your file URL
        'github_repo_url': 'https://github.com/mwiks-dev/HNGx1',  # Replace with your repo URL
        'status_code': 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
