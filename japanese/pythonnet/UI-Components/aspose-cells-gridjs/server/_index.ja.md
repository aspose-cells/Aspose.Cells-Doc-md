---
title: GridJsサーバーサイドで作業する
type: docs
weight: 250
url: /ja/python-net/aspose-cells-gridjs/server/
keywords: ユースケース、Excel、GridJs、スプレッドシート、ファイル、ダウンロード、編集、エディター、表示、ビューアー
description: この記事では、Aspose.Cells.GridJsライブラリの使用方法について説明しています。
---


# GridJsサーバーサイドで作業する
## 1. Configで適切なフォルダーパスを設定します
Config.set_file_cache_directoryを使用してキャッシュパスを設定します。
```python
 Config.set_file_cache_directory('c:/storage/cache/')
```

ストレージの詳細については、この[ガイド](/python-net/aspose-cells-gridjs/storage/)をご覧ください。


## 2. スプレッドシートファイルからJSONを取得します。
```python
path='c:/files/example.xlsx'
gwb = new GridJsWorkbook();
gwb.ImportExcelFile(path);

ret =gwb.export_to_json();
```
## 3. スプレッドシートファイルから画像/図形を取得します
```python
# Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache  


# get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
fileid=(uniqueid + '.' + (sheetid + '_batch.zip'))

# get the zip file  by the fileid
os.path.join(Config.file_cache_directory, fileid)
```
## 4. キャッシュ内のスプレッドシートファイルを更新します
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
ret = gwb.UpdateCell(p, uid);
```
## 5. キャッシュ内のスプレッドシートファイルを保存します
```python
gwb = new GridJsWorkbook();
# p is the update json,uid is the unique id for the spreadsheet
gwb.merge_excel_file_from_json(uid, p);
gwb.save_to_cache_with_file_name(uid, filename,password);
```

詳細については、こちらの例をご覧ください：
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Python-via-.NET/tree/main/Examples.GridJs>
