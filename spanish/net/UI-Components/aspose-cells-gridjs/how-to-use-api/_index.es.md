---
title: Trabajando con GridJs del lado del servidor
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/how-to-use-api/
description: Este artículo describe cómo usar APIs en GridJs.
keywords: GridJs, servidor, GridCacheForStream
aliases:
  - /net/aspose-cells-gridjs/server/
  - /net/aspose-cells-gridjs/server-api/
  - /net/aspose-cells-gridjs/api-introduction/
  - /net/aspose-cells-gridjs/how-to-use-apis/
  - /net/aspose-cells-gridjs/work-with-serverside-api/
  - /net/aspose-cells-gridjs/work-with-serverside-apis/
---


# Trabajando con GridJs del lado del servidor
## 1. agregar servicio en ConfigureServices en startup.cs 
```C#
   services.AddScoped<IGridJsService, GridJsService>();
```
## 2. Establecer la ruta para almacenar archivos en caché

Puedes elegir cualquiera de las siguientes formas:

 Opción 1: Establecer GridJsOptions en ConfigureServices en Startup.cs
```C#
   services.Configure<GridJsOptions>(options =>
	{
		options.FileCacheDirectory = TestConfig.TempDir;
	});
```

 Opción 2: Establecer directamente la propiedad estática
```C#
   Config.FileCacheDirectory = TestConfig.TempDir;
```

 Opción 3: Definir tu propia regla de almacenamiento en caché implementando GridCacheForStream

Para el almacenamiento de archivos local, aquí hay un ejemplo:

{{< gist "aspose-cells-gists" "fb32f5c7a98978432e5e05c50995a4ca" "LocalFileCache.cs" >}}


Para almacenamiento en el lado del servidor, también proporcionamos un ejemplo. Por favor, revisa: 

<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/blob/master/Examples_GridJs/Models/AwsCache.cs>


Para más detalles sobre almacenamiento, consulta esta [guía](/cells/es/net/aspose-cells-gridjs/storage/)


## 3. Implementar acciones en el controlador

### 1. Crear un controlador que extienda GridJsControllerBase
```C#
public class GridJs2Controller : GridJsControllerBase
```
### 2. Obtener JSON en la acción

Hay dos formas de obtener datos JSON en tu acción:

Opción 1: Usando GridJsWorkbook
```C#
GridJsWorkbook wbj = new GridJsWorkbook();
Workbook wb = new Workbook(fullFilePath); 
wbj.ImportExcelFile(wb);
String ret =wbj.ExportToJson(fileName);
```
Opción 2: Usando IGridJsService en GridJsControllerBase
```C#
 String uid= GridJsWorkbook.GetUidForFile(fileName)
 StringBuilder ret= _gridJsService.DetailFileJsonWithUid(fullFilePath, uid);
```

Para obtener información detallada, puede consultar el ejemplo aquí:
<https://github.com/aspose-cells/Aspose.Cells.Grid-for-.NET/tree/master/Examples_GridJs>
