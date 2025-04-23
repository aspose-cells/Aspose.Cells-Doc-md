---
title: كيفية طباعة إكسل كصفحات مناسبة للعرض بشكل واسع ومرتفعة
type: docs
weight: 200
url: /ar/java/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: يُظهر لك هذا المقال رمز يوضح كيفية تعيين FitToPagesWide و FitToPagesTall باستخدام مكتبة Aspose.Cells.
keywords: Java كيفية تعيين FitToPagesWide و FitToPagesTall، كيفية إضافة FitToPagesWide و FitToPagesTall في جافا، كيفية تعيين FitToPagesWide و FitToPagesTall في إكسل، كيفية مسح FitToPagesWide و FitToPagesTall في إكسل، كيفية طباعة إكسل كصفحات مناسبة للعرض بشكل واسع ومرتفعة، كيفية طباعة ورقة العمل كصفحة واحدة، كيفية طباعة جميع الأعمدة في ورقة العمل في صفحة واحدة.
---

## **مقدمة**

يتم استخدام إعدادات FitToPagesWide و FitToPagesTall في تطبيقات جداول البيانات (مثل مايكروسوفت إكسل) للتحكم في كيفية تكبير الجدول عند الطباعة. تساعد هذه الإعدادات على ضمان أن المخرجات المطبوعة تتوافق مع عدد معين من الصفحات، أفقياً وعمودياً. إليك شرح لكل إعداد:

1. FitToPagesWide: يحدد هذا الإعداد عدد الصفحات عرضه يجب أن تتناسب مع المخرجات المطبوعة. على سبيل المثال، ضبطه إلى 1 يعني أن المحتوى سيتم تكبيره ليتلاءم مع عرض صفحة واحدة بغض النظر عن عرض الجدول.
1. FitToPagesTall: يحدد هذا الإعداد عدد الصفحات ارتفاعاً يجب أن تتناسب معه المخرجات المطبوعة. على سبيل المثال، ضبطه إلى 1 يعني أن المحتوى سيتم تكبيره ليتناسب مع ارتفاع صفحة واحدة بغض النظر عن عدد الصفوف.

## **لماذا نستخدم FitToPagesWide و FitToPagesTall**
وفيما يلي بعض الأسباب لضبط هذا الإعداد:
1. التحكم في التنسيق المطبوع: من خلال تحديد عدد الصفحات عرضاً وارتفاعاً، يمكنك ضمان أن يكون المستند المطبوع سهل القراءة ومنظم بشكل جيد، دون تقسيم الأعمدة أو الصفوف بشكل غير مناسب عبر الصفحات.
1. الاتساق: إذا كنت تطبع عدة أوراق أو تقارير، فإن استخدام هذه الإعدادات يساعد على الحفاظ على تنسيق موحد، مما يسهل مقارنة وتحليل المستندات المطبوعة.
1. عرض احترافي: يمكن لضبط وتكيف المحتوى بشكل مناسب لعدد صفحات معين أن يؤدي إلى تقديم أكثر احترافية واناقة لبياناتك.

## **كيفية طباعة الملف كصفحات مناسبة عريضة وطويلة في Excel**

لتعيين إعدادات FitToPagesWide و FitToPagesTall في Microsoft Excel، اتبع الخطوات التالية:

1. افتح مصنف Excel الخاص بك وانتقل إلى الورقة التي تريد طباعةها.
1. انتقل إلى علامة التبويب تخطيط الصفحة على الشريط.
1. في مجموعة إعداد الصفحة، انقر على السهم الصغير في الزاوية اليمنى السفلى لفتح مربع حوار إعداد الصفحة.
1. في مربع حوار إعداد الصفحة، انتقل إلى علامة التبويب الصفحة.
1. تحت مقياس الحجم، اختر خيار "توافق" ثم حدد عدد الصفحات عريضة وطويلة التي تريدها: أدخل عدد الصفحات عريضة التي تريدها في المربع الأول (توافق مع x صفحات عريضة). أدخل عدد الصفحات طويلة التي تريدها في المربع الثاني (توافق مع y صفحات طويلة).
<br>
<img src="2.png" width=60% />

1. انقر على موافق لتطبيق الإعدادات.


## **كيفية طباعة Excel كصفحات مناسبة عريضة وطويلة باستخدام Aspose.Cells**

لتعيين FitToPagesWide و FitToPagesTall في ورقة عمل محددة: أولاً، قم بتحميل [ملف العينة](input.xlsx)، ثم يتعين عليك استدعاء طريقتي [**Worksheet.PageSetup.setFitToPagesTall(int value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/#setFitToPagesTall-int-) و [**Worksheet.PageSetup.setFitToPagesWide(int value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/#setFitToPagesWide-int-) للكائن [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/) للورقة المرغوبة. إليك مثال في جافا:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-set-FitToPagesWide-FitToPagesTall.java" >}}

نتيجة الإخراج:
<br>
<img src="1.png" width=60% />

## **كيفية طباعة ورقة عمل كصفحة واحدة باستخدام Aspose.Cells**

لطباعة ورقة عمل كصفحة واحدة: أولاً، قم بتحميل [ملف العينة](sample.xlsx)، ثم يتعين عليك استدعاء طريقة [**PdfSaveOptions.setOnePagePerSheet(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setOnePagePerSheet-boolean-) للكائن [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/). إليك مثال في جافا:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-OnePagePerSheet.java" >}}

نتيجة الإخراج:
<br>
<img src="3.png" width=60% />


## **كيفية طباعة جميع الأعمدة في ورقة العمل في صفحة واحدة باستخدام Aspose.Cells**

لطباعة جميع أعمدة ورقة العمل في صفحة واحدة: أولاً، قم بتحميل [ملف العينة](sample.xlsx)، ثم يتعين عليك استدعاء طريقة [**PdfSaveOptions.setAllColumnsInOnePagePerSheet(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setAllColumnsInOnePagePerSheet-boolean-) للكائن [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/). إليك مثال في جافا:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-AllColumnsInOnePagePerSheet.java" >}}

نتيجة الإخراج:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="java" >}}
