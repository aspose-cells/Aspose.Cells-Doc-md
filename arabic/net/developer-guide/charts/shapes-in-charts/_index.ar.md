---
title: الأشكال في الرسوم البيانية
description: تعلم كيفية استخدام Aspose.Cells for .NET لإضافة عناصر التحكم وتخصيص الرسوم البيانية في Microsoft Excel. سيظهر دليلنا كيفية التلاعب بعناصر الرسم البياني وضبط التنسيق وتعزيز المظهر العام وقابلية استخدام الرسوم البيانية الخاصة بك.
keywords: Aspose.Cells for .NET، عناصر التحكم في الرسم البياني، تخصيص الرسم البياني، Microsoft Excel، عناصر الرسم البياني، التنسيق.
type: docs
weight: 70
url: /ar/net/controls-in-charts/
---

{{% alert color="primary" %}}

أحيانًا تحتاج إلى إدراج كائنات الرسم مثل التسميات وصناديق النص والصور وما إلى ذلك في رسم بياني. يمكن لـ Aspose.Cells إضافة عناصر التحكم إلى رسم بياني في وقت التشغيل.

{{% /alert %}}

## **إضافة عنصر تحكم التسمية إلى الرسم البياني.**

توفر التسميات وسيلة لإعطاء معلومات للمستخدمين حول محتوى جدول البيانات.
تتيح لك Aspose.Cells إضافة التسميات والتلاعب بها حتى في الرسوم البيانية.

توفر فئة [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) طريقة تسمى [**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart) تُستخدَم لإضافة عنصر تحكم تسمية إلى رسم بياني. فيما يلي قائمة بالمعلمات المستخدمة للطريقة:

- الأعلى - الإزاحة الرأسية للتسمية عن الزاوية اليسرى العلوية بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- اليسار - الإزاحة الرأسية للتسمية عن الزاوية اليسرى العلوية بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- الارتفاع - ارتفاع التسمية، بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- العرض - عرض التسمية، بوحدات تمثل 1/4000 من منطقة الرسم البياني.

تعيد الطريقة كائن [**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label). فئة [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) تمثل تسمية في الرسم البياني. لديها بعض الأعضاء المهمة.

- [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) (خاصية) - تحدد سلسلة تسمية التسمية.
- [**Fill**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (خاصية) - تحدد سمات لون التعبئة.

المثال التالي يوضح كيفية إضافة تسمية إلى الرسم البياني. يستخدم المثال ملف مصمم (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نستخدم هذا الملف لإدراج تسمية في الرسم البياني. وفيما يلي الشفرة الأصلية لإضافة تسمية إلى الرسم البياني. يتم إنشاء الناتج التالي عند تنفيذ الشفرة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

**ملاحظة:** هذا النوع من عناصر تحكم التسمية مدعوم فقط في ملفات XLS. إذا كنت تريد تأثيرًا مشابهًا في ملف XLSX، يرجى استخدام أحد البدائل التالية:

1. استخدم عنصر تحكم مربع النص بدلاً من ذلك، هناك بديل مماثل لعنصر التسمية في ملفات XLSX.
- [**Example**](https://docs.aspose.com/cells/net/controls-in-charts/#adding-textbox-control-to-the-chart) لدعم مربعات النص، يمكن أن تدعم ملفات XLSX.

2. أضف ورقة عمل يكون نوع الورقة فيها "SheetType.Chart"، ثم أضف رسمًا بيانيًا وعنصر تحكم على هذه الورقة.
- [**Example**](https://docs.aspose.com/cells/net/controls-in-charts/#adding-checkbox-in-the-chart) لإضافة نوع الورقة "SheetType.Chart".

## **إضافة عنصر تحكم مربع نص إلى الرسم البياني**

أحد الطرق لتسليط الضوء على معلومات مهمة في تقرير هو استخدام مربع نص. على سبيل المثال ، أدخل نصًا لتسليط الضوء على اسم الشركة أو للإشارة إلى المنطقة الجغرافية ذات أعلى مبيعات. توفر صف الفصل [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) طريقة تسمى [**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart) ، التي تُستخدم لإضافة عنصر تحكم مربع نص إلى رسم بياني. وفيما يلي قائمة المعلمات المستخدمة للطريقة:

- **top** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **left** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **height** - ارتفاع مربع النص ، بوحدات 1/4000 من منطقة الرسم البياني.
- **width** - عرض مربع النص ، بوحدات 1/4000 من منطقة الرسم البياني.

تُرجع الطريقة كائنًا [**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox). صف الفصل [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) يمثل عنصر تحكم مربع نص في الرسم البياني.

المثال التالي يوضح كيفية إضافة مربع نص إلى رسم بياني. يستخدم المثال الملف المصمم السابق (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نستخدم هذا الملف لإدراج مربع نص في الرسم البياني لعرض عنوان الرسم البياني. يتم إنشاء الشفرة الأصلية لإضافة مربع نص إلى الرسم البياني أدناه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **إضافة صورة إلى الرسم البياني**

تسمح Aspose.Cells لك بإدراج الصور في الرسم البياني. على سبيل المثال ، أضف صورة لتسليط الضوء على الرسم البياني أو محتوياته بمعنى أكبر ، أو قم بإدراج ملف صورة العلامة التجارية.

يوفر صف الفصل [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) طريقة تسمى [**AddPictureInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart) ، والتي تُستخدم لإضافة كائن صورة إلى الرسم البياني. وفيما يلي قائمة المعلمات المستخدمة للطريقة:

- **top** - الإزاحة الرأسية للصورة من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **left** - الإزاحة الرأسية للصورة من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **stream** - كائن تدفق يحتوي على بيانات الصورة.
- **widthScale** - مقياس عرض الصورة ، قيمة نسبية.
- **heightScale** - مقياس ارتفاع الصورة ، قيمة نسبية.

تُرجع الطريقة كائنًا [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). صف الفصل [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) يمثل كائن صورة في الرسم البياني.

المثال التالي يوضح كيفية إضافة صورة إلى الرسم البياني. يستخدم المثال الملف التصميمي السابق (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نحن نستخدم هذا الملف لإدراج صورة في الرسم البياني. أدناه هو الكود الأصلي لإضافة صورة إلى الرسم البياني.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **إضافة خانة اختيار في الرسم البياني**

تسمح Aspose.Cells بإدراج خانات الاختيار في ورقة الرسم البياني باستخدام تعداد [**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype). يوضح المثال التالي إضافة خانة اختيار إلى ورقة الرسم البياني.

الصورة التالية تظهر ورقة الرسم البياني مع خانة الاختيار في ملف الإخراج.

![todo:image_alt_text](controls-in-charts_1.jpg)

الملف الناتج (101089316.xlsx) الذي تم إنشاؤه بواسطة مقتطف الكود التالي مرفق للرجوع إليه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **مواضيع متقدمة**
- [إضافة علامة مائية WordArt إلى الرسم البياني](/cells/ar/net/add-wordart-watermark-to-chart/)
{{< app/cells/assistant language="csharp" >}}
