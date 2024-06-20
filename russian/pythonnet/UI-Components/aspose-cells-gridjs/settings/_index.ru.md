---
title: Настройки для GridJs
type: docs
weight: 250
url: /ru/python-net/aspose-cells-gridjs/settings/
description: В этой статье описаны настройки для GridJs.
keywords: настройки, электронная таблица, книга Excel, gridjs, редактор
---


Существуют некоторые настройки, которые мы можем указать с помощью настроек GridWorkbookSettings:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs/GridWorkbookSettings)


Например, следующий код устанавливает ReCalculateOnOpen в false, чтобы остановить вычисление при открытии файла :
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	# do not re-calculate all formulas on opening the file.
	gws.re_calculate_on_open = False
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
 следующий код задает автора для файла :
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	#  et author
	gws.author = "peter"
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
Вы можете проверить больше настроек в этом классе.

