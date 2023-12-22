---
title: إعدادات التعبئة
description: Aspose.Cells هي مكتبة .NET للعمل مع ملفات جداول البيانات. وهو يدعم ضبط إعدادات تعبئة الخلايا، مما يسمح للمستخدمين بتخصيص خلفية الخلايا ونمطها. ستقدم هذه المقالة كيفية استخدام مكتبة Aspose.Cells لضبط إعدادات تعبئة الخلايا.
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style
type: docs
weight: 50
url: /ar/net/cells-fill-settings/
---
##  **الألوان وأنماط الخلفية**

Microsoft يمكن لـ Excel تعيين ألوان المقدمة (المخطط التفصيلي) والخلفية (الملء) للخلايا وأنماط الخلفية.

Aspose.Cells يدعم أيضًا هذه الميزات بطريقة مرنة. في هذا الموضوع نتعلم كيفية استخدام هذه الميزات باستخدام الرقم Aspose.Cells.

###  **ضبط الألوان وأنماط الخلفية**

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الذي يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل.

 ال[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) لديه[**احصل على ستايل**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) و[**سيت ستايل**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) الأساليب المستخدمة للحصول على تنسيق الخلية وتعيينه. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)توفر الفئة خصائص لتعيين الألوان الأمامية والخلفية للخلايا. Aspose.Cells يوفر أ[**نوع الخلفية**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)التعداد الذي يحتوي على مجموعة من أنواع أنماط الخلفية المحددة مسبقًا والموضحة أدناه.

|**أنماط الخلفية**|**وصف**|
| :- | :- |
|قطريCrosshatch|يمثل نمط التظليل المتقاطع القطري|
|شريط قطري|يمثل نمط شريط قطري|
|رمادي6|يمثل 6.25% نمط رمادي|
|رمادي12|يمثل 12.5% نمط رمادي|
|رمادي25|يمثل 25% نمط رمادي|
|رمادي50|يمثل 50% نمط رمادي|
|رمادي75|يمثل 75% نمط رمادي|
|شريط أفقي|يمثل نمط شريط أفقي|
|لا أحد|لا يمثل أي خلفية|
|شريط قطري عكسي|يمثل نمط شريط قطري عكسي|
|صلب|يمثل نمطًا ثابتًا|
|سميكة قطري Crossshatch|يمثل نمط التظليل المتقاطع السميك|
|ThinDiagonalCrosshatch|يمثل نمط التظليل المتقاطع الرفيع|
|شريط قطري رفيع|يمثل نمط شريط قطري رفيع|
|ThinHorizontalCrossshatch|يمثل نمط التظليل الأفقي الرقيق|
|شريط أفقي رفيع|يمثل نمط شريط أفقي رفيع|
|شريط قطري عكسي رفيع|يمثل نمط شريط قطري عكسي رفيع|
|شريط عمودي رقيق|يمثل نمط شريط عمودي رفيع|
|شريط عمودي|يمثل نمط شريط عمودي|

في المثال أدناه، تم تعيين اللون الأمامي للخلية A1 ولكن تم تكوين A2 بحيث تحتوي على ألوان المقدمة والخلفية مع نمط خلفية شريطي عمودي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

###  **من المهم أن تعرف**

{{% alert color="primary" %}}

-  لتعيين لون المقدمة أو الخلفية للخلية، استخدم[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**لون المقدمة**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) أو[**لون الخلفية**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) ملكيات. لن تصبح كلتا الخاصيتين ساريتين إلا إذا تم[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**نمط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)تم تكوين الخاصية.
-  ال[**لون المقدمة**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)الخاصية تحدد لون ظل الخلية.
 ال[**نمط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)تحدد الخاصية نوع نمط الخلفية المستخدم للون المقدمة أو الخلفية. Aspose.Cells يوفر التعداد،[**نوع الخلفية**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype). يحتوي على مجموعة من أنواع أنماط الخلفية المحددة مسبقًا.
-  إذا قمت بتحديد*نوع الخلفية. لا شيء* القيمة من[**نوع الخلفية**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)التعداد، لا يتم تطبيق اللون الأمامي.
 وبالمثل، لا يتم تطبيق لون الخلفية إذا قمت بتحديد*نوع الخلفية. لا شيء* أو*نوع الخلفية.صلب* قيم.
-  عند استرداد لون تظليل/تعبئة الخلية، إذا[**نمط.نمط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) هو *BackgroundType.None*،[**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) سيعود *اللون.فارغ*.

{{% /alert %}}

###  **تطبيق تأثيرات التعبئة المتدرجة**

 لتطبيق تأثيرات التعبئة المتدرجة المطلوبة على الخلية، استخدم[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)الطريقة وفقا لذلك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

##  **الألوان ولوحة**

اللوحة هي عدد الألوان المتاحة للاستخدام في إنشاء الصورة. يتيح استخدام لوحة موحدة في العرض التقديمي للمستخدم إنشاء مظهر متسق. يحتوي كل ملف Microsoft Excel (97-2003) على لوحة مكونة من 56 لونًا يمكن تطبيقها على الخلايا والخطوط وخطوط الشبكة والكائنات الرسومية والتعبئات والخطوط في المخطط.

مع Aspose.Cells، من الممكن ليس فقط استخدام الألوان الموجودة في اللوحة ولكن أيضًا الألوان المخصصة. قبل استخدام لون مخصص، قم بإضافته إلى اللوحة أولاً.

يناقش هذا الموضوع كيفية إضافة ألوان مخصصة إلى لوحة الألوان.

###  **إضافة ألوان مخصصة إلى لوحة الألوان**

Aspose.Cells يدعم Microsoft لوحة ألوان Excel المكونة من 56 لونًا. لاستخدام لون مخصص غير محدد في لوحة الألوان، قم بإضافة اللون إلى لوحة الألوان.

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يوفر الفصل أ[**تغيير لوحة**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) الطريقة التي تأخذ المعلمات التالية لإضافة لون مخصص لتعديل اللوحة:

- اللون المخصص، اللون المخصص المراد إضافته.
- الفهرس، فهرس اللون الموجود في اللوحة الذي سيحل محله اللون المخصص. ينبغي أن يكون بين 0-55.

يضيف المثال أدناه لونًا مخصصًا (Orchid) إلى لوحة الألوان قبل تطبيقه على الخط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

تحتوي اللوحة على 56 لونًا فقط. عند إضافة لون مخصص إلى لوحة الألوان، يتم تغيير اللوحة وتغيير أي عنصر في الملف المنسق باللون السابق. لذا، عند تغيير لوحة الألوان، يرجى توخي الحذر الشديد. علاوة على ذلك، هذا هو القيد في تنسيق الملف XLS (Excel 97 - 2003) فقط حيث لا يوجد مثل هذا القيد على XLSX أو تنسيقات ملفات MS Excel المتقدمة الأخرى (2007/2010 أو 2013).

{{% /alert %}}
