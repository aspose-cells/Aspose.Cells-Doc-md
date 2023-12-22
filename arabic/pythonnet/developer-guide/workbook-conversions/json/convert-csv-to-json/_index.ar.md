---
title: تحويل CSV إلى JSON
type: docs
weight: 220
url: /ar/python-net/convert-csv-to-json/
description: تحويل CSV إلى JSON باستخدام Aspose.Cells for Python via .NET API.
keywords: Convert CVS to JSON, Convert CSV to JSON in Python via NET, Python convert CSV to JSON, Save CSV to JSON
---
##  **تحويل CSV إلى JSON**

Aspose.Cells for Python via .NET يدعم تحويل CSV إلى JSON. ولهذا يوفر API**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**و**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** الطبقات. ال**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**توفر الفئة خيارات لتصدير النطاق إلى JSON**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**الطبقة لديها الخصائص التالية.

- *[Export_as_string](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/)**: يؤدي ذلك إلى تصدير قيمة سلسلة الخلايا إلى JSON.
- *[has_header_row](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/)**: يشير هذا إلى ما إذا كان النطاق يحتوي على صف رأس.
- *[مسافة بادئة](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/)**: يشير إلى المسافة البادئة.

ال**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)**تقوم الفئة بتصدير JSON باستخدام خيارات التصدير المعينة مع**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**فصل.

يوضح نموذج التعليمات البرمجية التالي استخدام**[ExportRangeToJsonOptions](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions)**و**[JsonUtility](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility)** فئات لتحميل[المصدر CSV الملف](104398879.csv)ويطبع الناتج JSON في وحدة التحكم.

###  **عينة من الرموز**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

###  **إخراج وحدة التحكم**
```json
[
{
"id": 1,
"language": "Java",
"edition": "third",
"author": "Herbert Schildt",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 2,
"language": "C++",
"edition": "second",
"author": "EAAAA",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
},
{
"id": 3,
"language": ".Net",
"edition": "second",
"author": "E.Balagurusamy",
"streetAddress": 126,
"city": "San Jone",
"state": "CA",
"postalCode": 394221
}
]
```