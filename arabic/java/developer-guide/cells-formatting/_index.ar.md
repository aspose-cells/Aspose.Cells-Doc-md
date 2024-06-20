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

توفر Aspose.Cells الطريقة [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) في فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) المستخدمة لتعيين نمط تنسيق الخلية. أيضًا، يتم استخدام كائن فئة [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) ويوفر خصائص لتكوين إعدادات الخط.
#### **إضافة حدود إلى خلية**
إضافة حدود إلى خلية باستخدام طريقة [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) الخاصة بكائن الفئة [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). يتم تمرير نوع الحدود كمعلمة. جميع أنواع الحدود معرفة مسبقًا في تعداد [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType).

|**أنواع الحدود**|**الوصف**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|الخط الحد السفلي
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|خط مائل من الجزء العلوي الأيسر إلى الجزء السفلي الأيمن
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|خط مائل من الجزء السفلي الأيسر إلى الجزء العلوي الأيمن
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|الخط الحد الأيسر
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|الخط الحد الأيمن
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|الخط الحد العلوي
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|فقط للنمط الديناميكي، مثل التنسيق الشرطي.
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|فقط للنمط الديناميكي، مثل التنسيق الشرطي.
لتعيين لون الخط، حدد لونًا باستخدام تعداد [Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color) وقم بتمريره إلى معلمة Color خاصة بطريقة [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) كائن الفئة [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). تم تعريف أنماط الخط مسبقًا في تعداد [CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType).

|**أنماط الخطوط**|**الوصف**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|يمثل خط متقطع رفيع مخطط بالنقاط
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|يمثل خط متقطع رفيع مخطط بالنقطة والنقطة
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|يمثل خط متقطع
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|يمثل خط متقطع|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|يمثل خط مزدوج|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|يمثل خط شعري|
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)| يمثل خط متقطع متقاطع بين الوسط |
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)| يمثل خط متقطع نقطة واحدة متوسطة |
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)| يمثل خط متقطع متوسط |
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)| يمثل عدم وجود خط |
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)| يمثل خط متوسط |
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)| يمثل خط متقطع مائل متوسط |
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)| يمثل خط سميك |
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)| يمثل خط رفيع |
حدد أحد أنماط الخط المذكورة أعلاه ثم اعتباره إلى [Style] (https://reference.aspose.com/cells/java/com.aspose.cells/Style) و [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) الأسلوب.

يتم توليد الإخراج التالي عند تنفيذ الكود أدناه.

**الحدود المطبقة على جميع جوانب الخلية** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **إضافة حدود لمجموعة من الخلايا**
من الممكن إضافة حدود إلى مجموعة من الخلايا بدلاً من خلية واحدة فقط. أولاً ، أنشئ مجموعة من الخلايا عن طريق استدعاء [Cells] (https://reference.aspose.com/cells/java/com.aspose.cells/Cells) تجميع [createRange] (https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) الأسلوب ، الذي يأخذ المعلمات التالية :

- **الصف الأول**, الصف الأول من النطاق.
- **العمود الأول**, العمود الأول من النطاق.
- **عدد الصفوف**, عدد الصفوف في النطاق.
- **عدد الأعمدة**, عدد الأعمدة في النطاق.

يعيد [createRange] (https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) الأسلوب [Range] (https://reference.aspose.com/cells/java/com.aspose.cells/Range) الكائن ، الذي يحتوي على النطاق المحدد. [Range] (https://reference.aspose.com/cells/java/com.aspose.cells/Range) الكائن يوفر [setOutlineBorders] (https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) الأسلوب الذي يأخذ المعلمات التالية :

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

يوفر Aspose.Cells فئة، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)، التي تمثل ملف Microsoft Excel. تقدم الفئة طريقة [changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)) التي تأخذ المعلمات التالية لإضافة لون مخصص لتعديل لوحة الألوان:

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

يوفر Aspose.Cells الطريقة [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) في فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) التي يتم استخدامها لتعيين تنسيق الخلية. كما يُمكن استخدام كائن فئة [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) لتكوين إعدادات الخط.

{{% alert color="primary" %}} 

لتعيين لون النص أو الخلفية للخلية، استخدم خاصية [setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) أو [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) من كائن [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style). تدخل هذه الخصائص حيز التنفيذ فقط إذا تم تهيئة خاصية [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) لكائن [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)

{{% /alert %}} 

خاصية [setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) تحدد لون التظليل للخلية.

خاصية [setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) تحدد نمط الخلفية المستخدم للون النص أو الخلفية. توفر Aspose.Cells تعداد [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) الذي يحتوي على مجموعة من أنواع الأنماط المحددة مسبقًا للخلفية.

|**نوع النمط**|**الوصف**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)| يمثل نمط التقاطع القطري
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)| يمثل نمط الشريط القطري
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)| يمثل نمط اللون الرمادي بنسبة 6.25%
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)| يمثل نمط اللون الرمادي بنسبة 12.5%
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)| يمثل نمط اللون الرمادي بنسبة 25%
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)| يمثل نمط اللون الرمادي بنسبة 50%
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)| يمثل نمط اللون الرمادي بنسبة 75%
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)| يمثل نمط الشريط الأفقي
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)| يمثل عدم وجود خلفية
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)| يمثل نمط الشريط القطري المعكوس
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)| يمثل نمط صلب
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)| يمثل نمط التقاطع القطري السميك
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)| يمثل نمط التقاطع القطري الرفيع
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)| يمثل نمط الشريط القطري الرفيع
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)| يمثل نمط التقاطع الأفقي الرفيع
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)| يمثل نمط الشريط الأفقي الرفيع
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|يمثل نقشة خط مائل قليلة
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|يمثل نقشة خط رأسي رفيعة
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|يمثل نقشة خط رأسي
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

فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) توفر طريقة [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)) التي تأخذ المعلمات التالية لتحديد مجموعة من الأحرف في خلية:

- **فهرس البداية**، فهرس الحرف للبدء في التحديد منه.
- **عدد الحروف**, عدد الأحرف المراد تحديدها.

في ملف الإخراج، في الخلية "A1"، يتم تنسيق الكلمة 'زيارة' بالخط الافتراضي ولكن 'أسبوز!' بخط عريض وأزرق.

**تنسيق الأحرف المحددة** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

إذا كنت مهتمًا بـ[تنسيق جزء من النص الغني في خلية](/cells/ar/java/access-and-update-the-portions-of-rich-text-of-cell/)، فضلاً عن استخدام طرق الـ[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) و Cell.setCharacters. يجب استخدام الطريقة [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) للوصول إلى أجزاء النص ثم يمكن القيام بالتعديلات باستخدام طريقة Cell.setCharacters بينما تعيد الطريقة **get** مجموعة من [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) التي يمكن التلاعب بها لتعيين خصائص مختلفة مثل اسم الخط ولون الخط وعرض الخط إلخ ويمكن استخدام الطريقة **set** لتطبيق التغييرات.

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
