---
title: تصفية البيانات
type: docs
weight: 85
url: /ar/python-net/data-filtering/
description: تعلم كيفية إضافة تصفية البيانات باستخدام Aspose.Cells for Python via .NET API.
keywords: مكتبة Python Excel ، إضافة Python تصفية حسب اللون ، إضافة Python تصفية حسب التاريخ ، إضافة Python تصفية حسب الأرقام ، إضافة Python تصفية ديناميكية ، إضافة Python تصفية نصوص ، إضافة Python تصفية مخصصة بالاحتواء ، إضافة Python تصفية مخصصة بدون الاحتواء ، إضافة Python تصفية مخصصة تبدأ بـ ، إضافة Python تصفية مخصصة تنتهي بـ
---

{{% alert color="primary" %}}

توفر Microsoft Excel ميزات جيدة لتلقائي عنصرية بيانات ورقة العمل. تدعم Aspose.Cells for Python via .NET بشكل كامل ميزات تلقائي عنصرية Microsoft Excel. يشرح هذا المقال كيفية استخدام الميزات في Microsoft Excel وكيفية كتابة الشفرة باستخدام Aspose.Cells for Python via .NET.

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

### **التصفية التلقائية باستخدام مكتبة Aspose.Cells for Python Excel**

توفر Aspose.Cells for Python via .NET فئة تمثل ملف Excel وتحتوي على مجموعة من ورق العمل التي تسمح بالوصول إلى كل ورق عمل في ملف Excel.

ورقة العمل ممثلة بفئة ورقة العمل، وتقدم فئة ورقة العمل مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لإنشاء تصفية تلقائية، استخدم خاصية AutoFilter من فئة ورقة العمل. وتعتبر خاصية AutoFilter كائنًا لفئة AutoFilter توفر خاصية Range لتحديد نطاق الخلايا التي تتكون من صف العنوان. يتم تطبيق التصفية التلقائية على نطاق الخلايا الذي يشكل صف العناوين.

في كل ورقة عمل، يمكنك تحديد نطاق تصفية واحد فقط وهذا محدود بواسطة Microsoft Excel. لتصفية البيانات المخصصة، استخدم الأسلوب AutoFilter.Custom.

في المثال أدناه، قمنا بإنشاء نفس التصفية التلقائية باستخدام Aspose.Cells for Python via .NET كما قمنا بإنشاءها باستخدام Microsoft Excel في الجزء السابق.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterData-1.py" >}}

#### **أنواع مختلفة من التصفية**

يوفر Aspose.Cells for Python via .NET خيارات متعددة لتطبيق أنواع مختلفة من التصفية مثل تصفية اللون، وتصفية التاريخ، وتصفية الرقم، وتصفية النص، وتصفية الخانات الفارغة، وتصفية الخانات غير الفارغة.

##### **لون التعبئة**

يوفر Aspose.Cells for Python via .NET وظيفة AddFillColorFilter لتصفية البيانات بناءً على خاصية لون التعبئة للخلايا. في المثال أدناه، تم استخدام ملف قالب يحتوي على ألوان تعبئة مختلفة في العمود الأول من الورقة لاختبار وظيفة تصفية الألوان. يمكن تنزيل الملفات العينية من الروابط التالية.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterColor-1.py" >}}

##### **تاريخ**

يمكن تنفيذ أنواع مختلفة من عمليات تصفية التاريخ مثل تصفية جميع الصفوف التي تحتوي على تواريخ في يناير 2018. يوضح الكود العيني التالي هذا التصفية باستخدام الدالة AddDateFilter. يتم إعطاء ملفات عينية أدناه.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDate-1.py" >}}

##### **تاريخ ديناميكي**

في بعض الأحيان، تكون التصفيات الديناميكية مطلوبة بناءً على التاريخ مثل جميع الخلايا التي تحتوي على تواريخ في يناير بغض النظر عن السنة. في هذه الحالة، يتم استخدام دالة DynamicFilter كما هو موضح في الكود العيني التالي. يتم إعطاء ملفات عينية أدناه.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDynamicFilter-1.py" >}}

##### **رقم**

تطبيق التصفية المخصصة يمكن استخدامها باستخدام Aspose.Cells for Python via .NET مثل اختيار الخلايا التي تحتوي على أرقام بين النطاق المعطى. يوضح المثال التالي استخدام الدالة Custom() لتصفية الأرقام. يتم تقديم ملفات عينة أدناه.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNumber-1.py" >}}

##### **نص**

إذا كانت العمود يحتوي على نص ويتعين تحديد الخلايا التي تحتوي على نص معين، فيمكن استخدام دالة Filter(). في المثال التالي، يحتوي ملف القالب على قائمة بالدول ويجب تحديد الصف الذي يحتوي على اسم دولة معين. يوضح الكود التالي تصفية النصوص. يتم تقديم ملفات عينة أدناه.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterText-1.py" >}}

##### **فراغات**

إذا كان العمود يحتوي على نص بحيث تكون بعض الخلايا فارغة ويتطلب التصفية لتحديد الصفوف فقط حيث يتواجد الخلية الفارغة، فيمكن استخدام الدالة MatchBlanks() كما هو موضح أدناه. تتم تقديم ملفات عينة أدناه.

1. [ملف فارغ.xlsx](72417324.xlsx)
1. [ملف فارغ مصفى.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterBlank-1.py" >}}

##### **غير فارغة**

عندما يتعين تصفية الخلايا التي تحتوي على أي نص، استخدم دالة MatchNonBlanks كمصفية كما هو موضح أدناه. تتم تقديم ملفات عينة أدناه.

1. [ملف فارغ.xlsx](72417324.xlsx)
1. [ملف تصفية غير فارغ.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNonBlank-1.py" >}}

##### **تصفية مخصصة مع الاحتواء**

يوفر Excel تصفية مخصصة مثل تصفية الصفوف التي تحتوي على سلسلة نصية معينة. يتوفر هذا الميزة في Aspose.Cells for Python via .NET ويتم توضيحه أدناه بتصفية الأسماء في الملف العينة. تتم تقديم ملفات عينة أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-Contains-1.py" >}}

##### **تصفية مخصصة مع عدم الاحتواء**

إكسل يوفر عوامل تصفية مخصصة مثل تصفية الصفوف التي لا تحتوي على سلسلة معينة. هذه الميزة متاحة في Aspose.Cells for Python via .NET وموضحة أدناه من خلال تصفية الأسماء في الملف النموذجي المعطى أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-NotContains-1.py" >}}

##### **تصفية مخصصة تبدأ ب**

إكسل يوفر عوامل تصفية مخصصة مثل تصفية الصفوف التي تبدأ بسلسلة معينة. هذه الميزة متاحة في Aspose.Cells for Python via .NET وموضحة أدناه من خلال تصفية الأسماء في الملف النموذجي المعطى أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterBeginsWith-1.py" >}}

##### **تصفية مخصصة تنتهي ب**

إكسل يوفر عوامل تصفية مخصصة مثل تصفية الصفوف التي تنتهي بسلسلة معينة. هذه الميزة متاحة في Aspose.Cells for Python via .NET وموضحة أدناه من خلال تصفية الأسماء في الملف النموذجي المعطى أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterEndsWith-1.py" >}}

## **مواضيع متقدمة**
- [تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة](/cells/ar/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [الحصول على جميع فهرسات الصفوف المخفية بعد تحديث تصفية السيارة.](/cells/ar/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="python-net" >}}
