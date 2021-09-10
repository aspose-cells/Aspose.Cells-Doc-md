---
title: Working with GridJs Server Side
type: docs
weight: 250
url: /net/aspose-cells-gridjs/server/
---


# Working with GridJs Server Side

## 1. Implement GridCacheForStream
For local file storage ,here is an example:
```C#
  public class LocalFileCache  : GridCacheForStream
    {

        /// <summary>
        /// Implement this method to savecache,save the stream to the cache object with the key id.
        /// </summary>
        /// <param name="s">the source stream </param>
        /// <param name="uid">he key id.</param>
        public override void SaveStream(Stream s, String uid)
        {
            String filepath = Path.Combine(Config.FileCacheDirectory + Path.DirectorySeparatorChar + "streamcache", uid.Replace('/', '.'));
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
        {
            String filepath = Path.Combine(Config.FileCacheDirectory + Path.DirectorySeparatorChar + "streamcache", uid.Replace('/', '.'));
            FileStream fs = new FileStream(filepath, FileMode.Open);
            return fs;
        }
        /// <summary>
        ///  implement the url in action controller  to get the file
        /// </summary>
        /// <param name="uid">the key id</param>
        /// <returns></returns>
        public override String GetFileUrl(string uid)
        {
            return "/GridJs2/GetFile?id=" + uid;
        }

    }
```
For server side storage,we also provide an example.
Please check: <https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs></https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>
## 2. Get json from the spreadsheet file.
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
using (FileStream fs = new FileStream(path, FileMode.Open))
{
    wbj.ImportExcelFile(fs,GridJsWorkbook.GetGridLoadFormat(Path.GetExtension(path)));
}
String ret =wbj.ExportToJson();
```
## 3. Get the images/shapes  from the spreadsheet file
```C#
//Gridjs will automatically zip all the images/shapes into a zip stream  and store it in cache using the cache implemention.
//GridJsWorkbook.CacheImp.SaveStream(zipoutStream, fileid);

//get the fileid in the cache,uid is the unique id for the spreadsheet  instance, sheetid is the sheet index,
String fileid=(uniqueid + "." + (sheetid + '_batch.zip'))

//get the zip file stream by the fileid
Stream s=GridJsWorkbook.CacheImp.LoadStream(fileid), mimeType, fileid.Replace('/', '.')
```
## 4. Update spreadsheet file in cache
```C#
GridJsWorkbook gwb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
String ret = gwb.UpdateCell(p, uid);
```
## 5.  Save spreadsheet file in cache
```C#
GridJsWorkbook wb = new GridJsWorkbook();
//p is the update json,uid is the unique id for the spreadsheet
wb.MergeExcelFileFromJson(uid, p);
wb.SaveToCacheWithFileName(uid, filename,password);
```

For detail info ,you can check the example here:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs></https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs>