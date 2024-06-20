---
title: Inställningar för GridJs
type: docs
weight: 250
url: /sv/python-net/aspose-cells-gridjs/settings/
description: Denna artikel beskriver inställningarna för GridJs.
keywords: inställningar, excel, arbetsbok, gridjs, redigerare
---


Det finns några inställningar vi kan ange genom att ange GridWorkbookSettings :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs/GridWorkbookSettings)


Till exempel, följande kod ställer ReCalculateOnOpen till falskt för att stoppa beräkningen vid öppning av filen :
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	# do not re-calculate all formulas on opening the file.
	gws.re_calculate_on_open = False
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
 följande kod ställer in författaren för filen :
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	#  et author
	gws.author = "peter"
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
Du kan kontrollera fler inställningar i denna klass.

