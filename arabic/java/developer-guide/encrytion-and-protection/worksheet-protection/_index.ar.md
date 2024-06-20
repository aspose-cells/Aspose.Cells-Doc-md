---
title: حماية وإلغاء الحماية لورق العمل
type: docs
weight: 50
url: /ar/java/protect-and-unprotect-worksheet/
---

## **حماية الأوراق العمل**

عندما تكون ورقة العمل محمية، تقتصر الإجراءات التي يمكن للمستخدم القيام بها. على سبيل المثال، لا يمكنه إدخال البيانات، أو إدراج أو حذف الصفوف أو الأعمدة إلخ. إجمالًا، الخيارات العامة للحماية في Microsoft Excel هي:

- المحتويات
- الكائنات
- السيناريوهات

الورقات المحمية لا تخفي أو تحمي البيانات الحساسة، لذا فإنها تختلف عن تشفير الملف. بشكل عام، حماية ورقة العمل مناسبة لأغراض العرض التقديمي. إنها تمنع المستخدم النهائي من تعديل البيانات والمحتوى والتنسيق في ورقة العمل.

### **إضافة أو إزالة الحماية**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة Workbook على مجموعة من الصفحات والتي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

توفر فئة الورقة العمل الطريقة [**Protect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)) التي تستخدم لتطبيق الحماية على ورقة عمل. تقبل الطريقة Protect المعلمات التالية:

- نوع الحماية، نوع الحماية المطبقة على ورقة العمل. يتم تطبيق نوع الحماية بمساعدة تعداد [**ProtectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType).
- كلمة المرور الجديدة ، كلمة المرور الجديدة المستخدمة لحماية ورقة العمل.
- كلمة مرور قديمة، كلمة المرور القديمة، إذا كانت ورقة العمل محمية بالفعل بكلمة مرور. إذا لم تكن ورقة العمل محمية بكلمة مرور بالفعل، فقط قم بتمرير قيمة فارغة.

تحتوي تعداد ProtectionType على أنواع الحمايات المحددة مسبقًا التالية:

|**أنواع الحماية**|**الوصف**|
| :- | :- |
|[**ALL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|لا يمكن للمستخدم تعديل أي شيء على هذه الورقة
|[**CONTENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|لا يمكن للمستخدم إدخال البيانات في هذه الورقة
|[**OBJECTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|لا يمكن للمستخدم تعديل كائنات الرسم
|[**SCENARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|لا يمكن للمستخدم تعديل السيناريوهات المحفوظة
|[**STRUCTURE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|لا يمكن للمستخدم تعديل الهيكل المحفوظ
|[**WINDOWS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|لا يمكن للمستخدم تعديل النوافذ المحفوظة
|[**NONE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|لا حماية

المثال أدناه يوضح كيفية حماية ورقة عمل بكلمة مرور.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

بعد استخدام الكود أعلاه لحماية ورقة العمل، تحقق من الحماية على ورقة العمل عن طريق فتحها. بمجرد فتح الملف ومحاولة إضافة بعض البيانات إلى ورقة العمل، يتم عرض الحوار التالي:

**تحذير يفيد بعدم إمكانية للمستخدم تعديل ورقة العمل** 

![todo:image_alt_text](protect-and-unprotect-worksheet_1.png)

للعمل على ورقة العمل، قم بإلغاء حماية الورقة العمل بتحديد **الحماية** ثم **إلغاء حماية الورقة** من عنصر قائمة **الأدوات** كما هو موضح أدناه.

**اختيار عنصر قائمة إلغاء حماية الورقة** 

![todo:image_alt_text](protect-and-unprotect-worksheet_2.png)

يتم فتح حوار يطالب بكلمة مرور.

**إدخال كلمة المرور لإلغاء حماية الورقة** 

![todo:image_alt_text](protect-and-unprotect-worksheet_3.png)

### **حماية بعض الخلايا**

قد تكون هناك حالات معينة حيث تحتاج إلى قفل بعض الخلايا فقط في ورقة العمل. إذا كنت ترغب في قفل بعض الخلايا المحددة في ورقة العمل، يجب أن تقوم بفتح جميع الخلايا الأخرى في ورقة العمل. جميع الخلايا في ورقة العمل مهيئة مسبقًا للقفل، يمكنك التحقق من هذا بفتح أي ملف إكسيل في برنامج مايكروسوفت إكسيل والنقر على **التنسيق|الخلايا...** لعرض حوار مربع **تنسيق الخلايا** ثم النقر على علامة التبويب **الحماية** ورؤية خانة اختيار مسمى "مقفل" محددة افتراضيًا.

فيما يلي الطريقتان لتنفيذ المهمة.

**الطريقة1:**

تصف النقاط التالية كيفية قفل بعض الخلايا باستخدام MS Excel. ينطبق هذا الأسلوب على Microsoft Office Excel 97 و 2000 و 2002 و 2003 والإصدارات الأحدث.

1. حدد جدول البيانات بالكامل عن طريق النقر فوق زر تحديد الكل (المستطيل الرمادي مباشرة فوق رقم الصف للصف 1 وعلى اليسار من رقم العمود للعمود A).
1. انقر على الخلايا في قائمة التنسيق، ثم انقر على علامة التبويب الحماية، ثم قم بإلغاء تحديد خانة القفل.

   هذا يفتح جميع الخلايا على الورقة العمل

{{% alert color="primary" %}}

إذا كانت عملية الخلايا غير متوفرة، قد يكون أجزاء من جدول البيانات قد تم تأمينها بالفعل. في قائمة الأدوات، حدد حماية، ثم انقر على إزالة حماية الورقة.

{{% /alert %}}

1. حدد فقط الخلايا التي تريد تأمينها وكرر الخطوة 2، ولكن هذه المرة حدد خانة القفل.
1. في قائمة **الأدوات**، حدد **الحماية**، انقر على **حماية الورقة**، ثم انقر على **موافق**.

{{% alert color="primary" %}}

في مربع حوار حماية الورقة، لديك الخيار لتحديد كلمة مرور واختيار العناصر التي ترغب في أن يكون بإمكان المستخدمين تغييرها.

{{% /alert %}}

**الأسلوب2:**

في هذه الطريقة، نستخدم واجهة برمجة التطبيقات Aspose.Cells فقط للقيام بالمهمة.

المثال التالي يوضح كيفية تأمين بعض الخلايا في جدول البيانات. يتم فتح جميع الخلايا في جدول البيانات أولاً ثم يتم تأمين 3 خلايا (A1، B1، C1) فيه. أخيرًا، يتم حماية جدول البيانات. تحتوي الصف/العمود على واجهة برمجة التطبيقات (API) تحتوي بدورها على طريقة Locked. يمكنك استخدام هذه الطريقة لتأمين أو فتح الصف/العمود.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **حماية صف في ورقة العمل**

تسمح Aspose.Cells لك بقفل أي صف بسهولة في ورقة العمل. هنا، يمكننا الاستفادة من طريقة [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) في فئة [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) لتطبيق النمط على صف معين في ورقة العمل. تأخذ هذه الطريقة معها معلمتين: كائن [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) وهيكل [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) الذي يحتوي على جميع أعضاء التنسيق المطبقة.

يوضح المثال التالي كيفية تأمين صف في جدول البيانات. يتم فتح جميع الخلايا في جدول البيانات أولاً ثم يتم تأمين الصف الأول فيه. أخيرًا، يتم حماية جدول البيانات. تحتوي الصف/العمود على واجهة برمجة التطبيقات (API) الخاصة بها التي تحتوي على طريقة setCellLocked. يمكنك تأمين أو فتح الصف/العمود باستخدام هيكل StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **حماية عمود في ورقة العمل**

تسمح Aspose.Cells لك بقفل أي عمود بسهولة في ورقة العمل. هنا، يمكننا الاستفادة من الطريقة [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)) في فئة [**Column**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) لتطبيق النمط على عمود معين في ورقة العمل. تأخذ هذه الطريقة معها معلمتين: كائن [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) وهيكل [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) الذي يحتوي على جميع أعضاء التنسيق المطبقة.

يوضح المثال التالي كيفية تأمين عمود في جدول البيانات. يتم فتح جميع الخلايا في جدول البيانات أولاً ثم يتم تأمين العمود الأول فيه. أخيرًا، يتم حماية جدول البيانات. تحتوي الصف/العمود على واجهة برمجة التطبيقات (API) الخاصة بها التي تحتوي على طريقة setCellLocked. يمكنك تأمين أو فتح الصف/العمود باستخدام هيكل StyleFlag.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **إلغاء حماية ورقة العمل**

[حماية أوراق البيانات](/cells/ar/java/protect-and-unprotect-worksheet/#protect-worksheets) و[إعدادات الحماية المتقدمة منذ إكسل XP](/cells/ar/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) يناقشان أساليب مختلفة لحماية أوراق البيانات. ماذا لو احتاج المطور إلى إزالة الحماية من ورقة بيانات محمية أثناء التشغيل حتى يمكن إجراء بعض التغييرات على الملف؟ يمكن القيام بذلك بسهولة باستخدام Aspose.Cells.

### **استخدام Microsoft Excel**

لإزالة الحماية من ورقة العمل:

من قائمة **الأدوات**, حدد **الحماية** تلاها **إلغاء حماية الورقة**.

**تحديد إلغاء حماية الورقة** 

![todo:image_alt_text](protect-and-unprotect-worksheet_4.png)

يتم إزالة الحماية، ما لم تكن الورقة منحماة بكلمة مرور. في هذه الحالة، يتم توجيه صندوق حوار لإدخال كلمة المرور.

**إدخال كلمة المرور لإلغاء حماية الورقة** 

![todo:image_alt_text](protect-and-unprotect-worksheet_5.png)

### **استخدام Aspose.Cells**

يمكن إلغاء حماية الورقة عن طريق استدعاء فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) وطريقة [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--). يمكن استخدام الطريقة [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--) بطريقتين، كما هو موضح أدناه.

### **إلغاء حماية ورقة محمية بشكل بسيط**

ورقة محمية بشكل بسيط هي ورقة ليست محمية بكلمة مرور. يمكن إلغاء حماية مثل هذه الأوراق عن طريق استدعاء الطريقة unprotect بدون تمرير معلمة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **إلغاء حماية ورقة محمية بكلمة مرور**

ورقة محمية بكلمة مرور هي واحدة محمية بكلمة المرور. يمكن إلغاء حماية مثل هذه الأوراق عن طريق استدعاء النسخة المحمية من طريقة Unprotect التي تأخذ كلمة المرور كمعلمة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **إعدادات الحماية المتقدمة منذ Excel XP**

[حماية الأوراق](/cells/ar/java/protect-and-unprotect-worksheet/#protect-worksheets) تناول حماية الورقة في Microsoft Excel 97 و 2000. ولكن منذ إصدار Excel 2002 أو XP، أضافت Microsoft العديد من إعدادات الحماية المتقدمة. تقوم هذه الإعدادات بتقييد أو السماح للمستخدمين بـ:

- حذف الصفوف أو الأعمدة.
- تحرير المحتويات أو الكائنات أو السيناريوهات.
- تنسيق الخلايا أو الصفوف أو الأعمدة.
- إدراج الصفوف أو الأعمدة أو الروابط الفرعية.
- تحديد الخلايا المقفلة أو غير المقفلة.
- استخدام الجداول المحورية وأكثر من ذلك بكثير.

Aspose.Cells يدعم جميع إعدادات الحماية المتقدمة المقدمة من قبل Excel XP والإصدارات اللاحقة.

### **إعدادات الحماية المتقدمة باستخدام Excel XP والإصدارات اللاحقة**

لعرض إعدادات الحماية المتاحة في Excel XP:

1. من القائمة **الأدوات**, حدد **الحماية** تلاها **حماية الورقة**.
   يتم عرض مربع حوار.

   **مربع حوار لإظهار خيارات الحماية في Excel XP**

![todo:image_alt_text](protect-and-unprotect-worksheet_6.png)

1. السماح أو تقييد ميزات صفحات العمل أو تطبيق كلمة مرور.

### **إعدادات الحماية المتقدمة باستخدام Aspose.Cells**

تدعم Aspose.Cells جميع إعدادات الحماية المتقدمة.

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة Workbook على مجموعة WorksheetCollection تتيح الوصول إلى كل صفحة عمل (ورقة عمل) في ملف Excel. تُمثّل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

يوفر فئة Worksheet خاصية Protection التي تُستخدم لتطبيق هذه الإعدادات المتقدمة للحماية. تكون خاصية Protection في الواقع كائنًا من فئة [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) الذي يغلّف عدة خصائص بوليانية لتمكين أو تعديل القيود.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

فيما يلي مثال تطبيقي صغير. يفتح ملف Excel ويستخدم معظم إعدادات الحماية المتقدمة المدعومة من Excel XP والإصدارات اللاحقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

احفظ الملف بتنسيق EXCEL97TO2003 أو XLSX لأن هذه الإعدادات المتقدمة للحماية مدعومة فقط بواسطة MS Excel XP والإصدارات اللاحقة.

{{% /alert %}}

### **مشكلة قفل الخلية**

إذا كنت ترغب في تقييد مستخدمين من تحرير الخلايا يجب أن تكون الخلايا مقفلة قبل تطبيق أي إعدادات حماية. وإلا يمكن تحرير الخلايا حتى لو تم حماية صفحة العمل. في Microsoft Excel XP، يمكن قفل الخلايا من خلال مربع الحوار التالي:

**مربع حوار لقفل الخلايا في Excel XP** 

![todo:image_alt_text](protect-and-unprotect-worksheet_7.png)

من الممكن قفل الخلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells أيضًا. كل خلية تحتوي على واجهة برمجة تطبيقات Style تحتوي بدورها على طريقة setLocked. استخدمها لقفل أو فتح الخلايا.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
