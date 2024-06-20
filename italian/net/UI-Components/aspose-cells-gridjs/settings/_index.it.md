---
title: Impostazioni per GridJs
type: docs
weight: 250
url: /it/net/aspose-cells-gridjs/settings/
description: Questo articolo descrive le impostazioni per GridJs.
keywords: GridJs, impostazioni, Impostazioni del workbook di Grid
---


Ci sono alcune impostazioni che possiamo specificare impostando GridWorkbookSettings :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)


Ad esempio, il seguente codice imposta ReCalculateOnOpen su false per impedire il calcolo all'apertura del file:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 il seguente codice imposta l'autore per il file:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
Puoi controllare più impostazioni in questa classe.

