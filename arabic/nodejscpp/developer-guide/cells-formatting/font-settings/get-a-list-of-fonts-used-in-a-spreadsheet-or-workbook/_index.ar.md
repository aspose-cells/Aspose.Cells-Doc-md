---
title: الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل
linktitle: الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل
description: تعلم كيفية الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو دفتر عمل باستخدام Aspose.Cells for Node.js via C++. ستوضح لك هذه المقالة كيفية استرجاع معلومات الخط من مستند.
keywords: Aspose.Cells، Node.js عبر C++، جدول بيانات، دفتر عمل، خط، قائمة
type: docs
weight: 20
url: /ar/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

غالبًا ما يكون من الضروري معرفة الخطوط المستخدمة في ملف العمل الخاص بك لأغراض العرض. عند تحويل ملف العمل إلى PDF أو صورة، فإن Aspose.Cells يتطلب تثبيت جميع الخطوط اللازمة على النظام الخاص بك أو وجودها في **مجلد الخطوط**. إذا كان Aspose.Cells غير قادر على العثور على الخط المطلوب، فإنه يحاول استبداله بخط مناسب آخر متوفر على نظامك أو في مجلد الخطوط الخاص بك ويمكن أن يحل محل الخط الفعلي الخاص بك. هذا لا يسفر فقط عن تصور غير مرغوب فيه لملف الـPDF أو الصور ولكنه يستغرق أيضًا وقت المعالجة للعثور على خطوط مناسبة.

للتعامل مع مثل هذه الحالات، يجب أن تعرف الخطوط المستخدمة في دفتر العمل الخاص بك، ثم إما تثبيت تلك الخطوط على نظامك في حالة بيئة Windows أو وضعها في دليل الخطوط في حالة بيئة Windows أو Linux.

يوفر Aspose.Cells for Node.js via C++ طريقة [**Workbook.getFonts**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFonts--) التي تعيد قائمة بجميع الخطوط المستخدمة في دفتر العمل أو جدول البيانات الخاص بك.

## **الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل**

يحمل الشيفرة النموذجية التالية ملف إكسل المصدر ويسترجع قائمة الخطوط المستخدمة في داخله. يحتوي على ورقة عمل وهمية وقد تمت إضافة بعض الخطوط الوهمية لأغراض توضيحية. عندما تطبع الشيفرة جميع الخطوط داخل الدفتر، فإنها تطبع أيضًا تلك الخطوط الوهمية. تظهر اللقطة الشاشية التالية [ملف إكسل عيني](25395211.xlsx) وكيفية سرد الخطوط الوهمية.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-GetFontsListUsedInWorkbook.js" >}}


## **مخرجات الوحدة**

إليك مخرجات الوحدة النمطية لكود العينة أعلاه عند تشغيله مع [ملف الإكسل العينة المعطى](25395211.xlsx).

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
