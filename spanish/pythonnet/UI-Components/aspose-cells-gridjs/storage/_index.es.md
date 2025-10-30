---
title: Trabajando con el almacenamiento de GridJs
type: docs
weight: 250
url: /es/python-net/aspose-cells-gridjs/storage/
description: Este artículo describe el procesamiento general para Aspose.Cells.GridJs.
keywords: almacenamiento de archivo, almacenamiento, GridJs, almacenamiento de GridJs, uid de GridJs, descarga, identificador único, caché, editor, editar, hoja de cálculo, excel
---


# Trabajando con el almacenamiento de GridJs
## el proceso general de archivos 
Después de importar un archivo de hoja de cálculo,

GridJs creará un archivo de caché con el uid especificado en la carpeta **`Config.file_cache_directory`**,

con el formato de [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat"),

GridJs también guardará todas las formas/imágenes en un archivo de archivo comprimido en la carpeta **`Config.file_cache_directory`** para mostrar más tarde las formas/imágenes en la interfaz de usuario del cliente.

y después de cada operación de actualización en la interfaz de usuario del cliente,

por ejemplo, establecer el valor de celda, establecer el estilo de celda, etc.,

El js del cliente de GridJs activará una llamada ajax para realizar una operación UpdateCell.

En esta acción, ocurrirá un guardado de nuevo al archivo de caché durante el método UpdateCell.
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

### cómo obtener el archivo de resultado actualizado
#### 1. un uid especificado para el archivo 
Asegúrese de tener una correspondencia de mapeo especificada entre el archivo y el uid, 

siempre puede obtener el mismo uid para un nombre de archivo específico, no generado aleatoriamente.

Por ejemplo, simplemente usar el nombre del archivo está bien.
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

#### 2. sincronizar con la operación de la interfaz de usuario del cliente
En realidad, para algunas operaciones de la interfaz de usuario del cliente,

por ejemplo:

cambiar la hoja activa a otra,

cambiar la posición de la imagen,

rotar/redimensionar la imagen, etc.

la acción UpdateCell no se activará.

Por lo tanto, si queremos obtener el archivo actualizado tal como lo muestra la interfaz de usuario del cliente,

necesitamos realizar una operación de fusión antes de la acción de guardado para sincronizar esas operaciones de la interfaz de usuario del cliente.
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

#### 3. obtener el archivo desde la caché
por ejemplo: en la acción getfile, puedes obtenerlo directamente desde el directorio de la caché por uid.
```python

        mimetype=guess_mime_type_from_filename(filename)
        file_path = os.path.join(Config.file_cache_directory, uid.replace('/', '.')+"."+filename)
        # check file
        if os.path.isfile(file_path):
             return send_file(file_path, as_attachment=True, download_name=filename, mimetype=mimetype)
```

Para obtener más información detallada, puedes consultar el ejemplo aquí:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>
