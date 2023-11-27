import traceback

from app import app
from database import create_db

if __name__ == "__main__":
    create_db()
    try:
        app.run(debug=True, host="localhost", port=8047)
    except Exception as e:
        traceback.print_exc()


