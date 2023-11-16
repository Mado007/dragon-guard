from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for dragons and maintenance
dragons = {}
maintenance = set()

# Simple route for the root URL
@app.route('/')
def index():
    return jsonify({"message": "Dragon Park Dashboard"})

# API endpoint to handle NUDLS events
@app.route('/nudls', methods=['POST'])
def handle_nudls_event():
    data = request.json

    if data['kind'] == 'dragon_added':
        handle_dragon_added(data)
    elif data['kind'] == 'dragon_removed':
        handle_dragon_removed(data)
    elif data['kind'] == 'dragon_location_updated':
        handle_dragon_location_updated(data)
    elif data['kind'] == 'dragon_fed':
        handle_dragon_fed(data)
    elif data['kind'] == 'maintenance_performed':
        handle_maintenance_performed(data)

    return jsonify({"status": "success"})

def handle_dragon_added(data):
    dragons[data['id']] = {
        "name": data['name'],
        "species": data['species'],
        "gender": data['gender'],
        "digestion_period_hours": data['digestion_period_hours'],
        "herbivore": data['herbivore'],
        "time": data['time'],
        "park_id": data['park_id']
    }

def handle_dragon_removed(data):
    if data['id'] in dragons:
        del dragons[data['id']]

def handle_dragon_location_updated(data):
    if data['dragon_id'] in dragons:
        dragons[data['dragon_id']]['location'] = data['location']

def handle_dragon_fed(data):
    pass

def handle_maintenance_performed(data):
    maintenance.add(data['location'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
