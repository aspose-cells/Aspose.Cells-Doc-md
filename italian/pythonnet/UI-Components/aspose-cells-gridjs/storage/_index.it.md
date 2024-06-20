---
title: Lavorare con lo storage di GridJs
type: docs
weight: 250
url: /it/python-net/aspose-cells-gridjs/storage/
description: Questo articolo descrive il trattamento generale per Aspose.Cells.GridJs.
keywords: file cache, archiviazione, GridJs, archiviazione GridJs, uid GridJs, download, id univoco, cache, editor, modifica, foglio elettronico, excel
---


# Lavorare con lo storage di GridJs
##  il processo generale dei file 
Dopo l'importazione di un file di foglio di calcolo ,

GridJs creerà un file di cache con l'uid specificato nella cartella **`Config.file_cache_directory`**,

con il formato di [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat"),

GridJs salva anche tutte le forme/immagini in un file di archivio zip nella cartella **`Config.file_cache_directory`** per visualizzare successivamente forme/immagini nell'interfaccia utente del client.

e dopo ogni operazione di aggiornamento nell'interfaccia utente del client,

ad esempio impostare il valore della cella, impostare lo stile della cella, ecc. ,

Il JavaScript lato client di GridJs attiverà una chiamata Ajax per eseguire un'operazione di UpdateCell.

In questa azione si verificherà un salvataggio nel file di cache durante il metodo UpdateCell.
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

###  come ottenere il file di risultato aggiornato
#### 1. un uid specifico per il file 
Assicurarsi di una corrispondenza mappatura specifica tra il file e l'uid, 

potete sempre ottenere lo stesso uid per un nome file specificato, non da una generazione casuale.

Ad esempio basta usare il nome del file.
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

#### 2. sincronizzazione con operazioni UI del client
In realtà per alcune operazioni UI del client,

ad esempio:

passare alla scheda attiva,

cambiare la posizione dell'immagine,

ruotare/ridimensionare l'immagine, ecc.

l'azione di UpdateCell non verrà attivata.

Quindi se vogliamo ottenere il file aggiornato esattamente come lo mostra l'interfaccia utente del client,

dobbiamo eseguire un'operazione di merge prima dell'azione di salvataggio per sincronizzare quelle operazioni UI del client.
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

### 3. ottenere il file dalla cache
ad esempio: nell'azione getfile, è possibile ottenerlo semplicemente dalla cartella cache tramite uid.
```python

        mimetype=guess_mime_type_from_filename(filename)
        file_path = os.path.join(Config.file_cache_directory, uid.replace('/', '.')+"."+filename)
        # check file
        if os.path.isfile(file_path):
             return send_file(file_path, as_attachment=True, download_name=filename, mimetype=mimetype)
```

Per maggiori dettagli, puoi controllare l'esempio qui:
<https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Examples_GridJs_Python_Net>
