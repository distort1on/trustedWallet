generate_grpc_code:
	python -m grpc_tools.protoc --proto_path=. grpcClient.proto --python_out=. --grpc_python_out=.
	pyside6-uic UI_Files/RegisterWindow.ui > PyUI_Files/ui_RegisterWindow.py
	pyside6-uic UI_Files/MainWindow.ui > PyUI_Files/ui_MainWindow.py
	pyside6-uic UI_Files/LoginWindow.ui > PyUI_Files/ui_LoginWindow.py
	pyside6-uic UI_Files/ResponseWindow.ui > PyUI_Files/ui_ResponseWindow.py
	pyside6-uic UI_Files/RestoreWindow.ui > PyUI_Files/ui_RestoreWindow.py
	pyside6-uic UI_Files/FindTxByHashWindow.ui > PyUI_Files/ui_FindTxByHashWindow.py
	pyside6-uic UI_Files/FindDocumentByHash.ui > PyUI_Files/ui_FindDocumentByHash.py



