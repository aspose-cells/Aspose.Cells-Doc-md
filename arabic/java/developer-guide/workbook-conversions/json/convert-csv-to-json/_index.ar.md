﻿---
title: حوّل CSV إلى JSON
type: docs
weight: 170
url: /ar/java/convert-csv-to-json/
---
## **حوّل CSV إلى JSON**

يدعم Aspose.Cells تحويل CSV إلى JSON. لهذا ، يوفر API[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)و[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)الطبقات. ال[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)توفر الفئة خيارات لتصدير النطاق إلى JSON. ملف[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)فئة لها الخصائص التالية.

- [**ExportAsString**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#ExportAsString): يؤدي هذا إلى تصدير قيمة سلسلة الخلايا إلى JSON.
- [**HasHeaderRow**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#HasHeaderRow): يشير هذا إلى ما إذا كان النطاق يحتوي على صف رأس.
- [**مسافة بادئة**](https://reference.aspose.com/cells/java/com.aspose.cells/exportrangetojsonoptions#Indent): يشير إلى المسافة البادئة.

ال[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)تقوم الفئة بتصدير JSON باستخدام مجموعة اختيارات التصدير مع الامتداد[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)صف دراسي.

يوضح نموذج التعليمات البرمجية التالي استخدام[**ExportRangeToJsonOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ExportRangeToJsonOptions)و[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)فئات لتحميل[المصدر CSV ملف](SampleCsv.csv)ويطبع ملف[JSON](SampleJson_out.csv) الإخراج في وحدة التحكم.

### **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertCsvToJson-1.java" >}}

### **إخراج وحدة التحكم**

[