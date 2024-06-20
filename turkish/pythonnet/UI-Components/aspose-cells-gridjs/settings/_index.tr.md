---
title: GridJs için Ayarlar
type: docs
weight: 250
url: /tr/python-net/aspose-cells-gridjs/settings/
description: Bu makale GridJs için ayarları açıklar.
keywords: ayarlar,excel,çalışma kitabı,gridjs,editör
---


GridWorkbookSettings'ı belirterek ayarlayabileceğimiz bazı ayarlarımız vardır:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs/GridWorkbookSettings)


Örneğin, aşağıdaki kod, Dosya'nın açılması sırasında hesaplamanın durdurulması için ReCalculateOnOpen özelliğini false olarak ayarlar:
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	# do not re-calculate all formulas on opening the file.
	gws.re_calculate_on_open = False
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
 aşağıdaki kod, dosyanın yazarını ayarlar:
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	#  et author
	gws.author = "peter"
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
Bu sınıfta daha fazla ayarı kontrol edebilirsiniz.

