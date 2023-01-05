---
title: GridJs ストレージの操作
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/storage/
description: この記事では、Aspose.Cells.GridJs の一般的な処理について説明します。
keywords: file cache,storage,GridJs,GridJs storage,GridJs uid,download,uniqueid
---
# GridJs ストレージの操作
## 一般的なファイル プロセス
スプレッドシートファイルをメモリにインポートしてUIを表示した後、

GridJs は、指定された uid でキャッシュ ファイルを作成します。

の形式で[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

そして、UIでのすべての更新操作の後、

たとえば、セル値の設定、セル スタイルの設定などです。 、

GridJs クライアント側 js は、コントローラ アクションをトリガーして UpdateCell 操作を実行します。

このアクションでは、メモリからキャッシュ ファイルへのセーブ バックが UpdateCell メソッド中に発生します。
```C#   
        // post: /GridJs/UpdateCell
        [HttpPost] 
        public ActionResult UpdateCell( )
        {
            string p = HttpContext.Request.Form["p"];
            string uid = HttpContext.Request.Form["uid"];
            GridJsWorkbook gwb = new GridJsWorkbook();
            String ret = gwb.UpdateCell(p, uid);
            return Content(ret, "text/plain", System.Text.Encoding.UTF8);
        }
```
### キャッシュディレクトリはどこですか
A. GridCacheForStream を実装し、GridJsWorkbook.CacheImp を設定した場合。
たとえば、以下のコードでは、キャッシュ ファイルを入れて取得することができます。**"D:\temp"**
```C#
Config.FileCacheDirectory=@"D:\temp";
GridJsWorkbook.CacheImp=new LocalFileCache();
public class LocalFileCache  : GridCacheForStream
    {
         
        /// <summary>
        /// Implement this method to savecache,save the stream to the cache object with the key id.
        /// </summary>
        /// <param name="s">the source stream </param>
        /// <param name="uid">the key id.</param>
        public override void SaveStream(Stream s, String uid)
        {//make sure the directory exist
            String filepath = Path.Combine(Config.FileCacheDirectory, uid);
            using (FileStream fs = new FileStream(filepath, FileMode.Create)) 
            {
                s.Position = 0;
                s.CopyTo(fs);
            }

        }

        /// <summary>
        /// Implement this method to loadcache with the key uid,return the stream from the cache object.
        /// </summary>
        /// <param name="uid">the key id</param>
        /// <returns>the stream from  the cache</returns>
        public override Stream LoadStream(String uid)
        {//make sure the directory is exist
            String filepath = Path.Combine(Config.FileCacheDirectory, uid);;
            FileStream fs = new FileStream(filepath, FileMode.Open);
            return fs;
        }
		...
```
B.GridJsWorkbook.CacheImpを設定しない場合、

 GridJs は、ファイルを作成して保存します**Config.FileCacheDirectory**これは、設定可能なデフォルトのキャッシュ ディレクトリです。

### 更新された結果ファイルを取得する方法
#### 1. ファイルの指定された uid
ファイルと uid の間で指定されたマップ対応を確認し、

ランダムな生成からではなく、指定したファイル名に対して常に同じ uid を取得できます。

たとえば、ファイル名を使用するだけで問題ありません。
```C#
//in controller  
...
        public ActionResult Uidtml(String filename)
        {
 
            return Redirect("~/xspread/uidload.html?file=" + filename + "&uid=" +  Path.GetFileNameWithoutExtension(filename));
        }
 ...
        public ActionResult DetailFileJsonWithUid(string filename,string uid)
        {
            String file = Path.Combine(TestConfig.ListDir, filename);
            GridJsWorkbook wbj = new GridJsWorkbook();
            //check if already in cache
           StringBuilder sb= wbj.GetJsonByUid(uid, filename);
            if(sb==null)
            {
                Workbook wb = new Workbook(file);
                wbj.ImportExcelFile(uid, wb);
                sb = wbj.ExportToJsonStringBuilder(filename);
            }

            return Content(sb.ToString(), "text/plain", System.Text.Encoding.UTF8);
        }
```

#### 2.UI操作で同期
実際にはいくつかのUI操作のために、

例えば：

アクティブシートを別のものに切り替え、

画像の位置を変更し、

画像の回転/サイズ変更など

UpdateCell アクションはトリガーされません。

したがって、UI が示すのと同じように更新されたファイルを取得したい場合は、

これらのUI操作を同期するには、保存アクションの前にマージ操作を行う必要があります。
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
```C#
//in controller action 
  GridJsWorkbook wb = new GridJsWorkbook();
  wb.MergeExcelFileFromJson(uid, p);
  //after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
  wb.SaveToXlsx(Path.Combine(Config.FileCacheDirectory, uid));
```         
#### 3. キャッシュからファイルを取得する
たとえば、ダウンロード アクションでは、キャッシュ ディレクトリから uid で取得できます。
```C#
//in controller  

        public async Task<IActionResult> DownloadfromBytes(string uid,string ext)
        {
            byte[] byteArr = await System.IO.File.ReadAllBytesAsync(Path.Combine(Config.FileCacheDirectory, uid) );
            string mimeType = "application/octet-stream";
            return new FileContentResult(byteArr, mimeType)
            {
                FileDownloadName = uid+ ext
            };
        }
```

詳細については、次の例を確認してください。
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
