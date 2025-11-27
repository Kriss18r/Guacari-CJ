from guacari import create_app

app = create_app()

## Run the application
if __name__ == "__main__": 
    app.run(debug=True)