---
title: تنسيق البيانات
type: docs
weight: 80
url: /ar/java/data-formatting/
---

## **النهج لتنسيق البيانات في الخلايا**
هو حقيقة شائعة أنه إذا تم تنسيق خلايا ورقة العمل بشكل صحيح ، فإنه يصبح أسهل بالنسبة للمستخدمين قراءة محتويات (البيانات) الخلية. هناك العديد من الطرق لتنسيق الخلايا ومحتوياتها. أسهل طريقة هي تنسيق الخلايا باستخدام Microsoft Excel في بيئة WYSIWYG أثناء إنشاء ورقة عمل مصممة. بعد إنشاء ورقة العمل المصممة ، يمكنك فتح ورقة العمل باستخدام Aspose.Cells مع الاحتفاظ بجميع إعدادات التنسيق المحفوظة مع ورقة العمل. طريقة أخرى لتنسيق الخلايا ومحتوياتها هي استخدام واجهة برمجة تطبيقات Aspose.Cells. في هذا الموضوع ، سنصف نهجين لتنسيق الخلايا ومحتوياتها باستخدام واجهة برمجة تطبيقات Aspose.Cells.
### **تنسيق الخلايا**
يمكن للمطورين تنسيق الخلايا ومحتوياتها باستخدام واجهة برمجة Aspose.Cells المرنة. توفر Aspose.Cells فئة ، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة خلايا. يُمثل كل عنصر في مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) كائن **Cell**.

توفر Aspose.Cells الخاصية [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) في فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) ، المستخدمة لتعيين نمط التنسيق للخلية. وعلاوة على ذلك ، توفر Aspose.Cells أيضًا فئة [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) التي تُستخدم لتحقيق نفس الغرض. قم بتطبيق أنواع مختلفة من أنماط التنسيق على الخلايا لتعيين ألوان الخلفية أو الخطوط الأمامية ، الحدود ، الخطوط ، الألوان ، التوجيه الأفقي والعمودي ، مستوى التحاذية ، اتجاه النص ، زاوية الدوران والمزيد.
#### **استخدام طريقة setStyle**
عند تطبيق أنماط تنسيق مختلفة على خلايا مختلفة ، فمن الأفضل استخدام طريقة setStyle من فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell). يظهر مثال أدناه لتوضيح استخدام طريقة setStyle لتطبيق إعدادات التنسيق المختلفة على خلية.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **استخدام كائن Style**
عند تطبيق نفس النمط التنسيقي على خلايا مختلفة ، استخدم كائن [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

1. أضف كائن [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) إلى مجموعة الأنماط لفئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) عن طريق استدعاء طريقة createStyle لفئة Workbook.
1. قم بالوصول إلى كائن Style الجديد المضاف من مجموعة الأنماط.
1. قم بتعيين الخصائص المطلوبة لكائن Style لتطبيق إعدادات التنسيق المرغوبة.
1. قم بتعيين كائن Style المكون لخلية معينة المطلوبة.

يمكن أن يحسن هذا النهج بشكل كبير كفاءة تطبيقاتك ويوفر ذاكرة أيضًا.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **تطبيق تأثيرات تعبئة التدرج**
لتطبيق تأثيرات ملء التدرج المرغوبة على الخلية ، استخدم طريقة setTwoColorGradient من كائن Style وفقًا لذلك.
#### **مثال الكود**
يتم تحقيق الإخراج التالي عن طريق تنفيذ الشيفرة أدناه. 

**تطبيق تأثيرات ملء التدرج** 

![todo:image_alt_text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **ضبط إعدادات المحاذاة**
أي شخص قد استخدم Microsoft Excel لتنسيق الخلايا سيكون متعودًا على إعدادات المحاذاة في Microsoft Excel.

إعدادات التوجيه في Microsoft Excel 

![todo:image_alt_text](data-formatting_2.png)

كما يمكنك رؤية من الشكل أعلاه، هناك أنواع مختلفة من خيارات المحاذاة:

- [توجيه النص](/cells/ar/java/data-formatting/) (أفقي وعمودي)
- [المسافة البادئة](/cells/ar/java/data-formatting/).
- [اتجاه](/cells/ar/java/data-formatting/).
- [التحكم في النص](/cells/ar/java/data-formatting/).
- [اتجاه النص](/cells/ar/java/data-formatting/).

كل إعدادات المحاذاة هذه مدعومة تمامًا بواسطة Aspose.Cells ويتم مناقشتها بمزيد من التفصيل أدناه.
### **ضبط إعدادات المحاذاة**
يوفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Excel. تحتوي فئة Workbook على مجموعة WorksheetCollection التي تسمح بالوصول إلى كل ورقة في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

توفر فئة Worksheet مجموعة خلايا. كل عنصر في مجموعة الخلايا يمثل كائن من فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

يوفر Aspose.Cells الطريقة setStyle في فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) التي تستخدم تنسيق الخلية. توفر فئة [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) خصائص مفيدة لتكوين إعدادات الخط.

حدد أي نوع توجيه نص باستخدام تعداد TextAlignmentType. يتمثل أنواع توجيه النص المحددة مسبقًا في تعداد TextAlignmentType على النحو التالي:

|** أنواع محاذاة النص **|** الوصف **|
| :- | :- |
|Bottom|يمثل محاذاة النص السفلي
|Center|يمثل محاذاة النص الوسطية
|CenterAcross|تمثل محاذاة النص في وسط النص|
|Distributed|تمثل توزيع محاذاة النص|
|Fill|تمثل ملء محاذاة النص|
|General|تمثل محاذاة النص العامة|
|Justify|تمثل محاذاة النص التبريري|
|Left|يمثل محاذاة النص اليسار|
|Right|يمثل محاذاة النص اليمين|
|Top|يمثل محاذاة النص العلوي|
{{% alert color="primary" %}} 

يمكنك أيضًا تطبيق إعداد موزع مبرر باستخدام طريقة Style.setJustifyDistributed().

{{% /alert %}} 
#### **المحاذاة الأفقية**
استخدم طريقة setHorizontalAlignment لكائن النمط [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) لمحاذاة النص أفقيًا.

يتم تحقيق الناتج التالي عن طريق تنفيذ رمز المثال أدناه:

**محاذاة النص أفقيًا** 

![todo:image_alt_text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **المحاذاة الرأسية**
استخدم طريقة setVerticalAlignment لكائن النمط [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) لمحاذاة النص رأسيًا.

يتم تحقيق الناتج التالي عندما يتم تعيين محاذاة رأسية إلى وسط.

**محاذاة النص رأسيًا** 

![todo:image_alt_text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **المسافة البادئة**
من الممكن تعيين مستوى المسافة البادئة للنص في خلية باستخدام طريقة setIndentLevel لكائن النمط [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

يتم تحقيق الناتج التالي عندما يتم تعيين مستوى المسافة البادئة إلى 2.

**تعديل مستوى المسافة البادئة إلى 2** 

![todo:image_alt_text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **الاتجاه**
قم بتعيين توجيه (دوران) النص في خلية باستخدام طريقة setRotationAngle لكائن النمط [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style).

يتم تحقيق الناتج التالي عند تعيين زاوية الدوران إلى 25.

**تم تعيين زاوية الدوران على 25** 

![todo:image_alt_text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **التحكم في النص**
يناقش القسم التالي كيفية التحكم في النص عن طريق تعيين التفاف النص، وتقليل حجم النص للتناسب وخيارات التنسيق الأخرى.
#### **تفاف النص**
تفاف النص في خلية يجعله أسهل في القراءة: يتم ضبط ارتفاع الخلية لتناسب كل النص، بدلاً من قصه أو تسربه إلى الخلايا المجاورة.

قم بتفعيل أو تعطيل تفاف النص باستخدام طريقة setTextWrapped() من كائن Style.

يتم تحقيق الناتج التالي عند تمكين تفاف النص.

**النص الملتف داخل الخلية** 

![todo:image_alt_text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **تقليص للتناسب**
خيار لتفاف النص في الحقل هو تقليص حجم النص ليتلاءم مع أبعاد الخلية. يتم ذلك عن طريق تعيين خاصية IsTextWrapped لكائن Style إلى **صحيح**.

يتم تحقيق الناتج التالي عند تقليص النص للملاءمة مع الخلية.

**النص المقلص ليتناسب مع حدود الخلية** 

![todo:image_alt_text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **دمج الخلايا**
مثل Microsoft Excel، يدعم Aspose.Cells دمج عدة خلايا في خلية واحدة.

يتم تحقيق الناتج التالي إذا تم دمج الخلايا الثلاث في الصف الأول لإنشاء خلية كبيرة واحدة.

**دمج ثلاث خلايا لإنشاء خلية كبيرة** 

![todo:image_alt_text](data-formatting_9.png)

استخدم طريقة الدمج Merge من مجموعة Cells لدمج الخلايا. تأخذ طريقة الدمج التالية المعلمات التالية:

- الصف الأول، الصف الأول من حيث يبدأ الدمج.
- العمود الأول، العمود الأول من حيث يبدأ الدمج.
- عدد الصفوف، عدد الصفوف المراد دمجها.
- عدد الأعمدة، عدد الأعمدة المراد دمجها.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **اتجاه النص**
من الممكن تعيين ترتيب القراءة للنص في الخلايا. ترتيب القراءة هو الترتيب المرئي الذي يتم عرض الأحرف والكلمات وما إلى ذلك. على سبيل المثال، اللغة الإنجليزية تكون من اليسار إلى اليمين بينما اللغة العربية تكون من اليمين إلى اليسار.

يتم تعيين ترتيب القراءة باستخدام خاصية TextDirection لكائن [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style). توفر Aspose.Cells أنواع توجيه النص المحددة مسبقًا في تعداد TextDirectionType.

|**أنواع توجيه النص**|**الوصف**|
| :- | :- |
|Context|ترتيب القراءة متسق مع لغة الحرف الأول المُدخل|
|LeftToRight|الترتيب من اليسار إلى اليمين
|RightToLeft|الترتيب من اليمين إلى اليسار






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





يتم تحقيق الإخراج التالي إذا تم تعيين ترتيب القراءة للنص إلى اليمين إلى اليسار.

**ضبط ترتيب قراءة النص إلى اليمين إلى اليسار** 

![todo:image_alt_text](data-formatting_10.png)
## **تنسيق الأحرف المحددة في خلية**
[التعامل مع إعدادات الخطوط](/cells/ar/java/dealing-with-font-settings/) شرح كيفية تنسيق الخلايا ولكن فقط كيفية تنسيق محتوى الخلايا بأكملها. ماذا لو كنت ترغب في تنسيق الأحرف المحددة فقط؟

Aspose.Cells يدعم هذه الميزة. يوضح هذا الموضوع كيفية استخدام هذه الميزة.
### **تنسيق الأحرف المحددة**
توفر Aspose.Cells فئة، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة Workbook على مجموعة Worksheets التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر فئة Worksheet مجموعة Cells. كل عنصر في مجموعة Cells يمثل كائن فئة [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

توفر فئة Cell طريقة characters التي تأخذ المعلمات التالية لتحديد نطاق من الأحرف في خلية:

- **فهرس البداية**، فهرس الحرف للبدء في التحديد منه.
- **عدد الحروف**, عدد الأحرف المراد تحديدها.

في ملف الإخراج، في الخلية "A1"، يتم تنسيق الكلمة 'زيارة' بالخط الافتراضي ولكن 'أسبوز!' بخط عريض وأزرق.

**تنسيق الأحرف المحددة** 

![todo:image_alt_text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

إذا كنت مهتمًا بتنسيق جزء من نص نصي غني في الخلية ، فكر في استخدام طريقة Cell.getCharacters & Cell.setCharacters. تستخدم طريقة Cell.getCharacters للوصول إلى أجزاء من النص ثم يمكن القيام بالتعديلات باستخدام طريقة Cell.setCharacters بينما تُرجع الطريقة الـ **get** مجموعة من كائنات FontSetting والتي يمكن التلاعب بها لتعيين مختلف خصائص اسم الخط ، لون الخط ، السمك إلخ ويمكن استخدام الطريقة **set** لتطبيق التغييرات.

{{% /alert %}} 
## **تفعيل الأوراق وجعل خلية نشطة أو تحديد مجموعة من الخلايا في ورقة العمل**
في بعض الأحيان ، قد تحتاج إلى تنشيط ورقة عمل معينة بحيث تكون الأولى التي يتم عرضها عندما يفتح أحدهم الملف في Microsoft Excel. قد تحتاج أيضًا إلى تنشيط خلية معينة بحيث تقوم أشرطة التمرير بالتمرير إلى الخلية النشطة بحيث تكون مرئية بشكل واضح. يمكن لـ Aspose.Cells القيام بجميع المهام المذكورة أعلاه.

ورقة عمل نشطة هي الورقة التي تعمل عليها في عمل مجلد. يتم تحديدها بوضع سمين افتراضيًا. الخلية النشطة ، في الوقت نفسه ، هي الخلية التي تم تحديدها والتي يتم إدخال البيانات إليها عند بدء الكتابة. يمكن أن تكون خلية واحدة نشطة في وقت واحد. تحيط الخلية النشطة بحد سميك لجعلها مرئية بشكل واضح مقابل الخلايا الأخرى. تتيح أيضًا لك Aspose.Cells تحديد مجموعة من الخلايا في ورقة العمل.
### **تنشيط ورقة عمل وجعل خلية نشطة**
توفر Aspose.Cells واجهة برمجة تطبيقات محددة لهذه المهام. على سبيل المثال ، الطريقة WorksheetCollection.setActiveSheetIndex مفيدة لتحديد ورقة عمل نشطة. بالمثل ، تُستخدم الطريقة Worksheet.setActiveCell لتعيين والحصول على خلية نشطة في ورقة عمل.

إذا كنت ترغب في أن تتم تمرير شريطي التمرير الأفقي والرأسي إلى موضع فهرس الصف والعمود لإعطاء رؤية جيدة للبيانات المحددة عند فتح الملف في Microsoft Excel ، استخدم خصائص Worksheet.setFirstVisibleRow و Worksheet.setFirstVisibleColumn.

المثال التالي يوضح كيفية تنشيط ورقة عمل وجعل خلية فيها نشطة. يتم تمرير أشرطة التمرير لجعل صف وعمود الظاهر الخاصين أولاً كصف وعمود.

**تعيين الخلية B2 كخلية نشطة** 

![todo:image_alt_text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **اختيار مجموعة من الخلايا في ورقة العمل**
توفر Aspose.Cells الطريقة Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers). باستخدام المعلمة الأخيرة - removeOthers - إلى true ، يتم إزالة تحديدات الخلية أو مجموعة الخلايا الأخرى في الورقة.

يوضح المثال التالي كيفية تحديد مجموعة من الخلايا في ورقة العمل النشطة.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

جميع الفصول والطرق المذكورة أعلاه متاحة مع الإصدار المرخص من Aspose.Cells.

{{% /alert %}} 
## **تنسيق الصفوف والأعمدة**
تنسيق الصفوف والأعمدة في جدول بيانات لإعطاء تقرير مظهر هو أمين الميزة الأكثر استخداماً في تطبيق Excel. توفر واجهات برمجة تطبيقات Aspose.Cells أيضًا هذه الوظيفة من خلال نموذج بياناتها الذي يكشف في المقام الأول عن الفصل الذي يتعامل مع جميع الميزات المتعلقة بالتنسيقات مثل الشكل وسماته وتوجيه النص وألوان الخلفية / الأمامية ، الحدود ، عرض التنسيق للأرقام وتواريخ الأرقام وما إلى ذلك. فصل آخر مفيد توفره واجهات برمجة تطبيقات Aspose.Cells هو فصل التنسيق الذي يسمح بإعادة استخدام كائن التنسيق. 

في هذه المقالة ، سنحاول شرح كيفية استخدام Aspose.Cells for Java API لتطبيق التنسيق على الصفوف والأعمدة. 
### **تنسيق الصفوف والأعمدة**
توفر Aspose.Cells فصلاً ، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) الذي يمثل ملف Microsoft Excel. يحتوي فصل [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على مجموعة ورق عمل تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فصل Worksheet. يوفر فصل [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة Cells. توفر مجموعة Cells مجموعة Rows.
#### **تنسيق صف**
يمثل كل عنصر في مجموعة الصفوف كائن صف. يوفر كائن الصف طريقة applyStyle تستخدم لتطبيق التنسيق على صف.

لتطبيق نفس التنسيق على صف معين، استخدم كائن Style.

1. أضف كائن Style إلى فئة Workbook عبر استدعاء طريقة createStyle.
1. قم بتعيين خصائص كائن Style لتطبيق إعدادات التنسيق.
1. قم بتعيين كائن Style المكون للمصفوفة إلى طريقة applyStyle من كائن Row.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **تنسيق عمود**
مجموعة الخلايا توفر مجموعة أعمدة. كل عنصر في مجموعة الأعمدة يمثل كائن عمود. مماثل لكائن الصف، يوفر كائن العمود طريقة applyStyle المستخدمة لتعيين تنسيق العمود. استخدم طريقة applyStyle من كائن العمود لتنسيق عمود بنفس الطريقة المستخدمة لصف.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **تعيين تنسيق العرض للأرقام والتواريخ للصفوف والأعمدة**
إذا كانت الحاجة إلى تحديد تنسيق العرض للأرقام والتواريخ لصف أو عمود كاملة فإن العملية تقريباً مماثلة للأعلى، ولكن بدلاً من تعيين المعلمات لمحتويات النص، ستقوم بتعيين التنسيق للأرقام والتواريخ باستخدام خصائص Style.Number أو Style.Custom. يرجى الملاحظة أن خصائص Style.Number من نوع عدد صحيح وتشير إلى التنسيقات المدمجة للأرقام والتواريخ، بينما خصائص Style.Custom من نوع string وتقبل الأنماط الصالحة.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

يرجى التحقق من المقال المفصل على [تعيين تنسيقات الأرقام و [التواريخ](/cells/ar/java/data-formatting/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
