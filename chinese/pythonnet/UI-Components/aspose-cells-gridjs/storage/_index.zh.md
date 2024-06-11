---
title: 使用 GridJs 存储实现
type: docs
weight: 250
url: /zh/python-net/aspose-cells-gridjs/storage/
description: 本文描述了 Aspose.Cells.GridJs 的通用处理。
keywords: 文件缓存、存储、GridJs、GridJs 存储、GridJs uid、下载、唯一标识、缓存、编辑器、编辑、电子表格、excel
---


# 使用 GridJs 存储
##  通用文件处理 
导入电子表格文件后，

GridJs 将在 **`Config.file_cache_directory`** 文件夹中创建具有指定 uid 的缓存文件，

格式为 [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat")，

GridJs 还将所有形状/图像保存到 **`Config.file_cache_directory`** 文件夹中的 zip 归档文件中，以便后续在客户端 UI 中显示形状/图像。

在客户端 UI 中的每次更新操作之后，

例如设置单元格值、设置单元格样式等，

GridJs 客户端 js 将触发 ajax 调用执行 UpdateCell 操作。

在此操作过程中，UpdateCell 方法将发生对缓存文件的保存。
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

### 如何获取更新后的结果文件
#### 1. 为文件指定uid 
请确保文件和uid之间有指定的映射对应关系， 

您可以始终为指定的文件名获取相同的uid，而不是随机生成的。

例如，只需使用文件名即可。
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
实际上，对于一些客户端UI操作，

例如：

切换活动工作表到另一个，

更改图像位置，

旋转/调整图像等。

UpdateCell操作将不被触发。

因此，如果我们想要获得更新后的文件与客户端UI显示的完全相同，

我们需要在保存操作之前执行合并操作，以同步这些客户端UI操作。
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

#### 3. get the file from cache
for example :in the getfile action,you can just get it from the cache directory by uid.
```python

        mimetype=guess_mime_type_from_filename(filename)
        file_path = os.path.join(Config.file_cache_directory, uid.replace('/', '.')+"."+filename)
        # check file
        if os.path.isfile(file_path):
             return send_file(file_path, as_attachment=True, download_name=filename, mimetype=mimetype)
```

更多详细信息，请查看这里的示例:
<https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Examples_GridJs_Python_Net>
