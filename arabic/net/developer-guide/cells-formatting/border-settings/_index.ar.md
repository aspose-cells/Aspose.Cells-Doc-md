---
title: إعدادات الحدود
description: كيفية استخدام مكتبة Aspose.Cells في C# لتعيين نمط الحدود ولون الخلايا. من خلال ضبط عرض الحدود ونمطها ولونها، يمكنك التحكم بشكل أكبر في كيفية ظهور الخلايا ومظهرها.
keywords: Aspose.Cells, Cell Border Settings, C#, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /ar/net/cells-border-settings/
---
##  **إضافة الحدود إلى Cells**

Microsoft يتيح Excel للمستخدمين تنسيق الخلايا عن طريق إضافة حدود. يعتمد نوع الحد على مكان إضافته. على سبيل المثال، الحد العلوي هو الحد الذي يتم إضافته إلى الموضع العلوي للخلية. يمكن للمستخدمين أيضًا تعديل نمط خط الحدود ولونه.

مع Aspose.Cells، يمكن للمطورين إضافة حدود وتخصيص شكلها بنفس الطريقة المرنة كما في Microsoft Excel.

###  **إضافة الحدود إلى Cells**

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الذي يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل.

 Aspose.Cells يوفر[**احصل على ستايل**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)الطريقة في[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)فصل. ال[**سيت ستايل**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)يتم استخدام الطريقة لتعيين نمط تنسيق الخلية. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)يوفر الفصل خصائص لإضافة حدود إلى الخلايا.

####  **إضافة الحدود إلى Cell**

يمكن للمطورين إضافة حدود إلى الخلية باستخدام[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**الحدود**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) مجموعة. يتم تمرير نوع الحدود كفهرس إلى ملف[**الحدود**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) مجموعة. يتم تعريف جميع أنواع الحدود مسبقًا في ملف[**نوع الحدود**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) تعداد.

**تعداد الحدود**

|**أنواع الحدود**|**وصف**|
| :- | :- |
|الحد السفلي|خط الحدود السفلي|
|قطري للأسفل|خط قطري من أعلى اليسار إلى أسفل اليمين|
|DiagonalUp|خط قطري من أسفل اليسار إلى أعلى اليمين|
|LeftBorder|خط الحدود الأيسر|
|RightBorder|خط الحدود الصحيح|
|TopBorder|خط الحدود العلوي|

ال[**الحدود**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)مجموعة مخازن جميع الحدود. كل الحدود في[**الحدود**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) يتم تمثيل المجموعة بـ أ[**حدود**](https://reference.aspose.com/cells/net/aspose.cells/border) الكائن الذي يوفر خاصيتين،[**لون**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) و[**أسلوب الخط**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)لتعيين لون خط الحدود ونمطه على التوالي.

لتعيين لون خط الحدود، حدد لونًا باستخدام تعداد الألوان (جزء من إطار عمل .NET) وقم بتعيينه لخاصية اللون لكائن الحدود.

 يتم تعيين نمط خط الحدود عن طريق تحديد نمط خط من[**نوع الخلية**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)تعداد.

**تعداد CellBorderType**

|**أنماط الخط**|**وصف**|
| :- | :- |
|داشدوت|خط رفيع منقط|
|DashDotDot|خط رفيع منقط بشرطة|
|متقطع|خط متقطع|
|منقط|خط منقط|
|مزدوج|خط مزدوج|
|شعر|شعري|
|MediumDashDot|خط منقط متوسط|
|متوسطDashDotDot|خط منقط بشرطة ونقطة متوسطة|
|متوسطمتقطع|خط متقطع متوسط|
|لا أحد|لا خط|
|واسطة|خط متوسط|
|SlantedDashDot|خط منقط متوسط مائل|
|سميك|خط سميك|
|رفيع|خيط رفيع|
حدد أحد أنماط الخطوط ثم قم بتعيينه إلى[**حدود**](https://reference.aspose.com/cells/net/aspose.cells/border) أشياء[**أسلوب الخط**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) ملكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

يجب عليك ضبط نمط الخط واللون في نفس الوقت. يجب أن يكون لخطي الحدود القطريين نفس نمط الخط واللون.

{{% /alert %}}

####  **إضافة حدود إلى نطاق Cells**

 من الممكن أيضًا إضافة حدود إلى نطاق من الخلايا بدلاً من مجرد خلية واحدة. للقيام بذلك، قم أولاً بإنشاء نطاق من الخلايا عن طريق استدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) طريقة. يستغرق المعلمات التالية:

- الصف الأول، الصف الأول من النطاق.
- العمود الأول، يمثل العمود الأول من النطاق.
- عدد الصفوف، عدد الصفوف في النطاق.
- عدد الأعمدة، عدد الأعمدة في النطاق.

 ال[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) طريقة إرجاع أ[**يتراوح**](https://reference.aspose.com/cells/net/aspose.cells/range) الكائن الذي يحتوي على نطاق الخلايا المحدد. ال[**يتراوح**](https://reference.aspose.com/cells/net/aspose.cells/range) يوفر الكائن أ[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) الطريقة التي تأخذ المعلمات التالية لإضافة حد إلى نطاق الخلايا:

-  *نوع الحدود**، نوع الحدود، المحدد من[**نوع الحدود**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)تعداد.
-  *نمط الخط**، نمط خط الحدود، تم تحديده من[**نوع الخلية**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)تعداد.
- *اللون**، لون الخط، المحدد من قائمة الألوان.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
