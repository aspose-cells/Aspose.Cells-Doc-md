---
title: Работа с GridJs на стороне сервера
type: docs
weight: 250
url: /ru/python-net/aspose-cells-gridjs/server/
keywords: использование, эксель, GridJs, электронная таблица, файл, скачать, редактировать, редактор, просмотр, просмотрщик,
description: Эта статья описывает, как использовать библиотеку Aspose.Cells.GridJs.
---


# Работа с сервером GridJs
## 1. установите правильный путь к папке в Config
используйте Config.set_file_cache_directory для установки пути кэша.
```python
 Config.set_file_cache_directory('c:/storage/cache/')
```

для деталей хранения, пожалуйста, проверьте этот [гид](/python-net/aspose-cells-gridjs/storage/)


## 2. Получить json из файла электронной таблицы.
```python
path='c:/files/example.xlsx'
gwb = new GridJsWorkbook();
gwb.ImportExcelFile(path);

ret =gwb.export_to_json();
```
## 3. Получить изображения/формы из файла электронной таблицы
```python
# Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache  


# get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
fileid=(uniqueid + '.' + (sheetid + '_batch.zip'))

# get the zip file  by the fileid
os.path.join(Config.file_cache_directory, fileid)
```
## 4. Обновить файл электронной таблицы в кэше
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
ret = gwb.UpdateCell(p, uid);
```
## 5.  Сохранить файл электронной таблицы в кэше
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
gwb.merge_excel_file_from_json(uid, p);
gwb.save_to_cache_with_file_name(uid, filename,password);
```

Для получения дополнительной информации, вы можете проверить пример здесь:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs_Python_Net>
