---
title: إعدادات التعبئة
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جدول بيانات. تدعم ضبط إعدادات التعبئة للخلايا، مما يسمح للمستخدمين بتخصيص الخلفية والنمط للخلايا. تقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لضبط إعدادات تعبئة الخلية.
keywords: Aspose.Cells، خلايا، إعدادات التعبئة، خلفية، نمط
type: docs
weight: 50
url: /ar/net/cells-fill-settings/
---

## **الألوان وأنماط الخلفية**

يمكن لبرنامج Microsoft Excel تعيين ألوان الأمام (الإطار) والخلفية (تعبئة) للخلايا وأنماط الخلفية.

تدعم Aspose.Cells أيضًا هذه الميزات بطريقة مرنة. في هذا الموضوع، نتعلم كيفية استخدام هذه الميزات باستخدام Aspose.Cells.

### **تعيين الألوان وأنماط الخلفية**

توفر أسبوس.خلايات فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) يُمثل كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) لديها [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) و [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) الأساليب التي تستخدم للحصول وتعيين تنسيق الخلية. يوفر فئة [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) خصائص لضبط لوني النص الأمامي والخلفية للخلايا. توفر Aspose.Cells تعدادًا [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype) يحتوي على مجموعة من أنواع أنماط الخلفية المحددة مسبقًا كما هو موضح أدناه.

|**أنماط الخلفية**|**الوصف**|
| :- | :- |
|DiagonalCrosshatch|تمثل نمط شفة الصليب المائل|
|DiagonalStripe| يمثل نمط خط مائل |
|Gray6| يمثل نمط رمادي بنسبة 6.25٪ |
|Gray12| يمثل نمط رمادي بنسبة 12.5٪ |
|Gray25| يمثل نمط رمادي بنسبة 25٪ |
|Gray50| يمثل نمط رمادي بنسبة 50٪ |
|Gray75| يمثل نمط رمادي بنسبة 75٪ |
|HorizontalStripe| يمثل نمط خط أفقي |
|None| يمثل عدم وجود خلفية |
|ReverseDiagonalStripe| يمثل نمط خط مائل عكسي |
|Solid| يمثل نمط صلب |
|ThickDiagonalCrosshatch| يمثل نمط علامة تقاطع مائلة سميكة |
|ThinDiagonalCrosshatch| يمثل نمط علامة تقاطع مائلة رفيعة |
|ThinDiagonalStripe| يمثل نمط خط مائل رفيع |
|ThinHorizontalCrosshatch| يمثل نمط علامة تقاطع أفقي رفيعة |
|ThinHorizontalStripe| يمثل نمط خط أفقي رفيع |
|ThinReverseDiagonalStripe| يمثل نمط خط مائل عكسي رفيع |
|ThinVerticalStripe| يمثل نمط خط عمودي رفيع |
|VerticalStripe| يمثل نمط خط عمودي |

في المثال أدناه ، تم تعيين لون الخلفية للخلية A1 ولكن تم تكوين A2 ليكون لها كل من لون الخلفية والأمامية مع نمط خلفية خط عمودي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **مهم معرفته**

{{% alert color="primary" %}}

- لتعيين لون الخلفية أو اللون الأمامي لخلية ما، استخدم خصائص [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) أو [**BackgroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) لكائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). سوف تؤثر كلا الخصائص فقط إذا تم تكوين خصية [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) لكائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style).
- تعيين الظل للخلية تحدد خاصية [**ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) لون الخلية.
  تحدد الخاصية [**Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) نوع نمط الخلفية المستخدمة للألوان الأمامية أو الخلفية. يوفر Aspose.Cells تعدادًا، [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype). يحتوي على مجموعة من الأنماط القياسية المحددة مسبقًا لأنماط الخلفية.
- إذا قمت بتحديد قيمة *BackgroundType.None* من تعداد [**BackgroundType**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)، لن يتم تطبيق اللون الأمامي.
  بالمثل، لن يتم تطبيق اللون الخلفي إذا قمت باختيار القيم *BackgroundType.None* أو *BackgroundType.Solid*.
- عند استرجاع لون السطوع/التعبئة للخلية، إذا كان [**Style.Pattern**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) يساوي *BackgroundType.None*، سيقوم [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) بإرجاع *Color.Empty*.

{{% /alert %}}

### **تطبيق تأثيرات تعبئة التدرج**

لتطبيق تأثيرات تعبئة التدرج المرغوبة على الخلية، استخدم الطريقة [**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient) لكائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) وفقًا لذلك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **الألوان واللوحة**

اللوحة هي عدد الألوان المتاحة للاستخدام في إنشاء صورة. يتيح استخدام لوحة معيارية في العرض للمستخدم إنشاء مظهر متسق. كل ملف من ملفات Microsoft Excel (97-2003) لديه لوحة تتكون من 56 لون يمكن تطبيقها على الخلايا، الخطوط، الخطوط الشبكية، الكائنات الرسومية، التعبئات والخطوط في الرسم البياني.

مع Aspose.Cells، يمكن للمستخدم استخدام الألوان الموجودة في اللوحة بالإضافة إلى الألوان المخصصة. قبل استخدام لون مخصص، قم بإضافته إلى اللوحة أولاً.

يناقش هذا الموضوع كيفية إضافة ألوان مخصصة إلى اللوحة.

### **إضافة ألوان مخصصة إلى اللوحة**

تدعم Aspose.Cells لوحة الألوان من Microsoft Excel التي تتكون من 56 لون. لاستخدام لون مخصص غير معرف في اللوحة، أضف اللون إلى اللوحة.

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تقدم فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) طريقة [**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) التي تأخذ المعلمات التالية لإضافة لون مخصص لتعديل اللوحة:

- لون مخصص، اللون المخصص الذي سيتم إضافته.
- الفهرس، فهرس اللون في اللوحة الذي سيحل محل اللون المخصص. يجب أن يكون بين 0-55.

المثال أدناه يضيف لون مخصص (Orchid) إلى اللوحة قبل تطبيقه على خط النص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

تحتوي اللوحة فقط على 56 لونًا. عندما تقوم بإضافة لون مخصص إلى اللوحة، يتم تغيير اللوحة ويتم تغيير أي عنصر في الملف المنسق باللون السابق. لذا، عند تغيير اللوحة، يرجى أن تكون حذرًا جدًا. علاوة على ذلك، هذه هي القيود في تنسيق ملف XLS (Excel 97 - 2003) فقط حيث لا يوجد مثل هذا القيد لتنسيق ملف XLSX أو لأنساق ملفات Microsoft Excel (2007/2010 أو 2013) المتقدمة.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
