---
title: إظهار الفاصلة العليا في الخلايا
type: docs
weight: 20
url: /ar/java/show-leading-apostrophe-in-cells/
---
## **إظهار الفاصلة العليا في الخلايا**

في Microsoft Excel ، يتم إخفاء الفاصلة العليا في قيمة الخلية. يوفر Aspose.Cells خاصية لعرض الفاصلة العليا بشكل افتراضي. لهذا ، يوفر API[**المصنف.الإعدادات**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)خاصية. تشير هذه الخاصية إلى ما إذا كان سيتم تعيين ملف[**اقتباس**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)الخاصية عند إدخال قيمة سلسلة تبدأ بعلامة اقتباس واحدة للخلية. وضع[**المصنف.الإعدادات**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)ملكية ل**خاطئة**سيعرض الفاصلة العليا في ملف Excel الناتج.

تُظهر لقطة الشاشة التالية ملف Excel الناتج مع الفاصلة العليا المرئية.

![ما يجب القيام به: image_بديل_نص](show-leading-apostrophe-in-cells_1.jpg)

يوضح مقتطف الكود التالي هذا عن طريق إضافة البيانات باستخدام Smart Markers في ملف Excel المصدر. يتم إرفاق ملفات إكسل المصدر والمخرجات كمرجع.

[مصدر الملف](AllowLeadingApostropheSample.xlsx)

[ملف إلاخراج](AllowLeadingApostropheSample_out.xlsx)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

تنفيذ*DataObject*يتم إعطاء فئة أدناه

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
