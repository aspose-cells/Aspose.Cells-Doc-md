---
title: تحويل CSV إلى JSON باستخدام Golang عبر C++
linktitle: تحويل CSV إلى JSON
type: docs
weight: 220
url: /ar/go-cpp/convert-csv-to-json/
description: تحويل ملف CSV إلى JSON باستخدام واجهة برمجة التطبيقات Aspose.Cells for C++ سهلة الاستخدام.
keywords: تحويل، تحويل CSV إلى JSON، CSV إلى JSON، CSV، JSON، تحويل CSV إلى JSON C++، كود C++ لتحويل CSV إلى JSON
---

## **تحويل CSV إلى JSON**

يدعم Aspose.Cells تحويل CSV إلى JSON. لهذا، توفر API الفئات [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) و [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). توفر فئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) الخيارات لتصدير النطاق إلى JSON. تحتوي فئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) على الخصائص التالية.

- [**GetExportAsString()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getexportasstring/): يقوم بتصدير قيمة السلسلة للخلايا إلى JSON.
- [**GetHasHeaderRow()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/gethasheaderrow/): يشير إلى ما إذا كان النطاق يحتوي على صف رأس.
- [**GetIndent()**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/getindent/): يشير إلى المسافة البادئة.

تقوم فئة [**JsonUtility**](https://reference.aspose.com/cells/go-cpp/jsonutility/) بتصدير JSON باستخدام خيارات التصدير المحددة بواسطة فئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/exportrangetojsonoptions/).

يوضح المثال البرمجي التالي استخدام فئات [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/go-cpp/exportrangetojsonoptions/) و [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) لتحميل ملف CSV المصدر (104398879.csv) وطباعة إخراج JSON في وحدة التحكم.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertCsvToJson.go" >}}
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
