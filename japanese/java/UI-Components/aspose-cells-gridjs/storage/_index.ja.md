---
title: GridJsストレージで作業する
type: docs
weight: 250
url: /ja/java/aspose-cells-gridjs/storage/
description: この記事では、GridJsの一般的なファイル処理について説明します。
keywords: ファイルキャッシュ、ストレージ、GridJs、GridJsストレージ、GridJs uid、ダウンロード、uniqueid
aliases:
  - /java/aspose-cells-gridjs/storage-introduction/
  - /java/aspose-cells-gridjs/work-with-storage/
---


# GridJsストレージで作業する
## 一般的なファイル処理 
スプレッドシートファイルをインポートした後、

GridJsは指定されたuidのキャッシュファイルを **`Config.getFileCacheDirectory()`** フォルダに作成します。

[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/java/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat")形式で、

また、Shapeや画像をすべてzipアーカイブファイルとして **`Config.getPictureCacheDirectory()`** フォルダに保存し、後でクライアントUIでShapeや画像を表示します。

クライアントUIでの更新操作後、

たとえば、セル値を設定する、セルスタイルを設定するなど、

GridJsのクライアント側JSはコントローラーアクションをトリガーしてUpdateCell操作を行います。

このアクションでは、UpdateCellメソッド中にキャッシュファイルへの保存が発生します。
```JAVA  
    @PostMapping("/UpdateCell")
    public ResponseEntity<String> updateCell(HttpServletRequest request) {
        String p = request.getParameter("p");
        String uid = request.getParameter("uid");
        GridJsWorkbook gwb = new GridJsWorkbook();
        String ret;
		try {
			ret = gwb.updateCell(p, uid);
			return new ResponseEntity<>(ret, HttpStatus.OK);
		} catch (Exception e) {
			// TODO Auto-generated catch block
			return new ResponseEntity<>(gwb.errorJson(e.getMessage()), HttpStatus.OK);
		}

    }
```
### キャッシュファイルの実際の場所 

A. GridCacheForStreamを実装し、GridJsWorkbook.CacheImpを設定した場合、
たとえば、以下のコードでは、**"D:\temp"**にキャッシュファイルを配置および取得できます。
```JAVA
Config.setFileCacheDirectory("D:\temp");
GridJsWorkbook.CacheImp=new LocalFileCache();
public class LocalFileCache extends GridCacheForStream {

	@Override
	public void saveStream(InputStream s, String uid) {
		// make sure the directory is exist
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		try (FileOutputStream fos = new FileOutputStream(filepath.toString())) {
			s.reset(); // Equivalent to s.Position = 0 in C#
			byte[] buffer = new byte[1024];
			int length;
			while ((length = s.read(buffer)) > 0) {
				fos.write(buffer, 0, length);
			}
			fos.flush();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

	@Override
	public InputStream loadStream(String uid) {
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		try {
			return new FileInputStream(filepath);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			return null;
		}
	}

	@Override
	public boolean isExisted(String uid) {
		String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
		return Files.exists(Paths.get(filepath));
	}

	@Override
	public String getFileUrl(String uid) {
		return "/GridJs2/GetFileUseCacheStream?id=" + uid;
	}

}
		...
```
B. GridJsWorkbook.CacheImpを設定しない場合、

GridJsは **`Config.getFileCacheDirectory()`** フォルダ内にファイルの作成と保存を行います。これは既定のキャッシュディレクトリで、設定可能です。

### 更新された結果ファイルの取得方法
#### 1. ファイルの指定されたUID 
ファイルとUIDの間の指定されたマッピングの対応を確認してください。 

指定されたファイル名の場合、常に同じUIDを取得できます。ランダムな生成ではありません。

たとえば、ファイル名だけを使用しても問題ありません。
```JAVA
//in controller  

     @GetMapping("/DetailStreamJsonWithUid")
    public void detailStreamJsonWithUid(@RequestParam String filename, @RequestParam String uid,HttpServletResponse response) {


        	Path filePath = Paths.get(listDir, filename);
            GridJsWorkbook wbj = new GridJsWorkbook();

            response.setContentType("application/json");
            response.setHeader("Content-Encoding", "gzip");
            try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
                wbj.importExcelFile(filePath.toString());
                wbj.jsonToStream(gzipOutputStream, filename);
            } catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
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
```JAVA
//in controller action 
  GridJsWorkbook wb = new GridJsWorkbook();
  wb.mergeExcelFileFromJson(uid, p);
  //after merge do save to chache or to a stream or whaterver you want to save to ,here we just save to cache
  wb.saveToCacheWithFileName(uid,filename,password);
```         
#### 3. キャッシュからファイルURLを取得
たとえば: ダウンロードアクションでは、uid によってキャッシュディレクトリから取得することができます。
```JAVA
//in controller  

      String fileUrl = null;
			if (GridJsWorkbook.CacheImp != null) {
				fileUrl = GridJsWorkbook.CacheImp.getFileUrl(uid + "/" + filename);
			} else {
				fileUrl = "/GridJs2/GetFile?id=" + uid + "&filename=" + filename;
			}
			return ResponseEntity.ok("\""+fileUrl+"\"");
```

詳細情報については、こちらの例をご確認ください：
<https://github.com/aspose-cells/Aspose.Cells-for-java/tree/master/Examples_GridJs>
