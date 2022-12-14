---
title: تصفية البيانات
type: docs
weight: 60
url: /ar/java/data-filtering/
---
{{% alert color="primary" %}}

يوفر Microsoft Excel بعض الميزات الجيدة للتصفية التلقائية لبيانات ورقة العمل. Aspose.Cells يدعم Microsoft ميزات التصفية التلقائية لبرنامج Excel بشكل كامل. تشرح هذه المقالة كيفية استخدام الميزات الموجودة في Microsoft Excel ، وكيفية ترميزها باستخدام Aspose.Cells.

{{% /alert %}}

## **بيانات التصفية التلقائية**

التصفية التلقائية هي أسرع طريقة لتحديد العناصر فقط من ورقة العمل التي تريد عرضها في قائمة. تتيح ميزة التصفية التلقائية للمستخدمين تصفية العناصر في قائمة وفقًا لمعايير محددة. تصفية على أساس النص أو الأرقام أو التواريخ.

### **التصفية التلقائية في Microsoft Excel**

لتنشيط ميزة التصفية التلقائية في Microsoft Excel:

1. انقر فوق صف العنوان في ورقة العمل.
1. من**بيانات**القائمة ، حدد**منقي**وثم**فلتر السيارات**.

عندما تقوم بتطبيق عامل التصفية التلقائي على ورقة عمل ، تظهر مفاتيح التصفية (الأسهم السوداء) على يمين عناوين الأعمدة.

1. انقر فوق سهم عامل التصفية لرؤية قائمة بخيارات التصفية.

بعض خيارات التصفية التلقائية هي:

|**خيارات**|**وصف**|
|:- |:- |
|الجميع|إظهار كافة العناصر في القائمة مرة واحدة.|
|العادة|تخصيص معايير التصفية مثل يحتوي على / لا يحتوي|
|تصفية حسب اللون|المرشحات على أساس اللون المعبأ|
|مرشحات التاريخ|ترشيح الصفوف بناءً على معايير مختلفة في التاريخ|
|مرشحات الرقم|نوع مختلف من التصفية على الأرقام مثل المقارنة والمتوسطات وأعلى 10 إلخ.|
|مرشحات النص|مرشحات مختلفة مثل يبدأ بـ ، وينتهي بـ ، يحتوي على إلخ ،|
|الفراغات / غير الفراغات|يمكن تنفيذ هذه المرشحات من خلال Text Filter Blank|
يقوم المستخدمون يدويًا بتصفية بيانات ورقة العمل الخاصة بهم في Microsoft Excel باستخدام هذه الخيارات.

### **مرشح تلقائي مع Aspose.Cells**

Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)يمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)فئة تحتوي على[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لإنشاء مرشح تلقائي ، استخدم ملف[**فلتر السيارات**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)ممتلكات[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)صف دراسي. ال[**فلتر السيارات**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)الخاصية هي كائن من[**فلتر السيارات**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)فئة ، والتي توفر[**نطاق**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)خاصية لتحديد نطاق الخلايا التي يتكون منها صف العنوان. يتم تطبيق عامل التصفية التلقائي على نطاق الخلايا الذي يمثل صف العنوان.

في كل ورقة عمل ، يمكنك تحديد نطاق تصفية واحد فقط. هذا مقيد بـ Microsoft Excel. لتصفية البيانات المخصصة ، استخدم ملف[**تصفية تلقائية**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) طريقة.

في المثال الموضح أدناه ، قمنا بإنشاء نفس التصفية التلقائية باستخدام Aspose.Cells كما أنشأنا باستخدام Microsoft Excel في القسم أعلاه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **أنواع مختلفة من الفلاتر**

يوفر Aspose.Cells خيارات متعددة لتطبيق أنواع مختلفة من المرشحات مثل مرشح اللون ومرشح التاريخ ومرشح الأرقام ومرشح النص والمرشحات الفارغة ومرشحات لا شيء فارغ.

##### **لون التعبئة**

Aspose.Cells يوفر وظيفة[**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)لتصفية البيانات بناءً على خاصية لون التعبئة للخلايا. في المثال الموضح أدناه ، يتم استخدام ملف قالب به ألوان تعبئة مختلفة في العمود الأول من الورقة لاختبار وظيفة تصفية الألوان. يمكن تنزيل الملفات التالية للتحقق من الوظيفة.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [تم تصفيته ColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **تاريخ**

يمكن تنفيذ أنواع مختلفة من عوامل تصفية التاريخ مثل تصفية جميع الصفوف التي لها تواريخ في يناير 2018. يوضح نموذج التعليمات البرمجية التالي هذا الفلتر باستخدام[**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)) وظيفة. يمكن استخدام الملفات التالية لاختبار هذه الوظيفة.

1. [Date.xlsx](72417317.xlsx)
1. [تاريخ التصفية. xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **التاريخ الديناميكي**

في بعض الأحيان ، تكون المرشحات الديناميكية مطلوبة استنادًا إلى تاريخ مثل جميع الخلايا التي لها تواريخ في يناير بغض النظر عن السنة. في هذه الحالة،[**مرشح ديناميكي**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int)) يتم استخدام الدالة على النحو الوارد في نموذج التعليمات البرمجية التالي. يمكن استخدام الملفات التالية للاختبار.

1. [Date.xlsx](72417317.xlsx)
1. [تم تصفيته DynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **رقم**

يمكن تطبيق المرشحات المخصصة باستخدام Aspose.Cells مثل اختيار الخلايا التي تحتوي على رقم بين نطاق معين. المثال التالي يوضح استخدام[**العادة()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) وظيفة لتصفية الأرقام. يمكن تنزيل ملفات نموذجية من الروابط التالية.

1. [الرقم. xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **نص**

إذا كان العمود يحتوي على نص وخلايا سيتم تحديدها تحتوي على نص معين ،[**منقي()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String)) وظيفة يمكن استخدامها. في المثال التالي ، يحتوي ملف القالب على قائمة بالبلدان وسيتم تحديد صف يحتوي على اسم بلد معين. يوضح الرمز التالي تصفية النص باستخدام الملفات النموذجية أدناه.

1. [نص. xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **الفراغات**

إذا كان العمود يحتوي على نص بحيث يكون هناك عدد قليل من الخلايا فارغة ، وكان المرشح مطلوبًا لتحديد تلك الصفوف فقط حيث توجد خلايا فارغة ،[**matchBlanks ()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int)) يمكن استخدام الوظيفة كما هو موضح أدناه. يمكن تنزيل ملفات نموذجية من الروابط التالية.

1. [فارغ. xlsx](72417324.xlsx)
1. [مُرشح Blank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **غير الفراغات**

عندما يتم تصفية الخلايا التي تحتوي على أي نص ، استخدم[**ماتش نون بلانكس**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)) وظيفة التصفية كما هو موضح أدناه. يمكن تنزيل ملفات نموذجية من الروابط التالية.

1. [فارغ. xlsx](72417324.xlsx)
1. [تمت تصفيته](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **مرشح مخصص يحتوي على**

يوفر Excel عوامل تصفية مخصصة مثل صفوف التصفية التي تحتوي على بعض السلاسل المحددة. تتوفر هذه الميزة في Aspose.Cells والموضحة أدناه من خلال تصفية الأسماء في نموذج الملف. يمكن تنزيل ملفات نموذجية من الروابط التالية.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **مرشح مخصص مع NotContains**

يوفر Excel عوامل تصفية مخصصة مثل صفوف التصفية التي لا تحتوي على سلسلة معينة. تتوفر هذه الميزة في Aspose.Cells والموضحة أدناه من خلال تصفية الأسماء في نموذج الملف أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **مرشح مخصص بـ BeginsWith**

يوفر Excel عوامل تصفية مخصصة مثل صفوف التصفية التي تبدأ ببعض السلاسل المحددة. تتوفر هذه الميزة في Aspose.Cells والموضحة أدناه من خلال تصفية الأسماء في نموذج الملف أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **مرشح مخصص مع EndsWith**

يوفر Excel عوامل تصفية مخصصة مثل صفوف التصفية التي تنتهي بسلسلة معينة. تتوفر هذه الميزة في Aspose.Cells والموضحة أدناه من خلال تصفية الأسماء في نموذج الملف أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **موضوعات مسبقة**
- [تطبيق عامل التصفية المتقدم لـ Microsoft Excel لعرض السجلات التي تفي بالمعايير المعقدة](/cells/ar/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [احصل على جميع مؤشرات الصفوف المخفية بعد تحديث التصفية التلقائية](/cells/ar/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

