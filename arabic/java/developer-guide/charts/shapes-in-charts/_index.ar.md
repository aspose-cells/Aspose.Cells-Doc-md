---
title: الضوابط في الرسوم البيانية
linktitle: الأشكال في الرسم البياني
type: docs
weight: 60
url: /ar/java/controls-in-charts/
---
{{% alert color="primary" %}}

تحتاج أحيانًا إلى إدراج كائنات رسومية مثل الملصقات ومربعات النص والصور وما إلى ذلك في مخطط. يمكن أن يقوم Aspose.Cells بإضافة عناصر التحكم إلى مخطط في وقت التشغيل.

{{% /alert %}}

## **إضافة عنصر تحكم التسمية إلى التخطيط**

توفر التصنيفات وسيلة لإعطاء معلومات للمستخدمين حول محتوى جدول البيانات. Aspose.Cells يسمح لك بإضافة ومعالجة التسميات حتى في المخططات.

 ال[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) توفر class طريقة تسمى[**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)) ، تُستخدم لإضافة عنصر تحكم تسمية إلى مخطط. فيما يلي قائمة بالمعلمات المستخدمة للطريقة:

- **أعلى** - الإزاحة الرأسية للملصق من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة الرسم البياني.
- **اليسار** - الإزاحة الرأسية للملصق من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة الرسم البياني.
- **ارتفاع** - ارتفاع الملصق بوحدات 1/4000 من منطقة الرسم البياني.
- **العرض** - عرض الملصق بوحدات 1/4000 من مساحة الرسم البياني.

 تقوم الطريقة بإرجاع كائن من[**مُلصَق**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) الطبقة ، حيث[**مُلصَق**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)فئة تمثل تسمية في الرسم البياني. لديها بعض الأعضاء المهمين كما هو مفصل أدناه:

- [**نص**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text)تحدد الخاصية سلسلة التسمية التوضيحية الخاصة بالتسمية.
- [**ملء**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) تحدد الخاصية سمات لون التعبئة.

يوضح المثال التالي كيفية إضافة تسمية إلى المخطط. يستخدم المثال ملف مصمم يحتوي على مخطط بداخله. نستخدم هذا الملف لإدراج تسمية في الرسم البياني.

يوجد أدناه لقطة شاشة لملف المصمم.

**مخطط المصمم**

![ما يجب القيام به: image_بديل_نص](controls-in-charts_1.png)

يوجد أدناه الرمز الأصلي لإضافة تسمية إلى الرسم البياني. يتم إنشاء الإخراج التالي عند تنفيذ التعليمات البرمجية.

**تمت إضافة تسمية في الرسم البياني**

![ما يجب القيام به: image_بديل_نص](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **إضافة عنصر تحكم مربع نص إلى التخطيط**

 تتمثل إحدى طرق تمييز المعلومات المهمة في التقرير في استخدام مربع نص. على سبيل المثال ، أدخل نصًا لتمييز اسم الشركة أو للإشارة إلى المنطقة الجغرافية التي تحقق أعلى مبيعات. ال[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) توفر class طريقة تسمى[**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)) ، والتي تُستخدم لإضافة عنصر تحكم مربع نص إلى مخطط. فيما يلي قائمة المعلمات المستخدمة للطريقة:

- **أعلى** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة الرسم البياني.
- **اليسار** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة الرسم البياني.
- **ارتفاع** ارتفاع مربع النص بوحدات 1/4000 من مساحة الرسم البياني.
- **العرض** - عرض مربع النص بوحدات 1/4000 من مساحة الرسم البياني.

 تقوم الطريقة بإرجاع كائن من[**مربع الكتابة**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) فئة حيث[**مربع الكتابة**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)يمثل class مربع نص في الرسم البياني.

يوضح المثال التالي كيفية إضافة مربع نص إلى مخطط. يستخدم المثال ملف المصمم السابق الذي يحتوي على مخطط بداخله. نستخدم هذا الملف لإدراج مربع نص في المخطط لإظهار عنوان المخطط.

يوجد أدناه الرمز الأصلي لإضافة مربع نص إلى المخطط. يتم إنشاء الإخراج التالي عند تنفيذ التعليمات البرمجية.

**تمت إضافة مربع نص في الرسم البياني**

![ما يجب القيام به: image_بديل_نص](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **إضافة صورة إلى المخطط**

Aspose.Cells يسمح لك بادراج صور في مخطط. على سبيل المثال ، أضف صورة للتأكيد أو لإعطاء معنى أكبر للمخطط أو محتوياته ، أو قم بإدراج ملف صورة العلامة التجارية.

 ال[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) توفر class طريقة تسمى[**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)) ، والذي يستخدم لإضافة كائن صورة إلى المخطط. فيما يلي قائمة المعلمات المستخدمة للطريقة:

- **أعلى** الإزاحة الرأسية للصورة من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة الرسم البياني.
- **اليسار** الإزاحة الرأسية للصورة من الزاوية اليسرى العليا بوحدات 1/4000 من منطقة الرسم البياني.
- **مجرى** - كائن تيار يحتوي على بيانات الصورة.
- **العرض** - مقياس عرض الصورة ، قيمة النسبة المئوية.
- **الارتفاع** - مقياس ارتفاع الصورة ، قيمة النسبة المئوية.

 تقوم الطريقة بإرجاع كائن من[**صورة**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) فئة حيث[**صورة**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)فئة تمثل كائن صورة في الرسم البياني.

يوضح المثال التالي كيفية إضافة صورة إلى المخطط. يستخدم المثال ملف المصمم السابق الذي يحتوي على مخطط بداخله. نستخدم هذا الملف لإدراج صورة في الرسم البياني.

يوجد أدناه الرمز الأصلي لإضافة صورة إلى المخطط. يتم إنشاء الإخراج التالي عند تنفيذ التعليمات البرمجية

**يتم ادراج صوره في المخطط**

![ما يجب القيام به: image_بديل_نص](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **إضافة خانة اختيار في الرسم البياني**

Aspose.Cells يسمح لك بإدراج مربعات الاختيار في ورقة المخطط باستخدام[**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType) تعداد. يوضح المثال التالي إضافة خانة اختيار إلى ورقة المخطط.

تُظهر الصورة التالية ورقة المخطط مع مربع الاختيار في ملف الإخراج.

![ما يجب القيام به: image_بديل_نص](controls-in-charts_5.jpg)

ال[ملف إلاخراج](InsertCheckboxInChartSheet_out.xlsx)تم إنشاؤه بواسطة مقتطف الشفرة التالي مرفقًا كمرجع لك.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
