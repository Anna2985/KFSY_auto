from Tools.scripts.make_ctype import method
from pywinauto import Application, timings
from flask import Flask, jsonify
app = Flask(__name__)
uds_app = Application('uia')
uds_app.connect(path='UDS022P.exe', timeout=5)
#print(app.windows())
np = uds_app['程式【UDS022P】版本:1.20.1.1 Butterfly@'] #代表記事本窗體
#np.dump_tree()
@app.route('/api/get_file_name', methods=['GET'])
def get_file_name():
    # np['查詢資料'].click_input()
    np['匯出'].click_input()
    # print(np.children())
    save_dialog = uds_app.window(title='另存新檔')
    # save_dialog.dump_tree()
    file_name_combo = save_dialog.child_window(title='檔案名稱(N):', control_type='ComboBox')

    file_name_edit = file_name_combo.child_window(control_type='Edit')
    default_file_name = file_name_edit.get_value()
    save_dialog['存檔(S)'].click_input()
    check_dialog = uds_app.window(title='程式')
    check_dialog['OKButton'].click_input()
    print(f'已取得 fileName : {default_file_name}')
    return jsonify({
        'result':default_file_name
    })


if __name__ == '__main__':
    app.run(debug=True)



