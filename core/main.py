import flask
import json
from Config.Server import config
from Delivery import handler

app = flask.Flask(config.SERVER_NAME)
# app.config["DEBUG"] = True

app = handler.setup(app)

app.run(host="0.0.0.0", port=config.PORT)
