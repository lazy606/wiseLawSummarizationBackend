from flask import (
    Blueprint
)

bp = Blueprint('summarization', __name__)


@bp.route('/cause', methods='POST')
def generate_cause():
    pass


@bp.route('/fact', methods='POST')
def generate_fact():
    pass


@bp.route('/laws', methods='POST')
def generate_laws():
    pass
