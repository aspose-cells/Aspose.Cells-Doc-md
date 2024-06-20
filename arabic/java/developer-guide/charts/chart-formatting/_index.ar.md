---
title: تنسيق الرسم البياني
type: docs
weight: 20
url: /ar/java/chart-formatting/
---

## **ضبط مظهر الرسم البياني**

في [أنواع الرسوم البيانية](/cells/ar/java/chart-types/) ، قدمنا ​​مقدمة موجزة لأنواع الرسوم البيانية وكائنات الرسم البياني التي تقدمها Aspose.Cells.

في هذه المقالة، نناقش كيفية تخصيص مظهر الرسوم البيانية عن طريق تعيين عدد من الخصائص المختلفة:

- [ضبط منطقة الرسم البياني](/cells/ar/java/chart-formatting/#setting-chart-area).
- [ضبط خطوط الرسم البياني](/cells/ar/java/chart-formatting/#setting-chart-lines).
- [تطبيق السمات](/cells/ar/java/chart-formatting/#applying-microsoft-excel-20072010-themes-to-charts).
- [ضبط عناوين الرسوم البيانية والمحاور](/cells/ar/java/chart-formatting/#setting-the-titles-of-charts-or-axes).
- [العمل مع خطوط الشبكة](/cells/ar/java/chart-formatting/#setting-major-gridlines).
- [ضبط حدود الجدران الخلفية والجانبية](/cells/ar/java/chart-formatting/#setting-borders-for-back-and-side-walls).

### **تعيين منطقة الرسم البياني**

هناك أنواع مختلفة من المناطق في الرسم البياني وتوفر Aspose.Cells مرونة تعديل مظهر كل منطقة. يمكن للمطورين تطبيق إعدادات تنسيق مختلفة على منطقة عن طريق تغيير لون الخلفية ولون الخلفية وتنسيق الملء وما إلى ذلك.

في المثال الوارد أدناه، قمنا بتطبيق إعدادات تنسيق مختلفة على أنواع مختلفة من المناطق في رسم بياني. هذه المناطق تشمل:

- منطقة الرسم
- منطقة الرسم البياني
- منطقة [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)
- منطقة نقطة واحدة في [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)

بعد تنفيذ كود المثال، سيتم إضافة رسم بياني للعمود إلى ورقة العمل كما هو موضح أدناه:

**رسم بياني للعمود مع مناطق مملوءة** 

![todo:image_alt_text](chart-formatting_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartArea-SettingChartArea.java" >}}

### **تعيين خطوط الرسم البياني**

يمكن للمطورين أيضًا تطبيق أنواع مختلفة من الأنماط على الخطوط أو علامات البيانات لـ [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) كما هو موضح أدناه في المثال. تنفيذ كود المثال يضيف رسم بياني لورقة العمل كما هو موضح أدناه:

**رسم بياني للأعمدة بعد تطبيق أنماط الخطوط** 

![todo:image_alt_text](chart-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartLines-SettingChartLines.java" >}}

### **تطبيق سمات مايكروسوفت اكسيل 2007/2010 على الرسوم البيانية**

يمكن للمطورين تطبيق ثيمات وألوان مايكروسوفت إكسيل المختلفة على [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) أو كائنات الرسم البياني الأخرى كما هو موضح في المثال أدناه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ApplyingThemes-ApplyingThemes.java" >}}

### **ضبط عناوين الرسوم البيانية أو المحاور**

يمكنك استخدام مايكروسوفت إكسيل لتعيين عناوين لرسم بياني ومحاوره في بيئة WYSIWYG كما هو موضح أدناه:

**تعيين عناوين لرسم بياني & محاوره باستخدام مايكروسوفت إكسيل** 

![todo:image_alt_text](chart-formatting_3.png)

تسمح Aspose.Cells أيضًا للمطورين بتعيين عناوين لرسم بياني ومحاوره عند التشغيل. تحتوي جميع الرسوم البيانية ومحاورها على طريقة [**Title.setText**](https://reference.aspose.com/cells/java/com.aspose.cells/title#Text) يمكن استخدامها لتعيين عناوينها كما هو موضح أدناه في مثال. بعد تنفيذ كود المثال، سيتم إضافة رسم بياني للعمود إلى ورقة العمل كما هو موضح أدناه:

**رسم بياني للأعمدة بعد تعيين العناوين** 

![todo:image_alt_text](chart-formatting_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingTitlesAxes-SettingTitlesAxes.java" >}}

### **تعيين خطوط الشبكة الرئيسية**

#### **إخفاء خطوط الشبكة الرئيسية**

يمكن للمطورين التحكم في رؤية خطوط الشبكة الرئيسية عن طريق استخدام طريقة [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/line#IsVisible) في كائن [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line). بعد إخفاء خطوط الشبكة الرئيسية، يظهر الرسم البياني العمودي المضاف إلى ورقة العمل بالمظهر التالي:

**رسم بياني عمودي مع خطوط شبكة رئيسية مخفية** 

![todo:image_alt_text](chart-formatting_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-MajorGridlines-1.java" >}}

#### **تغيير إعدادات خطوط الشبكة الرئيسية**

لا يمكن للمطورين فقط التحكم في رؤية خطوط الشبكة الرئيسية ولكن أيضًا خصائص أخرى بما في ذلك لونها وما إلى ذلك. بعد تعيين لون خطوط الشبكة الرئيسية، سيكون الرسم البياني العمودي المضاف إلى ورقة العمل بالمظهر التالي:

**رسم بياني عمودي مع خطوط شبكة رئيسية ملونة** 

![todo:image_alt_text](chart-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-ChangingMajorGridlines-1.java" >}}

### **تعيين حدود للجدران الخلفية والجانبية**

منذ إصدار Microsoft Excel 2007، تم تقسيم جدران الرسم البياني ثلاثي الأبعاد إلى قسمين: الجدار الجانبي والجدار الخلفي، لذا يجب علينا استخدام كائنين [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls) لتمثيلهما على حدة ويمكنك الوصول إليهما من خلال استخدام [**Chart.getBackWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#BackWall) و [**Chart.getSideWall()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#SideWall).

المثال أدناه يوضح كيفية تعيين حدود الجدار الجانبي باستخدام سمات مختلفة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-SettingChartsAppearance-SettingBorders-1.java" >}}

## **تغيير موقع الرسم البياني وحجمه**

في بعض الأحيان، قد ترغب في تغيير الموضع أو الحجم للرسم البياني الجديد أو القائم داخل ورقة العمل. توفر Aspose.Cells الخاصية [**Chart.getChartObject()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#ChartObject) لتحقيق ذلك. يمكنك استخدام خصائصه الفرعية لإعادة تحجيم الرسم البياني بارتفاع وعرض جديدين أو إعادة تمركزه بإحداثيات **X** و **Y** جديدة.

### **تعديل موقع وحجم الرسم البياني**

لتغيير موقع الرسم البياني (إحداثيات X و Y) وحجمه (ارتفاع وعرض)، استخدم هذه الخصائص:

1. [**Chart.getChartObject().get/setWidth()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Width)
1. [**Chart.getChartObject().get/setHeight()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Height)
1. [**Chart.getChartObject().get/setX()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#X)
1. [**Chart.getChartObject().get/setY()**](https://reference.aspose.com/cells/java/com.aspose.cells/chartshape#Y)

المثال التالي يشرح كيفية استخدام الخصائص أعلاه. يحمل الدفتر العمل الموجود الذي يحتوي على رسم بياني في ورقته الأولى. ثم يقوم بإعادة تحجيم وإعادة تمركز الرسم البياني ويحفظ الدفتر العمل.

قبل تنفيذ كود العينة، يبدو الملف الأصلي على النحو التالي:

**حجم الرسم البياني وموضعه قبل تنفيذ رمز العينة** 

![todo:image_alt_text](chart-formatting_7.png)

بعد التنفيذ، يبدو ملف الإخراج هكذا:

حجم وموقع الرسم البياني بعد تنفيذ الشفرة المثالية 

![todo:image_alt_text](chart-formatting_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChangeChartPositionAndSize-ChangeChartPositionAndSize.java" >}}

## **تلاعب الرسوم البيانية للمصمم**

هناك وقت قد تحتاج فيه إلى تلاعب أو تعديل الرسومات في ملفات القوالب المصممة. Aspose.Cells تدعم بشكل كامل تلاعب الرسومات المصممة مع محتوياتها وعناصرها. يمكن الحفاظ على البيانات ومحتويات الرسم البياني وصورة الخلفية والتنسيق بدقة.

### **تلاعب برسومات المصمم في ملفات القوالب**

لتلاعب برسومات المصمم في ملف القالب، استخدم جميع المكالمات البرمجية ذات الصلة بالرسم البياني. على سبيل المثال، استخدم خاصية [**Worksheet.getCharts**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Charts) للحصول على مجموعة الرسوم البيانية الحالية في ملف القالب.

#### **إنشاء رسم بياني**

المثال التالي يوضح كيفية إنشاء رسم بياني دائري. سنقوم لاحقًا بتلاعب في هذا الرسم البياني. الإخراج التالي مولّد بواسطة الشفرة.

تم تعديل رسم الكعكة 

![todo:image_alt_text](chart-formatting_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

#### **تلاعب الرسم البياني**

المثال التالي يوضح كيفية تلاعب الرسم البياني الحالي. في هذا المثال نقوم بتعديل الرسم البياني الذي تم إنشاؤه أعلاه. الإخراج التالي مولّد بواسطة الشفرة. لاحظ أن لون عنوان الرسم البياني تغير من الأزرق إلى الأسود، وتغير 'إنجلترا 30000' إلى 'المملكة المتحدة، 30 ألف'.

تم تعديل رسم الكعكة 

![todo:image_alt_text](chart-formatting_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyPieChart-ModifyPieChart.java" >}}

#### **تلاعب رسم بياني الخط في القالب المصمم**

في هذا المثال، سنقوم بتلاعب رسم بياني خطي. سنضيف بعض سلاسل البيانات إلى الرسم البياني الحالي وتغيير ألوان خطوطها.

أولاً، دعنا نلقي نظرة على رسم البياني الخطي المصمم.

تم تعديل رسم البياني الخطي 

![todo:image_alt_text](chart-formatting_11.png)

الآن نقوم بتلاعب في رسم البياني الخطي (الموجود في ملف linechart.xls) باستخدام الشفرة التالية. الإخراج التالي مولّد بواسطة الشفرة.

تم تعديل رسم البياني الخطي 

![todo:image_alt_text](chart-formatting_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ModifyLineChart-ModifyLineChart.java" >}}

## **استخدام الشرائط**

يمكن لبرنامج Microsoft Excel 2010 تحليل المعلومات بطرق أكثر من أي وقت مضى. يسمح للمستخدمين بتتبع وتسليط الضوء على اتجاهات البيانات المهمة باستخدام أدوات تحليل البيانات والرؤية الجديدة. الشرائط هي رسومات مصغرة يمكنك وضعها داخل الخلايا بحيث يمكنك عرض البيانات والرسم البياني على الجدول نفسه. عند استخدام الشرائط بشكل صحيح، يكون تحليل البيانات أسرع وأكثر دقة. كما أنها توفر رؤية بسيطة للمعلومات، مما يجنب ورقات العمل المزدحمة بالرسوم البيانية الكثيرة.

توفر Aspose.Cells واجهة برمجة التطبيقات للتلاعب في الشرائط في جداول البيانات.

### **الشرائط في Microsoft Excel**

لإدراج الشرائط في Microsoft Excel 2010:

1. حدد الخلايا التي ترغب في ظهور الشرائط فيها. لجعلها سهلة الرؤية، حدد الخلايا على جانب البيانات.
1. انقر على **Insert** في الشريط واختر **column** في **Sparklines**.

![todo:image_alt_text](chart-formatting_13.png)

1. حدد أو أدخل نطاق الخلايا في ورقة العمل التي تحتوي على بيانات المصدر.
   ستظهر الرسوم البيانية.

تساعد التأثيرات البصرية الصغيرة في رؤية الاتجاهات، على سبيل المثال، أو سجل الفوز أو الخسارة لرابطة الكرة اللينة. يمكن للتأثيرات البصرية الصغيرة حتى تلخص موسم كل فريق في الرابطة بأكمله.

![todo:image_alt_text](chart-formatting_14.png)

### **شرائط البيانات باستخدام Aspose.Cells**

يمكن للمطورين إنشاء، حذف أو قراءة التأثيرات البصرية الصغيرة (في ملف القالب) باستخدام واجهة برمجة التطبيقات المقدمة بواسطة Aspose.Cells. من خلال إضافة رسومات مخصصة لنطاق البيانات المعطى، يحظى المطورون بحرية إضافة أنواع مختلفة من الرسوم البيانية الصغيرة إلى مناطق الخلايا المحددة.

يوضح المثال أدناه ميزة شرائط البيانات. يوضح المثال كيفية:

1. فتح ملف قالب بسيط.
1. قراءة معلومات شرائط البيانات لورقة عمل.
1. إضافة شرائط بيانات جديدة لنطاق بيانات معطى إلى منطقة خلية.
1. حفظ ملف Excel إلى القرص.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-UsingSparklines-UsingSparklines.java" >}}

## **تطبيق تنسيق ثلاثي الأبعاد على الرسم البياني**

قد تحتاج إلى أنماط الرسوم البيانية ثلاثية الأبعاد حتى تحصل على النتائج المناسبة لسيناريو الخاص بك. توفر واجهات برمجة التطبيقات لـ Aspose.Cells الواجهة البرمجية ذات الصلة لتطبيق التنسيق ثلاثي الأبعاد لـ Microsoft Excel 2007 كما هو موضح في هذا المقال.

### **تحديد تنسيق ثلاثي الأبعاد للرسم البياني**

يتضمن المثال الكامل أدناه لتوضيح كيفية إنشاء رسم بياني وتطبيق تنسيق ثلاثي الأبعاد لـ Microsoft Excel 2007. بعد تنفيذ رمز المثال أعلاه، سيتم إضافة رسم بياني عمودي (برؤوس ثلاثية الأبعاد) إلى ورقة العمل كما هو موضح أدناه.

**رسم بياني عمودي بتنسيق ثلاثي الأبعاد**

![todo:image_alt_text](chart-formatting_15.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-Applying3DFormat-Applying3DFormat.java" >}}

{{% alert color="primary" %}}

للحصول على قائمة كاملة باستخدام أنواع الرسوم البيانية ثنائية وثلاثية الأبعاد المدعمة، انظر [أنواع الرسوم البيانية المدعومة للعرض](/cells/ar/java/chart-rendering/#supported-chart-types-for-rendering).

{{% /alert %}}

## **مواضيع متقدمة**
- [تعيين صورة كحشو خلفية في الرسم البياني](/cells/ar/java/set-picture-as-background-fill-in-the-chart/)
