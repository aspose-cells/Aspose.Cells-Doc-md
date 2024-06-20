---
title: Работа с хранилищем GridJs
type: docs
weight: 250
url: /ru/python-net/aspose-cells-gridjs/storage/
description: В этой статье описана общая обработка для Aspose.Cells.GridJs.
keywords: кэш файлов, хранилище, GridJs, хранилище GridJs, уник идентификатор GridJs, скачать, уникальный идентификатор, кэш, редактор, редактировать, электронная таблица, Excel
---


# Работа с хранилищем GridJs
##  процесс работы с общим файлом 
После импорта файла таблицы ,

GridJs создаст файл кэша с указанным идентификатором (UID) в папке **`Config.file_cache_directory`** ,

в формате [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat"),

GridJs также сохраняет все формы/изображения в zip-архивном файле в папке **`Config.file_cache_directory`** для последующего отображения форм/изображений в пользовательском интерфейсе (UI).

и после каждой операции обновления в клиентском интерфейсе (UI),

например, установка значения ячейки, установка стиля ячейки и т. д.,

клиентская часть js GridJs вызовет ajax-запрос для выполнения операции UpdateCell.

В этом действии происходит сохранение обратно в файл кэша во время выполнения метода UpdateCell.
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

###  как получить обновленный результат файла
#### 1. указанный идентификатор (UID) для файла 
Убедитесь, что существует соответствие между файлом и идентификатором (UID), 

вы всегда можете получить один и тот же идентификатор (UID) для заданного имени файла, а не случайно сгенерированный.

Например, достаточно использовать имя файла.
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

#### 2. синхронизация с клиентским интерфейсом (UI)
Фактически, для некоторых операций интерфейса (UI) клиента,

например:

смена активного листа на другой,

изменение позиции изображения,

вращать/изменить размер изображения и т. д.

действие UpdateCell не будет вызвано.

Таким образом, если мы хотим получить обновленный файл такой же, как показывает клиентский интерфейс,

нам нужно выполнить операцию слияния перед сохранением, чтобы синхронизировать операции клиентского интерфейса.
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

#### 3. получить файл из кэша
например: в действии getfile, вы можете просто получить его из каталога кэша по uid.
```python

        mimetype=guess_mime_type_from_filename(filename)
        file_path = os.path.join(Config.file_cache_directory, uid.replace('/', '.')+"."+filename)
        # check file
        if os.path.isfile(file_path):
             return send_file(file_path, as_attachment=True, download_name=filename, mimetype=mimetype)
```

Для получения более подробной информации вы можете проверить пример здесь:
<https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Examples_GridJs_Python_Net>
