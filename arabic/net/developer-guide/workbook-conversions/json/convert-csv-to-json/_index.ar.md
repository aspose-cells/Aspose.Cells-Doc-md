---
title: تحويل CSV إلى JSON
type: docs
weight: 220
url: /ar/net/convert-csv-to-json/
description: قم بتحويل ملف CSF إلى JSON باستخدام طريقة الاستخدام البسيطة Aspose.Cells for .NET API.
keywords: Convert, Convert CVS to JSON, CSV to JSON, CSV, JSON, Convert CSV to JSON CSharp, c# code to convert CSV to JSON
---
## **تحويل CSV إلى JSON**

Aspose.Cells يدعم تحويل CSV إلى JSON. لهذا ، يوفر API**[ExportRangeToJsonOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**و**[JsonUtility] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** الطبقات. ال**[ExportRangeToJsonOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**توفر فئة خيارات لتصدير النطاق إلى JSON. ال**[ExportRangeToJsonOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**فئة لها الخصائص التالية.

- **[ExportAsString] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring)**يؤدي هذا إلى تصدير قيمة سلسلة الخلايا إلى JSON.
- **[HasHeaderRow] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow)**: يشير هذا إلى ما إذا كان النطاق يحتوي على صف رأس.
- **[مسافة بادئة] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent)**: يشير إلى المسافة البادئة.

ال**[JsonUtility] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**تقوم الفئة بتصدير JSON باستخدام خيارات التصدير المعينة بامتداد**[ExportRangeToJsonOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**صف دراسي.

يوضح نموذج التعليمات البرمجية التالي استخدام**[ExportRangeToJsonOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions)**و**[JsonUtility] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**فئات لتحميل[مصدر ملف CSV](104398879.csv)ويطبع إخراج JSON في وحدة التحكم.

### **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

### **إخراج وحدة التحكم**
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