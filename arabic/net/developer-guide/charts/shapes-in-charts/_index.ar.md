---
title: الأشكال في المخططات
type: docs
weight: 70
url: /ar/net/controls-in-charts/
---
{{% alert color="primary" %}}

تحتاج أحيانًا إلى إدراج كائنات رسومية مثل الملصقات ومربعات النص والصور وما إلى ذلك في مخطط. يمكن أن يقوم Aspose.Cells بإضافة عناصر التحكم إلى مخطط في وقت التشغيل.

{{% /alert %}}

## **إضافة عنصر تحكم التسمية إلى التخطيط**

توفر التصنيفات وسيلة لإعطاء معلومات للمستخدمين حول محتوى جدول البيانات.
Aspose.Cells يسمح لك بإضافة ومعالجة التسميات حتى في المخططات.

ال[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart)، تستخدم لإضافة عنصر تحكم تسمية إلى مخطط. فيما يلي قائمة بالمعلمات المستخدمة للطريقة:

- **أعلى** - الإزاحة الرأسية للملصق من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة الرسم البياني.
- **اليسار** - الإزاحة الرأسية للملصق من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة الرسم البياني.
- **ارتفاع** - ارتفاع الملصق بوحدات 1/4000 من منطقة الرسم البياني.
- **العرض** - عرض الملصق بوحدات 1/4000 من مساحة الرسم البياني.

 طريقة إرجاع[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)موضوع. ال[**مُلصَق**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) فئة تمثل تسمية في الرسم البياني. لها بعض الأعضاء المهمين:

- [**نص**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(خاصية) - تحدد سلسلة التسمية التوضيحية.
- [**ملء**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (خاصية) - تحدد سمات لون التعبئة.

يوضح المثال التالي كيفية إضافة تسمية إلى المخطط. يستخدم المثال ملف المصمم (**exp_piechart.xls**) الذي يحتوي على مخطط بداخله. نستخدم هذا الملف لإدراج تسمية في الرسم البياني. يوجد أدناه الرمز الأصلي لإضافة تسمية إلى الرسم البياني. يتم إنشاء الإخراج التالي عند تنفيذ التعليمات البرمجية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

## **إضافة عنصر تحكم مربع نص إلى التخطيط**

 تتمثل إحدى طرق تمييز المعلومات المهمة في التقرير في استخدام مربع نص. على سبيل المثال ، أدخل نصًا لتمييز اسم الشركة أو للإشارة إلى المنطقة الجغرافية التي تحقق أعلى مبيعات. ال[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart)، والذي يستخدم لإضافة عنصر تحكم مربع نص إلى مخطط. فيما يلي قائمة المعلمات المستخدمة للطريقة:

- **أعلى** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة الرسم البياني.
- **اليسار** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة الرسم البياني.
- **ارتفاع** ارتفاع مربع النص بوحدات 1/4000 من مساحة الرسم البياني.
- **العرض** - عرض مربع النص بوحدات 1/4000 من مساحة الرسم البياني.

 طريقة إرجاع[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) موضوع. ال[**مربع الكتابة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)يمثل class مربع نص في الرسم البياني.

يوضح المثال التالي كيفية إضافة مربع نص إلى مخطط. يستخدم المثال ملف المصمم السابق (**exp_piechart.xls**) الذي يحتوي على مخطط بداخله. نستخدم هذا الملف لإدراج مربع نص في المخطط لإظهار عنوان المخطط. يوجد أدناه الرمز الأصلي لإضافة مربع نص إلى المخطط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **إضافة صورة إلى المخطط**

Aspose.Cells يسمح لك بادراج صور في مخطط. على سبيل المثال ، أضف صورة للتأكيد أو لإعطاء معنى أكبر للمخطط أو محتوياته ، أو قم بإدراج ملف صورة العلامة التجارية.

 ال[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) توفر class طريقة تسمى[**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart)، والذي يستخدم لإضافة كائن صورة إلى المخطط. فيما يلي قائمة المعلمات المستخدمة للطريقة:

- **أعلى** الإزاحة الرأسية للصورة من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة الرسم البياني.
- **اليسار** الإزاحة الرأسية للصورة من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة الرسم البياني.
- **مجرى** - كائن تيار يحتوي على بيانات الصورة.
- **العرض** - مقياس عرض الصورة ، قيمة النسبة المئوية.
- **الارتفاع** - مقياس ارتفاع الصورة ، قيمة النسبة المئوية.

 تقوم الطريقة بإرجاع ملف[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) موضوع. ال[**صورة**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)فئة تمثل كائن صورة في الرسم البياني.

يوضح المثال التالي كيفية إضافة صورة إلى المخطط. يستخدم المثال ملف المصمم السابق (**exp_piechart.xls**) الذي يحتوي على مخطط بداخله. نستخدم هذا الملف لإدراج صورة في الرسم البياني. يوجد أدناه الرمز الأصلي لإضافة صورة إلى الرسم البياني.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **إضافة خانة اختيار في الرسم البياني**

 Aspose.Cells يسمح لك بإدراج مربعات الاختيار في ورقة المخطط باستخدام[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) تعداد. يوضح المثال التالي إضافة خانة اختيار إلى ورقة المخطط.

تُظهر الصورة التالية ورقة المخطط مع مربع الاختيار في ملف الإخراج.

![ما يجب القيام به: image_بديل_نص](controls-in-charts_1.jpg)

 ال[ملف إلاخراج](101089316.xlsx)تم إنشاؤه بواسطة مقتطف الشفرة التالي مرفقًا كمرجع لك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **موضوعات مسبقة**
- [أضف علامة WordArt المائية إلى التخطيط](/cells/ar/net/add-wordart-watermark-to-chart/)
