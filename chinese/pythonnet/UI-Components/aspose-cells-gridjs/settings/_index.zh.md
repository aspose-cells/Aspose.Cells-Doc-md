---
title: GridJs的设置
type: docs
weight: 250
url: /zh/python-net/aspose-cells-gridjs/settings/
description: 本文描述了GridJs的设置。
keywords: 设置，excel，工作簿，gridjs，编辑器
---


我们可以通过设置GridWorkbookSettings来指定一些设置：


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs/GridWorkbookSettings)


例如，以下代码将ReCalculateOnOpen设置为false，在打开文件时停止计算：
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	# do not re-calculate all formulas on opening the file.
	gws.re_calculate_on_open = False
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
 以下代码为文件设置作者：
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	#  et author
	gws.author = "peter"
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
您可以在此类中查看更多设置。

