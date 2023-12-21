# from flask import Blueprint, jsonify, request
# from ..models import Evento

# evento_blueprint = Blueprint('event', __name__)

# evento_blueprint.route('/event/<path:name_evento>', methods=['GET'])
# def search_events(name_event):
#     try:
#         events = Evento.query.filter(Evento.name_event.ilike(f"%{name_event}%")).all()

#         if not events:
#             return jsonify({"Evento": "Não encontrado!"}), 404
        
#         events_list = [{
#             "id": event.id,
#             "name_event": event.name_event,
#             "local": event.local,
#             "company": event.company,
#             "gender": event.gender,
#             "is_free": event.is_free,
#         }for event in events]
#         return jsonify({"events": events_list})

#     except Exception as e:
#         return jsonify({"error": f"An error occurred while searching Client: {str(e)}"}), 500
