##Working with GridJs Server Side
This article describes how to use APIs in GridJs .
# Working with GridJs Server Side
## 1. add service in ConfigureServices in startup.cs
```C#
services.AddScoped<IGridJsService, GridJsService>();
```
## 2. Set the Path to Store Cache Files
You can choose any of the following ways:
Option 1: Set GridJsOptions in ConfigureServices in Startup.cs
```C#
services.Configure<GridJsOptions>(options =>
{
options.FileCacheDirectory = TestConfig.TempDir;
});
```
Option 2: Directly Set the Static Property
```C#
Config.FileCacheDirectory = TestConfig.TempDir;
```
Option 3: Define Your Own Cache Storage Rule by Implementing GridCacheForStream
For local file storage ,here is an example:
For server-side storage,we also provide an example.Please check:
For more details about storage,  please refer to this [guide](https://docs.aspose.com/cells/net/aspose-cells-gridjs/storage/)
## 3.  Implement Controller Actions
### 1. Create a Controller that Extends GridJsControllerBase
```C#
public class GridJs2Controller : GridJsControllerBase
```
### 2 Get JSON in action
There are two ways to get JSON data in your action:
Option 1: Using GridJsWorkbook
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
Workbook wb = new Workbook(fullFilePath);
wbj.ImportExcelFile(wb);
String ret =wbj.ExportToJson(fileName);
```
Option 2: Using IGridJsService in GridJsControllerBase
```C#
String uid= GridJsWorkbook.GetUidForFile(fileName)
StringBuilder ret= _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
```
For detail info ,you can check the example here:
