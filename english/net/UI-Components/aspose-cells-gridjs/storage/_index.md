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
## The General File Process

After importing a spreadsheet file, GridJs will create a cache file with the specified UID according to the `GridCacheForStream` implementation, with the format of [Aspose.Cells.SaveFormat.Xlsx](https://reference.aspose.com/cells/net/aspose.cells/saveformat/ "Aspose.Cells.SaveFormat").

GridJs will also save all shapes/images to a zip archive file in the cache folder for later display in the client UI.

After every update operation in the client UI, for example, set cell value, set cell style, etc., GridJs client‑side JavaScript will trigger a controller action to perform an update operation.

In this action, a save back to the cache file occurs during the `UpdateCell` method.

```csharp
// post: /GridJs/UpdateCell
[HttpPost] 
public ActionResult UpdateCell()
{
    string p = HttpContext.Request.Form["p"];
    string uid = HttpContext.Request.Form["uid"];
    GridJsWorkbook gwb = new GridJsWorkbook();
    string ret = gwb.UpdateCell(p, uid);
    return Content(ret, "text/plain", System.Text.Encoding.UTF8);
}
```

### Where Is the Cache File Actually

**A.** If you implement `GridCacheForStream` yourself, for example, in the code below you can store and retrieve the cache file from **`"D:\temp"`**:

```csharp
Config.FileCacheDirectory = @"D:\temp";
GridJsWorkbook.CacheImp = new LocalFileCache();

public class LocalFileCache : GridCacheForStream
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
    /// Implement this method to save cache, save the stream to the cache object with the key ID.
    /// </summary>
    /// <param name="s">The source stream.</param>
    /// <param name="uid">The key ID.</param>
    public override void SaveStream(Stream s, string uid)
    {
        // Make sure the directory exists
        string filepath = Path.Combine(Config.FileCacheDirectory, uid);
        using (FileStream fs = new FileStream(filepath, FileMode.Create))
        {
            s.Position = 0;
            s.CopyTo(fs);
        }
    }

    /// <summary>
    /// Implement this method to load cache with the key UID, return the stream from the cache object.
    /// </summary>
    /// <param name="uid">The key ID.</param>
    /// <returns>The stream from the cache.</returns>
    public override Stream LoadStream(string uid)
    {
        // Make sure the directory exists
        string filepath = Path.Combine(Config.FileCacheDirectory, uid);
        FileStream fs = new FileStream(filepath, FileMode.Open);
        return fs;
    }
    // ...
}
```

**B.** If you do not set `GridJsWorkbook.CacheImp`, GridJs already implements a default one. GridJs will create and save the cache file within the path **`Config.FileCacheDirectory/streamcache`**.

### How to Get the Updated Result File

#### 1. Create a Specified UID for the File  
Make sure there is a specific mapping correspondence between the file and the UID.

For example:

```csharp
// ...     
// Generate a UID for the file
string uid = GridJsWorkbook.GetUidForFile(filename);

// Get JSON result which will be used in the client UI for the file by filename and UID
public ActionResult DetailFileJsonWithUid(string filename, string uid)
{
    string file = Path.Combine(TestConfig.ListDir, filename);
    GridJsWorkbook wbj = new GridJsWorkbook();

    // Check if already in cache
    StringBuilder sb = wbj.GetJsonByUid(uid, filename);
    if (sb == null)
    {
        Workbook wb = new Workbook(file);
        wbj.ImportExcelFile(uid, wb);
        sb = wbj.ExportToJsonStringBuilder(filename);
    }
    return Content(sb.ToString(), "text/plain", System.Text.Encoding.UTF8);
}
```

#### 2. Get the File from Cache by the UID  
For example, in the download action you can retrieve it from the cache directory by UID and filename:

```csharp
Stream fileStream = GridJsWorkbook.CacheImp.LoadStream(uid + "/" + filename);
```

For more detailed information, you can check the example here:  
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
