---
title: التحكم في الرسوم البيانية
linktitle: الأشكال في الرسم البياني
type: docs
weight: 60
url: /ar/java/controls-in-charts/
---

{{% alert color="primary" %}}

أحيانًا تحتاج إلى إدراج كائنات الرسم مثل التسميات وصناديق النص والصور وما إلى ذلك في رسم بياني. يمكن لـ Aspose.Cells إضافة عناصر التحكم إلى رسم بياني في وقت التشغيل.

{{% /alert %}}

## **إضافة عنصر تحكم التسمية إلى الرسم البياني.**

توفر التسميات وسيلة لتقديم معلومات للمستخدمين حول محتوى جدول بيانات. تسمح Aspose.Cells لك بإضافة وتلاعب التسميات حتى في الرسوم البيانية.

توفر فئة [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) طريقة تسمى [**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart-int-int-int-int-) لإضافة عنصر تحكم بالتسمية إلى رسم بياني. فيما يلي قائمة بالمعلمات المستخدمة للطريقة:

- الأعلى - الإزاحة الرأسية للتسمية عن الزاوية اليسرى العلوية بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- اليسار - الإزاحة الرأسية للتسمية عن الزاوية اليسرى العلوية بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- الارتفاع - ارتفاع التسمية، بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- **width** – العرض للتسمية، بوحدات 1/4000 من مساحة الرسم البياني.

تُعيد الطريقة كائنًا من فئة [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)، حيث تُمثل الفئة [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) تسمية في الرسم البياني. تحتوي على بعض الأعضاء المهمة كما هو مفصل أدناه:

- تحدد [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text) السمة سلسلة التسمية.
- تحدد السمة [**Fill**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) سمات لون التعبئة.

يوضح المثال التالي كيفية إضافة تسمية إلى الرسم البياني. يستخدم المثال ملف مصمم يحتوي على رسم بياني فيه. نستخدم هذا الملف لإدراج تسمية في الرسم البياني.

أدناه لقطة شاشة للملف المصمم.

**مخطط التصميم**

![todo:image_alt_text](controls-in-charts_1.png)

فيما يلي الرمز الأصلي لإضافة تسمية إلى المخطط. يتم توليد النتائج التالية عند تنفيذ الرمز.

**تمت إضافة تسمية في المخطط**

![todo:image_alt_text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **إضافة عنصر تحكم مربع نص إلى الرسم البياني**

أحد الطرق لتسليط الضوء على معلومات مهمة في تقرير هو استخدام مربع نص. على سبيل المثال ، أدخل نصًا لتسليط الضوء على اسم الشركة أو للإشارة إلى المنطقة الجغرافية ذات أعلى مبيعات. توفر صف الفصل [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) طريقة تسمى [**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart-int-int-int-int-) ، التي تُستخدم لإضافة عنصر تحكم مربع نص إلى رسم بياني. وفيما يلي قائمة المعلمات المستخدمة للطريقة:

- **top** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **left** – الإزاحة الأفقية لمربع النص عن الزاوية العلوية اليسرى بوحدات تعادل 1/4000 من منطقة المخطط.
- **height** - ارتفاع مربع النص ، بوحدات 1/4000 من منطقة الرسم البياني.
- **width** - عرض مربع النص ، بوحدات 1/4000 من منطقة الرسم البياني.

تُرجع الطريقة كائنًا من فئة [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) حيث تمثل الفئة [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) مربع نص في المخطط.

يلخص المثال التالي كيفية إضافة مربع نص إلى مخطط. يستخدم المثال الملف التصميمي السابق الذي يحتوي على مخطط. نحن نستخدم هذا الملف لإدراج مربع نص في المخطط لعرض عنوان المخطط.

فيما يلي الرمز الأصلي لإضافة مربع نص إلى المخطط. يتم توليد النتائج التالية عند تنفيذ الرمز.

**تمت إضافة مربع نص في المخطط**

![todo:image_alt_text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **إضافة صورة إلى الرسم البياني**

تسمح Aspose.Cells لك بإدراج الصور في الرسم البياني. على سبيل المثال ، أضف صورة لتسليط الضوء على الرسم البياني أو محتوياته بمعنى أكبر ، أو قم بإدراج ملف صورة العلامة التجارية.

يوفر صف الفصل [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) طريقة تسمى [**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart-int-int-java.io.InputStream-int-int-) ، والتي تُستخدم لإضافة كائن صورة إلى الرسم البياني. وفيما يلي قائمة المعلمات المستخدمة للطريقة:

- **top** - الإزاحة الرأسية للصورة من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **left** - الإزاحة الرأسية للصورة من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **stream** - كائن تدفق يحتوي على بيانات الصورة.
- **widthScale** - مقياس عرض الصورة ، قيمة نسبية.
- **heightScale** - مقياس ارتفاع الصورة ، قيمة نسبية.

تقوم الطريقة بإرجاع كائن من الفئة [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) حيث تمثل الفئة [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) كائن صورة في الرسم البياني.

المثال التالي يوضح كيفية إضافة صورة إلى الرسم البياني. يستخدم المثال الملف المصمم السابق الذي يحتوي على رسم بياني فيه. نحن نستخدم هذا الملف لإدراج صورة في الرسم البياني.

أدناه هو الكود الأصلي لإضافة صورة إلى الرسم البياني. يتم توليد الناتج التالي عند تنفيذ الكود.

**يتم إدراج صورة في الرسم البياني**

![todo:image_alt_text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **إضافة خانة اختيار في الرسم البياني**

تسمح Aspose.Cells لك بإدراج مربعات اختيار في ورقة الرسم البياني باستخدام تعداد [**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType). يوضح المثال التالي إضافة مربع اختيار إلى ورقة الرسم البياني.

الصورة التالية تظهر ورقة الرسم البياني مع خانة الاختيار في ملف الإخراج.

![todo:image_alt_text](controls-in-charts_5.jpg)

[ملف الناتج](InsertCheckboxInChartSheet_out.xlsx) الذي تم إنشاؤه بواسطة مقتطف الكود التالي مرفق للرجوع إليه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
{{< app/cells/assistant language="java" >}}
