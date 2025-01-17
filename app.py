from flask import Flask
from routes.user_routes import user_bp
from routes.inventory_routes import inventory_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    
    # 注册蓝图
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)