from flask import Blueprint, jsonify, request
from ..models import db, Cliente

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

@client_blueprint.route('/client', methods=['POST'])
def create_client():
    data = request.get_json()

    required_fields = ["first_name",
                       "last_name",
                       "cpf",
                       "email",
                       "telephone",
                       "password"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "All required fields"})
    
    try:
        new_clients = Cliente(
            first_name=data["first_name"],
            last_name=data["last_name"],
            cpf=data["cpf"],
            email=data["email"],
            telephone=data["telephone"],
            password=data["password"]
        )

        db.session.add(new_clients)
        db.session.commit()

        return jsonify({"message": "Cliente adicionado com sucesso!"}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error ocurred while creating the client"}), 500
    