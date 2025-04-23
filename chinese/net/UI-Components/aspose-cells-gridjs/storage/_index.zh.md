---
title: 使用GridJs存储
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/storage/
description: 本文描述了 GridJs 的一般文件处理。
keywords: 文件缓存, 存储, GridJs, GridJs 存储, GridJs uid, 下载, 唯一标识
aliases:
  - /net/aspose-cells-gridjs/storage-introduction/
  - /net/aspose-cells-gridjs/work-with-storage/
---


# 使用GridJs存储
## 一般文件处理 

导入电子表格文件后，

GridJs 将根据 GridCacheForStream 实现创建指定 uid 的缓存文件，

格式为 [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ，

GridJs 还会将所有形状/图片保存到缓存文件夹中的zip归档文件中，以便之后在客户端界面显示形状/图片。

并且在客户端UI中的每次更新操作之后，

例如设置单元格值，设置单元格样式等，

GridJs 客户端js将触发控制器操作以进行更新操作。

在此操作中，在UpdateCell方法期间将进行一次保存回缓存文件。
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
缓存文件实际在哪里？ 

一. 如果你自己实现 GridCacheForStream。
例如在下面的代码中，我们可以直接将缓存文件放在"D:\temp"中。
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
二. 如果你没有设置 GridJsWorkbook.CacheImp， 

GridJs  已经实现了一个默认的。

GridJs 将在路径 **`Config.FileCacheDirectory/streamcache`** 内创建并保存缓存文件。

### 如何获得更新后的结果文件
#### 1. 为文件创建一个指定的uid 
确保文件和uid之间有指定的映射对应关系， 

例如 

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


#### 2. 通过uid从缓存中获取文件
例如：在下载操作中，您可以直接通过uid和文件名从缓存目录获取。
```C#
	 Stream fileStream = GridJsWorkbook.CacheImp.LoadStream(uid + "/" + filename);
```

更多详细信息，请参阅此处示例：
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
