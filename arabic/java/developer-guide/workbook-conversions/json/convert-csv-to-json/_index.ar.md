---
title: تحويل CSV إلى JSON
type: docs
weight: 170
url: /ar/java/convert-csv-to-json/
---
## **تحويل CSV إلى JSON**

Aspose.Cells يدعم تحويل CSV إلى JSON. لهذا ، يوفر API[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)و[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)الطبقات. ال[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)توفر فئة خيارات لتصدير النطاق إلى JSON. ال[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)فئة لها الخصائص التالية.

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString)يؤدي هذا إلى تصدير قيمة سلسلة الخلايا إلى JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): يشير هذا إلى ما إذا كان النطاق يحتوي على صف رأس.
- [**مسافة بادئة**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): يشير إلى المسافة البادئة.

ال[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)تقوم الفئة بتصدير JSON باستخدام خيارات التصدير المعينة بامتداد[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)صف دراسي.

يوضح نموذج التعليمات البرمجية التالي استخدام[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)و[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)فئات لتحميل[مصدر ملف CSV](SampleCsv.csv)ويطبع ملف[جسون](SampleJson_out.csv) الإخراج في وحدة التحكم.

### **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **إخراج وحدة التحكم**

[ { "id": 1،  "language": "Java"، _ x000d_ "edition": "Third"، _ x000d_ "author": "Herbert Schildt"، _ x000d_ "streetAddress": 126،  "city": "San Jone"، _ x000d_ "state": "CA"، _ x000d_ "postalCode": 394221}، _ x000d_ { "id": 2،  "language": "C++"، _ x000d_ "edition": "second"، _ x000d_ "المؤلف": "EAAAA"، _ x000d_ "streetAddress": 126،  "city": "San Jone"، _ x000d_ "state": "CA"، _ x000d_ "postalCode": 394221}، _ x000d_ { "id": 3 ،  "language": ".Net"، _ x000d_ "edition": "second"، _ x000d_ "author": "E.Balagurusamy"، _ x000d_ "streetAddress": 126،  "city": "San Jone"، _ x000d_ " الحالة ":" CA "، _ x000d_" postalCode ": 394221} ]