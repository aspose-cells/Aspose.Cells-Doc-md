---
title: احصل على قائمة الخطوط المستخدمة في جدول بيانات أو مصنف مع Golang عبر C++
linktitle: الحصول على قائمة الخطوط
description: Aspose.Cells هي مكتبة C++ للعمل مع ملفات جداول البيانات، وتدعم الحصول على قائمة الخطوط المستخدمة في جدول البيانات أو دفتر العمل، مما يتيح للمستخدمين معرفة معلومات الخطوط المستخدمة في المستند. يوضح هذا المقال كيفية استخدام مكتبة Aspose.Cells للحصول على قائمة الخطوط.
keywords: Aspose.Cells، جدول بيانات، دفتر عمل، خط، قائمة
type: docs
weight: 20
url: /ar/go-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

غالبًا ما يكون من الضروري معرفة الخطوط المستخدمة في ملف العمل الخاص بك لأغراض العرض. عند تحويل ملف العمل إلى PDF أو صورة، فإن Aspose.Cells يتطلب تثبيت جميع الخطوط اللازمة على النظام الخاص بك أو وجودها في **مجلد الخطوط**. إذا كان Aspose.Cells غير قادر على العثور على الخط المطلوب، فإنه يحاول استبداله بخط مناسب آخر متوفر على نظامك أو في مجلد الخطوط الخاص بك ويمكن أن يحل محل الخط الفعلي الخاص بك. هذا لا يسفر فقط عن تصور غير مرغوب فيه لملف الـPDF أو الصور ولكنه يستغرق أيضًا وقت المعالجة للعثور على خطوط مناسبة.

من أجل التعامل مع مثل هذه الحالات، يجب أن تعرف ما هي الخطوط التي يتم استخدامها في ملف العمل الخاص بك، ثم إما تثبيت تلك الخطوط على النظام الخاص بك في حالة بيئة Windows أو وضعها في مجلد الخطوط الخاص بك في حالة ويندوز أو بيئة لينكس.

يوفر Aspose.Cells الطريقة [**Workbook.GetFonts**](https://reference.aspose.com/cells/go-cpp/workbook/getfonts/) التي تُرجع قائمة بجميع الخطوط المستخدمة في مصفوفة العمل أو الجدول الخاص بك.

## **الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل**

يحمل الشيفرة النموذجية التالية ملف إكسل المصدر ويسترجع قائمة الخطوط المستخدمة في داخله. يحتوي على ورقة عمل وهمية وقد تمت إضافة بعض الخطوط الوهمية لأغراض توضيحية. عندما تطبع الشيفرة جميع الخطوط داخل الدفتر، فإنها تطبع أيضًا تلك الخطوط الوهمية. تظهر اللقطة الشاشية التالية [ملف إكسل عيني](25395211.xlsx) وكيفية سرد الخطوط الوهمية.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAListOfFontsUsedInASpreadsheetOrWorkbook.go" >}}
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
