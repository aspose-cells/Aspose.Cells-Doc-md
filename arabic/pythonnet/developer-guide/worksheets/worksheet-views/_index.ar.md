---
title: عروض الورقة العمل
type: docs
weight: 40
url: /ar/python-net/worksheet-views/
description: ستصف هذه المقالة كيفية استخدام API Aspose.Cells لـ بايثون via .NET للتفاعل مع معاينة فاصل الصفحات في دفتر إكسل وورق العمل الخاص به. العمل مع اللوحات المنقسمة، والألواح المجمدة، ومعامل التكبير أيضًا. 
keywords: مكتبة إكسل بايثون، كيفية إعداد معاينة فاصل الصفحة، تمكين العرض العادي، تعيين معامل التكبير، تجميد الألواح، تقسيم الألواح، إزالة الألواح.
---

## **معاينة كسر الصفحة**

يمكن عرض جميع الصفحات العمل في وضعين:

- العرض العادي.
- معاينة كسر الصفحة.

العرض العادي هو العرض الافتراضي لورقة العمل. معاينة فاصل الصفحة هي عرض تحرير يعرض ورقة العمل كما ستطبع. تظهر معاينة فاصل الصفحة المعلومات التي ستُدرج على كل صفحة بحيث يمكنك تعديل منطقة الطباعة وفواصل الصفحات. باستخدام Aspose.Cells لـ بايثون via .NET يمكن للمطورين تمكين وضع العرض العادي أو وضع معاينة فاصل الصفحة.

### **التحكم في أوضاع العرض**

يوفر Aspose.Cells لـ بايثون via .NET فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) التي تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) تسمح بالوصول لكل ورقة عمل في ملف إكسل.

يتمثل صفحة العمل في فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة صفحات العمل. لتمكين العرض العادي أو وضع معاينة فواصل الصفحات، استخدم [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مع [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview). [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) هو خاصية منطقية، مما يعني أنه يمكنها تخزين قيمة صحيحة أو خاطئة فقط.

#### **تمكين العرض العادي**

قم بتعيين صفحة العمل إلى العرض العادي عن طريق ضبط [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) الخاصية في فئة [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) إلى **false**.

#### **تمكين معاينة كسر الصفحة**

يمكن تعيين أي صفحة عمل إلى وضع معاينة فواصل الصفحات عن طريق ضبط [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) الخاصية في فئة [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) إلى **true**. بذلك يقوم بتبديل صفحة العمل من العرض العادي إلى معاينة فواصل الصفحات.

يلي أدناه مثال كامل يوضح كيفية استخدام [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) لتمكين وضع معاينة فواصل الصفحات لأول ورقة عمل في ملف Excel.

يتم فتح ملف book1.xls عن طريق إنشاء مثيل من فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). يتم تبديل العرض إلى معاينة فواصل الصفحات لأول ورقة عمل عن طريق ضبط [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) إلى **true**. يتم حفظ الملف المعدل باسم output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-PageBreakPreview-1.py" >}}

## **عامل التكبير**

### **استخدام Microsoft Excel**

يوفر Microsoft Excel ميزة تتيح للمستخدمين تعيين عامل تكبير أو تدرج الورقة العمل. تساعد هذه الميزة المستخدمين في رؤية محتويات ورقة العمل في عروض أصغر أو أكبر. يمكن للمستخدمين تعيين عامل التكبير إلى أي قيمة.

### **Aspose.Cells وعامل التكبير**

تسمح Aspose.Cells للمطورين بتعيين عامل تكبير الورقة.
توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) التي تتيح الوصول إلى كل صفحة عمل في ملف Excel.

تمثل صفحة العمل في فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة صفحات العمل. لتعيين عامل تكبير الورقة، استخدم [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) في فئة [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom). يتم تعيين عامل التكبير عن طريق تعيين قيمة رقمية (صحيحة) إلى الخاصية [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom).

يلي أدناه مثال كامل يوضح كيفية استخدام [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) لضبط عامل تكبير أول ورقة عمل في ملف Excel.

يتم فتح ملف book1.xls عن طريق إنشاء مثيل للفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). تُعين عامل التكبير للورقة العمل الأولى على 75 ويتم حفظ الملف المعدل ك output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ZoomFactor-1.py" >}}

## **تجميد الألواح**

### **استخدام Microsoft Excel**

تجميد الألواح هو ميزة تقدمها مايكروسوفت إكسل. يتيح لك تجميد الألواح تحديد البيانات التي تظل مرئية عند التمرير في ورقة البيانات.

### **Aspose.Cells & تجميد الألواح**

تسمح Aspose.Cells للمطورين بتطبيق تجميد الألواح على ورق العمل أثناء التشغيل.

يوفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel.

تُمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورق العمل. لتكوين تجميد الألواح، قم بإيجاد طريقة [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) لفئة الورقة العمل. تأخذ الطريقة [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) المعلمات التالية:

- **صف**، مؤشر الصف حيث سيبدأ التجميد.
- **عمود**، مؤشر العمود حيث سيبدأ التجميد.
- **صفوف مجمدة**، عدد الصفوف المرئية في اللوحة العليا.
- **أعمدة مجمدة**، عدد الأعمدة المرئية في اللوحة اليسرى.

يتم فتح ملف book1.xls بالاتصال ببناء الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) أثناء إنشائه وتجميد عدد قليل من الصفوف والأعمدة في الورقة العمل الأولى. يتم حفظ الملف المعدل ك output.xls.

يتم تقديم مثال كامل أدناه يوضح كيفية استخدام الطريقة [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) لتجميد الصفوف والأعمدة (بداية من C4، الممثلة بالصف الرابع والعمود الثالث، حيث الصفوف والأعمدة تبدأ من فهرس 0) من ورقة العمل الأولى لملف Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-FreezePanes-1.py" >}}

## **تقسيم الألواح**

إذا كنت بحاجة إلى تقسيم الشاشة للحصول على مناظر مختلفة في نفس ورقة البيانات، استخدم تقسيم الألواح. تقدم مايكروسوفت إكسل ميزة مفيدة تسمح لك بعرض أكثر من نسخة واحدة من ورقة البيانات الخاصة بك، وتمكنك من التمرير من خلال كل لوحة من ورقة البيانات بشكل مستقل: تقسيم الألواح.

الألواح تعمل بشكل متزامن. إذا قمت بإجراء تغيير في أحدها، فإن التغيير يظهر بشكل متزامن في الآخر. توفر Aspose.Cells ميزة تقسيم الألواح للمستخدمين.

### **تطبيق وإزالة تقسيم الألواح**

#### **تقسيم الألواح**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) مجموعة واسعة من الخصائص والأساليب لإدارة ملف Excel. لتنفيذ عروض متقسمة، استخدم [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) لفئة [**split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split). لإزالة تقسيم الألواح، استخدم الطريقة [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split).

في المثال، نستخدم ملف قالب بسيط يتم تحميله، ثم يتم تطبيق ميزة تقسيم الألواح المحددة على خلية في الورقة البيانات الأولى. يتم حفظ الملف المحدث.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-SplitPanes-1.py" >}}

بعد تشغيل الكود أعلاه، سيحتوي الملف الذي تم إنشاؤه على عرض مقسم.

#### **إزالة النوافذ**

قم بإزالة أجزاء الانقسام باستخدام الطريقة [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-RemovePanes-1.py" >}}

## **مواضيع متقدمة**
- [إخفاء عرض القيم الصفرية في صفحة العمل](/cells/ar/python-net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [تعيين لون علامة تبويب الصفحة العمل](/cells/ar/python-net/set-worksheet-tab-color/)
- [إظهار وإخفاء خطوط الشبكة ورؤوس الصف والعمود](/cells/ar/python-net/show-and-hide-gridlines-and-row-column-headers/)
- [إظهار وإخفاء الصفوف والأعمدة وأشرطة التمرير](/cells/ar/python-net/show-and-hide-rows-columns-and-scroll-bars/)
- [إظهار وإخفاء الأوراق العمل وعلامات التبويب](/cells/ar/python-net/show-and-hide-worksheets-and-tabs/)
- [إظهار الصيغ بدلاً من القيم في ورقة العمل](/cells/ar/python-net/show-formulas-instead-of-values-in-a-worksheet/)
- [استخدام خيارات فحص الأخطاء](/cells/ar/python-net/use-error-checking-options/)

{{< app/cells/assistant language="python-net" >}}
