from src import app, PORT, HOST

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)