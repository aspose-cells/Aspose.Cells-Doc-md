---
title: حماية الأوراق العمل
type: docs
weight: 10
url: /ar/net/protecting-worksheets/
---

{{% alert color="primary" %}}

عندما تكون ورقة العمل محمية ، يتم تقييد الإجراءات التي يمكن للمستخدم اتخاذها. على سبيل المثال ، لا يمكنهم إدخال البيانات ، أو إدراج أو حذف الصفوف أو الأعمدة إلخ.

{{% /alert %}}

## **حماية الأوراق العمل**

### **مقدمة**

خيارات الحماية العامة في Microsoft Excel هي:

- المحتويات
- الكائنات
- السيناريوهات

لاتخفي أوراق العمل المحمية البيانات الحساسة أو تحميها ، لذا فإنها تختلف عن تشفير الملف. بشكل عام ، يعتبر حماية ورقة العمل مناسبة لأغراض العرض. فهي تمنع المستخدم النهائي من تعديل البيانات والمحتوى والتنسيق في ورقة العمل.

### **حماية ورقة العمل**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) الطريقة [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) التي تُستخدم لتطبيق الحماية على ورقة العمل. تقبل الطريقة [**Protect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) المعلمات التالية:

- نوع الحماية ، نوع الحماية المطبقة على ورقة العمل. يتم تطبيق نوع الحماية بمساعدة تعداد [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype).
- كلمة المرور الجديدة ، كلمة المرور الجديدة المستخدمة لحماية ورقة العمل.
- كلمة المرور القديمة ، كلمة المرور السابقة ، إذا كانت ورقة العمل محمية بكلمة مرور بالفعل. إذا لم تكن ورقة العمل محمية بكلمة مرور بالفعل ، فقط قم بتمرير قيمة فارغة.

يحتوي تعداد [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype) على أنواع حماية محددة مسبقًا التالية:

|**أنواع الحماية**|**الوصف**|
| :- | :- |
|All| لا يمكن للمستخدم تعديل أي شيء على هذه الورقة العمل|
|Contents| لا يمكن للمستخدم إدخال بيانات في هذه الورقة العمل|
|Objects| لا يمكن للمستخدم تعديل أجسام الرسم|
|Scenarios| لا يمكن للمستخدم تعديل السيناريوهات المحفوظة|
|Structure| لا يمكن للمستخدم تعديل الهيكل|
|Windows| تم تطبيق الحماية على النوافذ|
|None| لا يوجد تطبيق للحماية|

المثال أدناه يوضح كيفية حماية ورقة عمل بكلمة مرور.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

بعد استخدام الكود أعلاه لحماية الورقة العمل، يمكنك التحقق من الحماية على الورقة العمل عن طريق فتحها. بمجرد فتح الملف ومحاولة إضافة بعض البيانات إلى الورقة العمل، ستظهر لك نافذة التالي:

|**تحذير الذي يظهر عندما لا يستطيع المستخدم تعديل الورقة العمل**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

للعمل على الورقة العمل، قم بإلغاء حمايتها عن طريق تحديد **Protection**، ثم **Unprotect Sheet** من عنصر القائمة **Tools**.

بعد اختيار عنصر القائمة Unprotect Sheet، ستفتح نافذة تطالبك بإدخال كلمة المرور حتى تتمكن من العمل على الورقة العمل كما هو موضح أدناه:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **حماية خلايا قليلة في الورقة العمل باستخدام Microsoft Excel**

قد توجد حالات معينة حيث تحتاج إلى قفل بعض الخلايا فقط في الورقة العمل. إذا كنت ترغب في قفل بعض الخلايا المحددة في الورقة العمل، عليك أن تقوم بفتح كافة الخلايا الأخرى في الورقة العمل. جميع الخلايا في الورقة العمل تم تهيئتها بالفعل للقفل، يمكنك التحقق من ذلك عن طريق فتح أي ملف Excel في MS Excel والنقر على **Format | Cells...** لعرض صندوق الحوار **Format Cells** ثم النقر على علامة التبويب **Protection** ومن ثم رؤية مربع الاختيار المسمى "مقفل" يكون محددًا افتراضيًا.

تصف النقاط التالية كيفية قفل بعض الخلايا باستخدام MS Excel. ينطبق هذا الأسلوب على Microsoft Office Excel 97 و 2000 و 2002 و 2003 والإصدارات الأحدث.

1. حدد الورقة العمل بأكملها بالنقر على زر **Select All** (المستطيل الرمادي مباشرة فوق رقم الصف للصف 1 وعند اليسار من حرف العمود A).
1. انقر على **Cells** في القائمة **Format**، انقر على علامة التبويب **Protection**، ثم قم بإلغاء تحديد مربع الاختيار **Locked**.
   هذا يفتح جميع الخلايا على الورقة العمل
   إذا كانت الأمر **Cells** غير متاح، فقد يكون بعض أجزاء الورقة العمل مقفلة بالفعل. في القائمة **Tools**، قم بتوجيه المؤشر إلى **Protection**، ثم انقر على **Unprotect Sheet**.
1. حدد فقط الخلايا التي ترغب في قفلها وكرر الخطوة 2، ولكن هذه المرة حدد مربع الاختيار **Locked**.
١. في قائمة الـ**أدوات**, حدد **الحماية**, انقر فوق **حماية الورقة** ثم انقر فوق **موافق**.
١. في مربع حوار **حماية الورقة**, لديك الخيار لتحديد كلمة المرور واختيار العناصر التي ترغب في أن يتمكن المستخدمون من تغييرها.

### **حماية خلايا قليلة في ورقة العمل باستخدام Aspose Cells**

في هذه الطريقة، نستخدم واجهة برمجة التطبيقات Aspose.Cells فقط للقيام بالمهمة.

مثال: يوضح المثال التالي كيفية حماية عدد قليل من الخلايا في ورقة العمل. يقوم بإلغاء قفل كافة الخلايا في الورقة أولاً ثم يقفل 3 خلايا (A1، B1، C1) فيها. أخيرًا، يحمي الورقة. يحتوي الكائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) على خاصية منطقية، [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). يمكنك تعيين الخاصية [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) إلى القيمة صحيح أو خاطئ وتطبيق طريقة *Column/Row.ApplyStyle()* لقفل أو فتح الصف/العمود بالسمات المطلوبة.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **حماية صف في ورقة العمل**

تُتيح Aspose.Cells لك قفل أي صف بسهولة في ورقة العمل. هنا، يمكننا استخدام طريقة [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) من فئة [**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) لتطبيق [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) على صف معين في ورقة العمل. تأخذ هذه الطريقة معها مُعاملين: كائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) وكائن [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) واللذان يحتويان على جميع الأعضاء المتعلقة بالتنسيق المطبق.

يُظهر المثال التالي كيفية حماية صف في ورقة العمل. يقوم بإلغاء قفل كافة الخلايا في الورقة أولاً ثم يقفل الصف الأول فيها. أخيرًا، يحمي الورقة. يحتوي الكائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) على خاصية منطقية، [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). يمكنك تعيين الخاصية [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) إلى القيمة صحيح أو خاطئ لقفل أو فتح الصف/العمود باستخدام كائن [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **حماية عمود في ورقة العمل**

تُتيح Aspose.Cells لك بسهولة قفل أي عمود في ورقة العمل. هنا، يمكننا استخدام طريقة [**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) من فئة [**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) لتطبيق [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) على عمود معين في ورقة العمل. تأخذ هذه الطريقة معها مُعاملين: كائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) وكائن [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) واللذان يحتويان على جميع الأعضاء المتعلقة بالتنسيق المطبق.

يُظهر المثال التالي كيفية حماية عمود في ورقة العمل. يقوم بإلغاء قفل كافة الخلايا في الورقة أولاً ثم يقفل العمود الأول فيه. أخيرًا، يحمي الورقة. يحتوي الكائن [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) على خاصية منطقية، [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). يمكنك تعيين الخاصية [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) إلى القيمة صحيح أو خاطئ لقفل أو فتح الصف/العمود باستخدام كائن [**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **السماح للمستخدمين بتعديل المدى**

يُظهر المثال التالي كيفية السماح للمستخدمين بتعديل مدى محدد في ورقة العمل الخاصة.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
