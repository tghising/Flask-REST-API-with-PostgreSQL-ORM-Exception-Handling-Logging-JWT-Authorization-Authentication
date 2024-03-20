from app import create_app


# create app
app = create_app(environment='development')

if __name__ == '__main__':
    # run app
    app.run()
