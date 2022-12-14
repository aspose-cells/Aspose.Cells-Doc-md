---
title: تنسيق المخطط
type: docs
weight: 20
url: /ar/java/chart-formatting/
---
## **ضبط مظهر المخطط**

 في[أنواع المخططات](/cells/ar/java/chart-types/)، قدمنا مقدمة موجزة عن أنواع المخططات وعناصر الرسوم البيانية التي يقدمها Aspose.Cells.

في هذه المقالة ، نناقش كيفية تخصيص مظهر المخططات من خلال تعيين عدد من الخصائص المختلفة:

- [تحديد منطقة المخطط](/cells/ar/java/chart-formatting/#setting-chart-area).
- [تحديد خطوط الرسم البياني](/cells/ar/java/chart-formatting/#setting-chart-lines).
- [تطبيق السمات](/cells/ar/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [تحديد العناوين للمخططات والمحاور](/cells/ar/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [العمل مع خطوط الشبكة](/cells/ar/java/chart-formatting/#setting-major-gridlines).
- [وضع حدود للجدران الخلفية والجانبية](/cells/ar/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **إعداد منطقة المخطط**

توجد أنواع مختلفة من المساحات في المخطط ويوفر Aspose.Cells مرونة في تعديل مظهر كل منطقة. يمكن للمطورين تطبيق إعدادات تنسيق مختلفة على منطقة ما عن طريق تغيير لون المقدمة ولون الخلفية وتنسيق التعبئة وما إلى ذلك.

في المثال الموضح أدناه ، قمنا بتطبيق إعدادات تنسيق مختلفة على أنواع مختلفة من مناطق الرسم البياني. تشمل هذه المناطق:

- منطقة المؤامرة
- منطقة الرسم البياني
- [**السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) منطقة
- منطقة نقطة واحدة في[**السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

بعد تنفيذ رمز المثال ، ستتم إضافة مخطط عمودي إلى ورقة العمل كما هو موضح أدناه:

**مخطط عمودي بمساحات معبأة** 

![ما يجب القيام به: image_بديل_نص](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **تحديد خطوط الرسم البياني**

 يمكن للمطورين أيضًا تطبيق أنواع مختلفة من الأنماط على الخطوط أو علامات البيانات في ملف[**السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)كما هو موضح أدناه في المثال. يؤدي تنفيذ رمز المثال إلى إضافة مخطط عمودي إلى ورقة العمل كما هو موضح أدناه:

**مخطط العمود بعد تطبيق أنماط الخط** 

![ما يجب القيام به: image_بديل_نص](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **تطبيق سمات Microsoft Excel 2007/2010 على المخططات**

 يمكن للمطورين تطبيق سمات وألوان Microsoft مختلفة على برنامج Excel[**السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)أو كائنات أخرى في المخطط كما هو موضح في المثال أدناه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **تحديد عناوين المخططات أو المحاور**

يمكنك استخدام Microsoft Excel لتعيين عناوين المخطط ومحاوره في بيئة WYSIWYG كما هو موضح أدناه.

**تحديد عناوين الرسم البياني ومحاوره باستخدام Microsoft Excel** 

![ما يجب القيام به: image_بديل_نص](chart-formatting_3.png)

يسمح Aspose.Cells أيضًا للمطورين بتعيين عناوين المخطط ومحاوره في وقت التشغيل. تحتوي جميع المخططات ومحاورها على ملف[**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text)الطريقة التي يمكن استخدامها لتعيين عناوينها كما هو موضح أدناه في مثال. بعد تنفيذ رمز المثال ، ستتم إضافة مخطط عمودي إلى ورقة العمل كما هو موضح أدناه:

**مخطط العمود بعد تحديد العناوين** 

![ما يجب القيام به: image_بديل_نص](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **تعيين خطوط الشبكة الرئيسية**

#### **إخفاء خطوط الشبكة الرئيسية**

 يمكن للمطورين التحكم في رؤية خطوط الشبكة الرئيسية باستخدام[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) طريقة[**خط**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)هدف. بعد إخفاء خطوط الشبكة الرئيسية ، يظهر مخطط العمود المضاف إلى ورقة العمل بالشكل التالي:

**مخطط عمودي مع خطوط شبكة رئيسية مخفية** 

![ما يجب القيام به: image_بديل_نص](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **تغيير إعدادات خطوط الشبكة الرئيسية**

لا يستطيع المطورون فقط التحكم في رؤية خطوط الشبكة الرئيسية ولكن أيضًا في الخصائص الأخرى بما في ذلك لونها وما إلى ذلك. بعد تعيين لون خطوط الشبكة الرئيسية ، سيظهر مخطط العمود المضاف إلى ورقة العمل بالشكل التالي:

**مخطط عمودي بخطوط شبكة رئيسية ملونة** 

![ما يجب القيام به: image_بديل_نص](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **وضع حدود للجدران الخلفية والجانبية**

 منذ إصدار Microsoft Excel 2007 ، تم تقسيم جدران المخطط ثلاثي الأبعاد إلى جزأين: جدار جانبي وجدار خلفي ، لذلك يتعين علينا استخدام جزأين[**الجدران**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) كائنات لتمثيلها بشكل منفصل ويمكنك الوصول إليها باستخدام[**Chart.getBackWall ()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) و[**Chart.getSideWall ()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

يوضح المثال الموضح أدناه كيفية تعيين حدود الجدار الجانبي باستخدام سمات مختلفة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **قم بتغيير موضع المخطط وحجمه**

 في بعض الأحيان ، تريد تغيير موضع أو حجم المخطط الجديد أو الموجود داخل ورقة العمل. يوفر Aspose.Cells ملف[**Chart.getChartObject ()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject) خاصية لتحقيق ذلك. يمكنك استخدام خصائصه الفرعية لتغيير حجم المخطط بجديد**ارتفاع** و**العرض** أو إعادة وضعه مع جديد** X ** و**Y ** إحداثيات.

### **تعديل موضع الرسم البياني وحجمه**

لتغيير موضع الرسم البياني (إحداثيات س ، ص) وحجمه (ارتفاع ، عرض) ، استخدم هذه الخصائص:

1. [**Chart.getChartObject (). get / setWidth ()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject (). get / setHeight ()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject (). get / setX ()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject (). get / setY ()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

يوضح المثال التالي استخدام الخصائص المذكورة أعلاه. يقوم بتحميل المصنف الحالي الذي يحتوي على مخطط في ورقة العمل الأولى الخاصة به. ثم يعيد حجم المخطط ويعيد مواضعه ويحفظ المصنف.

قبل تنفيذ نموذج التعليمات البرمجية ، يبدو الملف المصدر كما يلي:

**حجم المخطط وموضعه قبل تنفيذ نموذج التعليمات البرمجية** 

![ما يجب القيام به: image_بديل_نص](chart-formatting_7.png)

بعد التنفيذ ، يبدو ملف الإخراج كالتالي:

**حجم المخطط وموضعه بعد تنفيذ نموذج التعليمات البرمجية** 

![ما يجب القيام به: image_بديل_نص](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **معالجة مخططات المصمم**

هناك وقت قد تحتاج فيه إلى معالجة المخططات أو تعديلها في ملفات قالب المصمم. يدعم Aspose.Cells بالكامل معالجة مخططات المصمم بمحتوياتها وعناصرها. يمكن الاحتفاظ بالبيانات ومحتويات المخطط وصورة الخلفية والتنسيق بدقة.

### **معالجة مخططات المصمم في ملفات القوالب**

 لمعالجة مخططات المصمم في ملف قالب ، استخدم كافة استدعاءات API المتعلقة بالرسم البياني. على سبيل المثال ، استخدم[**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) للحصول على مجموعة المخططات الموجودة في ملف القالب.

#### **إنشاء مخطط**

يوضح المثال التالي كيفية إنشاء مخطط دائري. سوف نتعامل مع هذا المخطط لاحقًا. يتم إنشاء الإخراج التالي بواسطة الكود.

**مخطط الإدخال الدائري** 

![ما يجب القيام به: image_بديل_نص](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **التلاعب في الرسم البياني**

يوضح المثال التالي كيفية التعامل مع المخطط الحالي. في هذا المثال نقوم بتعديل الرسم البياني الذي تم إنشاؤه أعلاه. يتم إنشاء الإخراج التالي بواسطة الكود. لاحظ أن لون عنوان المخطط قد تغير من الأزرق إلى الأسود ، كما تم تغيير "إنجلترا 30000" إلى "المملكة المتحدة ، 30 ألفًا".

**تم تعديل المخطط الدائري** 

![ما يجب القيام به: image_بديل_نص](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **معالجة مخطط خطي في قالب المصمم**

في هذا المثال ، سنتعامل مع مخطط خطي. سنضيف بعض سلاسل البيانات إلى المخطط الحالي ونغير ألوان خطها.

أولاً ، ألق نظرة على مخطط خط المصمم.

**مخطط خط الإدخال** 

![ما يجب القيام به: image_بديل_نص](chart-formatting_11.png)

 الآن نحن نتعامل مع المخطط الخطي (الموجود في ملف**linechart.xls** file) باستخدام الكود التالي. يتم إنشاء الإخراج التالي بواسطة الكود.

**المخطط الخطي المتلاعب به** 

![ما يجب القيام به: image_بديل_نص](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **باستخدام خطوط سباركلينز**

Microsoft يمكن لبرنامج Excel 2010 تحليل المعلومات بطرق أكثر من أي وقت مضى. يسمح للمستخدمين بتتبع اتجاهات البيانات المهمة وإبرازها باستخدام أدوات تحليل وتصور جديدة للبيانات. خطوط المؤشر هي مخططات مصغرة يمكنك وضعها داخل الخلايا بحيث يمكنك عرض البيانات والمخطط على نفس الجدول. عندما يتم استخدام خطوط المؤشرات بشكل صحيح ، يكون تحليل البيانات أسرع وأكثر دقة. كما أنها توفر عرضًا بسيطًا للمعلومات ، وتجنب أوراق العمل المزدحمة بالكثير من المخططات المزدحمة.

يوفر Aspose.Cells API لمعالجة خطوط المؤشرات في جداول البيانات.

### **خطوط سباركلينز في Microsoft Excel**

لإدراج خطوط مؤشر في Microsoft Excel 2010:

1. حدد الخلايا التي تريد ظهور خطوط المؤشر فيها. لتسهيل عرضها ، حدد الخلايا الموجودة بجانب البيانات.
1.  انقر**إدراج** على الشريط ثم اختر**عمودي** في ال**سباركلينز** مجموعة.

![ما يجب القيام به: image_بديل_نص](chart-formatting_13.png)

1. حدد أو أدخل نطاق الخلايا في ورقة العمل التي تحتوي على البيانات المصدر.
 تظهر الرسوم البيانية.

تساعدك Sparklines على رؤية الاتجاهات ، على سبيل المثال ، أو سجل الفوز أو الخسارة لدوري الكرة اللينة. يمكن أن تلخص Sparklines الموسم بأكمله لكل فريق في الدوري.

![ما يجب القيام به: image_بديل_نص](chart-formatting_14.png)

### **خطوط الشرارة باستخدام Aspose.Cells**

يمكن للمطورين إنشاء أو حذف أو قراءة خطوط المؤشرات (في ملف القالب) باستخدام API المقدم بواسطة Aspose.Cells. بإضافة رسومات مخصصة لنطاق بيانات معين ، يتمتع المطورون بحرية إضافة أنواع مختلفة من المخططات الصغيرة إلى مناطق الخلايا المحددة.

يوضح المثال أدناه ميزة Sparklines. يوضح المثال كيفية:

1. افتح ملف قالب بسيط.
1. اقرأ معلومات خطوط المؤشرات لورقة عمل.
1. أضف خطوط مؤشرات جديدة لنطاق بيانات معين إلى منطقة خلية.
1. يحفظ ملف Excel على القرص.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **تطبيق تنسيق ثلاثي الأبعاد على الرسم البياني**

قد تحتاج إلى أنماط مخططات ثلاثية الأبعاد حتى تتمكن من الحصول على نتائج السيناريو الخاص بك فقط. توفر واجهات برمجة التطبيقات Aspose.Cells API ذي الصلة لتطبيق تنسيق Microsoft Excel 2007 ثلاثي الأبعاد كما هو موضح في هذه المقالة.

### **ضبط تنسيق ثلاثي الأبعاد على الرسم البياني**

يوجد مثال كامل أدناه لتوضيح كيفية إنشاء مخطط وتطبيق تنسيق Microsoft Excel 2007 3D. بعد تنفيذ رمز المثال أعلاه ، ستتم إضافة مخطط عمودي (مع تأثيرات ثلاثية الأبعاد) إلى ورقة العمل كما هو موضح أدناه.

**مخطط عمودي بتنسيق ثلاثي الأبعاد**

![ما يجب القيام به: image_بديل_نص](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

 للحصول على قائمة كاملة بالمخططات ثنائية وثلاثية الأبعاد المدعومة ، راجع[أنواع المخططات المدعومة للعرض](/cells/ar/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **موضوعات مسبقة**
- [قم بتعيين الصورة كخلفية تعبئة في المخطط](/cells/ar/java/set-picture-as-background-fill-in-the-chart/)
