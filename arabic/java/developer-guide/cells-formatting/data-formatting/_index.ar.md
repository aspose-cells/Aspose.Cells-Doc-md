---
title: تنسيق البيانات
type: docs
weight: 80
url: /ar/java/data-formatting/
---
## **مقاربات لتنسيق البيانات في Cells**
من الحقائق الشائعة أنه إذا تم تنسيق خلايا ورقة العمل بشكل صحيح ، فسيصبح من السهل على المستخدمين قراءة محتويات (بيانات) الخلية. توجد طرق عديدة لتنسيق الخلايا ومحتوياتها. إن أبسط طريقة هي تنسيق الخلايا باستخدام Microsoft Excel في بيئة WYSIWYG أثناء إنشاء جدول بيانات مصمم. بعد إنشاء جدول بيانات المصمم ، يمكنك فتح جدول البيانات باستخدام Aspose.Cells مع الاحتفاظ بجميع إعدادات التنسيق المحفوظة في جدول البيانات. هناك طريقة أخرى لتنسيق الخلايا ومحتوياتها وهي استخدام Aspose.Cells API. في هذا الموضوع ، سنصف طريقتين لتنسيق الخلايا ومحتوياتها باستخدام Aspose.Cells API.
### **التنسيق Cells**
 يمكن للمطورين تنسيق الخلايا ومحتوياتها باستخدام API المرن من Aspose.Cells. يوفر Aspose.Cells فئة ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) فئة توفر مجموعة Cells. كل عنصر في[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)تمثل المجموعة كائنًا من**Cell** صف دراسي.

 يوفر Aspose.Cells ملف[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) الممتلكات في[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) فئة ، تُستخدم لتعيين نمط تنسيق الخلية. علاوة على ذلك ، يوفر Aspose.Cells أيضًا[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) فئة تُستخدم لخدمة نفس الغرض. قم بتطبيق أنواع مختلفة من أنماط التنسيق على الخلايا لتعيين ألوان الخلفية أو المقدمة ، والحدود ، والخطوط ، والمحاذاة الأفقية والرأسية ، ومستوى المسافة البادئة ، واتجاه النص ، وزاوية التدوير والمزيد.
#### **باستخدام طريقة setStyle**
 عند تطبيق أنماط تنسيق مختلفة على خلايا مختلفة ، فمن الأفضل استخدام طريقة setStyle لملف[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) صف دراسي. يوجد مثال أدناه لتوضيح استخدام طريقة setStyle لتطبيق إعدادات تنسيق مختلفة على خلية.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **استخدام كائن النمط**
 عند تطبيق نفس نمط التنسيق على خلايا مختلفة ، استخدم ملحق[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) موضوع.

1.  أضف[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) إلى مجموعة Styles الخاصة بـ[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class عن طريق استدعاء طريقة createStyle لفئة المصنف.
1. قم بالوصول إلى كائن النمط المضاف حديثًا من مجموعة الأنماط.
1. قم بتعيين الخصائص المطلوبة لكائن النمط لتطبيق إعدادات التنسيق المطلوبة.
1. قم بتعيين كائن Style الذي تم تكوينه إلى خاصية Style لأي خلية مرغوبة.

يمكن أن يؤدي هذا النهج إلى تحسين كفاءة تطبيقاتك بشكل كبير وتوفير الذاكرة أيضًا.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **تطبيق تأثيرات تعبئة متدرجة**
لتطبيق تأثيرات التعبئة المتدرجة المطلوبة على الخلية ، استخدم أسلوب setTwoColorGradient الخاص بكائن النمط وفقًا لذلك.
#### **مثال رمز**
 يتم تحقيق الإخراج التالي عن طريق تنفيذ الكود أدناه.

**تطبيق تأثيرات تعبئة متدرجة** 

![ما يجب القيام به: image_بديل_نص](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **تكوين إعدادات المحاذاة**
أي شخص استخدم Microsoft Excel لتنسيق الخلايا سيكون على دراية بإعدادات المحاذاة في Microsoft Excel.

**إعدادات المحاذاة في Microsoft Excel** 

![ما يجب القيام به: image_بديل_نص](data-formatting_2.png)

كما ترى من الشكل أعلاه ، هناك أنواع مختلفة من خيارات المحاذاة:

- [محاذاة النص](/cells/ar/java/data-formatting/) (افقي عمودي)
- [المسافة الفارغة](/cells/ar/java/data-formatting/).
- [اتجاه](/cells/ar/java/data-formatting/).
- [التحكم بالنص](/cells/ar/java/data-formatting/).
- [اتجاه النص](/cells/ar/java/data-formatting/).

يتم دعم كافة إعدادات المحاذاة هذه بالكامل بواسطة Aspose.Cells وتتم مناقشتها بمزيد من التفاصيل أدناه.
### **تكوين إعدادات المحاذاة**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel. تحتوي فئة المصنف على مجموعة أوراق العمل التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي.

 توفر فئة ورقة العمل مجموعة Cells. يمثل كل عنصر في مجموعة Cells عنصرًا من عناصر[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) صف دراسي.

يوفر Aspose.Cells طريقة setStyle في ملف[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) الفئة المستخدمة في تنسيق الخلية. ال[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) توفر فئة خصائص مفيدة لتكوين إعدادات الخط.

حدد أي نوع من أنواع محاذاة النص باستخدام تعداد TextAlignmentType. أنواع محاذاة النص المحددة مسبقًا في تعداد TextAlignmentType هي:

|**أنواع محاذاة النص**|**وصف**|
|:- |:- |
|قاع|يمثل محاذاة النص السفلي|
|مركز|يمثل مركز محاذاة النص|
|CenterAcross|يمثل المركز عبر محاذاة النص|
|وزعت|يمثل محاذاة النص الموزع|
|ملء|يمثل محاذاة النص التعبئة|
|عام|يمثل محاذاة نص عامة|
|يبرر|التمثيلات تضبط محاذاة النص|
|اليسار|يمثل محاذاة النص الأيسر|
|الصحيح|يمثل محاذاة النص الصحيحة|
|قمة|يمثل محاذاة النص العلوي|
{{% alert color="primary" %}} 

يمكنك أيضًا تطبيق إعداد الضبط الموزع باستخدام طريقة Style.setJustifyDistributed ().

{{% /alert %}} 
#### **المحاذاة الأفقية**
 استخدم ال[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) أسلوب setHorizontalAlignment للكائن لمحاذاة النص أفقيًا.

يتم تحقيق الإخراج التالي عن طريق تنفيذ رمز المثال أدناه:

**محاذاة النص أفقيا** 

![ما يجب القيام به: image_بديل_نص](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **انحياز عمودي**
 استخدم ال[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) setVerticalAlignment للكائن لمحاذاة النص عموديًا.

يتم تحقيق الإخراج التالي عند ضبط VerticalAlignment على المركز.

**محاذاة النص عموديا** 

![ما يجب القيام به: image_بديل_نص](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **المسافة الفارغة**
 من الممكن تعيين مستوى المسافة البادئة للنص في خلية باستخدام[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) أسلوب setIndentLevel الخاص بالكائن.

يتم تحقيق الإخراج التالي عند ضبط IndentLevel على 2.

**تم ضبط مستوى المسافة البادئة على 2** 

![ما يجب القيام به: image_بديل_نص](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **اتجاه**
 عيّن اتجاه (تدوير) النص في خلية بامتداد[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) طريقة setRotationAngle للكائن.

يتم تحقيق الإخراج التالي عند ضبط زاوية الدوران على 25.

**ضبط زاوية الدوران على 25** 

![ما يجب القيام به: image_بديل_نص](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **التحكم بالنص**
يناقش القسم التالي كيفية التحكم في النص عن طريق تعيين التفاف النص ، وتقليص حجمه للاحتواء وخيارات التنسيق الأخرى.
#### **التفاف النص**
يسهل التفاف النص في خلية القراءة: يتم ضبط ارتفاع الخلية لاحتواء النص بالكامل ، بدلاً من قطعه أو امتداده إلى الخلايا المجاورة.

 قم بتعيين التفاف النص أو إيقاف تشغيله بامتداد[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) طريقة setTextWrapped للكائن.

يتم تحقيق الإخراج التالي عند تمكين التفاف النص.

**نص ملفوف داخل الخلية** 

![ما يجب القيام به: image_بديل_نص](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **تقلص لتناسب**
 يتمثل أحد خيارات التفاف النص في حقل في تقليص حجم النص ليلائم أبعاد الخلية. يتم ذلك عن طريق تحديد ملف[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) كائن IsTextWrapped إلى**حقيقي**.

يتم تحقيق الإخراج التالي عندما يتم تقليص النص ليلائم الخلية.

**تم تقليص النص ليلائم حدود الخلية** 

![ما يجب القيام به: image_بديل_نص](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **دمج Cells**
مثل Microsoft Excel ، يدعم Aspose.Cells دمج عدة خلايا في خلية واحدة.

يتم تحقيق الإخراج التالي إذا تم دمج الخلايا الثلاث في الصف الأول لإنشاء خلية مفردة كبيرة.

**تم دمج ثلاث خلايا لإنشاء خلية كبيرة** 

![ما يجب القيام به: image_بديل_نص](data-formatting_9.png)

 استخدم ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) طريقة دمج المجموعة لدمج الخلايا. تأخذ طريقة الدمج المعلمات التالية:

- الصف الأول ، الصف الأول من حيث يتم بدء الدمج.
- العمود الأول ، العمود الأول من حيث يتم بدء الدمج.
- عدد الصفوف ، عدد الصفوف المراد دمجها.
- عدد الأعمدة ، عدد الأعمدة المراد دمجها.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **اتجاه النص**
من الممكن ضبط ترتيب قراءة النص في الخلايا. ترتيب القراءة هو الترتيب المرئي الذي يتم به عرض الأحرف والكلمات وما إلى ذلك. على سبيل المثال ، اللغة الإنجليزية هي لغة من اليسار إلى اليمين بينما اللغة العربية هي لغة من اليمين إلى اليسار.

 يتم تعيين ترتيب القراءة بامتداد[أسلوب](https://reference.aspose.com/cells/java/com.aspose.cells/style) خاصية TextDirection للكائن. يوفر Aspose.Cells أنواع اتجاهات النص المحددة مسبقًا في تعداد TextDirectionType.

|**أنواع اتجاه النص**|**وصف**|
|:- |:- |
|سياق الكلام|ترتيب القراءة المتوافق مع لغة أول حرف تم إدخاله|
|من اليسار إلى اليمين|ترتيب القراءة من اليسار إلى اليمين|
|من اليمين الى اليسار|ترتيب القراءة من اليمين إلى اليسار|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





يتم تحقيق الإخراج التالي إذا تم ضبط ترتيب قراءة النص من اليمين إلى اليسار.

**ضبط ترتيب قراءة النص من اليمين إلى اليسار** 

![ما يجب القيام به: image_بديل_نص](data-formatting_10.png)
## **تنسيق الأحرف المحددة في Cell**
[التعامل مع إعدادات الخط](/cells/ar/java/dealing-with-font-settings/)شرح كيفية تنسيق الخلايا ولكن فقط كيفية تنسيق محتوى الخلايا wntire. ماذا لو كنت تريد تنسيق الأحرف المختارة فقط؟

Aspose.Cells يدعم هذه الميزة. يشرح هذا الموضوع كيفية استخدام هذه الميزة.
### **تنسيق الأحرف المحددة**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. تحتوي فئة المصنف على مجموعة أوراق عمل تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي. توفر فئة ورقة العمل مجموعة Cells. يمثل كل عنصر في مجموعة Cells عنصرًا من عناصر[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) صف دراسي.

توفر الفئة Cell طريقة الأحرف التي تأخذ المعلمات التالية لتحديد نطاق من الأحرف في خلية:

- **فهرس البداية**، فهرس الحرف الذي سيبدأ الاختيار منه.
- **عدد الشخصيات**، عدد الأحرف المراد تحديده.

في ملف الإخراج ، في الخلية A1 "، تم تنسيق كلمة" زيارة "بالخط الافتراضي ولكن" Aspose! " جريئة وأزرق.

**تنسيق الأحرف المختارة** 

![ما يجب القيام به: image_بديل_نص](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

 إذا كنت مهتما في[تنسيق جزء من Rich Text في [خلية]](/cells/ar/java/access-and-update-the-portions-of-rich-text-of-cell/) ، ضع في اعتبارك استخدام طرق Cell.getCharacters & Cell.setCharacters. يتم استخدام طريقة Cell.getCharacters للوصول إلى أجزاء النص ومن ثم يمكن إجراء التعديلات باستخدام طريقة Cell.setCharacters بينما**احصل على** تقوم الطريقة بإرجاع مجموعة من كائنات FontSetting التي يمكن معالجتها لتعيين خصائص مختلفة ، اسم الخط ، ولون الخط ، والجرأة ، إلخ.**تعيين** يمكن استخدام الطريقة لتطبيق التغييرات.

{{% /alert %}} 
## **تنشيط الأوراق وإجراء Cell نشطًا أو تحديد نطاق Cells في ورقة العمل**
في بعض الأحيان ، قد تحتاج إلى تنشيط ورقة عمل محددة بحيث تكون أول ورقة يتم عرضها عندما يفتح شخص ما الملف في Microsoft Excel. قد تحتاج أيضًا إلى تنشيط خلية معينة بحيث يتم تمرير أشرطة التمرير إلى الخلية النشطة بحيث تكون مرئية بوضوح. Aspose.Cells قادر على القيام بجميع المهام المذكورة أعلاه.

الورقة النشطة هي الورقة التي تعمل عليها في مصنف. يكون الاسم الموجود في علامة تبويب الورقة النشطة غامقًا بشكل افتراضي. في هذه الأثناء ، الخلية النشطة هي الخلية المحددة والتي يتم إدخال البيانات فيها عند بدء الكتابة. فقط خلية واحدة نشطة في كل مرة. الخلية النشطة محاطة بحد ثقيل لجعلها تظهر ضد الخلايا الأخرى. يسمح لك Aspose.Cells أيضًا بتحديد نطاق من الخلايا في ورقة العمل.
### **تنشيط ورقة وتنشيط Cell**
يوفر Aspose.Cells API محددًا لهذه المهام. على سبيل المثال ، تعتبر طريقة WorksheetCollection.setActiveSheetIndex مفيدة لتعيين ورقة نشطة. وبالمثل ، يتم استخدام طريقة Worksheet.setActiveCell لتعيين خلية نشطة والحصول عليها في ورقة العمل.

إذا كنت تريد تمرير أشرطة التمرير الأفقية والعمودية إلى موضع فهرس الصف والعمود لإعطاء عرض جيد للبيانات المحددة عند فتح الملف في Microsoft Excel ، فاستخدم خصائص Worksheet.setFirstVisibleRow و Worksheet.setFirstVisibleColumn.

يوضح المثال التالي كيفية تنشيط ورقة عمل وتنشيط خلية فيها. يتم تمرير أشرطة التمرير لجعل الصف الثاني والعمود الثاني أول صف وعمود مرئيين.

**تعيين خلية B2 كخلية نشطة** 

![ما يجب القيام به: image_بديل_نص](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **تحديد نطاق Cells في ورقة العمل**
يوفر Aspose.Cells الطريقة Worksheet.selectRange (int startRow، int startColumn، int totalRows، int totalColumns، bool removeOthers). باستخدام المعلمة الأخيرة - removeOthers - إلى true ، تتم إزالة تحديدات الخلية أو نطاق الخلايا الأخرى في الورقة.

يوضح المثال التالي كيفية تحديد نطاق من الخلايا في ورقة العمل النشطة.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

جميع الفئات والطرق المذكورة أعلاه متوفرة بالإصدار المرخص Aspose.Cells.

{{% /alert %}} 
## **تنسيق الصفوف والأعمدة**
ربما يكون تنسيق الصفوف والأعمدة في جدول بيانات لإلقاء نظرة على التقرير هو الميزة الأكثر استخدامًا في تطبيق Excel. توفر واجهات برمجة التطبيقات Aspose.Cells أيضًا هذه الوظيفة من خلال نموذج البيانات الخاص بها عن طريق عرض فئة النمط التي تتعامل بشكل أساسي مع جميع الميزات المتعلقة بالتصميم مثل الخط وسماته ومحاذاة النص وألوان الخلفية / المقدمة والحدود وتنسيق عرض الأرقام والتاريخ الحرفي وما إلى ذلك. . هناك فئة مفيدة أخرى توفرها واجهات برمجة التطبيقات Aspose.Cells وهي StyleFlag التي تسمح بإعادة استخدام كائن النمط.

سنحاول في هذه المقالة شرح كيفية استخدام Aspose.Cells for Java API لتطبيق التنسيق على الصفوف والأعمدة.
### **تنسيق الصفوف والأعمدة**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على مجموعة أوراق العمل التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة ورقة العمل. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) توفر فئة المجموعة Cells. توفر مجموعة Cells مجموعة صفوف.
#### **تنسيق صف**
يمثل كل عنصر في مجموعة الصفوف كائن صف. يقدم الكائن Row طريقة applyStyle المستخدمة لتطبيق التنسيق على صف.

لتطبيق نفس التنسيق على صف ، استخدم كائن النمط:

1. أضف كائن Style إلى فئة Workbook عن طريق استدعاء أسلوب createStyle الخاص به.
1. قم بتعيين خصائص كائن النمط لتطبيق إعدادات التنسيق.
1. قم بتعيين كائن Style الذي تم تكوينه إلى أسلوب applyStyle الخاص بكائن Row.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **تنسيق عمود**
توفر مجموعة Cells مجموعة أعمدة. يمثل كل عنصر في مجموعة الأعمدة كائن عمود. على غرار كائن الصف ، يقدم كائن العمود طريقة applicationStyle المستخدمة لتعيين تنسيق العمود. استخدم طريقة applyStyle لكائن العمود لتنسيق عمود بنفس طريقة الصف.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **ضبط تنسيق العرض Numbers وتواريخ الصفوف والأعمدة**
إذا كان المتطلب هو تعيين تنسيق عرض الأرقام والتواريخ لصف أو عمود كامل ، فستكون العملية أكثر أو أقل كما تمت مناقشته أعلاه ، ومع ذلك ، بدلاً من تعيين معلمات للمحتويات النصية ، ستقوم بتعيين التنسيق للأرقام والتواريخ باستخدام Style.Number أو Style.Custom. يرجى ملاحظة أن الخاصية Style.Number هي من النوع الصحيح وتشير إلى تنسيقات الأرقام والتاريخ المضمنة ، بينما الخاصية Style.Custom هي من نوع السلسلة وتقبل الأنماط الصالحة.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

 يرجى مراجعة المقال المفصل على[ضبط تنسيقات العرض Numbers و [التواريخ]](/cells/ar/java/data-formatting/).

{{% /alert %}}
