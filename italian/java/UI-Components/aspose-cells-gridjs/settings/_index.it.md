---
title: Impostazioni per GridJs
type: docs
weight: 250
url: /it/java/aspose-cells-gridjs/settings/
description: Questo articolo descrive le impostazioni per GridJs.
keywords: GridJs, impostazioni, Impostazioni del workbook di Grid
aliases:
  - /java/aspose-cells-gridjs/how-to-use-setting/
  - /java/aspose-cells-gridjs/work-with-setting/
---


Ci sono alcune impostazioni che possiamo specificare impostando GridWorkbookSettings :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/GridWorkbookSettings)


Ad esempio, il seguente codice imposta ReCalculateOnOpen su false per impedire il calcolo all'apertura del file:
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.setReCalculateOnOpen(false);
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
 il seguente codice imposta l'autore per il file:
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.setAuthor("peter");
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
Puoi controllare più impostazioni in questa classe.

