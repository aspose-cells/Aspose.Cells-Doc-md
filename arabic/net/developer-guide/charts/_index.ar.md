---
title: إنشاء وإدارة الرسم البياني
description: تعرف على كيفية استخدام Aspose.Cells for .NET لإنشاء المخططات في Microsoft Excel. سيوضح دليلنا الأنواع المختلفة من المخططات التي يمكن إنشاؤها، بالإضافة إلى كيفية تخصيص مظهرها وتنسيقها.
keywords: Aspose.Cells for .NET, Chart Creation, Microsoft Excel, Chart Types, Customization, Appearance, Formatting.
linktitle: الرسوم البيانية
type: docs
weight: 130
url: /ar/net/creating-charts/
description: قم بإنشاء مخطط في CSharp for Excel وملفات ODS.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

من الممكن إضافة مجموعة متنوعة من المخططات إلى جداول البيانات باستخدام Aspose.Cells. يوفر Aspose.Cells العديد من كائنات الرسوم البيانية المرنة. يناقش هذا الموضوع كائنات التخطيط Aspose.Cells.

{{% /alert %}}

##  **إنشاء الرسوم البيانية**

###  **ببساطة إنشاء مخطط**
من السهل إنشاء مخطط بالرقم Aspose.Cells باستخدام رموز الأمثلة التالية:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

###  **أشياء يجب معرفتها لإنشاء مخطط**

قبل إنشاء المخططات، من المهم فهم بعض المفاهيم الأساسية التي تكون مفيدة عند إنشاء المخططات باستخدام Aspose.Cells.

####  **رسم الكائنات**

 Aspose.Cells يوفر مجموعة خاصة من الفئات في[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)مساحة الاسم المستخدمة لإنشاء المخططات التي يدعمها Aspose.Cells. يتم استخدام هذه الفئات لإنشاء *كائنات المخططات**، والتي تعمل كعناصر بناء للمخطط. كائنات التخطيط مدرجة أدناه:

- السلسلة، سلسلة بيانات واحدة في مخطط.
- المحور، محور المخطط.
- الرسم البياني، مخطط Excel واحد.
- منطقة التخطيط، منطقة المخطط في ورقة العمل.
- ChartDataTable، جدول بيانات الرسم البياني.
- ChartFrame، كائن الإطار في المخطط.
- ChartPoint، نقطة واحدة في سلسلة في المخطط.
- ChartPointCollection، مجموعة تحتوي على كافة النقاط في سلسلة واحدة.
- الرسوم البيانية، مجموعة من كائنات الرسم البياني.
- DataLabels، مجموعة من كافة كائنات DataLabel للسلسلة المحددة.
- فيلفورمات، تعبئة الشكل للشكل.
- أرضية، أرضية مخطط ثلاثي الأبعاد.
- أسطورة، أسطورة الرسم البياني.
- الخط، خط الرسم البياني.
- SeriesCollection، مجموعة من كائنات السلسلة.
- TickLabels، تسميات علامات التجزئة المرتبطة بعلامات التجزئة على محور المخطط.
- العنوان، عنوان المخطط أو المحور.
- خط الاتجاه، خط الاتجاه في الرسم البياني.
- TrendlineCollection، مجموعة من كافة كائنات Trendline لسلسلة البيانات المحددة.
- الجدران، جدران مخطط ثلاثي الأبعاد.

####  **استخدام كائنات التخطيط**

كما هو مذكور أعلاه، فإن كافة كائنات التخطيط هي مثيلات لفئاتها الخاصة وتوفر خصائص وأساليب محددة لتنفيذ مهام محددة. استخدم كائنات التخطيط لإنشاء المخططات.

 أضف أي نوع من المخططات إلى ورقة العمل باستخدام[**الرسوم البيانية**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) مجموعة. كل عنصر في[**الرسوم البيانية**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) جمع يمثل أ[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) هدف. أ[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)يقوم الكائن بتغليف كافة كائنات التخطيط الأخرى المطلوبة لتخصيص مظهر المخطط. يوضح القسم التالي كيفية استخدام بعض كائنات التخطيط الأساسية لإنشاء مخطط بسيط.

###  **إنشاء مخطط باستخدام Aspose.Cells**

**خطوات:**

1. أضف بعض البيانات إلى خلايا ورقة العمل باستخدام الملحق[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) أشياء[**ضع القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)طريقة.
 سيتم استخدام هذا كمصدر بيانات للمخطط.
1.  أضف مخططًا إلى ورقة العمل عن طريق استدعاء[**الرسوم البيانية**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) المجموعة[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) الطريقة، مغلفة في[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)هدف.
1.  حدد نوع المخطط باستخدام[**نوع التخطيط**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)تعداد.
 على سبيل المثال، يستخدم المثال أدناه[**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)القيمة كنوع المخطط.
1.  الوصول إلى الجديد[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) كائن من[**الرسوم البيانية**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)جمع عن طريق تمرير فهرسها.
1.  استخدم أيًا من كائنات التخطيط المغلفة في[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)كائن لإدارة المخطط.
 يستخدم المثال أدناه[**مجموعة السلسلة**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)كائن التخطيط لتحديد مصدر بيانات المخطط.

عند إضافة بيانات المصدر إلى المخطط، يمكن أن يكون مصدر البيانات عبارة عن نطاق من الخلايا (مثل "A1:C3")، أو تسلسل من الخلايا غير المتجاورة (مثل "A1، A3، A5")، أو تسلسل من الخلايا القيم (مثل "1،2،3").

تسمح لك هذه الخطوات العامة بإنشاء أي نوع من المخططات. استخدم كائنات تخطيطية مختلفة لإنشاء مخططات مختلفة.

من الممكن إنشاء العديد من أنواع المخططات المختلفة باستخدام Aspose.Cells. جميع المخططات القياسية التي يدعمها Aspose.Cells محددة مسبقًا في تعداد يسمى[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

أنواع المخططات المحددة مسبقًا هي:

|**أنواع المخططات**|**وصف**|
| :- | :- |
|عمود|يمثل مخطط عمود متفاوت المسافات|
|عمود مكدس|يمثل مخططًا عموديًا مكدسًا|
|عمود100%مكدس|يمثل مخططًا عموديًا مكدسًا بنسبة 100%|
|Column3Dمجمع|يمثل مخططًا عموديًا متفاوت المسافات ثلاثي الأبعاد|
|Column3DStacked|يمثل مخططًا عموديًا مكدسًا ثلاثي الأبعاد|
|العمود3D100٪مكدس|يمثل مخططًا عموديًا مكدسًا ثلاثي الأبعاد بنسبة 100%|
|عمود3D|يمثل مخططًا عموديًا ثلاثي الأبعاد|
|حاجِز|يمثل مخطط شريطي متفاوت المسافات|
|BarStacked|يمثل مخطط شريطي مكدس|
|شريط مكدس بنسبة 100%|يمثل مخططًا شريطيًا مكدسًا بنسبة 100%|
|Bar3Dمجمع|يمثل مخطط شريطي متفاوت المسافات ثلاثي الأبعاد|
|Bar3DStacked|يمثل مخطط شريطي مكدس ثلاثي الأبعاد|
|شريط3D100%مكدس|يمثل مخططًا شريطيًا مكدسًا ثلاثي الأبعاد بنسبة 100%|
|خط|يمثل الرسم البياني الخطي|
|LineStacked|يمثل مخططًا خطيًا مكدسًا|
|Line100%مكدس|يمثل مخططًا خطيًا مكدسًا بنسبة 100%|
|LineWithDataMarkers|يمثل مخططًا خطيًا مع علامات البيانات|
|LineStackedWithDataMarkers|يمثل مخططًا خطيًا مكدسًا مع علامات البيانات|
|Line100%مكدس مع علامات البيانات|يمثل مخططًا خطيًا مكدسًا بنسبة 100% مع علامات البيانات|
|Line3D|يمثل مخطط خطي ثلاثي الأبعاد|
|فطيرة|يمثل الرسم البياني الدائري|
|فطيرة3D|يمثل مخططًا دائريًا ثلاثي الأبعاد|
|فطيرة فطيرة|يمثل فطيرة الرسم البياني الدائري|
|فطيرة انفجرت|يمثل مخطط دائري انفجر|
|Pie3DExploded|يمثل مخطط دائري انفجر ثلاثي الأبعاد|
|بيبار|يمثل شريط الرسم البياني الدائري|
|مبعثر|يمثل مخطط مبعثر|
|مبعثر متصل بواسطة منحنيات مع DataMarker|يمثل مخططًا مبعثرًا متصلاً بواسطة منحنيات، مع علامات البيانات|
|مبعثر متصل بواسطة منحنيات بدون علامة البيانات|يمثل مخططًا مبعثرًا متصلاً بواسطة منحنيات، بدون علامات بيانات|
|ScatterConnectedByLinesWithDataMarker|يمثل مخططًا مبعثرًا متصلاً بخطوط، مع علامات البيانات|
|ScatterConnectedByLinesWithoutDataMarker|يمثل مخططًا مبعثرًا متصلاً بخطوط، بدون علامات بيانات|
|منطقة|يمثل مخطط المنطقة|
|منطقة مكدسة|يمثل مخططًا مساحيًا مكدسًا|
|المساحة 100%مكدسة|يمثل مخططًا مساحيًا مكدسًا بنسبة 100%|
|منطقة3D|يمثل مخطط منطقة ثلاثي الأبعاد|
|Area3DStacked|يمثل مخططًا مساحيًا مكدسًا ثلاثي الأبعاد|
|المساحة 3D100%مكدسة|يمثل مخططًا مساحيًا ثلاثي الأبعاد مكدسًا بنسبة 100%|
|كعكة محلاة|يمثل مخطط الدونات|
|دوناتانفجرت|يمثل مخطط الدونات المنفجر|
|رادار|يمثل مخطط الرادار|
|الرادار مع علامات البيانات|يمثل مخطط الرادار مع علامات البيانات|
|رادار معبأ|يمثل مخطط الرادار المملوء|
|سطح3D|يمثل مخطط سطحي ثلاثي الأبعاد|
|SurfaceWireframe3D|يمثل مخطط سطحي ثلاثي الأبعاد للإطار السلكي|
|SurfaceContour|يمثل مخطط كفاف|
|SurfaceContourWireframe|يمثل مخطط محيطي سلكي|
|فقاعة|يمثل مخطط الفقاعة|
|Bubble3D|يمثل مخطط فقاعي ثلاثي الأبعاد|
|اسطوانة|يمثل مخطط الاسطوانة|
|CylinderStacked|يمثل مخطط اسطوانة مكدسة|
|الأسطوانة مكدسة بنسبة 100%|يمثل مخططًا أسطوانيًا مكدسًا بنسبة 100%|
|CylindericalBar|يمثل مخطط شريطي أسطواني.|
|CylindericalBarStacked|يمثل مخطط شريطي أسطواني مكدس|
|شريط أسطواني مكدس بنسبة 100%|يمثل مخططًا شريطيًا أسطوانيًا مكدسًا بنسبة 100%|
|عمود أسطواني3D|يمثل مخططًا عموديًا أسطوانيًا ثلاثي الأبعاد|
|مخروط|يمثل مخطط المخروط|
|ConeStacked|يمثل مخططًا مخروطيًا مكدسًا|
|مخروطي100%مكدس|يمثل مخططًا مخروطيًا مرصوفًا بنسبة 100%|
|ConicalBar|يمثل مخطط شريطي مخروطي|
|ConicalBarStacked|يمثل مخطط شريطي مخروطي مكدس|
|شريط مخروطي بنسبة 100% مكدس|يمثل مخططًا شريطيًا مخروطيًا مكدسًا بنسبة 100%|
|ConicalColumn3D|يمثل مخطط عمود مخروطي ثلاثي الأبعاد|
|هرم|يمثل مخطط الهرم|
|الهرممكدس|يمثل مخطط الهرم المكدس|
|الهرم مكدس بنسبة 100%|يمثل مخططًا هرميًا مرصوفًا بنسبة 100%|
|PyramidBar|يمثل مخطط شريط الهرم|
|PyramidBarStacked|يمثل مخطط شريطي هرمي مكدس|
|PyramidBar100%مكدس|يمثل مخططًا شريطيًا هرميًا مكدسًا بنسبة 100%|
|الهرم العمود3D|يمثل مخطط عمود الهرم ثلاثي الأبعاد|
{{% alert color="primary" %}}

عندما تقوم بتعيين نطاق من الخلايا كمصدر بيانات، يمكنك فقط تعيين النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال، "A1:C3" صالح بينما "C3:A1" غير صالح.

{{% /alert %}}

####  **مخطط الهرم**

عند تنفيذ التعليمات البرمجية النموذجية، تتم إضافة مخطط هرمي إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

####  **خط الرسم البياني**

 في المثال أعلاه، ببساطة تغيير[**نوع التخطيط**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) ل*خط*ينشئ مخططًا خطيًا. ويرد المصدر الكامل أدناه. عند تنفيذ التعليمات البرمجية، تتم إضافة مخطط خطي إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

####  **الرسم البياني الفقاعي**

 من أجل إنشاء مخطط فقاعي، يجب استخدام[**نوع التخطيط**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) يجب أن يتم ضبطه على[**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)ويجب تعيين بعض الخصائص الإضافية مثل BubbleSizes وValues وXValues وفقًا لذلك. عند تنفيذ التعليمات البرمجية التالية، تتم إضافة مخطط فقاعي إلى ورقة العمل.

####  **يتماشى مع مخطط علامة البيانات**

 من أجل إنشاء خط مع مخطط علامة البيانات،[**نوع التخطيط**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)يجب أن يتم ضبطه على*ChartType.LineWithDataMarkers*ويجب تعيين عدد قليل من الخصائص الإضافية مثل منطقة الخلفية وعلامات السلسلة والقيم وقيم X وفقًا لذلك. عند تنفيذ التعليمات البرمجية التالية، تتم إضافة سطر مع مخطط علامة البيانات إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

##  **مواضيع متقدمة**
- [قراءة ومعالجة مخططات Excel 2016](/cells/ar/net/read-and-manipulate-excel-2016-charts/)
- [إدارة محاور مخططات Excel](/cells/ar/net/chart-axes/)
- [ضبط مظهر الرسم البياني](/cells/ar/net/setting-chart-appearance/)
- [أنواع المخططات](/cells/ar/net/chart-types/)
- [تخصيص الرسوم البيانية](/cells/ar/net/customizing-charts/)
- [قم بتعيين مصدر البيانات للمخطط](/cells/ar/net/data-formatting-in-charts/)
- [إدارة DataLabels لمخططات Excel](/cells/ar/net/insert-datalabels-to-chart/)
- [إنشاء مخطط عن طريق معالجة العلامات الذكية](/cells/ar/net/generate-chart-by-processing-smart-markers/)
- [الحصول على ورقة عمل الرسم البياني](/cells/ar/net/get-worksheet-of-the-chart/)
- [إدارة مخططات Legend of Excel](/cells/ar/net/chart-legend/)
- [التعامل مع حجم المركز ومخطط المصمم](/cells/ar/net/manipulate-position-size-and-designer-chart/)
- [إنشاء مخطط دائري مع خطوط الزعيم](/cells/ar/net/creating-pie-chart-with-leader-lines/)
- [الأشكال في المخططات](/cells/ar/net/controls-in-charts/)
- [إدارة عناوين مخططات Excel](/cells/ar/net/chart-and-axis-titles/)
- [عرض الرسم البياني](/cells/ar/net/chart-rendering/)
- [الحصول على نص المعادلة لخط الاتجاه الرسم البياني](/cells/ar/net/get-equation-text-of-chart-trendline/)
