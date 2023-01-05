---
title: Configuraciones para GridJs
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/settings/
description: Este artículo describe la configuración de GridJs.
keywords: settings
---
Hay algunas configuraciones que podemos especificar mediante set GridWorkbookSettings:

 
- **[Configuración de GridWorkbook](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)**


Por ejemplo, el siguiente código establece ReCalculateOnOpen en falso para detener el cálculo al abrir el archivo:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 el siguiente código establece el autor del archivo:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
Puede consultar más configuraciones en esta clase.
 