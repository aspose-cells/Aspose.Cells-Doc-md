---
title: 使用GridJs存储
type: docs
weight: 250
url: /zh/java/aspose-cells-gridjs/storage/
description: 本文描述了 GridJs 的一般文件处理。
keywords: 文件缓存, 存储, GridJs, GridJs 存储, GridJs uid, 下载, 唯一标识
aliases:
  - /java/aspose-cells-gridjs/storage-introduction/
  - /java/aspose-cells-gridjs/work-with-storage/
---


# 使用GridJs存储
## 一般文件处理 
导入电子表格文件后，

GridJs 将在 **`Config.getFileCacheDirectory()`** 文件夹中创建具有指定 uid 的缓存文件。

使用[Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/java/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat")格式，

GridJs还将所有形状/图片保存到一个zip存档文件中，以便将来在客户端UI中显示形状/图片，存档文件位于**`Config.getPictureCacheDirectory()`**文件夹。

并且在客户端UI中的每次更新操作之后，

例如设置单元格值，设置单元格样式等，

GridJs客户端js将触发控制器操作执行UpdateCell操作。

在此操作中，在UpdateCell方法期间将进行一次保存回缓存文件。
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
缓存文件实际在哪里？ 

A.如果我们实现GridCacheForStream并设置GridJsWorkbook.CacheImp。
例如在下面的代码中，我们可以直接将缓存文件放在"D:\temp"中。
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
B.如果我们不设置GridJsWorkbook.CacheImp，

GridJs将在**`Config.getFileCacheDirectory()`**文件夹中创建并保存文件，默认的缓存目录，可以在其中进行设置。

### 如何获得更新后的结果文件
#### 1. 为文件指定uid 
确保文件和uid之间有指定的映射对应关系， 

您始终可以获得指定文件名的相同uid，而不是随机生成的。

例如，只使用文件名即可。
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

#### 2. 与客户端UI操作同步
实际上，对于某些客户端UI操作，

例如：

切换活动工作表到另一个，

改变图像位置，

旋转/调整图像大小等。

不会触发UpdateCell操作。

因此，如果想要获得更新后的文件与客户端UI显示的内容相同，

我们需要在保存操作之前执行一个合并操作，以同步客户端UI操作。
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
#### 3. 从缓存中获取文件URL
例如：在下载操作中，您可以根据 uid 直接从缓存目录中获取文件。
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

更多详细信息，请参阅此处示例：
<https://github.com/aspose-cells/Aspose.Cells-for-java/tree/master/Examples_GridJs>
