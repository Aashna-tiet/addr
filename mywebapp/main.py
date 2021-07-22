from flask import Flask
import views as V


def create_app():
    app = Flask(__name__, static_url_path='')
    # app.config.from_pyfile(config_filename)
    # Set the secret key to some random bytes. Keep this really secret!
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    return app


def init_routes(app):
    app.add_url_rule("/", view_func=V.entry, methods=["GET"])
    # app.add_url_rule("/login", view_func = V.loginPage , methods = ["GET","POST"])
    app.add_url_rule("/login", view_func=V.login, methods=["POST", "GET"])
    app.add_url_rule("/registration", view_func=V.doRegistration,
                     methods=["POST", "GET"])
    app.add_url_rule("/home/<user>", view_func=V.home, methods=["POST", "GET"])
    app.add_url_rule("/logout", view_func=V.logout, methods=["GET"])
    app.add_url_rule("/ajaxtest", view_func=V.myajax, methods=["GET"])
    app.add_url_rule("/ajax/<string:msg>/<string:res_type>",
                     view_func=V.test_ajax, methods=["GET"])


if __name__ == "__main__":
    myApp = create_app()
    init_routes(myApp)
    print("Created app. Starting it...")
    myApp.run(host="localhost", port=8888)
# changes
