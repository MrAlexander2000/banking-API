from bank_api_app import create_app


#create setup app routes
app = create_app()

#run app
if __name__ == "__main__":
    app.run(debug=True)