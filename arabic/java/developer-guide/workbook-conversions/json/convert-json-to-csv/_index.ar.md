---
title: تحويل JSON إلى CSV
type: docs
weight: 160
url: /ar/java/convert-json-to-csv/
---
يدعم Aspose.Cells تحويل JSON البسيط والمتداخل إلى CSV. لهذا ، يوفر API[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)و[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)الطبقات. ال[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)توفر فئة خيارات تنسيق JSON مثل[**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle)(يتجاهل العنوان إذا كانت المصفوفة خاصية لكائن) أو[**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable)(يعالج المصفوفة كجدول). ال[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)يقوم class بمعالجة JSON باستخدام خيارات التخطيط التي تم تعيينها باستخدام[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)صف دراسي.

يوضح نموذج التعليمات البرمجية التالي استخدام[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)و[**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility)فئات لتحميل[ملف JSON المصدر](SampleJson.json)ويولد ال[إخراج ملف CSV](SampleJson_out.csv).

## عينة من الرموز

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.java" >}}
