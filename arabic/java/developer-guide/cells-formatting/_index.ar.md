---
title: تنسيقات الخلايا
type: docs
weight: 100
url: /ar/java/cells-formatting/
---

## **إضافة حدود إلى الخلايا**
يسمح Microsoft Excel للمستخدمين بتنسيق الخلايا عن طريق إضافة حدود.

إعدادات الحدود في Microsoft Excel 

![todo:image_alt_text](cells-formatting_1.png)

نوع الحدود يعتمد على المكان الذي تمت إضافته إليه. على سبيل المثال، حدود الأعلى هي تلك التي تمت إضافتها إلى الوضع العلوي للخلية. يمكن للمستخدمين أيضًا تعديل نمط ولون خطوط الحدود.

مع Aspose.Cells، يمكن للمطورين إضافة حدود وتخصيص مظهرها بنفس الطريقة المرنة التي يمكنهم فيها ذلك في Microsoft Excel.
### **إضافة حدود إلى الخلايا**
توفر Aspose.Cells فئة، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) على مجموعة [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). يمثل كل عنصر في مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) كائنًا من فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

يقدم Aspose.Cells الطريقة [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) في فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) والتي تُستخدم لضبط نمط تنسيق خلية. كما أن كائن فئة [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) يُستخدم ويوفر خصائص لضبط إعدادات الخط.
#### **إضافة حدود إلى خلية**
إضافة حدود لخلية باستخدام طريقة [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) لكائن [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). نوع الحد يُمرر كوسيطة. جميع أنواع الحدود معرفة مسبقًا في التعداد [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType).

|**أنواع الحدود**|**الوصف**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM-BORDER)|حدود أسفل الخط|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL-DOWN)|خط قطري من أعلى اليسار إلى أسفل اليمين|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL-UP)|خط قطري من أسفل اليسار إلى أعلى اليمين|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT-BORDER)|الحد الأيسر للخط|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT-BORDER)|الحد الأيمن للخط|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP-BORDER)|الحد العلوي للخط|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|فقط للنمط الديناميكي، مثل التنسيق الشرطي.
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|فقط للنمط الديناميكي، مثل التنسيق الشرطي.
لتعيين لون الخط، اختر لونًا باستخدام التعداد [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) ومرره إلى معلمة اللون في طريقة [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) في كائن [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). أنماط الخطوط مُعرفة مسبقًا في التعداد [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).

|**أنماط الخطوط**|**الوصف**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH-DOT)|يمثل خط متصل بنقطة رفيعة|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH-DOT_DOT)|يمثل خط نقطة متصل بنقطة رفيعة|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|يمثل خط متقطع
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|يمثل خط متقطع|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|يمثل خط مزدوج|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|يمثل خط شعري|
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASH-DOT)|يمثل خط متصل بنقطة متوسط السمك|
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASH-DOT_DOT)|يمثل خط من نقط ونقطة متوسطة|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM-DASHED)|يمثل خط مخطط متوسط|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)| يمثل عدم وجود خط |
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)| يمثل خط متوسط |
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED-DASH-DOT)|يمثل خط مائل مخطط من نقاط وخطوط متوسطة|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)| يمثل خط سميك |
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)| يمثل خط رفيع |
اختر أحد أنماط الخطوط أعلاه ثم قم بتعيينه على كائن [النمط](https://reference.aspose.com/cells/java/com.aspose.cells/Style) طريقة [تعيين الحد](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder-int-int-com.aspose.cells.Color-) الخاصة به.

يتم توليد الإخراج التالي عند تنفيذ الكود أدناه.

**الحدود المطبقة على جميع جوانب الخلية** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **إضافة حدود لمجموعة من الخلايا**
من الممكن إضافة حدود إلى مجموعة خلايا بدلاً من خلية واحدة فقط. أولاً، أنشئ مجموعة خلايا عن طريق استدعاء طريقة [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) لمجموعة [الخلايا](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)، والتي تأخذ المعلمات التالية:

- **الصف الأول**, الصف الأول من النطاق.
- **العمود الأول**, العمود الأول من النطاق.
- **عدد الصفوف**, عدد الصفوف في النطاق.
- **عدد الأعمدة**, عدد الأعمدة في النطاق.

ترجع طريقة [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange-int-int-boolean-) كائن [نطاق](https://reference.aspose.com/cells/java/com.aspose.cells/Range)، والذي يحتوي على النطاق المحدد. يوفر كائن [النطاق](https://reference.aspose.com/cells/java/com.aspose.cells/Range) طريقة [setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders-int-com.aspose.cells.Color-) التي تأخذ المعلمات التالية:

- **CellBorderType**, نمط خط الحدود ، يتم اختياره من تعداد [CellBorderType] (https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).
- **اللون**, لون خط الحدود ، محدد من تعداد [Color] (https://reference.aspose.com/cells/java/com.aspose.cells/Color).

يتم توليد الإخراج التالي عند تنفيذ الكود أدناه.

**تطبيق الحدود على مجموعة من الخلايا** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **الألوان واللوحة**
اللوحة هي عدد الألوان المتاحة للاستخدام في إنشاء صورة. يتيح استخدام لوحة معيارية في العرض للمستخدم إنشاء مظهر متسق. كل ملف من ملفات Microsoft Excel (97-2003) لديه لوحة تتكون من 56 لون يمكن تطبيقها على الخلايا، الخطوط، الخطوط الشبكية، الكائنات الرسومية، التعبئات والخطوط في الرسم البياني.

**إعدادات لوحة الألوان في Microsoft Excel** 

![todo:image_alt_text](cells-formatting_4.png)

مع Aspose.Cells، لا يُمكن القيام بذلك فقط باستخدام الألوان الموجودة ولكن أيضًا الألوان المخصصة. قبل استخدام لون مخصص، يجب إضافته إلى لوحة الألوان. يشرح هذا الموضوع كيفية إضافة ألوان مخصصة إلى لوحة الألوان.
### **إضافة ألوان مخصصة إلى اللوحة**
تدعم Aspose.Cells أيضًا لوحة ألوان تحتوي على 56 لونًا. يتم عرض لوحة ألوان قياسية أعلاه. إذا كنت ترغب في استخدام لون مخصص غير معرف في لوحة الألوان، فإنك ستحتاج إلى إضافة ذلك اللون إلى لوحة الألوان قبل الاستخدام.

{{% alert color="primary" %}} 

يحتوي لوحة الألوان فقط على 56 لونًا. عند إضافة لون مخصص إلى لوحة الألوان، يتم تغيير لوحة الألوان ويتم تغيير أي عنصر في الملف المنسق باللون السابق. لذا، عند تغيير لوحة الألوان، يُرجى أن تكون حذرًا جدًا. علاوة على ذلك، هذا هو القيد في تنسيق ملف XLS (Excel 97 - 2003) فقط حيث لا يوجد قيد مماثل لتنسيقات ملفات XLSX أو أي تنسيقات ملفات Microsoft Excel المتقدمة الأخرى.

{{% /alert %}} 

يقدم Aspose.Cells فئة، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)، والتي تمثل ملف إكسل من مايكروسوفت. توفر الفئة طريقة [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette-com.aspose.cells.Color-int-) التي تأخذ المعلمات التالية لإضافة لون مخصص لتعديل لوحة الألوان:

- **اللون المخصص**: اللون المخصص الذي سيتم إضافته إلى لوحة الألوان.
- **الفهرس**: فهرس اللون الذي سيتم استبداله باللون المخصص. يجب أن يكون بين 0 و 55.

يضيف المثال أدناه لونًا مخصصًا إلى لوحة الألوان قبل تطبيقه على الخط.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **الألوان وأنماط الخلفية**
يمكن لبرنامج Microsoft Excel تعيين ألوان الأمامية (الإطار) والخلفية (الملء) للخلايا وأنماط الخلفية كما هو مبين أدناه.

**تعيين الألوان وأنماط الخلفية في Microsoft Excel** 

![todo:image_alt_text](cells-formatting_5.png)

تدعم Aspose.Cells أيضًا هذه الميزات بطريقة مرنة. في هذا الموضوع، نتعلم كيفية استخدام هذه الميزات باستخدام Aspose.Cells.
### **تعيين الألوان وأنماط الخلفية**
Aspose.Cells يوفر فئة، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) على مجموعة [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة عمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). كل عنصر في مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) يمثل كائن فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

يقدم Aspose.Cells طريقة [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle-com.aspose.cells.Style-) في فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) والتي تُستخدم لضبط تنسيق خلية. أيضًا، يمكن استخدام كائن فئة [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) لتكوين إعدادات الخطوط.

{{% alert color="primary" %}} 

لتعيين لون النص أو الخلفية للخلية، استخدم خاصية [setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) أو [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) من كائن [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). تدخل هذه الخصائص حيز التنفيذ فقط إذا تم تهيئة خاصية [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) لكائن [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)

{{% /alert %}} 

خاصية [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) تحدد لون التظليل للخلية.

خاصية [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) تحدد نمط الخلفية المستخدم للون النص أو الخلفية. توفر Aspose.Cells تعداد [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) الذي يحتوي على مجموعة من أنواع الأنماط المحددة مسبقًا للخلفية.

|**نوع النمط**|**الوصف**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL-CROSSHATCH)|يمثل نمط التهاتف مائل منقطقط|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL-STRIPE)|يمثل نمط الشرط المائل|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-6)|يمثل نمط الرمادي بنسبة 6.25%|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-12)|يمثل نمط الرمادي بنسبة 12.5%|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-25)|يمثل نمط الرمادي بنسبة 25%|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-50)|يمثل نمط الرمادي بنسبة 50%|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY-75)|يمثل نمط الرمادي بنسبة 75%|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL-STRIPE)|يمثل نمط الشرط الأفقي|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)| يمثل عدم وجود خلفية
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE-DIAGONAL-STRIPE)|يمثل نمط الشرط المائل العكسي|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)| يمثل نمط صلب
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK-DIAGONAL-CROSSHATCH)|يمثل نمط التهاتف المائل السميك|
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-DIAGONAL-CROSSHATCH)|يمثل نمط التهاتف المائل الرقيق|
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-DIAGONAL-STRIPE)|يمثل نمط الشرط المائل الرقيق|
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-HORIZONTAL-CROSSHATCH)|يمثل نمط الشرط الأفقي الرقيق|
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-HORIZONTAL-STRIPE)|يمثل نمط الشرط الأفقي الرقيق|
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-REVERSE-DIAGONAL-STRIPE)|يمثل نمط الشرط المائل العكسي الرقيق|
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN-VERTICAL-STRIPE)|يمثل نمط الشرط الرأسي الرقيق|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL-STRIPE)|يمثل نمط الشرط الرأسي|
في المثال أدناه ، تم تعيين لون الخلفية للخلية A1 ولكن تم تكوين A2 ليكون لها كل من لون الخلفية والأمامية مع نمط خلفية خط عمودي.

يتم إنشاء الإخراج التالي عند تنفيذ الكود.

**تطبيق الألوان الأمامية والخلفية على الخلايا بأنماط الخلفية** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **مهم معرفته**
{{% alert color="primary" %}} 

- لتعيين لون خلفية الخلية أو الأمامية، استخدم خاصية [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) أو [BackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) لكائن [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). ستؤثر كلتا الخاصيتين فقط إذا تم تهيئة خاصية النمط لكائن [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style).
- خاصية [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) تحدد لون ظل الخلية. 
  خاصية [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) تحدد نوع النمط الخلفي المستخدم للون الأمامي أو الخلفي. توفر Aspose.Cells تعدادًا، [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)، يحتوي على مجموعة من أنواع النمط الخلفية المحددة مسبقًا.
- إذا حددت قيمة [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) من تعداد [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)، فإن لون الأمامية لن يتم تطبيقه.
  وبالمثل، لن يتم تطبيق لون الخلفية إذا حددت [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) أو [BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID).
- عند استرجاع لون التظليل/التعبئة للخلية، إذا كان [نمط النمط](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) هو [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)، سيقوم [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) بإرجاع *Color.Empty*.

{{% /alert %}} 
## **تنسيق الأحرف المحددة في خلية**
[التعامل مع إعدادات الخط](/cells/ar/java/dealing-with-font-settings/) شرح كيفية تنسيق الخلايا ولكن فقط كيفية تنسيق محتوى الخلايا بأكملها. ماذا إذا كنت ترغب في تنسيق الأحرف المحددة فقط؟

Aspose.Cells يدعم هذه الميزة. يوضح هذا الموضوع كيفية استخدام هذه الميزة.
### **تنسيق الأحرف المحددة**
Aspose.Cells يوفر فئة، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) على مجموعة [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة عمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). كل عنصر في مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) يمثل كائن فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

يوفر فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) طريقة [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters-int-int-) التي تأخذ المعلمات التالية لاختيار مجموعة من الأحرف في خلية:

- **فهرس البداية**، فهرس الحرف للبدء في التحديد منه.
- **عدد الحروف**, عدد الأحرف المراد تحديدها.

في ملف الإخراج، في الخلية "A1"، يتم تنسيق الكلمة 'زيارة' بالخط الافتراضي ولكن 'أسبوز!' بخط عريض وأزرق.

**تنسيق الأحرف المحددة** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

إذا كنت مهتمًا بـ [تنسيق جزء من النص الغني في خليّة](/cells/ar/java/access-and-update-the-portions-of-rich-text-of-cell/)، فكر في استخدام طريقتي [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) و [Cell.setCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setCharacters). تُستخدم طريقة [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) للوصول إلى أجزاء النص ثم يمكن إجراء التعديلات باستخدام طريقة [Cell.setCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setCharacters)، بينما تُرجع طريقة [get](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters--) مجموعة من كائنات [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) والتي يمكن التلاعب بها لضبط خصائص مختلفة مثل اسم الخط، لون الخط، العريض، إلخ ويمكن استخدام طريقة [set](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setCharacters) لتطبيق التغييرات.

{{% /alert %}}

## **مواضيع متقدمة**
- [إعدادات المحاذاة](/cells/ar/java/cells-alignment-settings/)
- [تنسيق مشروط](/cells/ar/java/conditional-formatting/)
- [تنسيق البيانات](/cells/ar/java/data-formatting/)
- [ثيمات وألوان Excel](/cells/ar/java/excel-2007-themes-and-colors/)
- [التعامل مع إعدادات الخط](/cells/ar/java/dealing-with-font-settings/)
- [تنسيق خلايا ورق عمل في بيان عمل](/cells/ar/java/format-worksheet-cells-in-a-workbook/)
- [تنفيذ نظام التاريخ 1904](/cells/ar/java/implement-1904-date-system/)
- [دمج وفصل الخلايا](/cells/ar/java/merging-and-unmerging-cells/)
- [إعدادات الأرقام](/cells/ar/java/cells-number-settings/)
- [الحفاظ على بادئة اقتباس واحدة لقيمة الخلية أو النطاق](/cells/ar/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [تنسيق وتنسيق البيانات](/cells/ar/java/styling-and-data-formatting/)
{{< app/cells/assistant language="java" >}}
