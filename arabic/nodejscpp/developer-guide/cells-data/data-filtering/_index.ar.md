---
title: تصفية البيانات
type: docs
weight: 85
url: /ar/nodejs-cpp/data-filtering/
description: تعلم كيفية إضافة مرشح بيانات باستخدام واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: إضافة مرشح بواسطة اللون باستخدام Node.js عبر C++، إضافة مرشحات التاريخ باستخدام Node.js عبر C++، إضافة مرشحات رقمية باستخدام Node.js عبر C++، إضافة مرشح ديناميكي باستخدام Node.js عبر C++، إضافة مرشحات نصية باستخدام Node.js عبر C++، إضافة مرشح مخصص ب contains باستخدام Node.js عبر C++، إضافة مرشح مخصص ب NotContains باستخدام Node.js عبر C++، إضافة مرشح مخصص ب BeginsWith باستخدام Node.js عبر C++، إضافة مرشح مخصص ب EndsWith باستخدام C++
---

{{% alert color="primary" %}}
يوفر Microsoft Excel بعض الميزات الجيدة لفلترة البيانات تلقائيًا في ورقة العمل. يدعم Aspose.Cells بشكل كامل ميزات التصفية التلقائية في Microsoft Excel. تشرح هذه المقالة كيفية استخدام الميزات في Microsoft Excel، وكيفية برمجتها باستخدام Aspose.Cells for Node.js via C++.
{{% /alert %}}

## **عنصرية البيانات**

التصفية التلقائية هي أسرع طريقة لتحديد العناصر الوحيدة التي ترغب في عرضها في قائمة. تتيح ميزة التصفية التلقائية للمستخدمين تصفية العناصر في القائمة وفقًا لمعايير محددة. تصفية بناءً على النصوص أو الأرقام أو التواريخ.

### **التصفية التلقائية في Microsoft Excel**

لتفعيل ميزة التصفية التلقائية في Microsoft Excel:

1. انقر على صف العنوان في ورقة العمل.
1. من قائمة **البيانات**، حدد **تصفية** ثم **تصفية تلقائية**.

عند تطبيق التصفية التلقائية على ورقة عمل، يظهر التبديل (السهام السوداء) إلى يمين عناوين العمود.

1. انقر على سهم التصفية لرؤية قائمة الخيارات التصفية.

بعض خيارات التصفية التلقائية هي:

| **الخيارات** | **الوصف** |
| :- | :- |
||All| عرض كافة العناصر في القائمة مرة واحدة.|
||Custom| تخصيص معايير التصفية مثل الاحتواء/عدم الاحتواء|
||Filter by Color| تصفية بناءً على اللون المملوء|
||Date Filters| تصفية الصفوف بناءً على معايير مختلفة على التاريخ|
||Number Filters| أنواع مختلفة من التصفية على الأرقام مثل المقارنة والمتوسطات وأعلى 10 وما إلى ذلك.|
||Text Filters| تصفية مختلفة مثل تبدأ بـ، تنتهي بـ، تحتوي على الخ،|
||Blanks/Non Blanks| يمكن تنفيذ هذه التصفيات من خلال تصفية النصوص الفارغة|

يقوم المستخدمون بتصفية بيانات ورقة العمل يدويًا في Microsoft Excel باستخدام هذه الخيارات.

### **تصفية تلقائية مع Aspose.Cells for Node.js via C++**

توفر Aspose.Cells فئة Workbook التي تمثل ملف Excel. تحتوي فئة Workbook على مجموعة من ورق العمل وتسمح بالوصول إلى كل ورق عمل في ملف Excel.

ورقة العمل ممثلة بفئة ورقة العمل، وتقدم فئة ورقة العمل مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لإنشاء تصفية تلقائية، استخدم خاصية AutoFilter من فئة ورقة العمل. وتعتبر خاصية AutoFilter كائنًا لفئة AutoFilter توفر خاصية Range لتحديد نطاق الخلايا التي تتكون من صف العنوان. يتم تطبيق التصفية التلقائية على نطاق الخلايا الذي يشكل صف العناوين.

في كل ورقة عمل، يمكنك تحديد نطاق تصفية واحد فقط وهذا محدود بواسطة Microsoft Excel. لتصفية البيانات المخصصة، استخدم الأسلوب AutoFilter.Custom.

في المثال المقدم أدناه، أنشأنا نفس التصفية التلقائية باستخدام Aspose.Cells for Node.js via C++ كما أنشأنا باستخدام Microsoft Excel في القسم أعلاه.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter.js" >}}

#### **أنواع مختلفة من التصفية**

توفر Aspose.Cells خيارات متعددة لتطبيق مرشحات مختلفة مثل مرشح الألوان، مرشح التاريخ، مرشح الأرقام، مرشح النص، مرشح الخانات الفارغة والخانات الغير فارغة.

##### **لون التعبئة**

توفر Aspose.Cells إضافة الوظيفة إضافة مرشح لون التعبئة لتصفية البيانات استنادًا إلى خاصية لون التعبئة للخلايا. في المثال الوارد أدناه، يتم استخدام ملف قالب يحتوي على ألوان تعبئة مختلفة في العمود الأول من الورقة لاختبار وظيفة تصفية الألوان. يمكن تنزيل الملفات العينية من الروابط التالية.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-FillColor.js" >}}


##### **تاريخ**

يمكن تنفيذ أنواع مختلفة من مرشحات التاريخ مثل تصفية جميع الصفوف التي تحتوي على تواريخ في يناير 2018. يوضح رمز العينة هذا هذا الفلتر باستخدام وظيفة AddDateFilter. يتم تقديم الملفات النموذجية أدناه.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Date.js" >}}


##### **تاريخ ديناميكي**

في بعض الأحيان، تكون التصفيات الديناميكية مطلوبة بناءً على التاريخ مثل جميع الخلايا التي تحتوي على تواريخ في يناير بغض النظر عن السنة. في هذه الحالة، يتم استخدام دالة DynamicFilter كما هو موضح في الكود العيني التالي. يتم إعطاء ملفات عينية أدناه.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-DynamicFilter.js" >}}


##### **رقم**

يمكن تطبيق مرشحات مخصصة باستخدام Aspose.Cells مثل اختيار الخلايا التي تحتوي على أرقام بين نطاق معين. يظهر المثال التالي استخدام الوظيفة المخصصة لتصفية الأرقام. يتم تقديم ملفات العينات أدناه.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Number.js" >}}


##### **نص**

إذا كانت العمود يحتوي على نص وكان من المقرر تحديد خلايا تحتوي على نص معين، يمكن استخدام دالة Filter(). في المثال التالي، يحتوي ملف النموذج قائمة بالدول ويجب تحديد الصف الذي يحتوي على اسم دولة معين. يوضح الكود التالي تصفية النصوص. الملفات النموذجية موضحة أدناه.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Text.js" >}}


##### **فراغات**

إذا كان العمود يحتوي على نص بحيث تكون بعض الخلايا فارغة ويتطلب التصفية لتحديد الصفوف فقط حيث يتواجد الخلية الفارغة، فيمكن استخدام الدالة MatchBlanks() كما هو موضح أدناه. تتم تقديم ملفات عينة أدناه.

1. [ملف فارغ.xlsx](72417324.xlsx)
1. [ملف فارغ مصفى.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Blanks.js" >}}


##### **غير فارغة**

عندما يتعين تصفية الخلايا التي تحتوي على أي نص، استخدم دالة MatchNonBlanks كمصفية كما هو موضح أدناه. تتم تقديم ملفات عينة أدناه.

1. [ملف فارغ.xlsx](72417324.xlsx)
1. [ملف تصفية غير فارغ.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-NonBlanks.js" >}}


##### **تصفية مخصصة مع الاحتواء**

توفر Excel عوامل تصفية مخصصة مثل تصفية الصفوف التي تحتوي على سلسلة نصية معينة. تتوفر هذه الميزة في Aspose.Cells وتُظهر أدناه عن طريق تصفية الأسماء في الملف النموذجي. الملفات النموذجية معروضة أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-Contains.js" >}}


##### **تصفية مخصصة مع عدم الاحتواء**

يقدم إكسل فلاتر مخصصة مثل تصفية الصفوف التي لا تحتوي على سلاسل معينة. تتوفر هذه الميزة في Aspose.Cells ويتم توضيحها أدناه من خلال تصفية الأسماء في الملف النموذجي المقدم أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-NotContains.js" >}}


##### **تصفية مخصصة تبدأ ب**

يقدم إكسل فلاتر مخصصة مثل تصفية الصفوف التي تبدأ بسلسلة محددة. تتوفر هذه الميزة في Aspose.Cells ويتم توضيحها أدناه من خلال تصفية الأسماء في الملف النموذجي المقدم أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-BeginsWith.js" >}}


##### **تصفية مخصصة تنتهي ب**

يوفر Excel تصفيات مخصصة مثل تصفية الصفوف التي تنتهي بسلسلة معينة. يتوفر هذا الميزة في Aspose.Cells وموضحة أدناه من خلال تصفية الأسماء في ملف العينة المعطاة أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-Custom-EndsWith.js" >}}


## **مواضيع متقدمة**
- [تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة](/cells/ar/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [الحصول على جميع فهرسات الصفوف المخفية بعد تحديث تصفية السيارة.](/cells/ar/nodejs-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/)
