---
title: تخصيص المخططات
type: docs
weight: 15
url: /ar/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---

## **إنشاء الرسوم البيانية**

من الممكن إضافة مجموعة متنوعة من الرسوم البيانية إلى جداول البيانات باستخدام Aspose.Cells. توفر Aspose.Cells العديد من كائنات الرسم البياني المرنة. يتناول هذا الموضوع كائنات الرسم البياني في Aspose.Cells.

### **ببساطة إنشاء رسم بياني**

من السهل إنشاء مخطط باستخدام Aspose.Cells مع أمثلة الشفرة التالية:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **أشياء يجب معرفتها لإنشاء مخطط**

قبل إنشاء المخططات، من المهم فهم بعض المفاهيم الأساسية التي تكون مفيدة عند إنشاء المخططات باستخدام Aspose.Cells.

#### **كائنات المخطط**

توفر Aspose.Cells مجموعة خاصة من الفئات المستخدمة لإنشاء جميع أنواع المخططات. تُستخدم هذه الفئات لإنشاء **كائنات المخططات**، التي تعمل كبناء المخطط. يتم سرد كائنات المخططات أدناه:

- [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis)، محور للمخطط.
- [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)، مخطط Excel واحد.
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea)، منطقة المخطط في ورقة العمل.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable)، جدول بيانات المخطط.
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame)، كائن الإطار في الرسم البياني.
- [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)، نقطة واحدة في سلسلة في رسم بياني.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection)، مجموعة تحتوي على جميع النقاط في سلسلة واحدة.
- [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)، مجموعة من [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) كائن.
- DataLabels، تسميات البيانات لل [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) المحدد، [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)، [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)، وما إلى ذلك.
- [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat)، تنسيق التعبئة لشكل.
- [**Floor**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor)، الطابق في الرسم البياني ثلاثي الأبعاد.
- [**Legend**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend)، أسطورة الرسم البياني.
- [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)، خط الرسم البياني.
- [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)، مجموعة من [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) كائن.
- [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)، يمثل سلسلة بيانات واحدة في الرسم البياني.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels)، تسميات علامات الصح عندما يرتبطون بعلامات على محور الرسم البياني.
- [**Title**](https://reference.aspose.com/cells/java/com.aspose.cells/Title)، عنوان الرسم البياني أو المحور.
- [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)، خط اتجاه في الرسم البياني.
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection)، مجموعة من جميع كائنات خط الاتجاه لسلسلة البيانات المحددة.
- [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)، الجدران في رسم بياني ثلاثي الأبعاد.

#### **استخدام كائنات الرسم البياني**

كما ذكر أعلاه، جميع كائنات الرسم البياني هي حالات من فئاتها الخاصة وتوفر خصائص وأساليب محددة لأداء مهام محددة. استخدم كائنات الرسم البياني لإنشاء رسوم بيانية.

أضف أي نوع من الرسوم البيانية إلى ورقة العمل باستخدام مجموعة [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) . كل عنصر في مجموعة [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) يمثل كائن [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) . يكتنف كائن [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) جميع أجسام الرسم البياني المطلوبة لتخصيص مظهر الرسم البياني. توضح القسم التالي كيفية استخدام بعض أجسام الرسم البياني الأساسية لإنشاء رسم بياني بسيط.

### **إنشاء رسم بياني بسيط**

من الممكن إنشاء العديد من أنواع مختلفة من الرسوم البيانية باستخدام Aspose.Cells. جميع الرسوم البيانية القياسية المدعومة بواسطة Aspose.Cells محددة مسبقا في تعداد يسمى [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). أنواع الرسوم البيانية المحددة مسبقا هي:

|**أنواع الرسوم البيانية**|**الوصف**|
| :- | :- |
|Column| يمثل مخطط العمود المتجمع
|ColumnStacked| يمثل مخطط الأعمدة المكدسة
|Column100PercentStacked| يمثل مخطط الأعمدة المكدسة بنسبة 100%
|Column3DClustered| يمثل مخطط الأعمدة المتجانبة ثلاثي الأبعاد
|Column3DStacked| يمثل مخطط الأعمدة المكدسة ثلاثي الأبعاد
|Column3D100PercentStacked| يمثل مخطط الأعمدة المكدسة بنسبة 100% ثلاثي الأبعاد
|Column3D| يمثل مخطط الأعمدة ثلاثي الأبعاد
|Bar| يمثل مخطط الأعمدة المتجانبة الأفقية
|BarStacked| يمثل مخطط الأعمدة المكدسة الأفقية
|Bar100PercentStacked| يمثل مخطط الأعمدة المكدسة بنسبة 100% الأفقية
|Bar3DClustered| يمثل مخطط الأعمدة المتجانبة ثلاثي الأبعاد الأفقية
|Bar3DStacked| يمثل مخطط الأعمدة المكدسة ثلاثي الأبعاد الأفقية
|Bar3D100PercentStacked| يمثل مخطط الأعمدة المكدسة بنسبة 100% ثلاثي الأبعاد الأفقية
|Line| يمثل مخطط الخطوط
|LineStacked| يمثل مخطط الخطوط المكدسة
|Line100PercentStacked| يمثل مخطط الخطوط المكدسة بنسبة 100%
|LineWithDataMarkers| يمثل مخطط الخط مع علامات البيانات
|LineStackedWithDataMarkers|تمثل مخطط خطوط مكدسة مع علامات البيانات|
|Line100PercentStackedWithDataMarkers|تمثل مخطط خطوط مكدسة 100% مع علامات البيانات|
|Line3D|تمثل مخطط خطوط ثلاثي الأبعاد|
|Pie|تمثل مخطط دائري|
|Pie3D|تمثل مخطط دائري ثلاثي الأبعاد|
|PiePie|تمثل مخطط دائري فوق الدائرة|
|PieExploded|تمثل مخطط دائري منفجر|
|Pie3DExploded|تمثل مخطط دائري منفجر ثلاثي الأبعاد|
|PieBar|تمثل مخطط بارز فوق القطعة من البيتزا|
|Scatter| تمثل مخطط النقاط|
|ScatterConnectedByCurvesWithDataMarker|تمثل مخطط النقاط المتصل بالمنحنيات مع علامات البيانات|
|ScatterConnectedByCurvesWithoutDataMarker|تمثل مخطط النقاط المتصل بالمنحنيات بدون علامات البيانات|
|ScatterConnectedByLinesWithDataMarker|تمثل مخطط النقاط المتصل بالخطوط مع علامات البيانات|
|ScatterConnectedByLinesWithoutDataMarker|تمثل مخطط النقاط المتصل بالخطوط بدون علامات البيانات|
|Area|تمثل مخطط المساحة|
|AreaStacked|تمثل مخطط المساحة المكدسة|
|Area100PercentStacked|تمثل مخطط المساحة المكدسة 100%|
|Area3D|تمثل مخطط المساحة ثلاثي الأبعاد|
|Area3DStacked|تمثل مخطط المساحة المكدسة ثلاثي الأبعاد|
|Area3D100PercentStacked|تمثل مخطط المساحة المكدسة 100% ثلاثي الأبعاد|
|Doughnut|يمثل مخطط الدونات|
|DoughnutExploded|يمثل مخطط الدونات المتفجر|
|Radar|يمثل تخطيط الرادار|
|RadarWithDataMarkers|يمثل تخطيط الرادار مع علامات البيانات|
|RadarFilled|يمثل مخطط الرادار المملوء|
|Surface3D|يمثل مخطط السطح ثلاثي الأبعاد|
|SurfaceWireframe3D|يمثل تخطيط السطح ثلاثي الأبعاد الشبكي|
|SurfaceContour|يمثل مخطط التكهف|
|SurfaceContourWireframe|يمثل مخطط التكهف بالأسلاك|
|Bubble|يمثل مخطط الفقاعات|
|Bubble3D|يمثل مخطط الفقاعات ثلاثي الأبعاد|
|Cylinder|يمثل مخطط الأسطوانة|
|CylinderStacked|يمثل مخطط الأسطوانة المكدسة|
|Cylinder100PercentStacked|يمثل المخطط الأسطواني المكدس بنسبة 100٪|
|CylindricalBar|يمثل تخطيط الشريط الأسطواني|
|CylindricalBarStacked|يمثل تخطيط الشريط الأسطواني المكدس|
|CylindricalBar100PercentStacked|يمثل تخطيط الشريط الأسطواني المكدس بنسبة 100%|
|CylindricalColumn3D|يمثل تخطيط الأعمدة الأسطوانية ثلاثية الأبعاد|
|Cone|يمثل مخطط المخروط|
|ConeStacked|يمثل مخطط المخروط المكدس|
|Cone100PercentStacked|يمثل 100% حجم الرسم البياني المكدس المخروطي|
|ConicalBar|يمثل رسم بياني شريطي مخروطي|
|ConicalBarStacked|يمثل رسم بياني شريطي مكدس مخروطي|
|ConicalBar100PercentStacked|يمثل رسم بياني شريطي مخروطي مكدس بنسبة 100%|
|ConicalColumn3D|يمثل رسم بياني أعمدة مخروطي ثلاثي الأبعاد|
|Pyramid|يمثل رسم بياني الهرم|
|PyramidStacked|يمثل رسم بياني الهرم المكدس|
|Pyramid100PercentStacked|يمثل رسم بياني الهرم المكدس بنسبة 100%|
|PyramidBar|تمثل رسم بياني بشكل هرمي مخروطي|
|PyramidBarStacked|يمثل رسم بياني شريطي هرمي مكدس|
|PyramidBar100PercentStacked|يمثل رسم بياني شريطي هرمي مكدس بنسبة 100%|
|PyramidColumn3D|يمثل رسم بياني أعمدة هرمي ثلاثي الأبعاد|
لا إنشاء رسم بياني باستخدام Aspose.Cells:

1. أضف بعض البيانات إلى خلايا ورقة العمل باستخدام الطريقة [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) لكائن [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell).
   سيتم استخدام هذا كمصدر بيانات للرسم البياني.
1. أضف رسمًا بيانيًا إلى ورقة العمل عن طريق استدعاء مجموعة [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) طريقة [*add*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add-int-int-int-int-int-)، المضمّنة في كائن [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).
1. حدد نوع الرسم البياني بتعداد [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType).
   على سبيل المثال، يستخدم المثال قيمة [**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID) كنوع رسم بياني.
1. اصطحب الكائن [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) المكون حديثًا من مجموعة [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) عن طريق تمرير فهرسه.
1. استخدم أي من كائنات الرسم البياني المغلفة في الكائن [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) لإدارة الرسم البياني.
   يستخدم المثال أدناه كائن الرسم البياني [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) لتحديد مصدر بيانات الرسم البياني.

عند إضافة بيانات المصدر إلى الرسم البياني، يمكن أن يكون مصدر البيانات مجموعة من الخلايا (مثل "A1:C3")، أو تسلسل من الخلايا غير المتصلة (مثل "A1، A3، A5")، أو تسلسل من القيم (مثل "1،2،3").

{{% alert color="primary" %}}

عندما تخصص مجموعة من الخلايا كمصدر للبيانات، يمكنك فقط تحديد المدى من أعلى اليسار إلى أسفل اليمين. على سبيل المثال، "A1:C3" هو صحيح بينما "C3:A1" غير صالح.

{{% /alert %}}

تتيح لك هذه الخطوات العامة إنشاء أي نوع من الرسم البياني. استخدم كائنات الرسم البياني المختلفة لإنشاء رسوم بيانية مختلفة.

عند تنفيذ كود المثال، يتم إضافة رسم بياني هرمي إلى ورقة العمل كما هو مبين أدناه.

**رسم بياني هرمي مع مصدر بياناته**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

لإنشاء رسم بياني فقاعة، يجب ضبط [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) ليكون [**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)، ويجب ضبط بعض الخصائص الإضافية مثل BubbleSizes, Values & XValues على هذا النحو. عند تنفيذ الكود التالي، يتم إضافة رسم بياني فقاعة إلى ورقة العمل كما هو مبين أدناه.

**رسم بياني فقاعة مع مصدر بياناته**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **رسم بياني خطي بمؤشرات البيانات**

لإنشاء رسم بياني خطي بعلامة بيانات، يجب ضبط ال [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) على أن يكون [**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE-WITH-DATA-MARKERS) ويجب ضبط بعض الخصائص الإضافية مثل منطقة الخلفية، علامات السلسلة، القيم وXValues بحسب ما هو مطلوب. عند تنفيذ الكود التالي، يتم إضافة رسم بياني خطي بعلامة بيانات إلى ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **إنشاء مخططات مخصصة**

حتى الآن، عندما تم مناقشة الرسوم البيانية، نظرنا إلى الرسوم البيانية القياسية التي لديها إعدادات تنسيق قياسية. نعرف فقط مصدر البيانات، ونضبط بعض الخصائص ويتم إنشاء الرسم البياني بإعدادات تنسيقه الافتراضية. ولكن Aspose.Cells تدعم أيضا إنشاء رسوم بيانية مخصصة تتيح للمطورين إنشاء رسوم بيانية بإعدادات تنسيق خاصة بهم.

### **إنشاء مخططات مخصصة**

يمكن للمطورين إنشاء رسوم بيانية مخصصة في وقت التشغيل باستخدام واجهة برمجة التطبيقات البسيطة لـ Aspose.Cells.

يتألف الرسم البياني من سلسلة بيانات. كل سلسلة بيانات في Aspose.Cells تُمثلها [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) بينما [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) يعمل كمجموعة من [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series). عند إنشاء رسم بياني مخصص، يحظى المطورون بحرية استخدام أنواع مختلفة من الرسوم البيانية لسلاسل البيانات المختلفة (التي يتم جمعها في [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)).

{{% alert color="primary" %}}

حالياً، تدعم Aspose.Cells فقط الرسوم البيانية المخصصة التي تجمع بين رسوم الدائرة، الخط، العمود والعمود المكدس ولكن سيتم دعم المزيد من الرسوم في الإصدارات المستقبلية. للحصول على قائمة كاملة بأنواع الرسوم البيانية القياسية التي تدعمها Aspose.Cells، اقرأ مقالة [أنواع الرسوم](/cells/ar/java/chart-types/).

{{% /alert %}}

الكود المثال أدناه يوضح كيفية إنشاء مخططات مخصصة. في هذا المثال، سنستخدم مخطط عمودي لأول سلسلة بيانات ومخطط خطي للسلسلة الثانية. النتيجة هي أننا نضيف مخطط عمودي، مع مخطط خطي، إلى ورقة العمل.

**رسم بياني مخصص يجمع بين رسوم العمود والخط**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**مثال برمجي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

لرؤية قائمة بأنواع الرسوم البيانية المدعومة، اقرأ مقالة [أنواع الرسوم](/cells/ar/java/chart-types/).

{{% /alert %}}

{{< app/cells/assistant language="java" >}}
