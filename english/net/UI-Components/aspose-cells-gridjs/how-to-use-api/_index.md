---
title: Working with GridJs Server Side
type: docs
weight: 250
url: /net/aspose-cells-gridjs/how-to-use-api/
description: This article describes how to use APIs in GridJs.
keywords: GridJs, server, GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


# Working with GridJs Server Side
## 1. Add service in ConfigureServices in Startup.cs 
```c#
services.AddScoped<IGridJsService, GridJsService>();
```

## 2. Set the Path to Store Cache Files

You can choose any of the following ways:

**Option 1:** Set GridJsOptions in ConfigureServices in Startup.cs
```c#
services.Configure<GridJsOptions>(options =>
{
    options.FileCacheDirectory = TestConfig.TempDir;
});
```

**Option 2:** Directly set the static property
```c#
Config.FileCacheDirectory = TestConfig.TempDir;
```

**Option 3:** Define your own cache storage rule by implementing `GridCacheForStream`

For local file storage, here is an example:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}

For server‑side storage, we also provide an example. Please check:

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>

For more details about storage, please refer to this [guide](/cells/net/aspose-cells-gridjs/storage/)


## 3. Implement Controller Actions

### 1. Create a controller that extends `GridJsControllerBase`
```c#
public class GridJs2Controller : GridJsControllerBase
```

### 2. Get JSON in action

There are two ways to get JSON data in your action:

**Option 1:** Using `GridJsWorkbook`
```c#
GridJsWorkbook wbj = new GridJsWorkbook();
Workbook wb = new Workbook(fullFilePath); 
wbj.ImportExcelFile(wb);
string ret = wbj.ExportToJson(fileName);
```

**Option 2:** Using `IGridJsService` in `GridJsControllerBase`
```c#
string uid = GridJsWorkbook.GetUidForFile(fileName);
StringBuilder ret = _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
```

For detailed info, you can check the example here:

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
