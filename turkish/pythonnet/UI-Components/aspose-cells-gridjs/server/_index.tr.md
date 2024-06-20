---
title: GridJs Sunucu Tarafı ile Çalışmak
type: docs
weight: 250
url: /tr/python-net/aspose-cells-gridjs/server/
keywords: kullanım durumu,excel,GridJs,çalışma tablosu,dosya,indir,düzenle,editör,görüntüleyici
description: Bu makale Aspose.Cells.GridJs kütüphanesini nasıl kullanacağınızı açıklar.
---


# GridJs Sunucu Tarafı ile Çalışmak
## 1. Doğru klasör yolunu Config'de ayarlayın
Depo yolunu ayarlamak için Config.set_file_cache_directory'yi kullanın.
```python
 Config.set_file_cache_directory('c:/storage/cache/')
```

depo ayrıntısı için lütfen bu [kılavuzu](/python-net/aspose-cells-gridjs/storage/) kontrol edin


## 2. Çalışma tablosundan json alın.
```python
path='c:/files/example.xlsx'
gwb = new GridJsWorkbook();
gwb.ImportExcelFile(path);

ret =gwb.export_to_json();
```
## 3. Çalışma tablosundan resimleri/şekilleri alın
```python
# Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache  


# get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
fileid=(uniqueid + '.' + (sheetid + '_batch.zip'))

# get the zip file  by the fileid
os.path.join(Config.file_cache_directory, fileid)
```
## 4. Önbellekte çalışma tablosunu güncelle
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
ret = gwb.UpdateCell(p, uid);
```
## 5.  Önbellekte çalışma tablosunu kaydedin
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
gwb.merge_excel_file_from_json(uid, p);
gwb.save_to_cache_with_file_name(uid, filename,password);
```

Detaylı bilgiler için buradaki örneği kontrol edebilirsiniz:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net>
