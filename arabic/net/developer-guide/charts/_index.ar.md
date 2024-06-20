---
title: إنشاء وإدارة الرسم البياني
description: تعلم كيفية استخدام Aspose.Cells for .NET لإنشاء رسوم بيانية في Microsoft Excel. سيقدم دليلنا توضيحًا للأنواع المختلفة من الرسوم البيانية التي يمكن إنشاؤها، فضلاً عن كيفية تخصيص مظهرها وتنسيقها.
keywords: Aspose.Cells for .NET، إنشاء رسم بياني، Microsoft Excel، أنواع الرسوم البيانية، التخصيص، المظهر، التنسيق.
linktitle: رسوم بيانية
type: docs
weight: 130
url: /ar/net/creating-charts/
description: إنشاء رسم بياني في CSharp لملفات Excel وODS.
keywords: إنشاء رسم بياني، إنشاء رسم بياني 
---

{{% alert color="primary" %}}

من الممكن إضافة مجموعة متنوعة من الرسوم البيانية إلى جداول البيانات باستخدام Aspose.Cells. توفر Aspose.Cells العديد من كائنات الرسم البياني المرنة. يتناول هذا الموضوع كائنات الرسم البياني في Aspose.Cells.

{{% /alert %}}

## **إنشاء الرسوم البيانية**

### **ببساطة إنشاء رسم بياني**
إنشاء مخطط بسيط باستخدام Aspose.Cells يمكن تحقيقه باستخدام أكواد الأمثلة التالية:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **الأشياء التي يجب معرفتها لإنشاء مخطط**

قبل إنشاء المخططات، من المهم فهم بعض المفاهيم الأساسية التي تكون مفيدة عند إنشاء المخططات باستخدام Aspose.Cells.

#### **كائنات المخطط**

تقدم Aspose.Cells مجموعة خاصة من الفصول في مساحة الاسم [**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts) والتي تُستخدم لإنشاء المخططات المدعومة بواسطة Aspose.Cells. يتم استخدام هذه الفصول لإنشاء **كائنات المخطط** التي تعتبر كبنية أساسية لبناء المخطط. يتم سرد كائنات المخطط أدناه:

- Series، سلسلة بيانات واحدة في المخطط.
- Axis، محور المخطط.
- Chart، مخطط Excel واحد.
- ChartArea، منطقة المخطط في ورقة العمل.
- ChartDataTable، جدول بيانات المخطط.
- ChartFrame، كائن الإطار في المخطط.
- ChartPoint، نقطة واحدة في سلسلة في المخطط.
- ChartPointCollection، مجموعة تحتوي على جميع النقاط في سلسلة واحدة.
- Charts، مجموعة من كائنات المخطط.
- DataLabels، مجموعة من جميع كائنات DataLabel للسلسلة المحددة.
- FillFormat، تنسيق الملء للشكل.
- Floor، الطابق لمخطط ثلاثي الأبعاد.
- Legend، وسام المخطط.
- Line، خط المخطط.
- SeriesCollection، مجموعة من كائنات Series.
- تسميات العلامات، علامات العلامة المرتبطة بعلامات ضبط على محور الرسم البياني.
- العنوان، عنوان الرسم البياني أو المحور.
- خط الاتجاه، خط اتجاه في الرسم البياني.
- مجموعة خطوط الاتجاه، مجموعة من جميع كائنات خط الاتجاه لسلسلة البيانات المحددة.
- الجدران، الجدران في رسم بياني ثلاثي الأبعاد.

#### **استخدام كائنات الرسم البياني**

كما ذكر أعلاه، جميع كائنات الرسم البياني هي حالات من فئاتها الخاصة وتوفر خصائص وأساليب محددة لأداء مهام محددة. استخدم كائنات الرسم البياني لإنشاء رسوم بيانية.

إضافة أي نوع من الرسم البياني إلى ورقة العمل باستخدام مجموعة [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts). كل عنصر في مجموعة [**Charts**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) يمثل كائن [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart). الكائن [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) يغلف جميع كائنات الرسم البياني الأخرى المطلوبة لتخصيص مظهر الرسم البياني. يوضح القسم التالي كيفية استخدام بعض كائنات الرسم البياني الأساسية لإنشاء رسم بياني بسيط.

### **إنشاء رسم بياني باستخدام Aspose.Cells**

**الخطوات:**

1. أضف بعض البيانات إلى خلايا ورقة العمل باستخدام الطريقة [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) لكائن [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).
   سيتم استخدام هذا كمصدر بيانات للرسم البياني.
1. أضف رسم بياني إلى ورقة العمل عن طريق استدعاء الطريقة [**Add**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) لمجموعة الكائنات [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)، التي تم تغليفها في الكائن [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).
1. حدد نوع الرسم البياني بتعداد [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).
   على سبيل المثال، يستخدم المثال أدناه القيمة [**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) كنوع للرسم البياني.
1. اصطحب الكائن [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) المكون حديثًا من مجموعة [**Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) عن طريق تمرير فهرسه.
1. استخدم أي من كائنات الرسم البياني المغلفة في الكائن [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) لإدارة الرسم البياني.
   يستخدم المثال أدناه كائن الرسم البياني [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) لتحديد مصدر بيانات الرسم البياني.

عند إضافة بيانات المصدر إلى الرسم البياني، يمكن أن يكون مصدر البيانات مجموعة من الخلايا (مثل "A1:C3")، أو تسلسل من الخلايا غير المتصلة (مثل "A1، A3، A5")، أو تسلسل من القيم (مثل "1،2،3").

تتيح لك هذه الخطوات العامة إنشاء أي نوع من الرسم البياني. استخدم كائنات الرسم البياني المختلفة لإنشاء رسوم بيانية مختلفة.

من الممكن إنشاء العديد من أنواع الرسوم البيانية المختلفة باستخدام Aspose.Cells. جميع الرسوم البيانية القياسية المدعومة بواسطة Aspose.Cells محددة مسبقًا في تعداد يسمى [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

تخطيطات الرسوم البيانية المحددة مسبقًا هي:

|**أنواع الرسوم البيانية**|**الوصف**|
| :- | :- |
|Column| يمثل مخطط الأعمدة المتجانبة
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
|Scatter|تمثل مخطط النقاط|
|ScatterConnectedByCurvesWithDataMarker|تمثل مخطط النقاط متصلة بالخطوط المنحنية، مع علامات البيانات|
|ScatterConnectedByCurvesWithoutDataMarker|تمثل مخطط النقاط متصلة بالخطوط المنحنية، بدون علامات البيانات|
|ScatterConnectedByLinesWithDataMarker|تمثل مخطط النقاط متصلة بخطوط، مع علامات البيانات|
|ScatterConnectedByLinesWithoutDataMarker|تمثل مخطط النقاط متصلة بخطوط، بدون علامات البيانات|
|Area|تمثل مخطط المساحة|
|AreaStacked|تمثل مخطط المساحة المكدسة|
|Area100PercentStacked|تمثل مخطط المساحة المكدسة 100%|
|Area3D|تمثل مخطط المساحة ثلاثي الأبعاد|
|Area3DStacked|تمثل مخطط المساحة المكدسة ثلاثي الأبعاد|
|Area3D100PercentStacked|تمثل مخطط المساحة المكدسة 100% ثلاثي الأبعاد|
|Doughnut|يمثل مخطط الدونات|
|DoughnutExploded|يمثل مخطط الدونات المتفجر|
|Radar|يمثل مخطط الرادار|
|RadarWithDataMarkers|يمثل مخطط الرادار مع علامات البيانات|
|RadarFilled|يمثل مخطط الرادار المملوء|
|Surface3D|يمثل مخطط السطح ثلاثي الأبعاد|
|SurfaceWireframe3D|يمثل مخطط سطح ثلاثي الأبعاد بالأسلاك|
|SurfaceContour|يمثل مخطط التكهف|
|SurfaceContourWireframe|يمثل مخطط التكهف بالأسلاك|
|Bubble|يمثل مخطط الفقاعات|
|Bubble3D|يمثل مخطط الفقاعات ثلاثي الأبعاد|
|Cylinder|يمثل مخطط الأسطوانة|
|CylinderStacked|يمثل مخطط الأسطوانة المكدسة|
|Cylinder100PercentStacked|يمثل المخطط الأسطواني المكدس بنسبة 100٪|
|CylindericalBar|يمثل مخطط الأعمدة الأسطوانية|
|CylindericalBarStacked|يمثل مخطط الأعمدة الأسطوانية المكدسة|
|CylindericalBar100PercentStacked|يمثل المخطط الأسطواني المكدس بنسبة 100٪|
|CylindericalColumn3D|يمثل مخطط الأعمدة الأسطوانية ثلاثي الأبعاد|
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
|PyramidBar|يمثل رسم بياني شريطي هرمي|
|PyramidBarStacked|يمثل رسم بياني شريطي هرمي مكدس|
|PyramidBar100PercentStacked|يمثل رسم بياني شريطي هرمي مكدس بنسبة 100%|
|PyramidColumn3D|يمثل رسم بياني أعمدة هرمي ثلاثي الأبعاد|
{{% alert color="primary" %}}

عندما تُسند نطاقًا من الخلايا كمصدر للبيانات، يمكنك تعيين النطاق فقط من الزاوية العلوية اليسرى إلى الزاوية السفلى اليمنى. على سبيل المثال، "A1:C3" صالح بينما "C3:A1" غير صالح.

{{% /alert %}}

#### **رسم بياني الهرم**

عند تنفيذ الشيفرة المرجعية، يتم إضافة رسم بياني للهرم إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **رسم بياني خطي**

في المثال أعلاه، ببساطة تغيير [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) إلى *Line* يُنشئ رسم بياني خطي. يتم توفير المصدر الكامل أدناه. عند تنفيذ الشيفرة، يتم إضافة رسم بياني خطي إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **رسم بياني فقاعي**

لإنشاء رسم بياني فقاعي، يجب تعيين [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) إلى [**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) وضبط خصائص إضافية بمثابة BubbleSizes, Values & XValues وفقًا لذلك. عند تنفيذ الشيفرة التالية، يتم إضافة رسم بياني فقاعي إلى ورقة العمل.

#### **رسم بياني خطي بمؤشرات البيانات**

لإنشاء خط برسم بياني البيانات، يجب ضبط [**ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) على *ChartType.LineWithDataMarkers* ويجب ضبط بعض الخصائص الإضافية مثل منطقة الخلفية، علامات السلاسل، القيم والقيم السينية وفقًا لذلك. عند تنفيذ الشفرة التالية، يتم إضافة خط برسم بياني البيانات إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **مواضيع متقدمة**
- [قراءة وتلاعب شكل بيانات Excel 2016](/cells/ar/net/read-and-manipulate-excel-2016-charts/)
- [إدارة محاور مخططات Excel](/cells/ar/net/chart-axes/)
- [ضبط مظهر الرسم البياني](/cells/ar/net/setting-chart-appearance/)
- [أنواع المخططات](/cells/ar/net/chart-types/)
- [تخصيص المخططات](/cells/ar/net/customizing-charts/)
- [تعيين مصدر البيانات للمخطط](/cells/ar/net/data-formatting-in-charts/)
- [إدارة تسميات البيانات في مخططات Excel](/cells/ar/net/insert-datalabels-to-chart/)
- [إنشاء مخطط بمعالجة العلامات الذكية](/cells/ar/net/generate-chart-by-processing-smart-markers/)
- [الحصول على ورقة العمل من المخطط](/cells/ar/net/get-worksheet-of-the-chart/)
- [إدارة الأسطورة في مخططات Excel](/cells/ar/net/chart-legend/)
- [تلاعب بموقع وحجم وتصميم المخطط](/cells/ar/net/manipulate-position-size-and-designer-chart/)
- [إنشاء مخطط دائري مع خطوط قيادة](/cells/ar/net/creating-pie-chart-with-leader-lines/)
- [الأشكال في المخططات](/cells/ar/net/controls-in-charts/)
- [إدارة عناوين مخططات Excel](/cells/ar/net/chart-and-axis-titles/)
- [عرض الرسم البياني](/cells/ar/net/chart-rendering/)
- [الحصول على نص المعادلة لخط اتجاه المخطط](/cells/ar/net/get-equation-text-of-chart-trendline/)
