from pywinauto import Application, timings

#app = Application('win32')
app = Application('uia')
#app.start('notepad')
app.connect(path='UDS022P.exe', timeout=5)
#app.connect()
#print(app.windows())
np = app['程式【UDS022P】版本:1.20.1.1 Butterfly@'] #代表記事本窗體
#np.dump_tree()
#np['查詢資料'].click_input()
np['匯出'].click_input()
#print(np.children())

save_dialog = app.window(title='另存新檔')
#save_dialog.dump_tree()
file_name_combo = save_dialog.child_window(title='檔案名稱(N):', control_type = 'ComboBox')

file_name_edit = file_name_combo.child_window(control_type ='Edit')
default_file_name  = file_name_edit.get_value()
save_dialog['存檔(S)'].click_input()
check_dialog = app.window(title='程式')
check_dialog['OKButton'].click_input()
print(f'已取得 fileName : {default_file_name}')

