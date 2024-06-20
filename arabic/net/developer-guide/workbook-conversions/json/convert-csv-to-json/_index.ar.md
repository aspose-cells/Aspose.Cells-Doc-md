---
title: تحويل CSV إلى JSON
type: docs
weight: 220
url: /ar/net/convert-csv-to-json/
description: قم بتحويل ملف CSF إلى JSON عن طريق استخدام واجهة الاستخدام البسيطة Aspose.Cells for .NET API.
keywords: تحويل، تحويل الملفات CVS إلى JSON، CSV إلى JSON، CSV، JSON، تحويل CSV إلى JSON بلغة CSharp، كود c# لتحويل CSV إلى JSON
---

## **تحويل CSV إلى JSON**

تدعم Aspose.Cells تحويل CSV إلى JSON. لهذا الغرض، توفر واجهة البرمجة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) وواجهة البرمجة [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility). توفر واجهة البرمجة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) خيارات لتصدير المجال إلى JSON. تحتوي واجهة البرمجة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) على الخصائص التالية.

- [**ExportAsString**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/exportasstring): يقوم بتصدير قيمة السلسلة للخلايا إلى JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/hasheaderrow): يشير إذا كانت المدى يحتوي على صف رأسي.
- [**Indent**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions/properties/indent): يشير إلى التنسيق.

تقوم الفئة [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) بتصدير JSON باستخدام خيارات التصدير المعينة باستخدام الفئة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions).

يُظهر الكود العيني التالي استخدام واجهة البرمجة [**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/net/aspose.cells.utility/exportrangetojsonoptions) وواجهة البرمجة [**JsonUtility**](https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility) لتحميل [ملف CSV المصدر](104398879.csv) ويطبع الإخراج JSON في وحدة التحكم.

### **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.cs" >}}

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
