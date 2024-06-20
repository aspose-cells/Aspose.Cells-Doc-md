---
title: إعدادات لـ GridJs
type: docs
weight: 250
url: /ar/python-net/aspose-cells-gridjs/settings/
description: يصف هذا المقال الإعداد لـ GridJs.
keywords: الإعدادات ، إكسل ، دفتر العمل ، جريدجس ، المحرر
---


هناك بعض الإعدادات التي يمكننا تحديدها عن طريق تعيين GridWorkbookSettings:


- [**GridWorkbookSettings**](https://reference.aspose.com/cells/python-net/aspose.cellsgridjs/GridWorkbookSettings)


على سبيل المثال، يقوم الكود التالي بتعيين ReCalculateOnOpen إلى القيمة false لإيقاف الحساب عند فتح الملف:
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	# do not re-calculate all formulas on opening the file.
	gws.re_calculate_on_open = False
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
 الكود التالي يقوم بتعيين المؤلف للملف:
```python
	gw = GridJsWorkbook()
	gws = GridWorkbookSettings()
	#  et author
	gws.author = "peter"
	gw.settings = gws
	gw.import_excel_file(r"c:\test.xlsx")
```
يمكنك التحقق من المزيد من الإعدادات في هذا الفصيل.

