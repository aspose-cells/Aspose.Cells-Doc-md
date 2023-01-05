---
title: Cells تنسيقات
type: docs
weight: 100
url: /ar/java/cells-formatting/
---
## **إضافة الحدود إلى Cells**
Microsoft يسمح Excel للمستخدمين بتنسيق الخلايا عن طريق إضافة حدود.

**إعدادات الحدود في Microsoft Excel** 

![ما يجب القيام به: image_بديل_نص](cells-formatting_1.png)

يعتمد نوع الحد على مكان إضافته. على سبيل المثال ، الحد العلوي هو الحد الذي يتم إضافته إلى الموضع العلوي للخلية. يمكن للمستخدمين أيضًا تعديل نمط خط الحدود ولونه.

باستخدام Aspose.Cells ، يمكن للمطورين إضافة حدود وتخصيص شكلها بنفس الطريقة المرنة التي يمكنهم بها في Microsoft Excel.
### **إضافة الحدود إلى Cells**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فئة توفر أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. كل عنصر في[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) تمثل المجموعة كائنًا من[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)صف دراسي.

 يوفر Aspose.Cells ملف[مجموعة](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) الطريقة في[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) فئة تستخدم لتعيين نمط تنسيق الخلية. أيضا ، موضوع[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/Style)يتم استخدام class وتوفر خصائص لتكوين إعدادات الخط.
#### **إضافة حدود إلى Cell**
 أضف حدودًا إلى خلية بامتداد[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/Style) أشياء[تعيين الحدود](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) طريقة. يتم تمرير نوع الحد كمعامل. جميع أنواع الحدود محددة مسبقًا في ملف[نوع الحدود](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)تعداد.

|**أنواع الحدود**|**وصف**|
|:- |:- |
|[الحد السفلي](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|خط الحد السفلي|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|خط قطري من أعلى اليسار إلى أسفل اليمين|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|خط قطري من أسفل اليسار إلى أعلى اليمين|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|خط الحد الأيسر|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|خط الحدود الصحيح|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|خط الحد العلوي|
|[عرضي](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|فقط للنمط الديناميكي ، مثل التنسيق الشرطي.|
|[عمودي](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|فقط للنمط الديناميكي ، مثل التنسيق الشرطي.|
 لتعيين لون الخط ، حدد لونًا باستخدام تنسيق[اللون](https://reference.aspose.com/cells/java/com.aspose.cells/Color) التعداد وتمريره إلى[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/Style) أشياء[تعيين الحدود](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) ) معلمة اللون الخاصة بالطريقة. يتم تحديد أنماط الخط مسبقًا في ملف[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)تعداد.

|**أنماط الخط**|**وصف**|
|:- |:- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|يمثل خطًا رفيعًا منقّطًا بشرطة|
|[اندفاع_نقطة_نقطة](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|يمثل خطًا رفيعًا منقّطًا بشرطة|
|[متقطع](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|يمثل خط متقطع|
|[منقط](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|يمثل خط منقط|
|[مزدوج](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|يمثل خط مزدوج|
|[شعر](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|يمثل خط الشعر|
|[متوسط_اندفاع_نقطة](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|يمثل خطًا متوسطًا منقّطًا بشرطة|
|[متوسط_اندفاع_نقطة نقطة](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|يمثل خطًا متوسطًا منقطًا وشرطة|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|يمثل خط متوسط متقطع|
|[لا أحد](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|لا يمثل أي خط|
|[متوسط](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|يمثل الخط المتوسط|
|[مائل_اندفاع_نقطة](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|يمثل خطًا مائلًا منقطًا بشرطة متوسطة|
|[سميك](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|يمثل خط سميك|
|[نحيف](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|يمثل خط رفيع|
 حدد أحد أنماط الخط أعلاه ثم قم بتعيينه إلى ملف[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/Style)أشياء[تعيين الحدود](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) طريقة.

يتم إنشاء الإخراج التالي عند تنفيذ الكود أدناه.

**حدود مطبقة على جميع جوانب الخلية** 

![ما يجب القيام به: image_بديل_نص](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **إضافة حدود إلى مدى من Cells**
 من الممكن إضافة حدود إلى نطاق من الخلايا بدلاً من مجرد خلية واحدة. أولاً ، قم بإنشاء نطاق من الخلايا عن طريق استدعاء[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) المجموعة[إنشاء المدى](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) ، والتي تأخذ المعلمات التالية:

- **السطر الاول**، الصف الأول من النطاق.
- **العمود الأول**، العمود الأول من النطاق.
- **عدد الصفوف**، عدد الصفوف في النطاق.
- **عدد الأعمدة**، وهو عدد الأعمدة في النطاق.

 ال[إنشاء المدى](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\) ) طريقة إرجاع أ[نطاق](https://reference.aspose.com/cells/java/com.aspose.cells/Range) الكائن الذي يحتوي على النطاق المحدد. ال[نطاق](https://reference.aspose.com/cells/java/com.aspose.cells/Range) كائن يوفر[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) الطريقة التي تأخذ المعلمات التالية:

- **CellBorderType**، نمط خط الحدود المحدد من ملف[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)تعداد.
- **اللون**، لون خط الحدود المحدد من[اللون](https://reference.aspose.com/cells/java/com.aspose.cells/Color)تعداد.

يتم إنشاء الإخراج التالي عند تنفيذ الكود أدناه.

**حدود مطبقة على نطاق من الخلايا** 

![ما يجب القيام به: image_بديل_نص](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **الألوان واللوحة**
اللوح هو عدد الألوان المتاحة للاستخدام في إنشاء صورة. يتيح استخدام لوحة قياسية في عرض تقديمي للمستخدم إنشاء مظهر متناسق. يحتوي كل ملف Microsoft Excel (97-2003) على لوحة من 56 لونًا يمكن تطبيقها على الخلايا والخطوط وخطوط الشبكة والكائنات الرسومية والتعبئة والخطوط في المخطط.

**إعدادات لوح الألوان في Microsoft Excel** 

![ما يجب القيام به: image_بديل_نص](cells-formatting_4.png)

مع Aspose.Cells ، لا يمكن استخدام الألوان الموجودة فقط ولكن أيضًا الألوان المخصصة. قبل استخدام لون مخصص ، قم بإضافته إلى اللوحة. يشرح هذا الموضوع كيفية إضافة ألوان مخصصة إلى اللوحة.
### **إضافة ألوان مخصصة إلى لوحة الألوان**
يدعم Aspose.Cells أيضًا لوحة من 56 لونًا. يتم عرض لوحة ألوان قياسية أعلاه. إذا كنت تريد استخدام لون مخصص غير محدد في اللوحة ، فستحتاج إلى إضافة هذا اللون إلى اللوحة قبل الاستخدام.

{{% alert color="primary" %}} 

تحتوي اللوحة على 56 لونًا فقط. عندما تضيف لونًا مخصصًا إلى اللوحة ، تتغير اللوحة ويتغير أي عنصر في الملف منسق باللون السابق. لذا ، عند تغيير لوحة الألوان ، يرجى توخي الحذر الشديد. علاوة على ذلك ، هذا هو القيد في تنسيق ملف XLS (Excel 97-2003) فقط حيث لا يوجد مثل هذا القيد على XLSX أو تنسيقات ملفات MS Excel (2007/2010) المتقدمة الأخرى.

{{% /alert %}} 

Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)، يمثل ملف Excel Microsoft. يوفر الفصل[التغيير](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)) طريقة تأخذ المعلمات التالية لإضافة لون مخصص لتعديل اللوحة:

- **لون مخصص**، اللون المخصص المراد إضافته إلى اللوحة.
- **فِهرِس**، فهرس اللون الذي سيتم استبداله باللون المخصص. يجب أن يكون بين 0-55.

يضيف المثال أدناه لونًا مخصصًا إلى اللوحة قبل تطبيقه على خط.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **الألوان وأنماط الخلفية**
Microsoft يمكن لبرنامج Excel تعيين ألوان المقدمة (المخطط التفصيلي) والخلفية (تعبئة) للخلايا وأنماط الخلفية كما هو موضح أدناه.

**ضبط الألوان وأنماط الخلفية في Microsoft Excel** 

![ما يجب القيام به: image_بديل_نص](cells-formatting_5.png)

يدعم Aspose.Cells أيضًا هذه الميزات بطريقة مرنة. في هذا الموضوع ، نتعلم استخدام هذه الميزات باستخدام Aspose.Cells.
### **ضبط الألوان وأنماط الخلفية**
Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)، يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)فئة توفر أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)مجموعة. كل عنصر في[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)تمثل المجموعة كائنًا من[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)صف دراسي.

يوفر Aspose.Cells ملف[مجموعة](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) الطريقة في[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)فئة تُستخدم لتعيين تنسيق الخلية. أيضا ، موضوع[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/Style)يمكن استخدام فئة لتكوين إعدادات الخط.

{{% alert color="primary" %}} 

 لتعيين لون المقدمة أو الخلفية لخلية ، استخدم الامتداد[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/Style) أشياء[setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) أو[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) الخصائص. لا تدخل هذه الخصائص حيز التنفيذ إلا إذا كان الامتداد[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/Style) أشياء[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) تم تكوين الخاصية.

{{% /alert %}} 

ال[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)تعيّن الخاصية لون تظليل الخلية.

ال[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) تحدد الخاصية نمط الخلفية المستخدم للون المقدمة أو الخلفية. يوفر Aspose.Cells ملف[نوع الخلفية](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)التعداد الذي يحتوي على مجموعة من الأنواع المحددة مسبقًا لأنماط الخلفية.

|**نوع نمط**|**وصف**|
|:- |:- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|يمثل نمط التظليل المتقاطع القطري|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|يمثل نمط شريط قطري|
|[رمادي_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|يمثل 6.25٪ نمط رمادي|
|[رمادي_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|يمثل 12.5٪ نمط رمادي|
|[رمادي_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|يمثل 25٪ نمط رمادي|
|[رمادي_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|يمثل 50٪ نمط رمادي|
|[رمادي_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|يمثل 75٪ نمط رمادي|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|يمثل نمط شريط أفقي|
|[لا أحد](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|لا يمثل أي خلفية|
|[يعكس_قطري_شريط](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|يمثل نمط شريط قطري معكوس|
|[صلب](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|يمثل نمط صلب|
|[سميك_قطري_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|يمثل نمط التظليل المتقاطع القطري السميك|
|[نحيف_قطري_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|يمثل نمط التظليل المتقاطع القطري الرقيق|
|[نحيف_قطري_شريط](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|يمثل نمط شريطي رقيق قطري|
|[نحيف_عرضي_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|يمثل نمط التظليل الأفقي الرفيع|
|[نحيف_عرضي_شريط](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|يمثل نمط شريط أفقي رقيق|
|[نحيف_يعكس_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|يمثل نمط شريطي قطري عكسي رقيق|
|[نحيف_عمودي_شريط](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|يمثل نمط شريط عمودي رقيق|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|يمثل نمط شريط عمودي|
في المثال أدناه ، تم تعيين لون المقدمة لخلية A1 ولكن تم تكوين A2 بحيث تحتوي على ألوان المقدمة والخلفية بنمط خلفية شريطي عمودي.

يتم إنشاء الإخراج التالي عند تنفيذ التعليمات البرمجية.

**يتم تطبيق ألوان المقدمة والخلفية على الخلايا ذات أنماط الخلفية** 

![ما يجب القيام به: image_بديل_نص](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **من المهم أن تعرف**
{{% alert color="primary" %}} 

-  لتعيين لون المقدمة أو الخلفية لخلية ، استخدم تنسيق[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/Style) أشياء[المقدمة](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) أو[لون الخلفية](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) الخصائص. تصبح كلتا الخاصيتين ساريتين فقط إذا كان الامتداد[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/Style) أشياء[نمط](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) تم تكوين الخاصية.
-  ال[المقدمة](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) تعيّن الخاصية لون تظليل الخلية.
 ال[نمط](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) تحدد الخاصية نوع نمط الخلفية المستخدم للون المقدمة أو الخلفية. يوفر Aspose.Cells تعداد ،[نوع الخلفية](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)الذي يحتوي على مجموعة من أنواع محددة مسبقًا من أنماط الخلفية.
-  إذا اخترت[نوع الخلفية](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) قيمة من[نوع الخلفية](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) التعداد ، لا يتم تطبيق اللون الأمامي.
 وبالمثل ، لا يتم تطبيق لون الخلفية إذا قمت بتحديد ملف[نوع الخلفية](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) أو[نوع الخلفية](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID) القيم.
-  عند استرداد لون التظليل / التعبئة للخلية ، إذا كان[أسلوب. نمط](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) يكون[نوع الخلفية](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) سيعود*اللون فارغ*.

{{% /alert %}} 
## **تنسيق الأحرف المحددة في Cell**
[التعامل مع إعدادات الخط](/cells/ar/java/dealing-with-font-settings/) شرح كيفية تنسيق الخلايا ولكن فقط كيفية تنسيق محتوى الخلايا بأكملها. ماذا لو كنت تريد تنسيق الأحرف المختارة فقط؟

Aspose.Cells يدعم هذه الميزة. يشرح هذا الموضوع كيفية استخدام هذه الميزة.
### **تنسيق الأحرف المحددة**
Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)، يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)فئة توفر أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)مجموعة. كل عنصر في[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)تمثل المجموعة كائنًا من[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)صف دراسي.

ال[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) فئة تقدم[الشخصيات](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)) طريقة تأخذ المعلمات التالية لتحديد نطاق من الأحرف في خلية:

- **فهرس البداية**، فهرس الحرف الذي سيبدأ الاختيار منه.
- **عدد الشخصيات**، عدد الأحرف المراد تحديده.

في ملف الإخراج ، في الخلية A1 "، تم تنسيق كلمة" زيارة "بالخط الافتراضي ولكن" Aspose! " جريئة وأزرق.

**تنسيق الأحرف المختارة** 

![ما يجب القيام به: image_بديل_نص](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

 إذا كنت مهتما في[تنسيق جزء من نص منسق في خلية](/cells/ar/java/access-and-update-the-portions-of-rich-text-of-cell/) ، ففكر في استخدام[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) و Cell.setCharactions Methods. ال[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) ) للوصول إلى أجزاء من النص ومن ثم يمكن إجراء التعديلات باستخدام طريقة Cell.setCharacters بينما**احصل على**تقوم الطريقة بإرجاع مصفوفة من[إعداد الخط](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) الكائنات التي يمكن معالجتها لتعيين خصائص مختلفة مثل اسم الخط ولون الخط والجرأة وما إلى ذلك و**تعيين** يمكن استخدام الطريقة لتطبيق التغييرات.

{{% /alert %}}

## **موضوعات مسبقة**
- [إعدادات المحاذاة](/cells/ar/java/cells-alignment-settings/)
- [تنسيق مشروط](/cells/ar/java/conditional-formatting/)
- [تنسيق البيانات](/cells/ar/java/data-formatting/)
- [سمات وألوان Excel](/cells/ar/java/excel-2007-themes-and-colors/)
- [التعامل مع إعدادات الخط](/cells/ar/java/dealing-with-font-settings/)
- [تنسيق ورقة العمل Cells في مصنف](/cells/ar/java/format-worksheet-cells-in-a-workbook/)
- [تطبيق نظام التاريخ 1904](/cells/ar/java/implement-1904-date-system/)
- [الدمج والدمج Cells](/cells/ar/java/merging-and-unmerging-cells/)
- [إعدادات الرقم](/cells/ar/java/cells-number-settings/)
- [احتفظ ببادئة اقتباس فردية بقيمة Cell أو نطاق](/cells/ar/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [التصميم وتنسيق البيانات](/cells/ar/java/styling-and-data-formatting/)
