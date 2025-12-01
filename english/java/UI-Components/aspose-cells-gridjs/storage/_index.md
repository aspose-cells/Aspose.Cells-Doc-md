---
title: Working with GridJs storage
type: docs
weight: 250
url: /java/aspose-cells-gridjs/storage/
description: This article describes the general file processing for GridJs.
keywords: file cache,storage,GridJs,GridJs storage,GridJs uid,download,uniqueid
aliases:
  - /java/aspose-cells-gridjs/storage-introduction/
  - /java/aspose-cells-gridjs/work-with-storage/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


# Working With GridJs Storage
##  the general file process 
After import a spread sheet file ,

GridJs will create a cache file with the specified uid in the **`Config.getFileCacheDirectory()`** folder  ,

with the format of [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/java/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs will also saves all shapes/images to a zip archive file in the **`Config.getPictureCacheDirectory()`** folder for later display shapes/images in the client UI.

and after every update operation in the client UI,

for example set cell value,set cell style,etc. ,

GridJs  client side js will trigger  controller action to do a UpdateCell operation.

In this action a save back to the cache file  will occur during the  UpdateCell method.
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
###  where is the cache file actually 

A. If we implement GridCacheForStream and set GridJsWorkbook.CacheImp.
for example in the below code we can just put and get the cache file from  **"D:\temp"**
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
B.If we do not set GridJsWorkbook.CacheImp,

GridJs will create and do save file within the folder of **`Config.getFileCacheDirectory()`** , which is the default cache directory which we can set.

###  how to get the updated result file
#### 1. a specified uid for file 
Make sure a specified maping correspondence  between the file and the uid, 

you can always get the same uid for a specifed file name,not from random generation.

For example just use the filename is ok.
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

#### 2. sync with client UI operation
Actually for some client UI operation,

for example:

switch the acitve sheet to another,

change the image postion,

rotate/resize image,etc.

the UpdateCell action will not triggered.

Thus if we want to get the updated file just same as the client UI shows,

we need to do a merge operation before save action to sync those client UI operation.
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
#### 3. get the file url from cache
for example :in the download action,you can just get it from the cache directory by uid.
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

For more detail info ,you can check the example here:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples_GridJs>
