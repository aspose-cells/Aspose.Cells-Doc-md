---
title: الأشكال في المخططات
description: تعرف على كيفية استخدام Aspose.Cells for .NET لإضافة عناصر التحكم وتخصيص المخططات في Microsoft Excel. سيوضح دليلنا كيفية التعامل مع عناصر المخطط، وضبط التنسيق، وتحسين المظهر العام وسهولة استخدام المخططات الخاصة بك.
keywords: Aspose.Cells for .NET, Chart Controls, Chart Customization, Microsoft Excel, Chart Elements, Formatting.
type: docs
weight: 70
url: /ar/net/controls-in-charts/
---
{{% alert color="primary" %}}

في بعض الأحيان تحتاج إلى إدراج كائنات رسومية مثل التسميات ومربعات النص والصور وما إلى ذلك في المخطط. Aspose.Cells يمكنه إضافة عناصر التحكم إلى المخطط في وقت التشغيل.

{{% /alert %}}

##  **إضافة التحكم في التسمية إلى المخطط**

توفر التصنيفات وسيلة لإعطاء معلومات للمستخدمين حول محتوى جدول البيانات.
Aspose.Cells يسمح لك بإضافة ومعالجة التسميات حتى في المخططات.

ال[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) يوفر الفصل طريقة تسمى[**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart)، يستخدم لإضافة عنصر تحكم التسمية إلى المخطط. فيما يلي قائمة بالمعلمات المستخدمة للطريقة:

- **قمة** الإزاحة الرأسية للملصق من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة المخطط.
- **غادر** الإزاحة الرأسية للملصق من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة المخطط.
- **ارتفاع** - ارتفاع الملصق بوحدات 1/4000 من مساحة المخطط.
- **عرض** – عرض الملصق بوحدات 1/4000 من مساحة المخطط.

 تعود الطريقة[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)هدف. ال[**ملصق**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) تمثل الفئة تسمية في المخطط. ويضم بعض الأعضاء المهمين:

- [**نص**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(خاصية) - تحدد سلسلة التسمية التوضيحية.
- [**يملأ**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (خاصية) - تحدد سمات لون التعبئة.

يوضح المثال التالي كيفية إضافة تسمية إلى المخطط. يستخدم المثال ملف مصمم (**exp_piechart.xls**) يحتوي على مخطط. نستخدم هذا الملف لإدراج تسمية في المخطط. يوجد أدناه الكود الأصلي لإضافة تسمية إلى المخطط. يتم إنشاء الإخراج التالي عند تنفيذ التعليمات البرمجية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

##  **إضافة عنصر تحكم TextBox إلى المخطط**

إحدى الطرق لتمييز المعلومات المهمة في التقرير هي استخدام مربع نص. على سبيل المثال، أدخل نصًا لتمييز اسم الشركة أو للإشارة إلى المنطقة الجغرافية ذات أعلى المبيعات. ال[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) يوفر الفصل طريقة تسمى[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart)، والذي يُستخدم لإضافة عنصر تحكم مربع نص إلى المخطط. فيما يلي قائمة المعلمات المستخدمة للطريقة:

- **قمة** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة المخطط.
- **غادر** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة المخطط.
- **ارتفاع** – ارتفاع مربع النص بوحدات 1/4000 من مساحة المخطط.
- **عرض** – عرض مربع النص بوحدات 1/4000 من منطقة المخطط.

 تعود الطريقة[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) هدف. ال[**مربع الكتابة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)يمثل class مربع نص في المخطط.

يوضح المثال التالي كيفية إضافة مربع نص إلى مخطط. يستخدم المثال ملف المصمم السابق (**exp_piechart.xls**) الذي يحتوي على مخطط. نستخدم هذا الملف لإدراج مربع نص في المخطط لإظهار عنوان المخطط. يوجد أدناه الكود الأصلي لإضافة مربع نص إلى المخطط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

##  **إضافة صورة إلى المخطط**

Aspose.Cells يسمح لك بإدراج الصور في المخطط. على سبيل المثال، قم بإضافة صورة للتأكيد على المخطط أو محتوياته أو إعطائها معنى أكبر، أو قم بإدراج ملف صورة العلامة التجارية.

 ال[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) يوفر الفصل طريقة تسمى[**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart)، والذي يُستخدم لإضافة كائن صورة إلى المخطط. فيما يلي قائمة المعلمات المستخدمة للطريقة:

- **قمة** – الإزاحة الرأسية للصورة من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة المخطط.
- **غادر** – الإزاحة الرأسية للصورة من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة المخطط.
- **تدفق** - كائن دفق يحتوي على بيانات الصورة.
- **widthScale** - مقياس عرض الصورة، قيمة النسبة المئوية.
- **heightScale** - مقياس ارتفاع الصورة، قيمة النسبة المئوية.

 ترجع الطريقة ملف[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) هدف. ال[**صورة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)تمثل الفئة كائن صورة في المخطط.

يوضح المثال التالي كيفية إضافة صورة إلى المخطط. يستخدم المثال ملف المصمم السابق (**exp_piechart.xls**) الذي يحتوي على مخطط. نستخدم هذا الملف لإدراج صورة في المخطط. يوجد أدناه الكود الأصلي لإضافة صورة إلى المخطط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

##  **إضافة مربع اختيار في المخطط**

 Aspose.Cells يسمح لك بإدراج مربعات الاختيار في ورقة الرسم البياني باستخدام[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) تعداد. يوضح المثال التالي إضافة خانة اختيار إلى ورقة التخطيط.

تُظهر الصورة التالية ورقة المخطط مع خانة الاختيار في ملف الإخراج.

![ما يجب القيام به:image_alt_text](controls-in-charts_1.jpg)

 ال[ملف إلاخراج](101089316.xlsx) تم إرفاق مقتطف الشفرة التالي للرجوع إليه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

##  **مواضيع متقدمة**
- [أضف علامة مائية WordArt إلى المخطط](/cells/ar/net/add-wordart-watermark-to-chart/)
