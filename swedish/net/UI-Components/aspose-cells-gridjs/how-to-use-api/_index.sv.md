---
title: Arbeta med GridJs på serversidan
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/how-to-use-api/
description: Denna artikel beskriver hur man använder API er i GridJs.
keywords: GridJs, server, GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# Arbeta med GridJs på serversidan
## 1. Lägg till tjänst i ConfigureServices i startup.cs 
```C#
   services.AddScoped<IGridJsService, GridJsService>();
```
## 2. Ange sökväg för att lagra cachefiler

Du kan välja något av följande sätt:

 Alternativ 1: Sätt GridJsOptions i ConfigureServices i Startup.cs
```C#
   services.Configure<GridJsOptions>(options =>
	{
		options.FileCacheDirectory = TestConfig.TempDir;
	});
```

 Alternativ 2: Sätt direkt den statiska egenskapen
```C#
   Config.FileCacheDirectory = TestConfig.TempDir;
```

 Alternativ 3: Definiera din egen cachelagringsregel genom att implementera GridCacheForStream

För lokal fil lagring, här är ett exempel:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}


För serverlagring, erbjuder vi även ett exempel. Kontrollera: 

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>


För mer information om lagring, se denna [guide](/cells/sv/net/aspose-cells-gridjs/storage/)


## 3. Implementera kontrollertjänster

### 1. Skapa en kontroll som utökar GridJsControllerBase
```C#
public class GridJs2Controller : GridJsControllerBase
```
### 2. Hämta JSON i action

Det finns två sätt att hämta JSON-data i din action:

Alternativ 1: Använda GridJsWorkbook
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
Workbook wb = new Workbook(fullFilePath); 
wbj.ImportExcelFile(wb);
String ret =wbj.ExportToJson(fileName);
```
Alternativ 2: Använda IGridJsService i GridJsControllerBase
```C#
 String uid= GridJsWorkbook.GetUidForFile(fileName)
 StringBuilder ret= _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
```

För detaljerad info kan du kolla exemplet här:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
