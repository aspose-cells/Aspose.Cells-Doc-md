---
title: Aspose.Cells for Java 19.9 ملاحظات الإصدار
type: docs
weight: 40
url: /ar/java/aspose-cells-for-java-19-9-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار for Java Aspose.Cells 19.9.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42990|يتم عرض الصفوف المخفية أثناء تحويل ملف Excel إلى HTML عند وجود التصفية التلقائية|خلل برمجي|
|CELLSJAVA-42997|فشل CalculateFormula () مع سلاسل صيغة كبيرة|خلل برمجي|
|CELLSJAVA-43000|CalculateFormula () يفسد ملف Excel|خلل برمجي|
|CELLSJAVA-42987|مشاكل التنسيق أثناء تحويل ملف Excel إلى PDF|خلل برمجي|
|CELLSJAVA-42986|تداخل النص بعد تحويل ملف XLSX صيني إلى PDF|خلل برمجي|
|CELLSJAVA-43012|Workbook.setRecalculateOnOpen (false) لا يعمل مع إصدارات Excel الأحدث|خلل برمجي|
|CELLSJAVA-42996|لم يتم تقديم ملصقات البيانات المستندة إلى الصيغ بشكل صحيح في PDF|خلل برمجي|
|CELLSJAVA-42992|تم رفع الاستثناء أثناء تحويل XLSM إلى صورة|استثناء|
|CELLSJAVA-42991|استثناء "يجب أن يكون عرض العمود بين 0 و 255" أثناء تحويل Excel إلى PDF في macOS|استثناء|
|CELLSJAVA-43004|استثناء java.lang.NumberFormatException: لسلسلة الإدخال: "0.0" أثناء تحويل Excel إلى HTML|استثناء|
|CELLSJAVA-43010|IllegalArgumentException أثناء تنفيذ deleteBlankColumns ()|استثناء|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يزيل خاصية Chart.Rotation التي عفا عليها الزمن**
استخدم خاصية Chart.RotationAngle بدلاً من ذلك.
### **يزيل خاصية Chart.IsDataTableShown القديمة**
استخدم خاصية Chart.ShowDataTable بدلاً من ذلك.
### **يزيل خاصية Chart.IsLegendShown القديمة**
استخدم خاصية Chart.ShowLegend بدلاً من ذلك.
### **يزيل عفا عليها الزمن Axis.Crosses الممتلكات**
استخدم خاصية Axis.Crosses بدلاً من ذلك.
### **إضافة خصائص Enum OoxmlCompressionType و XlsbSaveOptions.CompressionType و OoxmlSaveOptions.CompressionType.**
يمثل نوع الضغط لملفات OOXML.
