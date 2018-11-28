from publish_doi import assemble_payload
from publish_doi import assemble_xml
from publish_doi import publish_doi

from update_doi import update_doi

from extract_metadata import gather_assets

# waiting to implement database refactor
# from extract_metadata import load_temp_table
# from extract_metadata import diff_temp_table

from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    return 'test'


@app.route('/assemble.payload', methods=['GET'])
def api_assemble_payload():
    socrata_4x4 = request.args.get('socrata_4x4')
    draft = request.args.get('draft')
    return jsonify(assemble_payload(socrata_4x4=socrata_4x4, draft=draft))


@app.route('/publish.doi', methods=['POST'])
def api_publish_doi():
    socrata_4x4 = request.args.get('socrata_4x4')
    return publish_doi(socrata_4x4=socrata_4x4)


@app.route('/update.doi', methods=['POST'])
def api_update_doi():
    socrata_4x4 = request.args.get('socrata_4x4')
    identifier = request.args.get('identifier')
    update_doi(socrata_4x4=socrata_4x4, identifier=identifier)


@app.route('/gather.socrata.assets', methods=['GET'])
def api_gather_assets():
    return jsonify(gather_assets())


if __name__ == '__main__':
    app.run(debug=True)
