---
title: الأشكال في الرسوم البيانية
description: تعلم كيفية استخدام Aspose.Cells للبايثون via .NET لإضافة عناصر تحكم وتخصيص المخططات في Microsoft Excel. سيرينا دليلنا كيفية التلاعب بعناصر الرسم، ضبط التنسيق، وتحسين المظهر العام وقابلية الاستخدام لرسومك البيانية.
keywords: Aspose.Cells للبايثون via .NET، عناصر تحكم الرسم، تخصيص المخططات، Microsoft Excel، عناصر الرسم، التنسيق.
type: docs
weight: 70
url: /ar/python-net/controls-in-charts/
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى إدراج كائنات رسومية مثل تسميات، مربعات نص، صور وغيرها في رسم بياني. يمكن لـ Aspose.Cells للبايثون via .NET إضافة العناصر إلى الرسم البياني في وقت التشغيل.

{{% /alert %}}

## **إضافة عنصر تحكم التسمية إلى الرسم البياني.**

توفر التسميات وسيلة لإعطاء معلومات للمستخدمين حول محتوى جدول البيانات.
يسمح Aspose.Cells للبايثون via .NET لك بإضافة وتلاعب بالتسميات حتى داخل الرسوم البيانية.

توفر فئة [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) طريقة تسمى [**add_label_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label_in_chart) تُستخدَم لإضافة عنصر تحكم تسمية إلى رسم بياني. فيما يلي قائمة بالمعلمات المستخدمة للطريقة:

- الأعلى - الإزاحة الرأسية للتسمية عن الزاوية اليسرى العلوية بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- اليسار - الإزاحة الرأسية للتسمية عن الزاوية اليسرى العلوية بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- الارتفاع - ارتفاع التسمية، بوحدات تمثل 1/4000 من منطقة الرسم البياني.
- العرض - عرض التسمية، بوحدات تمثل 1/4000 من منطقة الرسم البياني.

تعيد الطريقة كائن [**aspose.cells.drawing.Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label). فئة [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) تمثل تسمية في الرسم البياني. لديها بعض الأعضاء المهمة.

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) (خاصية) - تحدد سلسلة تسمية التسمية.
- [**fill**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill) (خاصية) - تحدد سمات لون التعبئة.

المثال التالي يوضح كيفية إضافة تسمية إلى الرسم البياني. يستخدم المثال ملف مصمم (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نستخدم هذا الملف لإدراج تسمية في الرسم البياني. وفيما يلي الشفرة الأصلية لإضافة تسمية إلى الرسم البياني. يتم إنشاء الناتج التالي عند تنفيذ الشفرة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingLabelControl-1.py" >}}

## **إضافة عنصر تحكم مربع نص إلى الرسم البياني**

أحد الطرق لتسليط الضوء على معلومات مهمة في تقرير هو استخدام مربع نص. على سبيل المثال ، أدخل نصًا لتسليط الضوء على اسم الشركة أو للإشارة إلى المنطقة الجغرافية ذات أعلى مبيعات. توفر صف الفصل [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) طريقة تسمى [**add_text_box_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_text_box_in_chart) ، التي تُستخدم لإضافة عنصر تحكم مربع نص إلى رسم بياني. وفيما يلي قائمة المعلمات المستخدمة للطريقة:

- **top** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **left** - الإزاحة الرأسية لمربع النص من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **height** - ارتفاع مربع النص ، بوحدات 1/4000 من منطقة الرسم البياني.
- **width** - عرض مربع النص ، بوحدات 1/4000 من منطقة الرسم البياني.

تُرجع الطريقة كائنًا [**aspose.cells.drawing.TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox). صف الفصل [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) يمثل عنصر تحكم مربع نص في الرسم البياني.

المثال التالي يوضح كيفية إضافة مربع نص إلى رسم بياني. يستخدم المثال الملف المصمم السابق (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نستخدم هذا الملف لإدراج مربع نص في الرسم البياني لعرض عنوان الرسم البياني. يتم إنشاء الشفرة الأصلية لإضافة مربع نص إلى الرسم البياني أدناه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.py" >}}

## **إضافة صورة إلى الرسم البياني**

يتيح Aspose.Cells for Python via .NET إدراج الصور في مخطط. على سبيل المثال، أضف صورة لتأكيد أو إعطاء مزيد من المعنى لمخطط أو محتوياته، أو أدخل ملف صورة علامة تجارية.

يوفر صف الفصل [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) طريقة تسمى [**add_picture_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture_in_chart) ، والتي تُستخدم لإضافة كائن صورة إلى الرسم البياني. وفيما يلي قائمة المعلمات المستخدمة للطريقة:

- **top** - الإزاحة الرأسية للصورة من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **left** - الإزاحة الرأسية للصورة من الزاوية اليسرى العلوية بوحدات 1/4000 من منطقة الرسم البياني.
- **stream** - كائن تدفق يحتوي على بيانات الصورة.
- **widthScale** - مقياس عرض الصورة ، قيمة نسبية.
- **heightScale** - مقياس ارتفاع الصورة ، قيمة نسبية.

تُرجع الطريقة كائنًا [**aspose.cells.drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). صف الفصل [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) يمثل كائن صورة في الرسم البياني.

المثال التالي يوضح كيفية إضافة صورة إلى الرسم البياني. يستخدم المثال الملف التصميمي السابق (**exp_piechart.xls**) الذي يحتوي على رسم بياني فيه. نحن نستخدم هذا الملف لإدراج صورة في الرسم البياني. أدناه هو الكود الأصلي لإضافة صورة إلى الرسم البياني.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingPictureToChart-1.py" >}}

## **إضافة خانة اختيار في الرسم البياني**

يتيح Aspose.Cells for Python via .NET إدراج مربعات اختيار في ورقة المخطط باستخدام [**MsoDrawingType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msodrawingtype) enumeration. يُظهر المثال التالي إضافة مربع اختيار إلى ورقة مخطط.

الصورة التالية تظهر ورقة الرسم البياني مع خانة الاختيار في ملف الإخراج.

![todo:image_alt_text](controls-in-charts_1.jpg)

الملف الناتج (101089316.xlsx) الذي تم إنشاؤه بواسطة مقتطف الكود التالي مرفق للرجوع إليه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.py" >}}

## **مواضيع متقدمة**
- [إضافة علامة مائية WordArt إلى الرسم البياني](/cells/ar/python-net/add-wordart-watermark-to-chart/)
