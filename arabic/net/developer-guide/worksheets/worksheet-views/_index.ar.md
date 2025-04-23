---
title: عروض الورقة العمل
type: docs
weight: 40
url: /ar/net/worksheet-views/
description: سيقوم هذا المقال بشرح كيفية استخدام C# و واجهة برمجة التطبيقات .NET للتفاعل مع معاينة استراحة الصفحة في سجل عمل إكسل وورقات العمل. يمكنك العمل باستخدام الأجزاء المقسمة، الأجزاء المجمدة، ومعامل التكبير. 
---

## **معاينة كسر الصفحة**

يمكن عرض جميع الصفحات العمل في وضعين:

- العرض العادي.
- معاينة كسر الصفحة.

عرض عادي هو العرض الافتراضي لصفحة العمل. معاينة فواصل الصفحات هي عرض تحرير يعرض صفحة العمل كما ستطبع. تعرض معاينة فواصل الصفحات البيانات التي ستظهر على كل صفحة حتى تتمكن من ضبط منطقة الطباعة وفواصل الصفحات. يمكن لمطورو Aspose.Cells تمكين العرض العادي أو وضع معاينة فواصل الصفحات.

### **التحكم في أوضاع العرض**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تتيح الوصول إلى كل صفحة عمل في ملف Excel.

يتمثل صفحة العمل في فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة صفحات العمل. لتمكين العرض العادي أو وضع معاينة فواصل الصفحات، استخدم [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مع [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview). [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) هو خاصية منطقية، مما يعني أنه يمكنها تخزين قيمة صحيحة أو خاطئة فقط.

#### **تمكين العرض العادي**

قم بتعيين صفحة العمل إلى العرض العادي عن طريق ضبط [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) الخاصية في فئة [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) إلى **false**.

#### **تمكين معاينة كسر الصفحة**

يمكن تعيين أي صفحة عمل إلى وضع معاينة فواصل الصفحات عن طريق ضبط [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) الخاصية في فئة [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) إلى **true**. بذلك يقوم بتبديل صفحة العمل من العرض العادي إلى معاينة فواصل الصفحات.

يلي أدناه مثال كامل يوضح كيفية استخدام [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) لتمكين وضع معاينة فواصل الصفحات لأول ورقة عمل في ملف Excel.

يتم فتح ملف book1.xls عن طريق إنشاء مثيل من فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). يتم تبديل العرض إلى معاينة فواصل الصفحات لأول ورقة عمل عن طريق ضبط [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) إلى **true**. يتم حفظ الملف المعدل باسم output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **عامل التكبير**

### **استخدام Microsoft Excel**

يوفر Microsoft Excel ميزة تتيح للمستخدمين تعيين عامل تكبير أو تدرج الورقة العمل. تساعد هذه الميزة المستخدمين في رؤية محتويات ورقة العمل في عروض أصغر أو أكبر. يمكن للمستخدمين تعيين عامل التكبير إلى أي قيمة.

### **Aspose.Cells وعامل التكبير**

تسمح Aspose.Cells للمطورين بتعيين عامل تكبير الورقة.
توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تتيح الوصول إلى كل صفحة عمل في ملف Excel.

تمثل صفحة العمل في فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة صفحات العمل. لتعيين عامل تكبير الورقة، استخدم [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) في فئة [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom). يتم تعيين عامل التكبير عن طريق تعيين قيمة رقمية (صحيحة) إلى الخاصية [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom).

يلي أدناه مثال كامل يوضح كيفية استخدام [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) لضبط عامل تكبير أول ورقة عمل في ملف Excel.

يتم فتح ملف book1.xls عن طريق إنشاء مثيل للفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). تُعين عامل التكبير للورقة العمل الأولى على 75 ويتم حفظ الملف المعدل ك output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **تجميد الألواح**

### **استخدام Microsoft Excel**

تجميد الألواح هو ميزة تقدمها مايكروسوفت إكسل. يتيح لك تجميد الألواح تحديد البيانات التي تظل مرئية عند التمرير في ورقة البيانات.

### **Aspose.Cells & تجميد الألواح**

تسمح Aspose.Cells للمطورين بتطبيق تجميد الألواح على ورق العمل أثناء التشغيل.

يوفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel.

تُمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورق العمل. لتكوين تجميد الألواح، قم بإيجاد طريقة [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) لفئة الورقة العمل. تأخذ الطريقة [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) المعلمات التالية:

- **الصف**، فهرس الصف للخلية التي سيبدأ منها التجميد.
- **العمود**، فهرس العمود للخلية التي سيبدأ منها التجميد.
- **الصفوف المجمدة**، عدد الصفوف المرئية في اللوحة العلوية.
- **الأعمدة المجمدة**، عدد الأعمدة المرئية في اللوحة اليسرى.

يتم فتح ملف book1.xls بالاتصال ببناء الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) أثناء إنشائه وتجميد عدد قليل من الصفوف والأعمدة في الورقة العمل الأولى. يتم حفظ الملف المعدل ك output.xls.

يتم تقديم مثال كامل أدناه يوضح كيفية استخدام الطريقة [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) لتجميد الصفوف والأعمدة (بداية من C4، الممثلة بالصف الرابع والعمود الثالث، حيث الصفوف والأعمدة تبدأ من فهرس 0) من ورقة العمل الأولى لملف Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **تقسيم الألواح**

إذا كنت بحاجة إلى تقسيم الشاشة للحصول على مناظر مختلفة في نفس ورقة البيانات، استخدم تقسيم الألواح. تقدم مايكروسوفت إكسل ميزة مفيدة تسمح لك بعرض أكثر من نسخة واحدة من ورقة البيانات الخاصة بك، وتمكنك من التمرير من خلال كل لوحة من ورقة البيانات بشكل مستقل: تقسيم الألواح.

الألواح تعمل بشكل متزامن. إذا قمت بإجراء تغيير في أحدها، فإن التغيير يظهر بشكل متزامن في الآخر. توفر Aspose.Cells ميزة تقسيم الألواح للمستخدمين.

### **تطبيق وإزالة تقسيم الألواح**

#### **تقسيم الألواح**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) مجموعة واسعة من الخصائص والأساليب لإدارة ملف Excel. لتنفيذ عروض متقسمة، استخدم [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) لفئة [**Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split). لإزالة تقسيم الألواح، استخدم الطريقة [**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit).

في المثال، نستخدم ملف قالب بسيط يتم تحميله، ثم يتم تطبيق ميزة تقسيم الألواح المحددة على خلية في الورقة البيانات الأولى. يتم حفظ الملف المحدث.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

بعد تشغيل الكود أعلاه، سيحتوي الملف الذي تم إنشاؤه على عرض مقسم.

#### **إزالة النوافذ**

قم بإزالة أجزاء الانقسام باستخدام الطريقة [**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **مواضيع متقدمة**
- [إخفاء عرض القيم الصفرية في صفحة العمل](/cells/ar/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [تعيين لون علامة تبويب الصفحة العمل](/cells/ar/net/set-worksheet-tab-color/)
- [إظهار وإخفاء خطوط الشبكة ورؤوس الصف والعمود](/cells/ar/net/show-and-hide-gridlines-and-row-column-headers/)
- [إظهار وإخفاء الصفوف والأعمدة وأشرطة التمرير](/cells/ar/net/show-and-hide-rows-columns-and-scroll-bars/)
- [إظهار وإخفاء الأوراق العمل وعلامات التبويب](/cells/ar/net/show-and-hide-worksheets-and-tabs/)
- [إظهار الصيغ بدلاً من القيم في ورقة العمل](/cells/ar/net/show-formulas-instead-of-values-in-a-worksheet/)
- [استخدام خيارات فحص الأخطاء](/cells/ar/net/use-error-checking-options/)

{{< app/cells/assistant language="csharp" >}}
