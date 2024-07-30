---
title: Einstellungen für GridJs
type: docs
weight: 250
url: /de/java/aspose-cells-gridjs/settings/
description: Dieser Artikel beschreibt die Einstellung für GridJs.
keywords: GridJs, Einstellungen, GridWorkbookSettings
aliases:
  - /java/aspose-cells-gridjs/how-to-use-setting/
  - /java/aspose-cells-gridjs/work-with-setting/
---


Es gibt einige Einstellungen, die wir durch Setzen von GridWorkbookSettings festlegen können:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/java/aspose.cells.gridjs/GridWorkbookSettings)


Zum Beispiel setzt der folgende Code das ReCalculateOnOpen auf false, um die Berechnung beim Öffnen der Datei zu stoppen:
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.setReCalculateOnOpen(false);
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
 Der folgende Code setzt den Autor für die Datei:
```JAVA
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.setAuthor("peter");
    gw.setSettings(gws);
    gw.importExcelFile(@"c:\test.xlsx");
```
Sie können weitere Einstellungen in dieser Klasse überprüfen.

