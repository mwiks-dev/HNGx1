from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/get_info', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    if slack_name is None or track is None:
        return jsonify({'error': 'Both slack_name and track are required'}), 400

    # Get the current day of the week
    current_day = datetime.datetime.utcnow().strftime('%A')

    # Get the current UTC time with validation of +/-2 minutes
    current_time = datetime.datetime.utcnow()
    time_with_offset = current_time + datetime.timedelta(minutes=2)

    # Construct the response JSON
    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': time_with_offset.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'track': track,
        'github_file_url': 'https://github.com/username/repo/blob/main/file_name.ext',  # Replace with your file URL
        'github_repo_url': 'https://github.com/username/repo',  # Replace with your repo URL
        'status_code': 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
