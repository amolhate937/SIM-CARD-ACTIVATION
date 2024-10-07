from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

DATABASE = 'sim_db.sqlite'

# Database connection function
def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

# Function to activate a SIM card
@app.route('/activate', methods=['POST'])
def activate_sim():
    data = request.json
    sim_number = data.get('sim_number')
    
    if not sim_number:
        return jsonify({'error': 'SIM Number is required'}), 400
    
    conn = get_db()
    cursor = conn.cursor()

    # Check if SIM card exists
    cursor.execute("SELECT status FROM sim_cards WHERE sim_number=?", (sim_number,))
    sim = cursor.fetchone()
    
    if not sim:
        return jsonify({'error': 'SIM card does not exist'}), 404
    
    # Check if SIM is already active
    if sim[0] == 'active':
        return jsonify({'error': 'SIM card is already active'}), 400
    
    # Activate the SIM
    activation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("UPDATE sim_cards SET status=?, activation_date=? WHERE sim_number=?", 
                   ('active', activation_date, sim_number))
    conn.commit()
    
    return jsonify({'message': 'SIM card activated successfully'}), 200

# Function to deactivate a SIM card
@app.route('/deactivate', methods=['POST'])
def deactivate_sim():
    data = request.json
    sim_number = data.get('sim_number')
    
    if not sim_number:
        return jsonify({'error': 'SIM Number is required'}), 400
    
    conn = get_db()
    cursor = conn.cursor()

    # Check if SIM card exists
    cursor.execute("SELECT status FROM sim_cards WHERE sim_number=?", (sim_number,))
    sim = cursor.fetchone()
    
    if not sim:
        return jsonify({'error': 'SIM card does not exist'}), 404
    
    # Check if SIM is already inactive
    if sim[0] == 'inactive':
        return jsonify({'error': 'SIM card is already inactive'}), 400
    
    # Deactivate the SIM
    cursor.execute("UPDATE sim_cards SET status=? WHERE sim_number=?", ('inactive', sim_number))
    conn.commit()
    
    return jsonify({'message': 'SIM card deactivated successfully'}), 200

# Function to get SIM card details
@app.route('/sim-details/<sim_number>', methods=['GET'])
def get_sim_details(sim_number):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sim_cards WHERE sim_number=?", (sim_number,))
    sim = cursor.fetchone()
    
    if not sim:
        return jsonify({'error': 'SIM card does not exist'}), 404
    
    sim_details = {
        'sim_number': sim[0],
        'phone_number': sim[1],
        'status': sim[2],
        'activation_date': sim[3]
    }
    
    return jsonify(sim_details), 200

if __name__ == '__main__':
    app.run(debug=True)
