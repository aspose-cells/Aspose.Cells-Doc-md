---
title: إعدادات التعبئة
description: Aspose.Cells مكتبة بايثون للعمل مع ملفات الجدول. يدعم تعيين إعدادات التعبئة للخلايا، مما يتيح للمستخدمين تخصيص خلفية ونمط الخلايا. ستقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لبايثون via .NET لضبط إعدادات تعبئة الخلايا.
keywords: مكتبة Aspose.Cells لبايثون via .NET، خلايا، إعدادات التعبئة، الخلفية، النمط
type: docs
weight: 50
url: /ar/python-net/cells-fill-settings/
---

## **الألوان وأنماط الخلفية**

يمكن لبرنامج Microsoft Excel تعيين ألوان الأمام (الإطار) والخلفية (تعبئة) للخلايا وأنماط الخلفية.

يدعم Aspose.Cells لبايثون via .NET أيضًا هذه الميزات بطريقة مرنة. في هذا الموضوع، نتعلم كيف نستخدم هذه الميزات باستخدام Aspose.Cells.

### **تعيين الألوان وأنماط الخلفية**

يوفر Aspose.Cells لبايثون via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) يمثل كائن من فئة [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

تحتوي [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) على طريقتي [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) و [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) التي تُستخدم للحصول على وتعيين تنسيق الخلية. توفر فئة [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) خصائص لضبط ألوان المقدمة والخلفية للخلايا. تقدم Aspose.Cells for Python via .NET تعدادًا [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) يحتوي على مجموعة من الأنماط الخلفية المعرفة مسبقًا والتي سيتم توضيحها أدناه.

|**أنماط الخلفية**|**الوصف**|
| :- | :- |
|DIAGONAL_CROSSHATCH| يمثل نمط متقاطع قطري|
|DIAGONAL_STRIPE| يمثل نمط شريط مائل قطري|
|GRAY6| يمثل نمط رمادي بنسبة 6.25%|
|GRAY12| يمثل نمط رمادي بنسبة 12.5%|
|GRAY25| يمثل نمط رمادي بنسبة 25%|
|GRAY50| يمثل نمط رمادي بنسبة 50%|
|GRAY75| يمثل نمط رمادي بنسبة 75%|
|HORIZONTAL_STRIPE| يمثل نمط شريط أفقي|
|NONE| لا يمثل خلفية|
|REVERSE_DIAGONAL_STRIPE| يمثل نمط شريط قطري عكسي|
|SOLID| يمثل نمط صلب|
|THICK_DIAGONAL_CROSSHATCH| يمثل نمط متقاطع قطري بسماكة عالية|
|THIN_DIAGONAL_CROSSHATCH| يمثل نمط متقاطع قطري رقيق|
|THIN_DIAGONAL_STRIPE| يمثل نمط شريط قطري رقيق|
|THIN_HORIZONTAL_CROSSHATCH| يمثل نمط متقاطع أفقي رقيق|
|THIN_HORIZONTAL_STRIPE| يمثل نمط شريط أفقي رقيق|
|THIN_REVERSE_DIAGONAL_STRIPE| يمثل نمط شريط قطري عكسي رقيق|
|THIN_VERTICAL_STRIPE| يمثل نمط شريط عمودي رقيق|
|VERTICAL_STRIPE| يمثل نمط شريط عمودي|

في المثال أدناه ، تم تعيين لون الخلفية للخلية A1 ولكن تم تكوين A2 ليكون لها كل من لون الخلفية والأمامية مع نمط خلفية خط عمودي.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndBackground-1.py" >}}

### **مهم معرفته**

{{% alert color="primary" %}}

- لتعيين لون الخلفية أو اللون الأمامي لخلية ما، استخدم خصائص [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) أو [**background_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_color) لكائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). سوف تؤثر كلا الخصائص فقط إذا تم تكوين خصية [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) لكائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style).
- تعيين الظل للخلية تحدد خاصية [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) لون الخلية.
  تحدد الخاصية [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) نوع النمط الخلفي المستخدم لللون الأمامي أو الخلفي. تقدم Aspose.Cells for Python via .NET تعدادًا [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) يحتوي على مجموعة من أنواع الأنماط الخلفية المعرفة مسبقًا.
- إذا قمت بتحديد قيمة *BackgroundType.None* من تعداد [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype)، لن يتم تطبيق اللون الأمامي.
  بالمثل، لن يتم تطبيق اللون الخلفي إذا قمت باختيار القيم *BackgroundType.None* أو *BackgroundType.Solid*.
- عند استرجاع لون السطوع/التعبئة للخلية، إذا كان [**Style.pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) يساوي *BackgroundType.None*، سيقوم [**Style.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) بإرجاع *Color.Empty*.

{{% /alert %}}

### **تطبيق تأثيرات تعبئة التدرج**

لتطبيق تأثيرات تعبئة التدرج المرغوبة على الخلية، استخدم الطريقة [**set_two_color_gradient**](https://reference.aspose.com/cells/python-net/aspose.cells/style/set_two_color_gradient) لكائن [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) وفقًا لذلك.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyingGradientFillEffects-1.py" >}}

## **الألوان واللوحة**

اللوحة هي عدد الألوان المتاحة للاستخدام في إنشاء صورة. يتيح استخدام لوحة معيارية في العرض للمستخدم إنشاء مظهر متسق. كل ملف من ملفات Microsoft Excel (97-2003) لديه لوحة تتكون من 56 لون يمكن تطبيقها على الخلايا، الخطوط، الخطوط الشبكية، الكائنات الرسومية، التعبئات والخطوط في الرسم البياني.

مع Aspose.Cells for Python via .NET لا يقتصر الأمر على استخدام ألوان اللوحة الحالية ولكن أيضًا يمكن استخدام الألوان المخصصة. قبل استخدام لون مخصص، أضفه إلى اللوحة أولاً.

يناقش هذا الموضوع كيفية إضافة ألوان مخصصة إلى اللوحة.

### **إضافة ألوان مخصصة إلى اللوحة**

يدعم Aspose.Cells for Python via .NET لوحة ألوان مايكروسوفت إكسل التي تتألف من 56 لونًا. لاستخدام لون مخصص غير معرف في اللوحة، أضف اللون إلى اللوحة.

توفر Aspose.Cells for Python via .NET فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، التي تمثل ملف إكسل من مايكروسوفت. توفر الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) طريقة [**change_palette**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/change_palette) التي تتطلب المعلمات التالية لإضافة لون مخصص لتعديل اللوحة:

- لون مخصص، اللون المخصص الذي سيتم إضافته.
- الفهرس، فهرس اللون في اللوحة الذي سيحل محل اللون المخصص. يجب أن يكون بين 0-55.

المثال أدناه يضيف لون مخصص (Orchid) إلى اللوحة قبل تطبيقه على خط النص.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ColorsAndPalette-1.py" >}}

{{% alert color="primary" %}}

تحتوي اللوحة فقط على 56 لونًا. عندما تقوم بإضافة لون مخصص إلى اللوحة، يتم تغيير اللوحة ويتم تغيير أي عنصر في الملف المنسق باللون السابق. لذا، عند تغيير اللوحة، يرجى أن تكون حذرًا جدًا. علاوة على ذلك، هذه هي القيود في تنسيق ملف XLS (Excel 97 - 2003) فقط حيث لا يوجد مثل هذا القيد لتنسيق ملف XLSX أو لأنساق ملفات Microsoft Excel (2007/2010 أو 2013) المتقدمة.

{{% /alert %}}

