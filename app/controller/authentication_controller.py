from flask import Blueprint, request

authentication = Blueprint('authentication', __name__, url_prefix="/rest/v1")


@authentication.route('/signup', methods=['POST'])
def signup():
    user_details = request.gt_json()