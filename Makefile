generate_grpc_code:
	python -m grpc_tools.protoc --proto_path=. test.proto --python_out=. --grpc_python_out=.
	pyside6-uic RegisterWindow.ui > ui_RegisterWindow.py
	pyside6-uic MainWindow.ui > ui_MainWindow.py
	pyside6-uic LoginWindow.ui > ui_LoginWindow.py




