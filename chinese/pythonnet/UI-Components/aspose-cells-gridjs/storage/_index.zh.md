---
title: 使用GridJs存储
type: docs
weight: 250
url: /zh/python-net/aspose-cells-gridjs/storage/
description: 本文描述了Aspose.Cells.GridJs的一般处理。
keywords: 文件缓存，存储，GridJs，GridJs存储，GridJs uid，下载，唯一标识，缓存，编辑器，编辑，电子表格，excel
---


# 使用GridJs存储
## 一般文件处理 
导入电子表格文件后，

GridJs将在**`Config.file_cache_directory`**文件夹中创建具有指定uid的缓存文件，

具有[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat")格式，

GridJs还将所有形状/图像保存到**`Config.file_cache_directory`**文件夹中的zip存档文件中，以便以后在客户端UI中显示形状/图像，

并且在客户端UI中的每次更新操作之后，

例如设置单元格值，设置单元格样式等，

GridJs客户端js将触发ajax调用以执行UpdateCell操作，

在此操作中，在UpdateCell方法期间将进行一次保存回缓存文件。
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

### 如何获得更新后的结果文件
#### 1. 为文件指定uid 
确保文件和uid之间有指定的映射对应关系， 

您始终可以获得指定文件名的相同uid，而不是随机生成的。

例如，只使用文件名即可。
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

#### 2. 与客户端UI操作同步
实际上，对于某些客户端UI操作，

例如：

切换活动工作表到另一个，

改变图像位置，

旋转/调整图像大小等。

不会触发UpdateCell操作。

因此，如果想要获得更新后的文件与客户端UI显示的内容相同，

我们需要在保存操作之前执行一个合并操作，以同步客户端UI操作。
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

#### 3. 从缓存中获取文件
例如：在getfile操作中，您可以通过uid直接从缓存目录获取文件。
```python

        mimetype=guess_mime_type_from_filename(filename)
        file_path = os.path.join(Config.file_cache_directory, uid.replace('/', '.')+"."+filename)
        # check file
        if os.path.isfile(file_path):
             return send_file(file_path, as_attachment=True, download_name=filename, mimetype=mimetype)
```

更多详细信息，请参阅此处示例：
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>
