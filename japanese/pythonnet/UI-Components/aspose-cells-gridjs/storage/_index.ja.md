---
title: GridJsストレージで作業する
type: docs
weight: 250
url: /ja/python-net/aspose-cells-gridjs/storage/
description: この記事では、Aspose.Cells.GridJsの一般的な処理について説明しています。
keywords: ファイルキャッシュ、ストレージ、GridJs、GridJsストレージ、GridJs UID、ダウンロード、ユニークID、キャッシュ、エディター、編集、スプレッドシート、Excel
---


# GridJsストレージで作業する
## 一般的なファイル処理 
スプレッドシートファイルをインポートした後、

GridJsは**`Config.file_cache_directory`**フォルダー内に指定されたUIDでキャッシュファイルを作成します。

[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat")の形式で保存します。

GridJsは、クライアントUIで後で図形/画像を表示するために、指定されたUIDで**`Config.file_cache_directory`**フォルダー内にzipアーカイブファイルにすべての図形/画像を保存します。

クライアントUIでの更新操作後、

たとえば、セル値を設定する、セルスタイルを設定するなど、

GridJsのクライアント側JSは、UpdateCell操作を行うためにAjax呼び出しをトリガーします。

このアクションでは、UpdateCellメソッド中にキャッシュファイルへの保存が発生します。
```python  
# update action :/GridJs2/UpdateCell
@app.route('/GridJs2/UpdateCell', methods=['POST'])
def update_cell():
    # get request param 
    p = request.form.get('p')
    uid = request.form.get('uid')

    gwb = GridJsWorkbook()

    ret = gwb.update_cell(p, uid)

    return Response(ret, content_type='text/plain; charset=utf-8')
```

### 更新された結果ファイルの取得方法
#### 1. ファイルの指定されたUID 
ファイルとUIDの間の指定されたマッピングの対応を確認してください。 

指定されたファイル名の場合、常に同じUIDを取得できます。ランダムな生成ではありません。

たとえば、ファイル名だけを使用しても問題ありません。
```python  

...
# get json info from : /GridJs2/DetailFileJsonWithUid?filename=&uid=
@app.route('/GridJs2/DetailFileJsonWithUid', methods=['GET'])
def detail_file_json_with_uid():
    filename = request.args.get('filename')
    uid = request.args.get('uid')
    if not filename:
        return jsonify({'error': 'filename is required'}), 400
    if not uid:
        return jsonify({'error': 'uid is required'}), 400
    gwb = GridJsWorkbook()
    file_path = os.path.join(FILE_DIRECTORY, filename)

    # check file
    if not os.path.isfile(file_path):
        return jsonify({'error': 'file not found:'+file_path}), 404
    try:
        sb = gwb.get_json_str_by_uid(uid, filename)
        if sb == None:
            gwb.import_excel_file(uid, file_path)
            sb = gwb.export_to_json(filename)
        response = Response(sb, status=200, mimetype='text/plain')
        response.headers['Content-Type'] = 'text/plain; charset=utf-8'
        return response

    except Exception as ex:
        return jsonify({'error': str(ex)}), 500

```

#### 2. クライアントUI操作と同期
実際には、一部のクライアントUI操作に対して、

たとえば：

別のシートにアクティブシートを切り替える、

画像の位置を変更する、

画像の回転/サイズ変更など。

UpdateCellアクションはトリガーされません。

したがって、クライアントUIが表示するように更新されたファイルを取得するには、

これらのクライアントUI操作を同期するために保存アクションの前にマージ操作を実行する必要があります。
```javascript
//in the js
  function save() {
            if (!xs.buffer.isFinish()) {
              alert('updating is inprogress,please try later');
                return;
            }
            let datas = xs.datas;
            delete datas.history;
            delete datas.search;
            delete datas.images;
            delete datas.shapes;

        var jsondata = {
          sheetname: xs.sheet.data.name,
          actrow: xs.sheet.data.selector.ri,
          actcol: xs.sheet.data.selector.ci,
          datas: xs.getUpdateDatas(),
        };

        const data = {
          p: JSON.stringify(jsondata),
          uid: uniqueid,
        };
		....
		//go on to do ajax post to trigger controller action
```
```python
# in download route action 
        gwb = new GridJsWorkbook();
        gwb.merge_excel_file_from_json(uid, p)
        # after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
        gwb.save_to_cache_with_file_name(uid, filename, None);
```         

#### 3. キャッシュからファイルを取得
例えば：getfileアクションでは、UIDによってキャッシュディレクトリから直接それを取得できます。
```python

        mimetype=guess_mime_type_from_filename(filename)
        file_path = os.path.join(Config.file_cache_directory, uid.replace('/', '.')+"."+filename)
        # check file
        if os.path.isfile(file_path):
             return send_file(file_path, as_attachment=True, download_name=filename, mimetype=mimetype)
```

詳細情報については、こちらの例をご確認ください：
<https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Examples_GridJs_Python_Net>
