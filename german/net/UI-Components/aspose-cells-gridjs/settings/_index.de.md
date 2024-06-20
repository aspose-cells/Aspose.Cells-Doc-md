---
title: Einstellungen für GridJs
type: docs
weight: 250
url: /de/net/aspose-cells-gridjs/settings/
description: Dieser Artikel beschreibt die Einstellung für GridJs.
keywords: GridJs, Einstellungen, GridWorkbookSettings
---


Es gibt einige Einstellungen, die wir durch Setzen von GridWorkbookSettings festlegen können:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells.gridjs/GridWorkbookSettings)


Zum Beispiel setzt der folgende Code das ReCalculateOnOpen auf false, um die Berechnung beim Öffnen der Datei zu stoppen:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //do not re-calculate all formulas on opening the file.
    gws.ReCalculateOnOpen = false;
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
 Der folgende Code setzt den Autor für die Datei:
```C#
   GridJsWorkbook gw = new GridJsWorkbook();
   GridWorkbookSettings gws = new GridWorkbookSettings();
   //set author.
    gws.Author = "peter";
    gw.Settings = gws;
    gw.ImportExcelFile(@"c:\test.xlsx");
```
Sie können weitere Einstellungen in dieser Klasse überprüfen.

