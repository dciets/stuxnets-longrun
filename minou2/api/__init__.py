from . import auth
from . import anal
from . import search

def Api(app):
    # # POST /auth
    # Authenticate a user.
    #
    # Request must include a  |username| and |password| field that will be used
    # to find and validate the user.
    #
    # The response contains the "token" field to be used in following
    # authenticated requests set in the "X-Auth-Token" header.
    app.add_url_rule('/auth', 'auth', auth.auth, methods=['POST'])

    # POST /anal
    # Create a new analysis job for a given text.
    #
    # The request should contains the |data| field containing the text to be
    # analyzed. The response should contains the |job| field that can later be
    # reused to poll the task status and get the task result from
    # `GET /anal/<task_id>`.
    app.add_url_rule('/anal', 'create_anal', anal.create, methods=['POST'])

    # GET /anal/<task_id>
    # Get a job status in the |status| field. If the job has successfully
    # completed, the result is available in the |result|.
    app.add_url_rule('/anal/<task_id>', 'poll_anal', anal.poll, methods=['GET'])

    # POST /search
    # Create a new job search for images related to concepts extracted from an
    # analysis job. The response should contains the |job| field that can later be
    # reused to poll the task status and get the task result from
    app.add_url_rule('/search', 'create_search', search.create, methods=['POST'])

    # GET /search/<task_id>
    # Get a job status in the |status| field. If the job has successfully
    # completed, the result is available in the |result|.
    app.add_url_rule('/search/<task_id>', 'poll_search', search.poll, methods=['GET'])

