---
title: Configuraciones para GridJs
type: docs
weight: 250
url: /es/java/aspose-cells-gridjs/settings/
description: Este artículo describe la configuración para GridJs.
keywords: GridJs,ajustes,Configuración de GridWorkbook
aliases:
  - /java/aspose-cells-gridjs/how-to-use-setting/
  - /java/aspose-cells-gridjs/work-with-setting/
---


Hay algunas configuraciones que podemos especificar mediante GridWorkbookSettings:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/GridWorkbookSettings)


Por ejemplo, el siguiente código establece ReCalculateOnOpen en falso para detener el cálculo al abrir el archivo:
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.setReCalculateOnOpen(false);
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
 El siguiente código establece el autor para el archivo:
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.setAuthor("peter");
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
Puede verificar más ajustes en esta clase.

