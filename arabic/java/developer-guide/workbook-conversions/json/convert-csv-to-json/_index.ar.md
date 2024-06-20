---
title: تحويل CSV إلى JSON
type: docs
weight: 170
url: /ar/java/convert-csv-to-json/
---

## **تحويل CSV إلى JSON**

تدعم Aspose.Cells تحويل CSV إلى JSON. لهذا الغرض، يوفر الواجهة البرمجية الخيارات التالية: [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) و [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility). يقدم الفئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) الخيارات لتصدير النطاق إلى JSON. تحتوي الفئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) على الخصائص التالية.

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): يقوم بتصدير قيمة السلسلة للخلايا إلى JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): يشير إذا كانت المدى يحتوي على صف رأسي.
- [**Indent**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): يشير إلى التنسيق.

تقوم الفئة [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) بتصدير JSON باستخدام خيارات التصدير المعينة باستخدام الفئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions).

توضح العينة البرمجية التالية استخدام الفئتين [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions) و[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) لتحميل الملف CSV المصدر (SampleCsv.csv) ويطبع الإخراج JSON (SampleJson_out.csv) في وحدة التحكم.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

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
