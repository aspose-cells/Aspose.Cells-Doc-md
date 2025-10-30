---
title: GridJs depolama ile çalışmak
type: docs
weight: 250
url: /tr/python-net/aspose-cells-gridjs/storage/
description: Bu makale, Aspose.Cells.GridJs için genel işlemi açıklar.
keywords: dosya önbelleği, depolama, GridJs, GridJs depolama, GridJs uid, indir, uniqueid, önbellek, düzenleyici, düzenleme, elektronik tablo
---


# GridJs Depolama ile Çalışmak
## genel dosya işlemi 
Bir elektronik tablo dosyası içe aktarıldıktan sonra,

GridJs, **`Config.file_cache_directory`** klasöründe belirtilen uid ile bir önbellek dosyası oluşturacaktır.,

[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") formatında kaydedecektir.,

GridJs ayrıca tüm şekilleri / resimleri ileride istemci arayüzünde şekilleri / resimleri görüntülemek için **`Config.file_cache_directory`** klasöründe bir zip arşiv dosyasına kaydedecektir.

ve istemci arayüzünde her güncelleme işleminden sonra,

örneğin hücre değeri ayarla, hücre stili ayarlama, vb.,

GridJs istemci tarafı js, bir GüncellemeHücre işlemi yapmak için ajax çağrısı başlatacak.

Bu eylem sırasında, Bir GüncellemeHücre yöntemi sırasında önbellek dosyasına bir kayıt gerçekleşecektir.
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

### güncellenmiş sonuç dosyasını nasıl alınır
#### 1. dosya için belirtilen bir uid 
Dosya ve uid arasında belirli bir eşleme bağlantısının olması gerektiğinden emin olun, 

bir dosya adı için her zaman aynı uid'yi alabilirsiniz, rastgele oluşturulmaz.

Örneğin, sadece dosya adını kullanmak yeterlidir.
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

#### 2. istemci arayüzü işlemi ile senkronize olun
Aslında bazı istemci arayüzü işlemleri için,

örneğin:

etkin sayfayı başka bir sayfaya değiştir,

resmin pozisyonunu değiştir,

resmi döndür/boyutlandır, vb.

GüncellemeHücre eylemi tetiklenmeyecektir.

Bu nedenle, güncellenmiş dosyayı istemci arayüzünün gösterdiği gibi almak istiyorsak,

bu istemci arayüzü işlemlerini senkronize etmek için kaydetme işleminden önce bir birleştirme işlemi yapmamız gerekmektedir.
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

#### 3. önbellekten dosyayı alın
örneğin: getfile işleminde, uid'ye göre önbellek dizininden doğrudan alabilirsiniz.
```python

        mimetype=guess_mime_type_from_filename(filename)
        file_path = os.path.join(Config.file_cache_directory, uid.replace('/', '.')+"."+filename)
        # check file
        if os.path.isfile(file_path):
             return send_file(file_path, as_attachment=True, download_name=filename, mimetype=mimetype)
```

Daha fazla detaylı bilgi için buradaki örneği kontrol edebilirsiniz:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>
