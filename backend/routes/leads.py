from flask import Blueprint, request, jsonify

leads_bp = Blueprint('leads', __name__)
leads = []

@leads_bp.route('/api/leads', methods=['GET'])
def get_leads():
    return jsonify(leads), 200

@leads_bp.route('/api/leads', methods=['POST'])
def add_lead():
    data = request.json
    data['id'] = str(len(leads) + 1)
    data.setdefault('status', 'new')
    data.setdefault('tag', '')
    leads.insert(0, data)
    return jsonify(data), 201

@leads_bp.route('/api/leads/<lead_id>', methods=['PATCH'])
def update_lead(lead_id):
    updates = request.json
    for lead in leads:
        if lead['id'] == lead_id:
            lead.update(updates)
            return jsonify(lead), 200
    return jsonify({'error': 'Lead not found'}), 404
