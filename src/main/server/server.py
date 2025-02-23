from flask import Flask # type: ignore
from src.main.routes.event import event_route_bp
from src.main.routes.subscriber import subs_route_bp
from src.main.routes.events_link import events_link_route_bp

app = Flask(__name__)

app.register_blueprint(event_route_bp)
app.register_blueprint(subs_route_bp)
app.register_blueprint(events_link_route_bp)