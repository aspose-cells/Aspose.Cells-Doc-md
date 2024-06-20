---
title: Einstellungen für GridJs
type: docs
weight: 250
url: /de/python-net/aspose-cells-gridjs/settings/
description: Dieser Artikel beschreibt die Einstellung für GridJs.
keywords: Einstellungen, Excel, Arbeitsmappe, GridJs, Editor
---


Es gibt einige Einstellungen, die wir durch Setzen von GridWorkbookSettings festlegen können:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs/GridWorkbookSettings)


Zum Beispiel setzt der folgende Code das ReCalculateOnOpen auf false, um die Berechnung beim Öffnen der Datei zu stoppen:
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	# do not re-calculate all formulas on opening the file.
	gws.re_calculate_on_open = False
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
 Der folgende Code setzt den Autor für die Datei:
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	#  et author
	gws.author = "peter"
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
Sie können weitere Einstellungen in dieser Klasse überprüfen.

