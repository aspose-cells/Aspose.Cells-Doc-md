---
title: حوّل JSON إلى CSV
type: docs
weight: 160
url: /ar/java/convert-json-to-csv/
---
يدعم Aspose.Cells التحويل البسيط والمتداخل من JSON إلى CSV. لهذا الغرض ، يوفر API[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)و[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)الطبقات. ال[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)توفر class خيارات تخطيط JSON مثل[**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(يتجاهل العنوان إذا كانت المصفوفة خاصية لكائن) أو[**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(يعالج المصفوفة كجدول). ال[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)يقوم class بمعالجة JSON باستخدام خيارات التخطيط التي تم ضبطها باستخدام[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)صف دراسي.

يوضح نموذج التعليمات البرمجية التالي استخدام[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)و[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)فئات لتحميل[المصدر JSON ملف](SampleJson.json)ويولد ال[ملف الإخراج CSV](SampleJson_out.csv).

## عينة من الرموز

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
