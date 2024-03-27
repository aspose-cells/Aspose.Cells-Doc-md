---
title: Working with GridJs storage
type: docs
weight: 250
url: /python-net/aspose-cells-gridjs/storage/
description: This article describes the general processing for  Aspose.Cells.GridJs.
keywords: file cache,storage,GridJs,GridJs storage,GridJs uid,download,uniqueid,cache,editor,edit,spreadsheet,excel
---


# Working With GridJs Storage
##  the general file process 
After import a spread sheet file ,

GridJs will create a cache file with the specified uid in the **`Config.file_cache_directory`** folder  ,

with the format of [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs will also saves all shapes/images to a zip archive file in the **`Config.file_cache_directory`** folder for later display shapes/images in the client UI.

and after every update operation in the client UI,

for example set cell value,set cell style,etc. ,

GridJs  client side js will trigger  ajax call  to do a UpdateCell operation.

In this action a save back to the cache file  will occur during the  UpdateCell method.
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
 
###  how to get the updated result file
#### 1. a specified uid for file 
Make sure a specified maping correspondence  between the file and the uid, 

you can always get the same uid for a specifed file name,not from random generation.

For example just use the filename is ok.
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

#### 2. sync with client UI operation
Actually for some client UI operation,

for example:

switch the acitve sheet to another,

change the image postion,

rotate/resize image,etc.

the UpdateCell action will not triggered.

Thus if we want to get the updated file just same as the client UI shows,

we need to do a merge operation before save action to sync those client UI operation.
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

For more detail info ,you can check the example here:
<https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Examples_GridJs_Python_Net>
