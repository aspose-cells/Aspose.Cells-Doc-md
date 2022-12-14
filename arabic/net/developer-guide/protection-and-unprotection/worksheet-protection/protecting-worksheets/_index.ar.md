---
title: حماية أوراق العمل
type: docs
weight: 10
url: /ar/net/protecting-worksheets/
---
{{% alert color="primary" %}}

عندما تكون ورقة العمل محمية ، يتم تقييد الإجراءات التي يمكن للمستخدم اتخاذها. على سبيل المثال ، لا يمكنهم إدخال البيانات أو إدراج أو حذف صفوف أو أعمدة وما إلى ذلك.

{{% /alert %}}

## **حماية أوراق العمل**

### **مقدمة**

خيارات الحماية العامة في Microsoft Excel هي:

- محتويات
- أشياء
- سيناريوهات

لا تخفي أوراق العمل المحمية البيانات الحساسة أو تحميها ، لذا فهي تختلف عن تشفير الملفات. بشكل عام ، تعد حماية ورقة العمل مناسبة لأغراض العرض. يمنع المستخدم النهائي من تعديل البيانات والمحتوى والتنسيق في ورقة العمل.

### **حماية ورقة العمل**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) الذي يمثل ملف إكسل Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)صف دراسي.

 ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)فئة توفر[**يحمي**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) الطريقة المستخدمة لتطبيق الحماية على ورقة العمل.[**يحمي**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) تقبل الطريقة المعلمات التالية:

-  نوع الحماية ، نوع الحماية المراد تطبيقها على ورقة العمل. يتم تطبيق نوع الحماية بمساعدة[**نوع الحماية**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)تعداد.
- كلمة المرور الجديدة ، كلمة المرور الجديدة المستخدمة لحماية ورقة العمل.
- كلمة المرور القديمة ، كلمة المرور القديمة ، إذا كانت ورقة العمل محمية بكلمة مرور بالفعل. إذا لم تكن ورقة العمل محمية بالفعل ، فقم فقط بتمريرها فارغة.

 ال[**نوع الحماية**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)يحتوي التعداد على أنواع الحماية المحددة مسبقًا التالية:

|**أنواع الحماية**|**وصف**|
|:- |:- |
|الجميع|لا يمكن للمستخدم تعديل أي شيء في ورقة العمل هذه|
|محتويات|لا يمكن للمستخدم إدخال البيانات في ورقة العمل هذه|
|أشياء|لا يمكن للمستخدم تعديل الكائنات الرسومية|
|سيناريوهات|لا يمكن للمستخدم تعديل السيناريوهات المحفوظة|
|بنية|لا يمكن للمستخدم تعديل الهيكل|
|Windows|يتم تطبيق الحماية على النوافذ|
|لا أحد|لا يتم تطبيق الحماية|

يوضح المثال أدناه كيفية حماية ورقة العمل بكلمة مرور.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

بعد استخدام الكود أعلاه لحماية ورقة العمل ، يمكنك التحقق من الحماية على ورقة العمل عن طريق فتحها. بمجرد فتح الملف ومحاولة إضافة بعض البيانات إلى ورقة العمل ، سترى مربع الحوار التالي:

|**مربع حوار يحذر من أن المستخدم لا يمكنه تعديل ورقة العمل**|
|:- |
|![ما يجب القيام به: image_بديل_نص](protecting-worksheets_1.png)|

للعمل على ورقة العمل ، قم بإلغاء حماية ورقة العمل عن طريق تحديد ملف**حماية** ، ومن بعد**ورقة غير محمية** من**أدوات** عنصر القائمة.

بعد تحديد عنصر قائمة Unprotect Sheet ، سيتم فتح مربع حوار يطالبك بإدخال كلمة المرور حتى تتمكن من العمل في ورقة العمل كما هو موضح أدناه:

|![ما يجب القيام به: image_بديل_نص](protecting-worksheets_2.png)|

### **قم بحماية بعض Cells في ورقة العمل باستخدام Microsoft Excel**

 قد تكون هناك سيناريوهات معينة تحتاج فيها إلى قفل بضع خلايا فقط في ورقة العمل. إذا كنت تريد قفل بعض الخلايا المحددة في ورقة العمل ، فيجب عليك إلغاء قفل جميع الخلايا الأخرى في ورقة العمل. تمت تهيئة جميع الخلايا الموجودة في ورقة العمل بالفعل للقفل ، يمكنك التحقق من فتح أي ملف Excel في MS Excel والنقر فوق الزر**تنسيق | Cells ...** ليعرض**شكل Cells**مربع الحوار ثم انقر فوق**حماية** علامة التبويب وشاهد مربع الاختيار المسمى "مغلق" محددًا بشكل افتراضي.

توضح النقاط التالية كيفية قفل بعض الخلايا باستخدام MS Excel. تنطبق هذه الطريقة على Microsoft Office Excel 97 و 2000 و 2002 و 2003 والإصدارات الأحدث.

1.  حدد ورقة العمل بأكملها بالنقر فوق**اختر الكل** زر (المستطيل الرمادي أعلى رقم الصف مباشرة للصف 1 وعلى يسار حرف A من العمود).
1.  انقر**Cells** على ال**شكل** القائمة ، انقر فوق**حماية** علامة التبويب ، ثم قم بإلغاء تحديد**مقفل** خانة الاختيار.
 هذا يفتح جميع الخلايا في ورقة العمل
 إذا كان**Cells** الأمر غير متوفر ، فقد تكون أجزاء من ورقة العمل مؤمنة بالفعل. على ال**أدوات** القائمة ، أشر إلى**حماية** ، ثم انقر فوق**ورقة غير محمية**.
1.  حدد فقط الخلايا التي تريد قفلها وكرر الخطوة 2 ، ولكن هذه المرة حدد ملف**مقفل** خانة الاختيار.
1.  على ال**أدوات** القائمة ، أشر إلى**حماية** ، انقر**ورقة حماية** ثم انقر فوق**نعم**.
1.  في ال**ورقة حماية** في مربع الحوار ، لديك خيار تحديد كلمة مرور وتحديد العناصر التي تريد أن يتمكن المستخدمون من تغييرها.

### **قم بحماية بعض Cells في ورقة العمل باستخدام Aspose Cells**

في هذه الطريقة ، نستخدم Aspose.Cells API فقط للقيام بالمهمة.

 مثال: يوضح المثال التالي كيفية حماية بعض الخلايا في ورقة العمل. يقوم بإلغاء تأمين جميع الخلايا الموجودة في ورقة العمل أولاً ثم قفل 3 خلايا (A1 ، B1 ، C1) فيها. أخيرًا ، يحمي ورقة العمل. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style)يحتوي الكائن على خاصية منطقية ،[**مقفل**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . يمكنك ضبط[**مقفل**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) الخاصية إلى صح أو خطأ وتطبيقها*العمود / الصف.* طريقة لقفل أو إلغاء قفل الصف / العمود بالسمات التي تريدها.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **حماية صف في ورقة العمل**

 Aspose.Cells يسمح لك بقفل أي صف في ورقة العمل بسهولة. هنا ، يمكننا الاستفادة من[**تطبيق ستايل ()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) طريقة[**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) فئة للتطبيق[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) إلى صف معين في ورقة العمل. تأخذ هذه الطريقة حجتين: أ[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) كائن و[**النمط**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) الكائن الذي يحتوي على جميع الأعضاء المرتبطين بالتنسيق المطبق.

 يوضح المثال التالي كيفية حماية صف في ورقة العمل. يقوم بإلغاء تأمين جميع الخلايا الموجودة في ورقة العمل أولاً ثم يقفل الصف الأول فيها. أخيرًا ، يحمي ورقة العمل. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) يحتوي الكائن على خاصية منطقية ،[**مقفل**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . يمكنك ضبط[**مقفل**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) الخاصية إلى صواب أو خطأ لقفل أو إلغاء قفل الصف / العمود باستخدام[**النمط**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)هدف.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **حماية عمود في ورقة العمل**

 يسمح لك Aspose.Cells بقفل أي عمود في ورقة العمل بسهولة. هنا ، يمكننا الاستفادة من[**تطبيق ستايل ()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) طريقة[**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) فئة للتطبيق[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) إلى عمود معين في ورقة العمل. تأخذ هذه الطريقة حجتين: أ[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) كائن و[**النمط**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)الكائن الذي يحتوي على جميع الأعضاء المرتبطين بالتنسيق المطبق.

يوضح المثال التالي كيفية حماية عمود في ورقة العمل. يقوم بإلغاء تأمين جميع الخلايا الموجودة في ورقة العمل أولاً ثم يقوم بتأمين العمود الأول فيها. أخيرًا ، يحمي ورقة العمل. ال[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) يحتوي الكائن على خاصية منطقية ،[**مقفل**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . يمكنك ضبط[**مقفل**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) الخاصية إلى صواب أو خطأ لقفل أو إلغاء قفل الصف / العمود باستخدام[**النمط**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)هدف.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **السماح للمستخدمين بتحرير النطاقات**

يوضح المثال التالي كيفية السماح للمستخدمين بتحرير نطاق في ورقة عمل محمية.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
