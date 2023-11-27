import traceback

from app import app
from database import create_db

if __name__ == "__main__":

    if create_db():
        print("Database created successfully")
    else:
        print("Database creation failed")
    try:
        app.run(debug=True, host="localhost", port=8047)
    except Exception as e:
        traceback.print_exc()


