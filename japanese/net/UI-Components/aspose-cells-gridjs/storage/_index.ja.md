---
title: GridJsストレージで作業する
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/storage/
description: この記事では、GridJsの一般的なファイル処理について説明します。
keywords: ファイルキャッシュ、ストレージ、GridJs、GridJsストレージ、GridJs uid、ダウンロード、uniqueid
---


# GridJsストレージで作業する
## 一般的なファイル処理 
スプレッドシートファイルをインポートした後、

GridJsは**`Config.FileCacheDirectory`**フォルダに指定されたuidでキャッシュファイルを作成します。

[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat")の形式で保存します。

また、GridJsはすべての図形/画像を**`Config.PictureCacheDirectory`**フォルダにzipアーカイブファイルとして保存し、後でクライアントUIで図形/画像を表示できるようにします。

クライアントUIでの更新操作後、

たとえば、セル値を設定する、セルスタイルを設定するなど、

GridJsのクライアント側JSはコントローラーアクションをトリガーしてUpdateCell操作を行います。

このアクションでは、UpdateCellメソッド中にキャッシュファイルへの保存が発生します。
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
### キャッシュファイルの実際の場所 

A. GridCacheForStreamを実装し、GridJsWorkbook.CacheImpを設定した場合、
たとえば、以下のコードでは、**"D:\temp"**にキャッシュファイルを配置および取得できます。
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
B. GridJsWorkbook.CacheImpを設定しない場合、

GridJsは**`Config.FileCacheDirectory`**内で保存ファイルを作成します。これは設定できるデフォルトのキャッシュディレクトリです。

### 更新された結果ファイルの取得方法
#### 1. ファイルの指定されたUID 
ファイルとUIDの間の指定されたマッピングの対応を確認してください。 

指定されたファイル名の場合、常に同じUIDを取得できます。ランダムな生成ではありません。

たとえば、ファイル名だけを使用しても問題ありません。
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

#### 2. クライアントUI操作と同期
実際には、一部のクライアントUI操作に対して、

たとえば：

別のシートにアクティブシートを切り替える、

画像の位置を変更する、

画像の回転/サイズ変更など。

UpdateCellアクションはトリガーされません。

したがって、クライアントUIが表示するように更新されたファイルを取得するには、

これらのクライアントUI操作を同期するために保存アクションの前にマージ操作を実行する必要があります。
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
#### 3. キャッシュからファイルを取得
たとえば: ダウンロードアクションでは、uid によってキャッシュディレクトリから取得することができます。
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

詳細情報については、こちらの例をご確認ください：
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
