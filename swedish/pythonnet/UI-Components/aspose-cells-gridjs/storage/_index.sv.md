---
title: Arbeta med GridJs lagring
type: docs
weight: 250
url: /sv/python-net/aspose-cells-gridjs/storage/
description: Denna artikel beskriver den allmänna bearbetningen för Aspose.Cells.GridJs.
keywords: filcache, lagring, GridJs, GridJs lagring, GridJs uid, nedladdning, unikid, cache, redigerare, redigering, kalkylblad, excel
---


# Arbeta med GridJs-lagring
## den allmänna filhanteringen 
Efter import av en kalkylbladsfil,

GridJs kommer att skapa en cacheläsningsfil med den angivna uid i **`Config.file_cache_directory`**-mappen ,

i formatet [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs sparar också alla former/bilder till en ziparkivfil i **`Config.file_cache_directory`**-mappen för senare visning av former/bilder i klientens UI.

och efter varje uppdatering i klientgränssnittet,

till exempel ställa in cellvärde, ställa in cellstil, osv.,

GridJs klient sid js kommer att utlösa en ajax-anrop  för att genomföra en UpdateCell-operation.

I denna åtgärd kommer en sparning tillbaka till cache-filen att inträffa under UpdateCell-metoden.
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

### hur man får den uppdaterade resultatsfilen
#### 1. ett specifierad uid för filen 
Se till att en specifierad kartläggning korrespondens mellan filen och uid finns, 

Du kan alltid få samma uid för ett angivet filnamn, inte från slumpmässig generering.

Till exempel är det bra att bara använda filnamnet.
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

#### 2. synkronisera med klientens UI-operation
Faktum är att för vissa klienters UI-operation,

till exempel:

växla det aktiva kalkylarket till ett annat,

ändra bildplaceringen,

rotera/ändra bildstorlek, etc.

kommer inte UpdateCell-åtgärden att utlösas.

Så om vi vill få den uppdaterade filen precis som klientens UI visar,

måste vi göra en sammanfogning innan spara-åtgärden för att synkronisera de där klientens UI-operationerna.
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

#### 3. hämta filen från cache
till exempel: i getfile-åtgärden kan du bara hämta den från cache-mappen efter UID.
```python

        mimetype=guess_mime_type_from_filename(filename)
        file_path = os.path.join(Config.file_cache_directory, uid.replace('/', '.')+"."+filename)
        # check file
        if os.path.isfile(file_path):
             return send_file(file_path, as_attachment=True, download_name=filename, mimetype=mimetype)
```

För mer detaljerad information kan du kolla exemplet här:
<https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Examples_GridJs_Python_Net>
