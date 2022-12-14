---
title: تصفية البيانات
type: docs
weight: 85
url: /ar/net/data-filtering/
---
{{% alert color="primary" %}}

يوفر Microsoft Excel بعض الميزات الجيدة للتصفية التلقائية لبيانات ورقة العمل. Aspose.Cells يدعم Microsoft ميزات التصفية التلقائية لبرنامج Excel بشكل كامل. تشرح هذه المقالة كيفية استخدام الميزات الموجودة في Microsoft Excel ، وكيفية ترميزها باستخدام Aspose.Cells.

{{% /alert %}}

## **بيانات التصفية التلقائية**

التصفية التلقائية هي أسرع طريقة لتحديد العناصر فقط من ورقة العمل التي تريد عرضها في قائمة. تتيح ميزة التصفية التلقائية للمستخدمين تصفية العناصر في قائمة وفقًا لمعايير محددة. تصفية على أساس النص أو الأرقام أو التواريخ.

### **التصفية التلقائية في Microsoft Excel**

لتنشيط ميزة التصفية التلقائية في Microsoft Excel:

1. انقر فوق صف العنوان في ورقة العمل.
1.  من**بيانات** القائمة ، حدد**منقي** وثم**فلتر السيارات**.

عندما تقوم بتطبيق عامل التصفية التلقائي على ورقة عمل ، تظهر مفاتيح التصفية (الأسهم السوداء) على يمين عناوين الأعمدة.

1. انقر فوق سهم عامل التصفية لرؤية قائمة بخيارات التصفية.

بعض خيارات التصفية التلقائية هي:

|**خيارات**|**وصف**|
|:- |:- |
|الجميع|إظهار كافة العناصر في القائمة مرة واحدة.|
|العادة|تخصيص معايير التصفية مثل يحتوي على / لا يحتوي|
|تصفية حسب اللون|المرشحات على أساس اللون المعبأ|
|مرشحات التاريخ|ترشيح الصفوف بناءً على معايير مختلفة في التاريخ|
|مرشحات الرقم|أنواع مختلفة من التصفية على الأرقام مثل المقارنة والمتوسطات وأعلى 10 إلخ.|
|مرشحات النص|مرشحات مختلفة مثل يبدأ بـ ، وينتهي بـ ، يحتوي على إلخ ،|
|الفراغات / غير الفراغات|يمكن تنفيذ هذه المرشحات من خلال Text Filter Blank|

يقوم المستخدمون يدويًا بتصفية بيانات ورقة العمل الخاصة بهم في Microsoft Excel باستخدام هذه الخيارات.

### **مرشح تلقائي مع Aspose.Cells**

يوفر Aspose.Cells فئة ، مصنف يمثل ملف Excel. تحتوي فئة المصنف على مجموعة أوراق عمل تتيح الوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة ورقة العمل. توفر فئة ورقة العمل نطاقًا واسعًا من الخصائص والأساليب لإدارة أوراق العمل. لإنشاء عامل تصفية تلقائي ، استخدم خاصية التصفية التلقائية لفئة ورقة العمل. خاصية التصفية التلقائية هي كائن من فئة التصفية التلقائية ، والتي توفر خاصية النطاق لتحديد نطاق الخلايا التي تشكل صف عنوان. يتم تطبيق عامل التصفية التلقائي على نطاق الخلايا الذي يمثل صف العنوان.

في كل ورقة عمل ، يمكنك تحديد نطاق تصفية واحد فقط. هذا مقيد بـ Microsoft Excel. لتصفية البيانات المخصصة ، استخدم طريقة AutoFilter.Custom.

في المثال الموضح أدناه ، قمنا بإنشاء نفس التصفية التلقائية باستخدام Aspose.Cells كما أنشأنا باستخدام Microsoft Excel في القسم أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

#### **أنواع مختلفة من الفلاتر**

يوفر Aspose.Cells خيارات متعددة لتطبيق أنواع مختلفة من المرشحات مثل مرشح اللون ومرشح التاريخ ومرشح الأرقام ومرشح النص والمرشحات الفارغة ومرشحات لا شيء فارغ.

##### **لون التعبئة**

يوفر Aspose.Cells الوظيفة AddFillColorFilter لترشيح البيانات بناءً على خاصية لون التعبئة للخانات. في المثال الموضح أدناه ، يتم استخدام ملف قالب به ألوان تعبئة مختلفة في العمود الأول من الورقة لاختبار وظيفة تصفية الألوان. يمكن تنزيل ملفات نموذجية من الروابط التالية.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [تم تصفيته ColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

##### **تاريخ**

يمكن تنفيذ نوع مختلف من عوامل تصفية التاريخ مثل تصفية جميع الصفوف التي لها تواريخ في يناير 2018. يوضح نموذج التعليمات البرمجية التالي عامل التصفية هذا باستخدام وظيفة AddDateFilter. يتم إعطاء ملفات عينة أدناه.

1. [Date.xlsx](72417317.xlsx)
1. [تاريخ التصفية. xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

##### **التاريخ الديناميكي**

في بعض الأحيان ، تكون المرشحات الديناميكية مطلوبة بناءً على التاريخ مثل جميع الخلايا التي لها تواريخ في يناير بغض النظر عن السنة. في هذه الحالة ، يتم استخدام دالة DynamicFilter كما هو موضح في نموذج التعليمات البرمجية التالي. يتم إعطاء ملفات عينة أدناه.

1. [Date.xlsx](72417317.xlsx)
1. [تم تصفيته DynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

##### **رقم**

يمكن تطبيق المرشحات المخصصة باستخدام Aspose.Cells مثل اختيار الخلايا التي تحتوي على رقم بين نطاق معين. يوضح المثال التالي استخدام وظيفة Custom () لتصفية الأرقام. يتم إعطاء ملفات عينة أدناه.

1. [الرقم. xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

##### **نص**

إذا كان العمود يحتوي على نص وخلايا سيتم تحديدها تحتوي على نص معين ، فيمكن استخدام وظيفة Filter (). في المثال التالي ، يحتوي ملف القالب على قائمة بالبلدان وسيتم تحديد صف يحتوي على اسم بلد معين. يوضح الكود التالي ترشيح النص. يتم إعطاء ملفات عينة أدناه.

1. [نص. xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

##### **الفراغات**

إذا كان العمود يحتوي على نص بحيث تكون بعض الخلايا فارغة ، وكان المرشح مطلوبًا لتحديد تلك الصفوف فقط حيث توجد خلايا فارغة ، فيمكن استخدام وظيفة MatchBlanks () كما هو موضح أدناه. يتم إعطاء ملفات عينة أدناه.

1. [فارغ. xlsx](72417324.xlsx)
1. [مُرشح Blank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

##### **غير الفراغات**

عند تصفية الخلايا التي تحتوي على أي نص ، استخدم وظيفة عامل التصفية MatchNonBlanks كما هو موضح أدناه. يتم إعطاء ملفات عينة أدناه.

1. [فارغ. xlsx](72417324.xlsx)
1. [تمت تصفيته](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

##### **مرشح مخصص يحتوي على**

يوفر Excel عوامل تصفية مخصصة مثل صفوف التصفية التي تحتوي على بعض السلاسل المحددة. تتوفر هذه الميزة في Aspose.Cells والموضحة أدناه من خلال تصفية الأسماء في نموذج الملف. يتم إعطاء ملفات عينة أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

##### **مرشح مخصص مع NotContains**

يوفر Excel عوامل تصفية مخصصة مثل صفوف التصفية التي لا تحتوي على سلسلة معينة. تتوفر هذه الميزة في Aspose.Cells والموضحة أدناه من خلال تصفية الأسماء في نموذج الملف أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

##### **مرشح مخصص بـ BeginsWith**

يوفر Excel عوامل تصفية مخصصة مثل صفوف التصفية التي تبدأ ببعض السلاسل المحددة. تتوفر هذه الميزة في Aspose.Cells والموضحة أدناه من خلال تصفية الأسماء في نموذج الملف أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

##### **مرشح مخصص مع EndsWith**

يوفر Excel عوامل تصفية مخصصة مثل صفوف التصفية التي تنتهي بسلسلة معينة. تتوفر هذه الميزة في Aspose.Cells والموضحة أدناه من خلال تصفية الأسماء في نموذج الملف أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

## **موضوعات مسبقة**
- [تطبيق عامل التصفية المتقدم لـ Microsoft Excel لعرض السجلات التي تفي بالمعايير المعقدة](/cells/ar/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [احصل على جميع مؤشرات الصفوف المخفية بعد تحديث التصفية التلقائية](/cells/ar/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
