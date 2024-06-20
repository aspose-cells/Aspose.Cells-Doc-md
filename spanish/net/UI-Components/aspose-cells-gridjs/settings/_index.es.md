---
title: Configuraciones para GridJs
type: docs
weight: 250
url: /es/net/aspose-cells-gridjs/settings/
description: Este artículo describe la configuración para GridJs.
keywords: GridJs,ajustes,Configuración de GridWorkbook
---


Hay algunas configuraciones que podemos especificar mediante GridWorkbookSettings:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)


Por ejemplo, el siguiente código establece ReCalculateOnOpen en falso para detener el cálculo al abrir el archivo:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 El siguiente código establece el autor para el archivo:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
Puede verificar más ajustes en esta clase.

