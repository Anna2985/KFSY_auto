from pywinauto import Application
from datetime import datetime
from flask import Flask, jsonify
import shutil
import os
# def move_file(source_path, destination_path):
#     if not os.path.exists(source_path):
#         print('來源檔案不存在')
#         return
#     if not os.path.exists(destination_path):
#         os.makedirs(destination_path)
#     destination_file_path = os.path.join(destination_path,os.path.basename(source_path))
#     if os.path.exists(destination_file_path):
#         os.remove(destination_file_path)
#     try:
#         shutil.move(source_path,destination_path)
#         print(f'檔案已從{source_path}移動到{destination_path}')
#     except Exception as e:
#         print(f'移動檔案發生錯誤')
time_start = datetime.now()
uds_app = Application('uia')
uds_app.connect(path='UDS022P.exe', timeout=5)
# print(app.windows())
np = uds_app['程式【UDS022P】版本:1.20.1.1 Butterfly@']  # 代表記事本窗體
# np.dump_tree()
# np['查詢資料'].click_input()
np['匯出'].click_input()
# print(np.children())
save_dialog = uds_app.window(title='另存新檔')
#save_dialog['Button10'].click_input()
save_dialog['本機'].click_input()
pc_dialog = uds_app.window(title='另存新檔')
file_list = pc_dialog.child_window(title="資料夾檢視",control_type="List")
file_group = file_list.child_window(title='裝置和磁碟機 (1)', control_type='Group')
#file_group.dump_tree()
file_group.child_window(title="本機磁碟 (C:)", control_type="ListItem").double_click_input()
pc_dialog.child_window(title="Anna", control_type="ListItem").double_click_input()
#pc_dialog.dump_tree()
# C_group = file_group.child_window(title="本機磁碟 (C:)", control_type="ListItem")
# C_group['本機磁碟 (C:)'].double_click_input()

file_name_combo = save_dialog.child_window(title='檔案名稱(N):', control_type='ComboBox')

file_name_edit = file_name_combo.child_window(control_type='Edit')
default_file_name = file_name_edit.get_value()

save_dialog['存檔(S)'].click_input()
check_dialog = uds_app.window(title='程式')
check_dialog['OKButton'].click_input()
print(f'已取得 fileName : {default_file_name}')
time_end = datetime.now()
print(f"取得EXCELL:{time_end-time_start}")
#source_file  = fr'C:\{default_file_name}'
#destination_folder = r"C:\Users\Administrator\Downloads\HIS"
#shutil.move(source_file, destination_folder)
#move_file(source_file,destination_folder)
# app = Flask(__name__)
# @app.route('/api/get_file_name', methods=['GET'])
# def get_file_name():
#     uds_app = Application('uia')
#     uds_app.connect(path='UDS022P.exe', timeout=5)
#     # print(app.windows())
#     np = uds_app['程式【UDS022P】版本:1.20.1.1 Butterfly@']  # 代表記事本窗體
#     # np.dump_tree()
#     # np['查詢資料'].click_input()
#     np['匯出'].click_input()
#     # print(np.children())
#     save_dialog = uds_app.window(title='另存新檔')
#     # save_dialog.dump_tree()
#     file_name_combo = save_dialog.child_window(title='檔案名稱(N):', control_type='ComboBox')
#
#     file_name_edit = file_name_combo.child_window(control_type='Edit')
#     default_file_name = file_name_edit.get_value()
#     save_dialog['存檔(S)'].click_input()
#     check_dialog = uds_app.window(title='程式')
#     check_dialog['OKButton'].click_input()
#     print(f'已取得 fileName : {default_file_name}')
#     source_file  = fr'C:\{default_file_name}'
#     destination_folder = r"C:\Users\Administrator\Downloads\HIS"
#     #shutil.move(source_file, destination_folder)
#     move_file(source_file,destination_folder)
#     return jsonify({
#         'result':default_file_name
#     })


# if __name__ == '__main__':
#     app.run(debug=True)





