---
title: Working with GridJs storage
type: docs
weight: 250
url: /net/aspose-cells-gridjs/storage/
description: This article describes the general file processing for GridJs.
keywords: file cache,storage,GridJs,GridJs storage,GridJs uid,download,uniqueid
aliases:
  - /net/aspose-cells-gridjs/storage-introduction/
  - /net/aspose-cells-gridjs/work-with-storage/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


# Working With GridJs Storage
##  the general file process 

After import a spread sheet file ,

GridJs will create a cache file with the specified uid according GridCacheForStream implementation,

with the format of [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat") ,

GridJs will also saves all shapes/images to a zip archive file in the  cache folder for later display shapes/images in the client UI.

and after every update operation in the client UI,

for example set cell value,set cell style,etc. ,

GridJs  client side js will trigger  controller action to do a update operation.

In this action a save back to the cache file  will occur during the  UpdateCell method.
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
###  where is the cache file actually 

A. If you implement GridCacheForStream youself.
for example in the below code we can just put and get the cache file from  **"D:\temp"**
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
B.If you do not set GridJsWorkbook.CacheImp, 

GridJs already implement a default one.

GridJs will create and do save cache file within the path: **`Config.FileCacheDirectory/streamcache`** .

###  how to get the updated result file
#### 1. create a specified uid for the file 
Make sure a specified maping correspondence  between the file and the uid, 

For example 

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

        
#### 2. get the file from cache by the uid
for example :in the download action,you can just get it from the cache directory by uid and filename.
```C#
	 Stream fileStream = GridJsWorkbook.CacheImp.LoadStream(uid + "/" + filename);
```

For more detail info ,you can check the example here:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
