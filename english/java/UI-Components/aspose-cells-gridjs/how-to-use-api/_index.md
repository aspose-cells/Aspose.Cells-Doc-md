---
title: Working with GridJs Server Side
type: docs
weight: 250
url: /java/aspose-cells-gridjs/how-to-use-api/
description: This article describes how to use APIs in GridJs.
keywords: GridJs,server,GridCacheForStream
aliases:
  - /java/aspose-cells-gridjs/server/
  - /java/aspose-cells-gridjs/server-api/
  - /java/aspose-cells-gridjs/api-introduction/
  - /java/aspose-cells-gridjs/how-to-use-apis/
  - /java/aspose-cells-gridjs/work-with-serverside-api/
  - /java/aspose-cells-gridjs/work-with-serverside-apis/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

# Working with GridJs Server Side
## 0. Set the right folder path in Config
**`Config.setFileCacheDirectory`** for the workbook cache file (required).  
**`Config.setPictureCacheDirectory`** for the image files cache in the workbook (optional, the default value is _piccache in the file cache directory).

For storage details, please check this [guide](/java/aspose-cells-gridjs/storage/).

## 1. Implement GridCacheForStream
For local file storage, here is an example:

```java
public class LocalFileCache extends GridCacheForStream {

    @Override
    public void saveStream(InputStream s, String uid) {
        // make sure the directory exists
        String filepath = Paths.get(Config.getFileCacheDirectory(), "streamcache", uid.replace('/', '.')).toString();
        try (FileOutputStream fos = new FileOutputStream(filepath)) {
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
```

## 2. Write JSON from the spreadsheet file to the response stream.
```java
GridJsWorkbook wbj = new GridJsWorkbook();
try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
    wbj.importExcelFile(filePath.toString());
    wbj.jsonToStream(gzipOutputStream, filename);
} catch (IOException e) {
    e.printStackTrace();
} catch (Exception e) {
    e.printStackTrace();
}
```

## 3. Get the images/shapes from the spreadsheet file
```java
// GridJs will automatically zip all the images/shapes into a zip stream and store it in cache using the cache implementation.
InputStream inputStream = GridJsWorkbook.CacheImp.loadStream(fileid);
```

## 4. Update spreadsheet file in cache
```java
GridJsWorkbook gwb = new GridJsWorkbook();
// p is the update JSON, uid is the unique ID for the spreadsheet
String ret = gwb.updateCell(p, uid);
```

## 5. Save spreadsheet file in cache
```java
GridJsWorkbook wb = new GridJsWorkbook();
// p is the update JSON, uid is the unique ID for the spreadsheet
wb.mergeExcelFileFromJson(uid, p);
wb.saveToCacheWithFileName(uid, filename, password);
```

For detailed info, you can check the example here:  
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples_GridJs>
