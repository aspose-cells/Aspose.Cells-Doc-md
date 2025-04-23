---
title: Arbeiten mit GridJs Server Side
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/how-to-use-api/
description: In diesem Artikel wird beschrieben, wie man APIs in GridJs verwendet.
keywords: GridJs,server,GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# Arbeiten mit GridJs Server Side
## 1. Dienst in ConfigureServices in startup.cs hinzufügen 
```C#
   services.AddScoped<IGridJsService, GridJsService>();
```
## 2. Pfad zum Speichern von Cache-Dateien festlegen

Sie können eine der folgenden Methoden wählen:

 Option 1: Setzen Sie GridJsOptions in ConfigureServices in Startup.cs
```C#
   services.Configure<GridJsOptions>(options =>
	{
		options.FileCacheDirectory = TestConfig.TempDir;
	});
```

 Option 2: Setzen Sie die statische Eigenschaft direkt
```C#
   Config.FileCacheDirectory = TestConfig.TempDir;
```

 Option 3: Definieren Sie Ihre eigene Cache-Speicherregel durch Implementierung von GridCacheForStream

Für die lokale Dateispeicherung, hier ist ein Beispiel:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}


Für die serverseitige Speicherung stellen wir auch ein Beispiel bereit. Bitte prüfen Sie: 

<https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>


Für weitere Details zur Speicherung lesen Sie bitte diesen [Leitfaden](/cells/de/net/aspose-cells-gridjs/storage/)


## 3. Implementieren Sie Controller-Aktionen

### 1. Erstellen Sie einen Controller, der GridJsControllerBase erweitert
```C#
public class GridJs2Controller : GridJsControllerBase
```
### 2. JSON in Aktion abrufen

Es gibt zwei Möglichkeiten, JSON-Daten in Ihrer Aktion zu erhalten:

Option 1: Mit GridJsWorkbook
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
Workbook wb = new Workbook(fullFilePath); 
wbj.ImportExcelFile(wb);
String ret =wbj.ExportToJson(fileName);
```
Option 2: Mit IGridJsService in GridJsControllerBase
```C#
 String uid= GridJsWorkbook.GetUidForFile(fileName)
 StringBuilder ret= _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
```

Für weitere Details können Sie hier das Beispiel überprüfen:
<https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Examples_GridJs>
