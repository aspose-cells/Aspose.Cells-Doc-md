---
title: تحويل CSV إلى JSON
type: docs
weight: 220
url: /ar/python-net/convert-csv-to-json/
description: تحويل CSV إلى JSON باستخدام Aspose.Cells for Python via .NET API.
keywords: تحويل CVS إلى JSON، تحويل CSV إلى JSON في Python via NET، تحويل CSV إلى JSON في Python، حفظ CSV إلى JSON
---

## **تحويل CSV إلى JSON**

Aspose.Cells for Python via .NET يدعم تحويل CSV إلى JSON. لهذا، يوفر الواجهة البرمجية [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) و [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility). الفئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) توفر الخيارات لتصدير النطاق إلى JSON. الفئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) لها الخصائص التالية.

- [**export_as_string**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/export_as_string/): يقوم بتصدير قيمة السلسلة للخلايا إلى JSON.
- [**has_header_row**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/has_header_row/): يشير إذا كانت المدى يحتوي على صف رأسي.
- [**indent**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions/indent/): يشير إلى التنسيق.

تقوم الفئة [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) بتصدير JSON باستخدام خيارات التصدير المعينة باستخدام الفئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions).

يُظهر الكود العيني التالي استخدام واجهة البرمجة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/exportrangetojsonoptions) وواجهة البرمجة [**JsonUtility**](https://reference.aspose.com/cells/python-net/aspose.cells.utility/jsonutility) لتحميل [ملف CSV المصدر](104398879.csv) ويطبع الإخراج JSON في وحدة التحكم.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.py" >}}

### **مخرجات الوحدة**
{{< highlight java >}}

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

{{< /highlight >}}
