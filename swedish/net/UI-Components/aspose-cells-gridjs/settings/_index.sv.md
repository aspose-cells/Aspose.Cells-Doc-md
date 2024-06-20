---
title: Inställningar för GridJs
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/settings/
description: Denna artikel beskriver inställningarna för GridJs.
keywords: GridJs,inställningar,GridWorkbookSettings
---


Det finns några inställningar vi kan ange genom att ange GridWorkbookSettings :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)


Till exempel, följande kod ställer ReCalculateOnOpen till falskt för att stoppa beräkningen vid öppning av filen :
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 följande kod ställer in författaren för filen :
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
Du kan kontrollera fler inställningar i denna klass.

