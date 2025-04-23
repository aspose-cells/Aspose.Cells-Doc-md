---
title: تصفية البيانات
type: docs
weight: 60
url: /ar/java/data-filtering/
---

{{% alert color="primary" %}}

يوفر Microsoft Excel بعض الميزات الجيدة لتصفية بيانات ورق العمل تلقائيًا. تدعم Aspose.Cells بشكل كامل ميزات تصفية بيانات Microsoft Excel الملقم. يشرح هذا المقال كيفية استخدام الميزات في Microsoft Excel، وكيفية كتابة الشفرات باستخدام Aspose.Cells.

{{% /alert %}}

## **عنصرية البيانات**

التصفية التلقائية هي أسرع طريقة لتحديد العناصر الوحيدة التي ترغب في عرضها في قائمة. تتيح ميزة التصفية التلقائية للمستخدمين تصفية العناصر في القائمة وفقًا لمعايير محددة. تصفية بناءً على النصوص أو الأرقام أو التواريخ.

### **التصفية التلقائية في Microsoft Excel**

لتفعيل ميزة التصفية التلقائية في Microsoft Excel:

1. انقر على صف العنوان في ورقة العمل.
1. من قائمة البيانات، حدد تصفية ثم تصفية تلقائية.

عند تطبيق التصفية التلقائية على ورقة عمل، يظهر التبديل (السهام السوداء) إلى يمين عناوين العمود.

1. انقر على سهم التصفية لرؤية قائمة الخيارات التصفية.

بعض خيارات التصفية التلقائية هي:

| **الخيارات** | **الوصف** |
| :- | :- |
||All| عرض كافة العناصر في القائمة مرة واحدة.|
||Custom| تخصيص معايير التصفية مثل الاحتواء/عدم الاحتواء|
||Filter by Color| تصفية بناءً على اللون المملوء|
||Date Filters| تصفية الصفوف بناءً على معايير مختلفة على التاريخ|
|Number Filters| نوع مختلف من التصفية على الأرقام مثل المقارنة والمتوسط ​​وأعلى 10 وما إلى ذلك.
||Text Filters| تصفية مختلفة مثل تبدأ بـ، تنتهي بـ، تحتوي على الخ،|
||Blanks/Non Blanks| يمكن تنفيذ هذه التصفيات من خلال تصفية النصوص الفارغة|
يقوم المستخدمون بتصفية بيانات ورقة العمل يدويًا في Microsoft Excel باستخدام هذه الخيارات.

### **تصفية أوتوماتيكية بواسطة Aspose.Cells**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورقة في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة الأوراق. لإنشاء تصفية تلقائية، استخدم خاصية [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) لفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). خاصية [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) هي كائن من فئة [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)، والتي توفر الخاصية [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range) لتحديد نطاق الخلايا التي تتكون من صف العنوان. يتم تطبيق تصفية تلقائية على نطاق الخلايا الذي يشكل صف العنوان.

في كل ورقة عمل ، يمكنك تحديد نطاق تصفية واحد فقط. تقتصر هذه الخاصية بواسطة Microsoft Excel. لتصفية البيانات المخصصة ، استخدم الأسلوب [**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-).

في المثال المعطى أدناه، قمنا بإنشاء نفس تصفية الأوتوماتيكية باستخدام Aspose.Cells كما قمنا بإنشائها باستخدام مايكروسوفت إكسل في القسم السابق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **أنواع مختلفة من التصفية**

توفر Aspose.Cells خيارات متعددة لتطبيق مرشحات مختلفة مثل مرشح الألوان، مرشح التاريخ، مرشح الأرقام، مرشح النص، مرشح الخانات الفارغة والخانات الغير فارغة.

##### **لون التعبئة**

توفر Aspose.Cells وظيفة [**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter-int-int-com.aspose.cells.CellsColor-com.aspose.cells.CellsColor-) لتصفية البيانات استنادًا إلى خاصية لون التعبئة للخلايا. في المثال أدناه ، يتم استخدام ملف قالب يحتوي على ألوان تعبئة مختلفة في العمود الأول من الورقة لاختبار وظيفة تصفية الألوان. يمكن تنزيل الملفات التالية للتحقق من الوظائف.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **تاريخ**

يمكن تنفيذ أنواع مختلفة من تصفية التواريخ مثل تصفية جميع الصفوف التي تحتوي على تواريخ في يناير 2018. يوضح الكود المثالي التالي تنفيذ هذه التصفية باستخدام الأسلوب [**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter-int-int-int-int-int-int-int-int-). يمكن استخدام الملفات التالية لاختبار هذه الوظائف.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **تاريخ ديناميكي**

في بعض الأحيان يكون هناك حاجة إلى تصفية ديناميكية استنادًا إلى تاريخ مثل جميع الخلايا التي تحتوي على تواريخ في يناير بغض النظر عن السنة. في هذه الحالة ، يتم استخدام الدالة [**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter-int-int-) كما هو موضح في الكود المثالي أدناه. يمكن استخدام الملفات التالية لاختبار هذه الوظائف.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **رقم**

يمكن تطبيق التصفيات المخصصة باستخدام Aspose.Cells مثل اختيار الخلايا التي تحتوي على رقم بين نطاق معين. يوضح المثال التالي استخدام الدالة [**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-) لتصفية الأرقام. يمكن تنزيل الملفات النموذجية من الروابط التالية.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **نص**

إذا كانت العمود يحتوي على نص ويجب اختيار الخلايا التي تحتوي على نص معين ، يمكن استخدام الدالة [**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter-int-java.lang.String-). يوضح الكود التالي تصفية النص باستخدام الملفات النموذجية أدناه.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **فراغات**

إذا كان العمود يحتوي على نص بحيث تكون بعض الخلايا فارغة ، ويتعين تحديد الصفوف فقط حيث تكون الخلايا الفارغة موجودة ، يمكن استخدام الدالة [**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks-int-) كما يوضح أدناه. يمكن تنزيل الملفات النموذجية من الروابط التالية.

1. [ملف فارغ.xlsx](72417324.xlsx)
1. [ملف فارغ مصفى.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **غير فارغة**

عندما يكون هناك خلايا تحتوي على أي نص ويجب تصفيةها ، استخدم دالة التصفية [**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks-int-) كما هو موضح أدناه. يمكن تنزيل الملفات النموذجية من الروابط التالية.

1. [ملف فارغ.xlsx](72417324.xlsx)
1. [ملف تصفية غير فارغ.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **تصفية مخصصة مع الاحتواء**

يوفر Excel تصفيات مخصصة مثل تصفية الصفوف التي تحتوي على سلسلة معينة. يتوفر هذا الميزة في Aspose.Cells وموضحة أدناه من خلال تصفية الأسماء في ملف العينة. يمكن تنزيل ملفات العينة من الروابط التالية.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **تصفية مخصصة مع عدم الاحتواء**

توفر Excel عوامل تصفية مخصصة مثل تصفية الصفوف التي لا تحتوي على سلسلة نصية معينة. تتوفر هذه الميزة في Aspose.Cells وتُظهر أدناه عن طريق تصفية الأسماء في الملف النموذجي المعطى أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **تصفية مخصصة تبدأ ب**

توفر Excel عوامل تصفية مخصصة مثل تصفية الصفوف التي تبدأ بسلسلة نصية معينة. تتوفر هذه الميزة في Aspose.Cells وتُظهر أدناه عن طريق تصفية الأسماء في الملف النموذجي المعطى أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **تصفية مخصصة تنتهي ب**

يوفر Excel تصفيات مخصصة مثل تصفية الصفوف التي تنتهي بسلسلة معينة. يتوفر هذا الميزة في Aspose.Cells وموضحة أدناه من خلال تصفية الأسماء في ملف العينة المعطاة أدناه.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **مواضيع متقدمة**
- [تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة](/cells/ar/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [الحصول على جميع فهرسات الصفوف المخفية بعد تحديث تصفية السيارة.](/cells/ar/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

{{< app/cells/assistant language="java" >}}
