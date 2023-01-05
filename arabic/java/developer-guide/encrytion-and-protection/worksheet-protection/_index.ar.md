---
title: حماية وإلغاء حماية ورقة العمل
type: docs
weight: 50
url: /ar/java/protect-and-unprotect-worksheet/
---
## **حماية أوراق العمل**

عندما تكون ورقة العمل محمية ، يتم تقييد الإجراءات التي يمكن للمستخدم اتخاذها. على سبيل المثال ، لا يمكنهم إدخال البيانات أو إدراج أو حذف صفوف أو أعمدة وما إلى ذلك. خيارات الحماية العامة في Microsoft Excel هي:

- محتويات
- أشياء
- سيناريوهات

لا تخفي أوراق العمل المحمية البيانات الحساسة أو تحميها ، لذا فهي تختلف عن تشفير الملفات. بشكل عام ، تعد حماية ورقة العمل مناسبة لأغراض العرض. يمنع المستخدم النهائي من تعديل البيانات والمحتوى والتنسيق في ورقة العمل.

### **إضافة أو إزالة الحماية**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. تحتوي فئة المصنف على مجموعة أوراق العمل التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي.

 توفر فئة ورقة العمل ملف[**يحمي**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)) الطريقة المستخدمة لتطبيق الحماية على ورقة العمل. تقبل طريقة Protect المعلمات التالية:

-  نوع الحماية ، نوع الحماية المراد تطبيقها على ورقة العمل. يتم تطبيق نوع الحماية بمساعدة[**نوع الحماية**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType) تعداد.
- كلمة المرور الجديدة ، كلمة المرور الجديدة المستخدمة لحماية ورقة العمل.
- كلمة المرور القديمة ، كلمة المرور القديمة ، إذا كانت ورقة العمل محمية بكلمة مرور بالفعل. إذا لم تكن ورقة العمل محمية بالفعل ، فقم فقط بتمرير قيمة خالية.

يحتوي تعداد ProtectionType على أنواع الحماية المحددة مسبقًا التالية:

|**أنواع الحماية**|**وصف**|
|:- |:- |
|[**الكل**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|لا يمكن للمستخدم تعديل أي شيء في ورقة العمل هذه|
|[**محتويات**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|لا يمكن للمستخدم إدخال البيانات في ورقة العمل هذه|
|[**أشياء**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|لا يمكن للمستخدم تعديل الكائنات الرسومية|
|[**السيناريوهات**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|لا يمكن للمستخدم تعديل السيناريوهات المحفوظة|
|[**بنية**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|لا يمكن للمستخدم تعديل الهيكل المحفوظ|
|[**شبابيك**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|لا يمكن للمستخدم تعديل النوافذ المحفوظة|
|[**لا أحد**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|لا حماية|

يوضح المثال أدناه كيفية حماية ورقة العمل بكلمة مرور.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

بعد استخدام الكود أعلاه لحماية ورقة العمل ، تحقق من الحماية على ورقة العمل بفتحها. بمجرد فتح الملف ومحاولة إضافة بعض البيانات إلى ورقة العمل ، يتم عرض مربع الحوار التالي:

**مربع حوار يحذر من أن المستخدم لا يمكنه تعديل ورقة العمل** 

![ما يجب القيام به: image_بديل_نص](protect-and-unprotect-worksheet_1.png)

للعمل على ورقة العمل ، قم بإلغاء حماية ورقة العمل عن طريق تحديد ملف**حماية** ، ومن بعد**ورقة غير محمية** من**أدوات** عنصر القائمة كما هو موضح أدناه.

**تحديد عنصر قائمة Unprotect Sheet** 

![ما يجب القيام به: image_بديل_نص](protect-and-unprotect-worksheet_2.png)

يفتح مربع حوار للمطالبة بكلمة مرور.

**إدخال كلمة مرور لإلغاء حماية ورقة العمل** 

![ما يجب القيام به: image_بديل_نص](protect-and-unprotect-worksheet_3.png)

### **حماية قليلة Cells**

 قد تكون هناك سيناريوهات معينة تحتاج فيها إلى قفل بضع خلايا فقط في ورقة العمل. إذا كنت تريد قفل بعض الخلايا المحددة في ورقة العمل ، فيجب عليك إلغاء قفل جميع الخلايا الأخرى في ورقة العمل. تمت تهيئة جميع الخلايا الموجودة في ورقة العمل بالفعل للقفل ، يمكنك التحقق من فتح أي ملف Excel في MS Excel والنقر فوق الزر**تنسيق | Cells ...** ليعرض**شكل Cells** مربع الحوار ثم انقر فوق علامة التبويب "الحماية" وانظر إلى خانة الاختيار "مؤمن" محددة بشكل افتراضي.

فيما يلي طريقتان لتنفيذ المهمة.

**طريقة 1:**

توضح النقاط التالية كيفية قفل بعض الخلايا باستخدام MS Excel. تنطبق هذه الطريقة على Microsoft Office Excel 97 و 2000 و 2002 و 2003 والإصدارات الأحدث.

1. حدد ورقة العمل بأكملها بالنقر فوق الزر تحديد الكل (المستطيل الرمادي أعلى رقم الصف للصف 1 مباشرة وعلى يسار حرف العمود A).
1. انقر فوق Cells في قائمة "تنسيق" ، ثم انقر فوق علامة التبويب "حماية" ، ثم قم بإلغاء تحديد خانة الاختيار "مؤمن".

 هذا يفتح جميع الخلايا في ورقة العمل

{{% alert color="primary" %}}

إذا لم يكن أمر الخلايا متاحًا ، فقد تكون أجزاء من ورقة العمل مؤمنة بالفعل. من القائمة أدوات ، أشر إلى حماية ، ثم انقر فوق إلغاء حماية الورقة.

{{% /alert %}}

1. حدد فقط الخلايا التي تريد قفلها وكرر الخطوة 2 ، ولكن هذه المرة حدد خانة الاختيار مؤمن.
1.  على ال**أدوات** القائمة ، حدد**حماية** ، انقر**ورقة حماية** ، ثم انقر فوق**نعم**.

{{% alert color="primary" %}}

في مربع الحوار Protect Sheet ، لديك خيار تحديد كلمة مرور وتحديد العناصر التي تريد أن يتمكن المستخدمون من تغييرها.

{{% /alert %}}

**الطريقة 2:**

في هذه الطريقة ، نستخدم Aspose.Cells API فقط للقيام بالمهمة.

يوضح المثال التالي كيفية حماية بعض الخلايا في ورقة العمل. يقوم بإلغاء تأمين جميع الخلايا الموجودة في ورقة العمل أولاً ثم قفل 3 خلايا (A1 ، B1 ، C1) فيها. أخيرًا ، يحمي ورقة العمل. يحتوي الصف / العمود على نمط API يحتوي أيضًا على مجموعة Locked method. يمكنك استخدام هذه الطريقة لقفل أو إلغاء قفل الصف / العمود.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **حماية صف في ورقة العمل**

 Aspose.Cells يسمح لك بقفل أي صف في ورقة العمل بسهولة. هنا ، يمكننا الاستفادة من[**تطبيق نمط ()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) طريقة[**صف**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) فئة لتطبيق النمط على صف معين في ورقة العمل. تأخذ هذه الطريقة حجتين: أ[**أسلوب**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) كائن و[**النمط**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) الهيكل الذي يحتوي على جميع الأعضاء المتعلقين بالتنسيق المطبق.

يوضح المثال التالي كيفية حماية صف في ورقة العمل. يقوم بإلغاء تأمين جميع الخلايا الموجودة في ورقة العمل أولاً ثم يقفل الصف الأول فيها. أخيرًا ، يحمي ورقة العمل. يحتوي الصف / العمود على النمط API الذي يحتوي أيضًا على طريقة setCellLocked. يمكنك قفل أو إلغاء قفل الصف / العمود باستخدام بنية StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **حماية عمود في ورقة العمل**

 يسمح لك Aspose.Cells بقفل أي عمود في ورقة العمل بسهولة. هنا ، يمكننا الاستفادة من[**تطبيق نمط ()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) طريقة[**عمود**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) فئة لتطبيق النمط على عمود معين في ورقة العمل. تأخذ هذه الطريقة حجتين: أ[**أسلوب**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) كائن و[**النمط**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) الهيكل الذي يحتوي على جميع الأعضاء المتعلقين بالتنسيق المطبق.

يوضح المثال التالي كيفية حماية عمود في ورقة العمل. يقوم بإلغاء تأمين جميع الخلايا الموجودة في ورقة العمل أولاً ثم يقوم بتأمين العمود الأول فيها. أخيرًا ، يحمي ورقة العمل. يحتوي الصف / العمود على نمط API يحتوي أيضًا على مجموعة Locked method. يمكنك قفل أو إلغاء قفل الصف / العمود باستخدام بنية StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **قم بإلغاء حماية ورقة العمل**

[حماية أوراق العمل](/cells/ar/java/protect-and-unprotect-worksheet/#protect-worksheets) و[إعدادات الحماية المتقدمة منذ Excel XP](/cells/ar/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) ناقش مناهج مختلفة لحماية أوراق العمل. ماذا لو احتاج المطور إلى إزالة الحماية من ورقة عمل محمية في وقت التشغيل بحيث يمكن إجراء بعض التغييرات على الملف؟ يمكن القيام بذلك بسهولة باستخدام Aspose.Cells.

### **باستخدام Microsoft إكسل**

لإزالة الحماية من ورقة العمل:

 من**أدوات** القائمة ، حدد**حماية** تليها**ورقة غير محمية**.

**تحديد Unprotect Sheet** 

![ما يجب القيام به: image_بديل_نص](protect-and-unprotect-worksheet_4.png)

تتم إزالة الحماية ، ما لم تكن ورقة العمل محمية بكلمة مرور. في هذه الحالة ، سيطالبك مربع حوار بكلمة المرور.

**إدخال كلمة مرور لإلغاء حماية ورقة العمل** 

![ما يجب القيام به: image_بديل_نص](protect-and-unprotect-worksheet_5.png)

### **باستخدام Aspose.Cells**

 يمكن إلغاء حماية ورقة العمل عن طريق استدعاء ملف[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[**غير محمي**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect() ) طريقة. ال[**غير محمي**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect()) يمكن استخدام الطريقة بطريقتين ، كما هو موضح أدناه.

### **عدم حماية ورقة عمل محمية ببساطة**

ورقة العمل المحمية ببساطة هي ورقة غير محمية بكلمة مرور. يمكن أن تكون أوراق العمل غير محمية عن طريق استدعاء الأسلوب غير المحمي دون تمرير معلمة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **إلغاء حماية ورقة عمل محمية بكلمة مرور**

ورقة العمل المحمية بكلمة مرور هي ورقة محمية بكلمة مرور. يمكن إلغاء حماية أوراق العمل هذه عن طريق استدعاء إصدار محمّل بشكل زائد من أسلوب Unprotect الذي يأخذ كلمة المرور كمعامل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **إعدادات الحماية المتقدمة منذ Excel XP**

[حماية أوراق العمل](/cells/ar/java/protect-and-unprotect-worksheet/#protect-worksheets) ناقش موضوع حماية ورقة العمل في Microsoft Excel 97 و 2000. ولكن منذ إصدار Excel 2002 أو XP ، أضاف Microsoft العديد من إعدادات الحماية المتقدمة. تعمل إعدادات الحماية هذه على تقييد المستخدمين أو السماح لهم بما يلي:

- احذف الصفوف أو الأعمدة.
- تحرير المحتويات أو الكائنات أو السيناريوهات.
- تنسيق الخلايا أو الصفوف أو الأعمدة.
- قم بإدراج صفوف أو أعمدة أو ارتباطات تشعبية.
- حدد الخلايا المؤمنة أو غير المؤمنة.
- استخدم الجداول المحورية وغير ذلك الكثير.

يدعم Aspose.Cells كافة إعدادات الحماية المتقدمة التي يوفرها Excel XP والإصدارات الأحدث.

### **إعدادات الحماية المتقدمة باستخدام Excel XP والإصدارات الأحدث**

لعرض إعدادات الحماية المتوفرة في Excel XP:

1.  من**أدوات** القائمة ، حدد**حماية** تليها**ورقة حماية**.
 يتم عرض مربع حوار.

   **مربع حوار لإظهار خيارات الحماية في Excel XP**

![ما يجب القيام به: image_بديل_نص](protect-and-unprotect-worksheet_6.png)

1. السماح أو تقييد ميزات أوراق العمل أو تطبيق كلمة مرور.

### **إعدادات الحماية المتقدمة باستخدام Aspose.Cells**

Aspose.Cells يدعم كل إعدادات الحماية المتقدمة.

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. تحتوي فئة المصنف على مجموعة WorksheetCollection التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي.

 توفر فئة ورقة العمل خاصية الحماية المستخدمة لتطبيق إعدادات الحماية المتقدمة هذه. في الواقع ، تعتبر خاصية الحماية موضوعًا من[**حماية**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) فئة تضم العديد من الخصائص المنطقية لتعطيل القيود أو تمكينها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

يوجد أدناه مثال صغير للتطبيق. يفتح ملف Excel ويستخدم معظم إعدادات الحماية المتقدمة التي يدعمها Excel XP والإصدارات الأحدث.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

احفظ الملف بتنسيق EXCEL97TO2003 أو XLSX لأن إعدادات الحماية المتقدمة هذه مدعومة فقط بواسطة MS Excel XP والإصدارات الأحدث.

{{% /alert %}}

### **Cell مشكلة الإقفال**

إذا كنت تريد تقييد المستخدمين من تحرير الخلايا ، فيجب تأمين الخلايا قبل تطبيق أي إعدادات حماية. وإلا يمكن تحرير الخلايا حتى إذا كانت ورقة العمل محمية. في Microsoft Excel XP ، يمكن تأمين الخلايا من خلال مربع الحوار التالي:

**مربع حوار لتأمين الخلايا في Excel XP** 

![ما يجب القيام به: image_بديل_نص](protect-and-unprotect-worksheet_7.png)

من الممكن قفل الخلايا باستخدام Aspose.Cells API أيضًا. تحتوي كل خلية على نمط API يحتوي أيضًا على طريقة setLocked. استخدمه لقفل أو إلغاء قفل الخلايا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
