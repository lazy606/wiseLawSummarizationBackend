from flask import (
    Blueprint
)

bp = Blueprint('summarization', __name__)


@bp.route('/keyword', methods='POST')
def generate_keyword():
    pass


@bp.route('/fact', methods='POST')
def generate_fact():
    pass


@bp.route('/laws', methods='POST')
def generate_laws():
    pass
