---
title: Configuraciones para GridJs
type: docs
weight: 250
url: /es/python-net/aspose-cells-gridjs/settings/
description: Este artículo describe la configuración para GridJs.
keywords: configuraciones,excel,libro de trabajo,gridjs,editor
---


Hay algunas configuraciones que podemos especificar mediante GridWorkbookSettings:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs/GridWorkbookSettings)


Por ejemplo, el siguiente código establece ReCalculateOnOpen en falso para detener el cálculo al abrir el archivo:
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	# do not re-calculate all formulas on opening the file.
	gws.re_calculate_on_open = False
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
 El siguiente código establece el autor para el archivo:
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	#  et author
	gws.author = "peter"
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
Puede verificar más ajustes en esta clase.

