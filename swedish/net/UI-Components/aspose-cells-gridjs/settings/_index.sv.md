---
title: Inställningar för GridJs
type: docs
weight: 250
url: /sv/net/aspose-cells-gridjs/settings/
description: Den här artikeln beskriver inställningen för GridJs.
keywords: settings
---
Det finns några inställningar vi kan specificera genom att ställa in GridWorkbookSettings:

 
- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)**


Till exempel ställer följande kod in ReCalculateOnOpen till false för att stoppa uträkningen när filen öppnas:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 följande kod ställer in författaren för filen:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
Du kan kontrollera fler inställningar i den här klassen.
 