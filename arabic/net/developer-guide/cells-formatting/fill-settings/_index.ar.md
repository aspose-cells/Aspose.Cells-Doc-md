---
title: إعدادات التعبئة
type: docs
weight: 50
url: /ar/net/cells-fill-settings/
---
## **الألوان وأنماط الخلفية**

Microsoft يمكن لبرنامج Excel تعيين ألوان المقدمة (المخطط التفصيلي) والخلفية (تعبئة) للخلايا وأنماط الخلفية.

يدعم Aspose.Cells أيضًا هذه الميزات بطريقة مرنة. في هذا الموضوع ، نتعلم استخدام هذه الميزات باستخدام Aspose.Cells.

### **ضبط الألوان وأنماط الخلفية**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)صف دراسي.

 ال[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) لديه[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) و[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) الطرق المستخدمة للحصول على تنسيق الخلية وتعيينه. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)يوفر class خصائص لتعيين ألوان المقدمة والخلفية للخلايا. يوفر Aspose.Cells أ[**نوع الخلفية**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)التعداد الذي يحتوي على مجموعة من الأنواع المحددة مسبقًا لأنماط الخلفية الموضحة أدناه.

|**أنماط الخلفية**|**وصف**|
|:- |:- |
|قطري|يمثل نمط التظليل المتقاطع القطري|
|قطري|يمثل نمط شريط قطري|
|رمادي 6|يمثل 6.25٪ نمط رمادي|
|رمادي 12|يمثل 12.5٪ نمط رمادي|
|رمادي 25|يمثل 25٪ نمط رمادي|
|رمادي 50|يمثل 50٪ نمط رمادي|
|رمادي 75|يمثل 75٪ نمط رمادي|
|أفقي ستريب|يمثل نمط شريط أفقي|
|لا أحد|لا يمثل أي خلفية|
|ReverseDiagonalStripe|يمثل نمط شريط قطري معكوس|
|صلب|يمثل نمط صلب|
|سميك قطري متقاطع|يمثل نمط التظليل المتقاطع القطري السميك|
|ThinDiagonalCrosshatch|يمثل نمط التظليل المتقاطع القطري الرقيق|
|ThinDiagonalStripe|يمثل نمط شريطي رقيق قطري|
|رقيق أفقي متقاطع|يمثل نمط التظليل الأفقي الرفيع|
|ThinHorizontalStripe|يمثل نمط شريط أفقي رقيق|
|ThinReverseDiagonalStripe|يمثل نمط شريطي قطري عكسي رقيق|
|ThinVerticalStripe|يمثل نمط شريط عمودي رقيق|
|عمودي الشريط|يمثل نمط شريط عمودي|

في المثال أدناه ، تم تعيين لون المقدمة لخلية A1 ولكن تم تكوين A2 بحيث تحتوي على ألوان المقدمة والخلفية بنمط خلفية شريطي عمودي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **من المهم أن تعرف**

{{% alert color="primary" %}}

-  لتعيين لون المقدمة أو الخلفية لخلية ، استخدم تنسيق[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**المقدمة**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) أو[**لون الخلفية**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) الخصائص. تصبح كلتا الخاصيتين ساريتين فقط إذا كان الامتداد[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**نمط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)تم تكوين الخاصية.
-  ال[**المقدمة**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)تعيّن الخاصية لون تظليل الخلية.
 ال[**نمط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)تحدد الخاصية نوع نمط الخلفية المستخدم للون المقدمة أو الخلفية. يوفر Aspose.Cells تعداد ،[**نوع الخلفية**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)الذي يحتوي على مجموعة من أنواع محددة مسبقًا من أنماط الخلفية.
-  إذا اخترت*نوع الخلفية* قيمة من[**نوع الخلفية**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)التعداد ، لا يتم تطبيق اللون الأمامي.
 وبالمثل ، لا يتم تطبيق لون الخلفية إذا قمت بتحديد ملف*نوع الخلفية* أو*نوع الخلفية* القيم.
-  عند استرداد لون التظليل / التعبئة للخلية ، إذا كان[**أسلوب. نمط**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) يكون*نوع الخلفية*, [**Style.ForegroundColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) سيعود*اللون فارغ*.

{{% /alert %}}

### **تطبيق تأثيرات تعبئة متدرجة**

 لتطبيق تأثيرات التعبئة المتدرجة التي تريدها على الخلية ، استخدم ملف[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)الطريقة وفقًا لذلك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **الألوان واللوحة**

اللوح هو عدد الألوان المتاحة للاستخدام في إنشاء صورة. يتيح استخدام لوحة قياسية في عرض تقديمي للمستخدم إنشاء مظهر متناسق. يحتوي كل ملف Microsoft Excel (97-2003) على لوحة من 56 لونًا يمكن تطبيقها على الخلايا والخطوط وخطوط الشبكة والكائنات الرسومية والتعبئة والخطوط في المخطط.

مع Aspose.Cells لا يمكن فقط استخدام الألوان الموجودة في اللوحة ولكن أيضًا الألوان المخصصة. قبل استخدام لون مخصص ، قم بإضافته إلى اللوحة أولاً.

يناقش هذا الموضوع كيفية إضافة ألوان مخصصة إلى اللوحة.

### **إضافة ألوان مخصصة إلى لوحة الألوان**

Aspose.Cells يدعم Microsoft لوحة الألوان 56 في Excel. لاستخدام لون مخصص غير محدد في اللوحة ، أضف اللون إلى اللوحة.

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة توفر أ[**ChangePalette**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) طريقة تأخذ المعلمات التالية لإضافة لون مخصص لتعديل اللوحة:

- لون مخصص ، اللون المخصص المراد إضافته.
- الفهرس ، فهرس اللون في اللوحة الذي سيحل محله اللون المخصص. يجب أن يكون بين 0-55.

يضيف المثال أدناه لونًا مخصصًا (Orchid) إلى اللوحة قبل تطبيقه على الخط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

تحتوي اللوحة على 56 لونًا فقط. عندما تضيف لونًا مخصصًا إلى اللوحة ، تتغير اللوحة ويتغير أي عنصر في الملف منسق باللون السابق. لذا ، عند تغيير لوحة الألوان ، يرجى توخي الحذر الشديد. علاوة على ذلك ، هذا هو القيد في تنسيق ملف XLS (Excel 97-2003) فقط حيث لا يوجد مثل هذا القيد على XLSX أو تنسيقات ملفات MS Excel المتقدمة الأخرى (2007/2010 أو 2013).

{{% /alert %}}
