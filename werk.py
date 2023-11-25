import traceback

from app import app

if __name__ == "__main__":
    try:
        app.run(debug=True, host="localhost", port=8047)
    except Exception as e:
        traceback.print_exc()

