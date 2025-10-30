---
title: Arbeiten mit GridJs Speicher
type: docs
weight: 250
url: /de/python-net/aspose-cells-gridjs/storage/
description: Dieser Artikel beschreibt die allgemeine Verarbeitung für Aspose.Cells.GridJs.
keywords: Dateicache, Speicher, GridJs, GridJs Speicher, GridJs UID, Herunterladen, eindeutige Kennung, Cache, Editor, Bearbeiten, Tabellenblatt, Excel
---


# Arbeiten mit GridJs-Speicher
##  Der allgemeine Dateiprozess 
Nach dem Import einer Tabellendatei erstellt GridJs eine Cache-Datei mit der angegebenen UID im Ordner **`Config.file_cache_directory`** ,

GridJs wird eine Cache-Datei mit der angegebenen UID im Ordner **`Config.file_cache_directory`** erstellen.

mit dem Format von [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs speichert auch alle Formen/Bilder in einer Zip-Archivdatei im Ordner **`Config.file_cache_directory`** , um sie später im Client-UI anzuzeigen.

und nach jeder Aktualisierung im Client-UI

zum Beispiel Zellenwert setzen, Zellenstil setzen usw.

GridJs clientseitiges js wird einen Ajax-Aufruf auslösen, um eine UpdateCell-Operation durchzuführen.

In dieser Aktion wird während der UpdateCell-Methode eine Rückkehr zur Cache-Datei erfolgen.
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

### wie man die aktualisierte Ergebnisdatei erhält
#### 1. eine spezifische UID für die Datei 
Stellen Sie sicher, dass es eine spezielle Zuordnung zwischen der Datei und der UID gibt, 

Sie können immer die gleiche UID für einen bestimmten Dateinamen erhalten, nicht durch zufällige Generierung.

Verwenden Sie zum Beispiel einfach den Dateinamen.
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

#### 2. Synchronisieren mit Client-UI-Betrieb
Tatsächlich für einige Client-UI-Operationen,

zum Beispiel:

Schalten Sie das aktive Blatt zu einem anderen um,

Ändern Sie die Bildposition,

Bild drehen/vergrößern, usw.

Die UpdateCell-Aktion wird nicht ausgelöst.

Deshalb, wenn wir die aktualisierte Datei genauso anzeigen möchten, wie es das Client-UI zeigt,

müssen wir vor der Speicheraktion eine Zusammenführungsoperation durchführen, um diese Client-UI-Operationen zu synchronisieren.
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

#### 3. die Datei aus dem Cache erhalten
zum Beispiel: in der getFile-Aktion können Sie sie einfach aus dem Cache-Verzeichnis nach der UID abrufen.
```python

        mimetype=guess_mime_type_from_filename(filename)
        file_path = os.path.join(Config.file_cache_directory, uid.replace('/', '.')+"."+filename)
        # check file
        if os.path.isfile(file_path):
             return send_file(file_path, as_attachment=True, download_name=filename, mimetype=mimetype)
```

Weitere Detailinformationen finden Sie hier:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>
