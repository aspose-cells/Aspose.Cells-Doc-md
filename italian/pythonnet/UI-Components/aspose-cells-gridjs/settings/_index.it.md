---
title: Impostazioni per GridJs
type: docs
weight: 250
url: /it/python-net/aspose-cells-gridjs/settings/
description: Questo articolo descrive le impostazioni per GridJs.
keywords: impostazioni, excel, cartella di lavoro, gridjs, editor
---


Ci sono alcune impostazioni che possiamo specificare impostando GridWorkbookSettings :


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs/GridWorkbookSettings)


Ad esempio, il seguente codice imposta ReCalculateOnOpen su false per impedire il calcolo all'apertura del file:
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	# do not re-calculate all formulas on opening the file.
	gws.re_calculate_on_open = False
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
 il seguente codice imposta l'autore per il file:
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	#  et author
	gws.author = "peter"
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
Puoi controllare più impostazioni in questa classe.

