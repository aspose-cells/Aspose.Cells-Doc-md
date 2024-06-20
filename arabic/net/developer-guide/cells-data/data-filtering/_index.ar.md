---
title: تصفية البيانات
type: docs
weight: 85
url: /ar/net/data-filtering/
description: تعلم كيفية إضافة مرشح البيانات باستخدام واجهة التطبيقات بـAspose.Cells for .NET.
keywords: إضافة مرشح حسب اللون، إضافة مرشحات التاريخ، إضافة مرشحات الأرقام، إضافة مرشح ديناميكي، إضافة مرشحات النص، إضافة مرشح مخصص بحسب الاحتواء، إضافة مرشح مخصص بدون الاحتواء، إضافة مرشح مخصص يبدأ بـ، إضافة مرشح مخصص ينتهي بـ
---

{{% alert color="primary" %}}

يوفر Microsoft Excel بعض الميزات الجيدة لتصفية بيانات ورق العمل تلقائيًا. تدعم Aspose.Cells بشكل كامل ميزات تصفية بيانات Microsoft Excel الملقم. يشرح هذا المقال كيفية استخدام الميزات في Microsoft Excel، وكيفية كتابة الشفرات باستخدام Aspose.Cells.

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

### **تصفية أوتوماتيكية بواسطة Aspose.Cells**

توفر Aspose.Cells فئة Workbook التي تمثل ملف Excel. تحتوي فئة Workbook على مجموعة من ورق العمل وتسمح بالوصول إلى كل ورق عمل في ملف Excel.

ورقة العمل ممثلة بفئة ورقة العمل، وتقدم فئة ورقة العمل مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لإنشاء تصفية تلقائية، استخدم خاصية AutoFilter من فئة ورقة العمل. وتعتبر خاصية AutoFilter كائنًا لفئة AutoFilter توفر خاصية Range لتحديد نطاق الخلايا التي تتكون من صف العنوان. يتم تطبيق التصفية التلقائية على نطاق الخلايا الذي يشكل صف العناوين.

في كل ورقة عمل، يمكنك تحديد نطاق تصفية واحد فقط وهذا محدود بواسطة Microsoft Excel. لتصفية البيانات المخصصة، استخدم الأسلوب AutoFilter.Custom.

في المثال المعطى أدناه، قمنا بإنشاء نفس تصفية الأوتوماتيكية باستخدام Aspose.Cells كما قمنا بإنشائها باستخدام مايكروسوفت إكسل في القسم السابق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

#### **أنواع مختلفة من التصفية**

توفر Aspose.Cells خيارات متعددة لتطبيق مرشحات مختلفة مثل مرشح الألوان، مرشح التاريخ، مرشح الأرقام، مرشح النص، مرشح الخانات الفارغة والخانات الغير فارغة.

##### **لون التعبئة**

توفر Aspose.Cells إضافة الوظيفة إضافة مرشح لون التعبئة لتصفية البيانات استنادًا إلى خاصية لون التعبئة للخلايا. في المثال الوارد أدناه، يتم استخدام ملف قالب يحتوي على ألوان تعبئة مختلفة في العمود الأول من الورقة لاختبار وظيفة تصفية الألوان. يمكن تنزيل الملفات العينية من الروابط التالية.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

##### **تاريخ**

يمكن تنفيذ أنواع مختلفة من عمليات تصفية التاريخ مثل تصفية جميع الصفوف التي تحتوي على تواريخ في يناير 2018. يوضح الكود العيني التالي هذا التصفية باستخدام الدالة AddDateFilter. يتم إعطاء ملفات عينية أدناه.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

##### **تاريخ ديناميكي**

في بعض الأحيان، تكون التصفيات الديناميكية مطلوبة بناءً على التاريخ مثل جميع الخلايا التي تحتوي على تواريخ في يناير بغض النظر عن السنة. في هذه الحالة، يتم استخدام دالة DynamicFilter كما هو موضح في الكود العيني التالي. يتم إعطاء ملفات عينية أدناه.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

##### **رقم**

يمكن تطبيق مرشحات مخصصة باستخدام Aspose.Cells مثل اختيار الخلايا التي تحتوي على أرقام بين نطاق معين. يظهر المثال التالي استخدام الوظيفة المخصصة لتصفية الأرقام. يتم تقديم ملفات العينات أدناه.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

##### **نص**

إذا كانت العمود يحتوي على نص ويتعين تحديد الخلايا التي تحتوي على نص معين، فيمكن استخدام دالة Filter(). في المثال التالي، يحتوي ملف القالب على قائمة بالدول ويجب تحديد الصف الذي يحتوي على اسم دولة معين. يوضح الكود التالي تصفية النصوص. يتم تقديم ملفات عينة أدناه.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

##### **فراغات**

إذا كان العمود يحتوي على نص بحيث تكون بعض الخلايا فارغة ويتطلب التصفية لتحديد الصفوف فقط حيث يتواجد الخلية الفارغة، فيمكن استخدام الدالة MatchBlanks() كما هو موضح أدناه. تتم تقديم ملفات عينة أدناه.

1. [ملف فارغ.xlsx](72417324.xlsx)
1. [ملف فارغ مصفى.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

##### **غير فارغة**

عندما يتعين تصفية الخلايا التي تحتوي على أي نص، استخدم دالة MatchNonBlanks كمصفية كما هو موضح أدناه. تتم تقديم ملفات عينة أدناه.

1. [ملف فارغ.xlsx](72417324.xlsx)
1. [ملف تصفية غير فارغ.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

##### **تصفية مخصصة مع الاحتواء**

توفر Excel عوامل تصفية مخصصة مثل تصفية الصفوف التي تحتوي على سلسلة نصية معينة. تتوفر هذه الميزة في Aspose.Cells وتُظهر أدناه عن طريق تصفية الأسماء في الملف النموذجي. الملفات النموذجية معروضة أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

##### **تصفية مخصصة مع عدم الاحتواء**

توفر Excel عوامل تصفية مخصصة مثل تصفية الصفوف التي لا تحتوي على سلسلة نصية معينة. تتوفر هذه الميزة في Aspose.Cells وتُظهر أدناه عن طريق تصفية الأسماء في الملف النموذجي المعطى أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

##### **تصفية مخصصة تبدأ ب**

توفر Excel عوامل تصفية مخصصة مثل تصفية الصفوف التي تبدأ بسلسلة نصية معينة. تتوفر هذه الميزة في Aspose.Cells وتُظهر أدناه عن طريق تصفية الأسماء في الملف النموذجي المعطى أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

##### **تصفية مخصصة تنتهي ب**

يوفر Excel تصفية مخصصة مثل تصفية الصفوف التي تنتهي بسلسلة معينة. يتوفر هذا الميزة في Aspose.Cells ويتم استعراضها أدناه من خلال تصفية الأسماء في ملف العينة المُعطى أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

## **مواضيع متقدمة**
- [تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة](/cells/ar/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [الحصول على جميع فهرسات الصفوف المخفية بعد تحديث تصفية السيارة.](/cells/ar/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
