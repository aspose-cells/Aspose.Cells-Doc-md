---
title: تمكين خصائص CSS المخصصة عند الحفظ إلى HTML باستخدام Python.NET
linktitle: تمكين خصائص CSS المخصصة عند الحفظ إلى HTML
type: docs
weight: 320
url: /ar/python-net/enable-css-custom-properties-while-saving-to-html/
description: تعلم كيفية تفعيل خصائص CSS المخصصة عند حفظ ملفات إكسل إلى HTML باستخدام API الخاص بـ Aspose.Cells for Python via .NET.
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف إكسل إلى HTML، في السيناريوهات التي توجد بها تكرارات متعددة لصور base64 واحدة، فإن استخدام خصائص CSS المخصصة يسمح بحفظ بيانات الصورة مرة واحدة فقط. هذا يحسن أداء HTML الناتج. استخدم الخاصية [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/) واضبطها على **True** أثناء الحفظ إلى HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **تمكين خصائص CSS المخصصة أثناء الحفظ إلى HTML**

يظهر الكود النموذجي التالي استخدام الخاصية [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/). تُظهر الصورة الملتقطة تأثير عدم تعيين هذه الخاصية على True. قم بتنزيل ملف إكسل النموذجي([ملف إكسل النموذجي](50528260.xlsx)) المستخدم في هذا الكود وملف HTML الناتج([ملف HTML الناتج](50528261.zip)) للمقارنة.

## **الكود المثالي**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

# Load sample workbook
wb = Workbook(os.path.join(source_dir, "sampleEnableCssCustomProperties.xlsx"))

# Configure HTML save options
opts = HtmlSaveOptions()
opts.export_images_as_base64 = True
opts.enable_css_custom_properties = True

# Save the workbook in HTML
wb.save(os.path.join(output_dir, "outputEnableCssCustomProperties.html"), opts)
```
{{< app/cells/assistant language="python-net" >}}
