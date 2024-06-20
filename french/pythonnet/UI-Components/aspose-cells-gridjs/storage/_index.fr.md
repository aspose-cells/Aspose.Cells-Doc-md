---
title: Travailler avec le stockage GridJs
type: docs
weight: 250
url: /fr/python-net/aspose-cells-gridjs/storage/
description: Cet article décrit le traitement général pour Aspose.Cells.GridJs.
keywords: cache de fichier,stockage,GridJs,stockage de GridJs,uid de GridJs,téléchargement,identifiant unique,cache,éditeur,modifier,feuille de calcul,excel
---


# Travailler avec le stockage GridJs
## le processus général du fichier 
Après avoir importé un fichier de feuille de calcul,

GridJs créera un fichier de cache avec l'uid spécifié dans le dossier **`Config.file_cache_directory`** ,

avec le format [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs sauvegardera également toutes les formes/images dans un fichier d'archive zip dans le dossier **`Config.file_cache_directory`** pour afficher ultérieurement les formes/images dans l'interface utilisateur du client.

et après chaque opération de mise à jour dans l'interface utilisateur du client,

par exemple, définir la valeur de la cellule, définir le style de la cellule, etc. ,

Le javascript côté client de GridJs déclenchera un appel ajax pour effectuer une opération UpdateCell.

Dans cette action, une sauvegarde dans le fichier de cache se produira pendant la méthode UpdateCell.
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

### comment obtenir le fichier de résultat mis à jour
#### 1. un uid spécifié pour le fichier 
Assurez-vous qu'il existe une correspondance de mappage spécifiée entre le fichier et l'uid. 

vous pouvez toujours obtenir le même uid pour un nom de fichier spécifié, pas généré aléatoirement.

Par exemple, utilisez simplement le nom du fichier.
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

#### 2. synchroniser avec l'opération de l'interface utilisateur du client
En fait, pour certaines opérations de l'interface utilisateur du client,

par exemple :

passer à une autre feuille active,

changer la position de l'image,

faire pivoter/redimensionner l'image, etc.

l'action UpdateCell ne sera pas déclenchée.

Ainsi, si nous voulons obtenir le fichier mis à jour exactement comme l'interface utilisateur du client le montre,

nous devons effectuer une opération de fusion avant l'action de sauvegarde pour synchroniser ces opérations de l'interface utilisateur du client.
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

#### 3. obtenir le fichier depuis le cache
par exemple : dans l'action getfile, vous pouvez simplement l'obtenir depuis le répertoire cache par uid.
```python

        mimetype=guess_mime_type_from_filename(filename)
        file_path = os.path.join(Config.file_cache_directory, uid.replace('/', '.')+"."+filename)
        # check file
        if os.path.isfile(file_path):
             return send_file(file_path, as_attachment=True, download_name=filename, mimetype=mimetype)
```

Pour plus d'informations détaillées, vous pouvez consulter l'exemple ici :
<https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET/tree/main/Examples_GridJs_Python_Net>
