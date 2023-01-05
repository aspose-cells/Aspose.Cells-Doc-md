---
title: Impostazioni per GridJs
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/settings/
description: Questo articolo descrive l'impostazione per GridJs.
keywords: settings
---
Ci sono alcune impostazioni che possiamo specificare set GridWorkbookSettings :

 
- **[GridWorkbookSettings](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)**


Ad esempio, il codice seguente imposta ReCalculateOnOpen su false per arrestare il caculate all'apertura del file:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 il codice seguente imposta l'autore del file:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
Puoi controllare più impostazioni in questa classe.
 