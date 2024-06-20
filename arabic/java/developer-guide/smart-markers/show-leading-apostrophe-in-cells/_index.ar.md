---
title: إظهار علامة الفتح في الخلايا
type: docs
weight: 20
url: /ar/java/show-leading-apostrophe-in-cells/
---

## **إظهار الترويسة الرئيسية في الخلايا**

في Microsoft Excel، يتم إخفاء الترويسة الرئيسية في قيمة الخلية. توفر Aspose.Cells ميزة عرض الترويسة الرئيسية افتراضيًا. يوفر الواجهة البرمجية للتطبيق الخاصية [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle). تُشير هذه الخاصية ما إذا كان تعيين الخاصية [**QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix) عند إدخال قيمة سلسلة تبدأ بعلامة اقتباس واحدة إلى الخلية. سيؤدي تعيين الخاصية [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle) إلى القيمة **false** إلى عرض الترويسة الرئيسية في ملف إكسل الناتج.

الصورة الملتقطة التالية تُظهر ملف إكسل الناتج مع علامة الفتح المرئية.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

الكود المقتطف التالي يظهر هذا عن طريق إضافة البيانات بواسطة العلامات الذكية في ملف إكسل المصدر. يتم إرفاق ملفات إكسل المصدر والإخراج للرجوع إليها.

[ملف المصدر](AllowLeadingApostropheSample.xlsx)

[ملف الناتج](AllowLeadingApostropheSample_out.xlsx)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

يتم تقديم تنفيذ فئة *DataObject* تحت:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
