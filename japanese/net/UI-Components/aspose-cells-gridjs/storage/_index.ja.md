---
title: GridJsストレージで作業する
type: docs
weight: 250
url: /ja/net/aspose-cells-gridjs/storage/
description: この記事では、GridJsの一般的なファイル処理について説明します。
keywords: ファイルキャッシュ、ストレージ、GridJs、GridJsストレージ、GridJs uid、ダウンロード、uniqueid
aliases:
  - /net/aspose-cells-gridjs/storage-introduction/
  - /net/aspose-cells-gridjs/work-with-storage/
---


# GridJsストレージで作業する
## 一般的なファイル処理 

スプレッドシートファイルをインポートした後、

GridJsは、GridCacheForStreamの実装に従って指定されたuidのキャッシュファイルを作成します。

[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat")の形式で保存します。

GridJsはまた、すべてのシェイプ/画像をキャッシュフォルダ内のzipアーカイブファイルに保存し、後でクライアントUIにシェイプ/画像を表示します。

クライアントUIでの更新操作後、

たとえば、セル値を設定する、セルスタイルを設定するなど、

GridJsのクライアント側JSはコントローラーアクションをトリガーして更新操作を行います。

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

A. 自分でGridCacheForStreamを実装する場合。
たとえば、以下のコードでは、**"D:\temp"**にキャッシュファイルを配置および取得できます。
```C#
Config.FileCacheDirectory=@"D:\temp";
GridJsWorkbook.CacheImp=new LocalFileCache();
public class LocalFileCache  : GridCacheForStream
    {

        public LocalFileCache()
        {
            string streampath = Config.FileCacheDirectory;
            if (!Directory.Exists(streampath))
            {

                Directory.CreateDirectory(streampath);

            }
        }
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

GridJsは既にデフォルトの実装を備えています。

GridJsはパス内にキャッシュファイルを作成し保存します：**`Config.FileCacheDirectory/streamcache`** 。

### 更新された結果ファイルの取得方法
#### 1. 指定したUIDでファイルを作成する 
ファイルとUIDの間の指定されたマッピングの対応を確認してください。 

例えば 

```C#

...     
        //generte a uid for the file
        String uid = GridJsWorkbook.GetUidForFile(filename)
...
        //get JSON result which will be used in client ui for the file by filename and uid
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


#### 2. UIDを使用してキャッシュからファイルを取得する
例：ダウンロードアクションでは、UIDとファイル名を使ってキャッシュディレクトリから取得できます。
```C#
	 Stream fileStream = GridJsWorkbook.CacheImp.LoadStream(uid + "/" + filename);
```

詳細情報については、こちらの例をご確認ください：
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
