---
title: 与GridJs服务器端配合工作
type: docs
weight: 250
url: /zh/net/aspose-cells-gridjs/how-to-use-api/
description: 该文章描述了如何在 GridJs 中使用 API。
keywords: GridJs, 服务器, GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# 与GridJs服务器端配合工作
## 1. 在startup.cs的ConfigureServices中添加服务 
```C#
   services.AddScoped<IGridJsService, GridJsService>();
```
## 2. 设置缓存文件存储路径

你可以选择以下任意方法：

 选项1：在Startup.cs的ConfigureServices中设置GridJsOptions
```C#
   services.Configure<GridJsOptions>(options =>
	{
		options.FileCacheDirectory = TestConfig.TempDir;
	});
```

 选项2：直接设置静态属性
```C#
   Config.FileCacheDirectory = TestConfig.TempDir;
```

 选项3：通过实现GridCacheForStream定义你自己的缓存存储规则

对于本地文件存储，这里有一个示例：

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}


对于服务器端存储，我们还提供了示例。请查看： 

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>


关于存储的更多详细信息，请参考[指南](/cells/zh/net/aspose-cells-gridjs/storage/)


## 3. 实现控制器动作

### 1. 创建一个扩展自GridJsControllerBase的控制器
```C#
public class GridJs2Controller : GridJsControllerBase
```
### 2. 在动作中获取JSON

在你的操作中获取JSON数据有两种方法：

选项1：使用GridJsWorkbook
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
Workbook wb = new Workbook(fullFilePath); 
wbj.ImportExcelFile(wb);
String ret =wbj.ExportToJson(fileName);
```
选项2：在GridJsControllerBase中使用IGridJsService
```C#
 String uid= GridJsWorkbook.GetUidForFile(fileName)
 StringBuilder ret= _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
```

有关详细信息，请查看此处的示例：
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
