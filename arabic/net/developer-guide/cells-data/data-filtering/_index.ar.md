---
title: تصفية البيانات
type: docs
weight: 85
url: /ar/net/data-filtering/
description: تعرف على كيفية إضافة عامل تصفية البيانات باستخدام Aspose.Cells for .NET API.
keywords: Add Filter by Color, Add Date Filters, Add Number Filters, Add Dynamic Filter, Add Text Filters, Add custom filter with Contains, Add custom filter with NotContains, Add custom filter with BeginsWith, Add custom filter with EndsWith
---
{{% alert color="primary" %}}

Microsoft يوفر Excel بعض الميزات الجيدة لتصفية بيانات ورقة العمل تلقائيًا. Aspose.Cells يدعم بشكل كامل Microsoft ميزات التصفية التلقائية في Excel. تشرح هذه المقالة كيفية استخدام الميزات الموجودة في Microsoft Excel، وكيفية ترميزها باستخدام Aspose.Cells.

{{% /alert %}}

##  **بيانات التصفية التلقائية**

تعد التصفية التلقائية أسرع طريقة لتحديد العناصر التي تريد عرضها في القائمة فقط من ورقة العمل. تتيح ميزة التصفية التلقائية للمستخدمين تصفية العناصر الموجودة في القائمة وفقًا لمعايير محددة. التصفية بناءً على النص أو الأرقام أو التواريخ.

###  **التصفية التلقائية في Microsoft إكسل**

لتفعيل خاصية التصفية التلقائية في Microsoft إكسل:

1. انقر فوق صف العنوان في ورقة العمل.
1.  من**بيانات** القائمة، حدد**منقي** ثم *تصفية تلقائية**.

عند تطبيق عامل تصفية تلقائي على ورقة عمل، تظهر مفاتيح التصفية (الأسهم السوداء) على يمين عناوين الأعمدة.

1. انقر فوق سهم عامل التصفية لرؤية قائمة بخيارات التصفية.

بعض خيارات التصفية التلقائية هي:

|**خيارات**|**وصف**|
| :- | :- |
|الجميع|إظهار كافة العناصر الموجودة في القائمة مرة واحدة.|
|مخصص|تخصيص معايير التصفية مثل يحتوي على/لا يحتوي|
|تصفية حسب اللون|المرشحات على أساس اللون المملوء|
|مرشحات التاريخ|يقوم بتصفية الصفوف بناءً على معايير مختلفة في التاريخ|
|مرشحات الأرقام|أنواع مختلفة من المرشحات على الأرقام مثل المقارنة والمتوسطات وأفضل 10 وما إلى ذلك.|
|مرشحات النص|مرشحات مختلفة مثل يبدأ بـ وينتهي بـ ويحتوي على وما إلى ذلك،|
|الفراغات/غير الفراغات|يمكن تنفيذ هذه المرشحات من خلال عامل تصفية النص الفارغ|

يقوم المستخدمون بتصفية بيانات ورقة العمل الخاصة بهم يدويًا في Microsoft Excel باستخدام هذه الخيارات.

###  **التصفية التلقائية مع Aspose.Cells**

يوفر Aspose.Cells فئة Workbook التي تمثل ملف Excel. تحتوي فئة Workbook على مجموعة أوراق العمل التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة ورقة العمل. توفر فئة ورقة العمل نطاقًا واسعًا من الخصائص والأساليب لإدارة أوراق العمل. لإنشاء عامل تصفية تلقائي، استخدم خاصية التصفية التلقائية لفئة ورقة العمل. الخاصية AutoFilter هي كائن من فئة التصفية التلقائية، والتي توفر خاصية النطاق لتحديد نطاق الخلايا التي تشكل صف العنوان. يتم تطبيق عامل التصفية التلقائي على نطاق الخلايا الذي يمثل صف العنوان.

في كل ورقة عمل، يمكنك تحديد نطاق مرشح واحد فقط. هذا يقتصر على Microsoft Excel. لتصفية البيانات المخصصة، استخدم الأسلوب AutoFilter.Custom.

في المثال الموضح أدناه، قمنا بإنشاء نفس التصفية التلقائية باستخدام Aspose.Cells كما أنشأناها باستخدام Microsoft Excel في القسم أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

####  **أنواع مختلفة من التصفية**

يوفر Aspose.Cells خيارات متعددة لتطبيق أنواع مختلفة من المرشحات مثل مرشح الألوان ومرشح التاريخ ومرشح الأرقام ومرشح النص ومرشحات فارغة ولا شيء مرشحات فارغة.

#####  **لون التعبئة**

يوفر Aspose.Cells وظيفة AddFillColorFilter لتصفية البيانات بناءً على خاصية لون التعبئة للخلايا. في المثال الموضح أدناه، يتم استخدام ملف قالب يحتوي على ألوان تعبئة مختلفة في العمود الأول من الورقة لاختبار وظيفة تصفية الألوان. يمكن تنزيل ملفات العينات من الروابط التالية.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilterColoredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

#####  **تاريخ**

يمكن تنفيذ نوع مختلف من عوامل تصفية التاريخ مثل تصفية جميع الصفوف التي لها تواريخ في يناير 2018. يوضح نموذج التعليمات البرمجية التالي عامل التصفية هذا باستخدام وظيفة AddDateFilter. وترد أدناه ملفات عينة.

1. [التاريخ.xlsx](72417317.xlsx)
1. [تاريخ التصفية.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

#####  **التاريخ الديناميكي**

في بعض الأحيان تكون المرشحات الديناميكية مطلوبة بناءً على التاريخ مثل جميع الخلايا التي تحتوي على تواريخ في شهر يناير بغض النظر عن السنة. في هذه الحالة يتم استخدام الدالة DynamicFilter كما هو موضح في نموذج التعليمات البرمجية التالي. وترد أدناه ملفات عينة.

1. [التاريخ.xlsx](72417317.xlsx)
1. [FilterDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

#####  **رقم**

يمكن تطبيق المرشحات المخصصة باستخدام Aspose.Cells مثل تحديد الخلايا التي لها رقم بين نطاق معين. يوضح المثال التالي استخدام الدالة Custom() لتصفية الأرقام. وترد أدناه ملفات عينة.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

#####  **نص**

إذا كان العمود يحتوي على نص وتم تحديد خلايا تحتوي على نص معين، فيمكن استخدام وظيفة Filter(). في المثال التالي، يحتوي ملف القالب على قائمة بالدول وسيتم تحديد صف يحتوي على اسم بلد معين. يوضح الكود التالي تصفية النص. وترد أدناه ملفات عينة.

1. [Text.xlsx](72417322.xlsx)
1. [FilterText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

#####  **الفراغات**

إذا كان العمود يحتوي على نص بحيث يكون هناك عدد قليل من الخلايا الفارغة، وكان هناك حاجة إلى عامل التصفية لتحديد تلك الصفوف التي توجد بها خلايا فارغة فقط، فيمكن استخدام وظيفة MatchBlanks() كما هو موضح أدناه. وترد أدناه ملفات عينة.

1. [فارغ.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

#####  **غير الفراغات**

عندما تريد تصفية الخلايا التي تحتوي على أي نص، استخدم وظيفة التصفية MatchNonBlanks كما هو موضح أدناه. وترد أدناه ملفات عينة.

1. [فارغ.xlsx](72417324.xlsx)
1. [تمت تصفيتهNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

#####  **مرشح مخصص يحتوي على**

يوفر Excel عوامل تصفية مخصصة مثل صفوف التصفية التي تحتوي على بعض السلاسل المحددة. هذه الميزة متوفرة في Aspose.Cells وموضحة أدناه من خلال تصفية الأسماء في ملف العينة. وترد أدناه ملفات عينة.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

#####  **مرشح مخصص مع NotContains**

يوفر Excel عوامل تصفية مخصصة مثل صفوف التصفية التي لا تحتوي على سلسلة معينة. هذه الميزة متوفرة في Aspose.Cells وموضحة أدناه من خلال تصفية الأسماء في نموذج الملف الوارد أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

#####  **مرشح مخصص مع BeginsWith**

يوفر Excel عوامل تصفية مخصصة مثل صفوف التصفية التي تبدأ بسلسلة معينة. هذه الميزة متوفرة في Aspose.Cells وموضحة أدناه من خلال تصفية الأسماء في نموذج الملف الوارد أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

#####  **مرشح مخصص مع EndsWith**

يوفر Excel عوامل تصفية مخصصة مثل صفوف التصفية التي تنتهي بسلسلة محددة. هذه الميزة متوفرة في Aspose.Cells وموضحة أدناه من خلال تصفية الأسماء في نموذج الملف الوارد أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

##  **مواضيع متقدمة**
- [قم بتطبيق عامل التصفية المتقدم لبرنامج Excel Microsoft لعرض معايير اجتماع السجلات المعقدة](/cells/ar/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [الحصول على كافة فهارس الصفوف المخفية بعد تحديث التصفية التلقائية](/cells/ar/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
