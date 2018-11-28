from publish_doi import assemble_payload
from publish_doi import assemble_xml
from publish_doi import publish_doi

from update_doi import update_doi

from extract_metadata import gather_assets

# waiting to implement database refactor
# from extract_metadata import load_temp_table
# from extract_metadata import diff_temp_table

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def lambda_handler(event=None, context=None):
    return 'test'


@app.route('/assemble.payload', methods=['GET'])
def assemble_payload():
    socrata_4x4 = request.headers.get('socrata_4x4')
    draft = request.headers.get('draft')
    return assemble_payload(socrata_4x4=socrata_4x4, draft=draft)


@app.route('/assemble.xml', methods=['GET'])
def assemble_xml():
    metadata = request.headers.get('metadata')
    doi_identifier = request.headers.get('doi_identifier')
    return assemble_xml(metadata=metadata, doi_identifier=doi_identifier)


@app.route('/publish.doi', methods=['POST'])
def publish_doi():
    socrata_4x4 = request.headers.get('socrata_4x4')
    return publish_doi(socrata_4x4=socrata_4x4)


@app.route('/update.doi', methods=['POST'])
def update_doi():
    socrata_4x4 = request.headers.get('socrata_4x4')
    identifier = request.headers.get('identifier')
    update_doi(socrata_4x4=socrata_4x4, identifier=identifier)


@app.route('/gather.socrata.assets', methods=['GET'])
def gather_assets():
    return gather_assets()


if __name__ == '__main__':
    app.run(debug=True)
