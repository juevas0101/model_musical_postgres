from flask import Blueprint, jsonify, request
from ..models import Cliente

client_blueprint = Blueprint('client', __name__)


@client_blueprint.route('/client/<cpf>', methods=['GET'])
def search_client(cpf):
    client = Cliente.query.filter_by(cpf=cpf).first()
    if not client:
        return jsonify({"Cliente": "Não encontrado!"}), 404
    try:
        client_list = [{
            "id": client.id,
            "first_name": client.first_name,
            "last_name": client.last_name,
            "cpf": client.cpf,
            "email": client.email,
            "telephone": client.telephone,
            "password": client.password
        }]
        return jsonify({"cliente_list": client_list})

    except Exception as e:
        return jsonify({"error": f"An error occurred while searching Client: {str(e)}"}), 500
