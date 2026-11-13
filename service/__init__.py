import os
from flask import Flask
from flask_talisman import Talisman

def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    
    # Konfigurasi Talisman untuk Security Headers
    # force_https diset False jika berjalan di lingkungan lokal/development port 8080 tanpa SSL
    talisman = Talisman(app, force_https=False)

    with app.app_context():
        # Import rute/blueprint aplikasi di sini
        from service import routes

        return app

app = create_app()
