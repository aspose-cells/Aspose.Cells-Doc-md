---
title: إعدادات الحدود
type: docs
weight: 40
url: /ar/net/cells-border-settings/
---
## **إضافة الحدود إلى Cells**

Microsoft يسمح Excel للمستخدمين بتنسيق الخلايا عن طريق إضافة حدود. يعتمد نوع الحد على مكان إضافته. على سبيل المثال ، الحد العلوي هو الحد الذي يتم إضافته إلى الموضع العلوي للخلية. يمكن للمستخدمين أيضًا تعديل نمط خط الحدود ولونه.

باستخدام Aspose.Cells ، يمكن للمطورين إضافة حدود وتخصيص شكلها بنفس الطريقة المرنة كما في Microsoft Excel.

### **إضافة الحدود إلى Cells**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)صف دراسي.

 يوفر Aspose.Cells ملف[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index)الطريقة في[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)صف دراسي. ال[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index)الطريقة المستخدمة لتعيين نمط تنسيق الخلية. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)توفر class خصائص لإضافة حدود إلى الخلايا.

#### **إضافة حدود إلى Cell**

يمكن للمطورين إضافة حدود إلى خلية باستخدام امتداد[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) أشياء[**الحدود**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) مجموعة. يتم تمرير نوع الحد كفهرس إلى ملف[**الحدود**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) مجموعة. جميع أنواع الحدود محددة مسبقًا في ملف[**نوع الحدود**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) تعداد.

**تعداد الحدود**

|**أنواع الحدود**|**وصف**|
|:- |:- |
|الحد السفلي|خط الحد السفلي|
|قطري إلى الأسفل|خط قطري من أعلى اليسار إلى أسفل اليمين|
|قطري|خط قطري من أسفل اليسار إلى أعلى اليمين|
|يسار|خط حد أيسر|
|الحد الأيمن|خط حد صحيح|
|TopBorder|خط حد علوي|

ال[**الحدود**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders)جمع يخزن جميع الحدود. كل حد في[**الحدود**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) المجموعة يمثلها[**الحدود**](https://reference.aspose.com/cells/net/aspose.cells/border) كائن يوفر خاصيتين ،[**اللون**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) و[**أسلوب الخط**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle)لتعيين لون خط الحدود ونمطه على التوالي.

لضبط لون خط الحد ، حدد لونًا باستخدام تعداد اللون (جزء من .NET Framework) وقم بتعيينه لخاصية Color الخاصة بكائن Border.

 يتم تعيين نمط خط الحدود عن طريق تحديد نمط خط من ملف[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)تعداد.

**تعداد CellBorderType**

|**أنماط الخط**|**وصف**|
|:- |:- |
|داش دوت|خط رفيع منقّط بشرطة|
|DashDotDot|خط رفيع منقّط بشرطة|
|متقطع|خط متقطع|
|منقط|خط منقط|
|مزدوج|خط مزدوج|
|شعر|شعري|
|متوسط|خط متوسط منقّط بشرطة|
|متوسط|خط متوسط منقّط بشرطة|
|متوسط متقطع|خط متقطع متوسط|
|لا أحد|لا خط|
|متوسط|خط متوسط|
|مائل|خط مائل منقط بشرطة متوسطة|
|سميك|خط سميك|
|رفيع|خيط رفيع|
حدد أحد أنماط الخطوط ثم قم بتعيينه إلى ملف[**الحدود**](https://reference.aspose.com/cells/net/aspose.cells/border) أشياء[**أسلوب الخط**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) منشأه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

يجب عليك تعيين كل من نمط الخط واللون في نفس الوقت. يجب أن يكون لخط الحد المائل نفس نمط الخط ولونه.

{{% /alert %}}

#### **إضافة حدود إلى مدى من Cells**

من الممكن أيضًا إضافة حدود إلى نطاق من الخلايا بدلاً من مجرد خلية واحدة. للقيام بذلك ، أولاً ، قم بإنشاء نطاق من الخلايا عن طريق استدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) طريقة. يأخذ المعلمات التالية:

- الصف الأول ، الصف الأول من النطاق.
- العمود الأول ، يمثل العمود الأول من النطاق.
- عدد الصفوف ، عدد الصفوف في النطاق.
- عدد الأعمدة ، عدد الأعمدة في النطاق.

 ال[**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) طريقة إرجاع أ[**نطاق**](https://reference.aspose.com/cells/net/aspose.cells/range) الكائن الذي يحتوي على نطاق محدد من الخلايا. ال[**نطاق**](https://reference.aspose.com/cells/net/aspose.cells/range) كائن يوفر[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) طريقة تأخذ المعلمات التالية لإضافة حد إلى نطاق الخلايا:

- **نوع الحدود** ، نوع الحد المحدد من ملف[**نوع الحدود**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)تعداد.
- **أسلوب الخط** ، نمط خط الحدود المحدد من ملف[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)تعداد.
- **اللون**، لون الخط المحدد من تعداد الألوان.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}

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

تحتوي اللوحة على 56 لونًا فقط. عندما تضيف لونًا مخصصًا إلى اللوحة ، تتغير اللوحة ويتغير أي عنصر في الملف منسق باللون السابق. لذا ، عند تغيير لوحة الألوان ، يرجى توخي الحذر الشديد. علاوة على ذلك ، هذا هو القيد في تنسيق ملف XLS (Excel 97-2003) فقط حيث لا يوجد مثل هذا التقييد لتنسيقات ملفات XLSX أو غيرها من تنسيقات MS Excel المتقدمة (2007/2010 أو 2013).

{{% /alert %}}


