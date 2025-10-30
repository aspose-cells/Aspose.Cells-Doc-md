---
title: Lavorare con GridJs lato server
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/how-to-use-api/
description: Questo articolo descrive come utilizzare le API in GridJs.
keywords: GridJs, server, GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# Lavorare con GridJs lato server
## 1. Aggiungi il servizio in ConfigureServices in startup.cs 
```C#
   services.AddScoped<IGridJsService, GridJsService>();
```
## 2. Imposta il percorso per memorizzare i file della cache

Puoi scegliere uno dei seguenti metodi:

 Opzione 1: Imposta GridJsOptions in ConfigureServices in Startup.cs
```C#
   services.Configure<GridJsOptions>(options =>
	{
		options.FileCacheDirectory = TestConfig.TempDir;
	});
```

 Opzione 2: Imposta direttamente la proprietà statica
```C#
   Config.FileCacheDirectory = TestConfig.TempDir;
```

 Opzione 3: Definisci la tua regola di archiviazione cache implementando GridCacheForStream

Per lo storage in file locale, ecco un esempio:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}


Per l'archiviazione lato server, forniamo anche un esempio. Per favore, verifica: 

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>


Per ulteriori dettagli sull'archiviazione, consulta questa [guida](/cells/it/net/aspose-cells-gridjs/storage/)


## 3. Implementa le azioni del Controller

### 1. Crea un Controller che estende GridJsControllerBase
```C#
public class GridJs2Controller : GridJsControllerBase
```
### 2. Ottieni JSON nell'azione

Ci sono due modi per ottenere i dati JSON nella tua azione:

Opzione 1: Usando GridJsWorkbook
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
Workbook wb = new Workbook(fullFilePath); 
wbj.ImportExcelFile(wb);
String ret =wbj.ExportToJson(fileName);
```
Opzione 2: Usando IGridJsService in GridJsControllerBase
```C#
 String uid= GridJsWorkbook.GetUidForFile(fileName)
 StringBuilder ret= _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
```

Per ulteriori informazioni, puoi controllare l'esempio qui:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
