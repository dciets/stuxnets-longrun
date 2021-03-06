Long running competition for team STUXNETS from ÉTS.

# Setup
 * `virtualenv -p python3 venv`
 * `source venv/bin/activate`
 * `pip install -r requirements.txt`
 * Install `redis`

# Running
 * Set up API keys:
   - AlchemyApi: `export ALCHEMYAPI_TOKEN=<your token>`
   - Shutterstock: `export SHUTTERSTOCK_SECRET=<your token>`
   - Get the token from one of the pinned items on DCI's Slack or register on
     both services.
 * Start redis: `redis-server`
 * Start Celery worker: `celery -A minou2 worker --loglevel=info`
 * Start web server: `python run.py`
 * Browse to `http://localhost:5000/static/index.html`

# Done
 * Create analysis tasks (`minou2/analysis.py`):
   - `POST /anal`
   - `GET /anal/<id>`
 * Search images related to analysis (`minou2/models/images.py`, `minou2/providers/*.py`):
   - `POST /search`
   - `GET /search/<id>`
 * Frontend:
   - TinyMCE editor
   - Drag and drop images in post
 * Authenticate [Partial] (`minou2/api/auth.py`)
   - `POST /auth`

# TODO
 * Local images provider
 * Cache analsysis/search results
 * Display images prices
 * Save/load posts
