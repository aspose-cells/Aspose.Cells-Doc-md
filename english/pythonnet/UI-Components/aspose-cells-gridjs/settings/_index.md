---
title: Settings for GridJs
type: docs
weight: 250
url: /python-net/aspose-cells-gridjs/settings/
description: This article describes the setting for GridJs.
keywords: settings,excel,workbook,gridjs,editor
---


There are some settings we can specified by set GridWorkbookSettings :

 
- [**GridWorkbookSettings**](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs/GridWorkbookSettings)


For example, the following code set the ReCalculateOnOpen to false to stop the caculate on opening the file :
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	# do not re-calculate all formulas on opening the file.
	gws.re_calculate_on_open = False
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
 the following code set the author for the file :
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	#  et author
	gws.author = "peter"
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
You can check more settings in this class.
 