---
title: الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل
type: docs
weight: 20
url: /ar/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

غالبًا ما يكون من الضروري معرفة الخطوط المستخدمة في جدول العمل الخاص بك لأغراض التقديم. عند تحويل جدول العمل الخاص بك إلى PDF أو صورة، يتطلب Aspose.Cells أن تكون جميع الخطوط اللازمة مثبتة على نظامك أو موجودة في دليل الخطوط الخاص بك. إذا كان Aspose.Cells غير قادرًا على العثور على الخط المطلوب، فيحاول استبداله بخط آخر مناسب موجود على نظامك أو في دليل الخطوط الخاص بك ويمكن أن يحل محل الخط الفعلي الخاص بك. يؤدي ذلك ليس فقط إلى تقديم غير مرغوب فيه لملف PDF أو الصور ولكن أيضا يستغرق وقت المعالجة في العثور على الخطوط المناسبة.

للتعامل مع مثل هذه الحالات، يجب عليك معرفة الخطوط التي تستخدمها في جدول عملك، ثم إما تثبيت تلك الخطوط على نظامك في حالة بيئة Windows أو وضعها في دليل الخطوط الخاص بك في حالة بيئة Windows أو Linux.

يوفر Aspose.Cells طريقة [Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts--) التي تُرجع قائمة جميع الخطوط المستخدمة في جدول العمل أو جدول البيانات الخاص بك.

## **الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل**

يحمل الكود العيني التالي ملف إكسل المصدر ويسترجع قائمة الخطوط المستخدمة بداخله. تحتوي ورقة العمل الوهمية على بعض الخطوط الوهمية المضافة لأغراض التوضيح. عندما يقوم الكود بطباعة جميع الخطوط داخل جدول العمل، فإنه يطبع أيضًا تلك الخطوط الوهمية. تظهر اللقطة الشاشة التالية [ملف الإكسل العيني](sampleGetFonts.xlsx) وكيف يتم سرد الخطوط الوهمية.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **مخرجات الوحدة**

هنا مخرجات وحدة التحكم لرمز العينة أعلاه عند تنفيذ الملف النموذجي المعطى

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

{{< /highlight >}}
