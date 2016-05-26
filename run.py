from app_package import app

host_ = app.config['HOST']
port_ = app.config['PORT']
debug_ = app.config['DEBUG']
if __name__ == '__main__':
	app.run(host=host_ , port=port_ ,debug=debug_)