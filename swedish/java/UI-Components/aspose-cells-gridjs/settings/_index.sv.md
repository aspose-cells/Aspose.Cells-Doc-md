---
title: Inställningar för GridJs
type: docs
weight: 250
url: /sv/java/aspose-cells-gridjs/settings/
description: Denna artikel beskriver inställningarna för GridJs.
keywords: GridJs,inställningar,GridWorkbookSettings
aliases:
  - /java/aspose-cells-gridjs/how-to-use-setting/
  - /java/aspose-cells-gridjs/work-with-setting/
---


Det finns några inställningar vi kan ange genom att ange GridWorkbookSettings :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/GridWorkbookSettings)


Till exempel, följande kod ställer ReCalculateOnOpen till falskt för att stoppa beräkningen vid öppning av filen :
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.setReCalculateOnOpen(false);
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
 följande kod ställer in författaren för filen :
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.setAuthor("peter");
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
Du kan kontrollera fler inställningar i denna klass.

