---
title: دعم الإعداد الألماني في معادلات النطاقات المسماة باستخدام Python.NET
linktitle: دعم اللغة الألمانية في صيغ النطاقات المسماة
type: docs
weight: 60
url: /ar/python-net/support-for-german-locale-in-named-range-formulae/
description: تعلّم كيفية التعامل مع إعدادات اللغة الألمانية لمعادل النطاقات المسماة في إكسل باستخدام Aspose.Cells لـ Python via .NET.
---

يتم كتابة المعادلات الإنجليزية ضمن المناطق المسماة. يمكن فتح هذا الملف في بيئة معدة للغة الألمانية، وستُترجم المعادلة الإنجليزية إلى اللغة الألمانية. يتطلب هذا المثال تثبيت إكسل مع إعدادات اللغة الألمانية وإعدادات النظام باللغة الألمانية.

يمكن تحميل ملف العينة لاختبار هذه الميزة من:   
[sampleNamedRangeTest.xlsm](73990165.xlsm)

```python
import os
from aspose.cells import Workbook

source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

name = "HasFormula"
value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))"

wb_source = Workbook(os.path.join(source_dir, "sampleNamedRangeTest.xlsm"))
ws_col = wb_source.worksheets

name_index = ws_col.names.add(name)
named_range = ws_col.names[name_index]
named_range.refers_to = value

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

wb_source.save(os.path.join(output_dir, "sampleOutputNamedRangeTest.xlsm"))
```
{{< app/cells/assistant language="python-net" >}}
