---
title: إنشاء وإدارة المخطط
linktitle: الرسوم البيانية
type: docs
weight: 130
url: /ar/net/creating-charts/
description: قم بإنشاء مخطط في CSharp لملفات Excel و ODS.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

من الممكن إضافة مجموعة متنوعة من المخططات إلى جداول البيانات باستخدام Aspose.Cells. يوفر Aspose.Cells العديد من كائنات الرسوم البيانية المرنة. يناقش هذا الموضوع Aspose.Cells 'كائنات الرسوم البيانية.

{{% /alert %}}

## **إنشاء الرسوم البيانية**

### **ببساطة إنشاء الرسم البياني**
من السهل إنشاء مخطط باستخدام Aspose.Cells باستخدام رموز الأمثلة التالية:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **أشياء يجب معرفتها لإنشاء مخطط**

قبل إنشاء المخططات ، من المهم فهم بعض المفاهيم الأساسية المفيدة عند إنشاء الرسوم البيانية باستخدام Aspose.Cells.

#### **كائنات الرسوم البيانية**

يوفر Aspose.Cells مجموعة خاصة من الفئات في[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts) تم استخدام مساحة الاسم لإنشاء الرسوم البيانية التي يدعمها Aspose.Cells. وتستخدم هذه الفئات في الإنشاء**رسم الأشياء**، والتي تعمل بمثابة اللبنات الأساسية للمخطط. كائنات التخطيط مذكورة أدناه:

- سلسلة ، سلسلة بيانات مفردة في مخطط.
- المحور ، محور المخطط.
- مخطط ، مخطط Excel واحد.
- ChartArea ، منطقة المخطط في ورقة العمل.
- ChartDataTable ، جدول بيانات الرسم البياني.
- ChartFrame ، كائن الإطار في الرسم البياني.
- ChartPoint ، نقطة واحدة في سلسلة في مخطط.
- ChartPointCollection ، مجموعة تحتوي على جميع النقاط في سلسلة واحدة.
- المخططات ، مجموعة من كائنات المخطط.
- DataLabels ، مجموعة من جميع كائنات DataLabel للسلسلة المحددة.
- FillFormat ، تنسيق التعبئة لشكل.
- Floor ، أرضية مخطط ثلاثي الأبعاد.
- الأسطورة ، أسطورة الرسم البياني.
- الخط ، خط الرسم البياني.
- SeriesCollection ، مجموعة من كائنات السلسلة.
- TickLabels ، تسميات علامات التجزئة المرتبطة بعلامات التجزئة على محور المخطط.
- العنوان ، عنوان المخطط أو المحور.
- خط الاتجاه ، خط اتجاه في الرسم البياني.
- TrendlineCollection ، مجموعة من كافة كائنات خط الاتجاه لسلسلة البيانات المحددة.
- الجدران ، جدران الرسم البياني ثلاثي الأبعاد.

#### **استخدام كائنات الرسوم البيانية**

كما هو مذكور أعلاه ، فإن جميع كائنات الرسوم البيانية هي أمثلة لفئاتها وتوفر خصائص وطرق محددة لأداء مهام محددة. استخدم كائنات المخططات لإنشاء المخططات.

أضف أي نوع من المخططات إلى ورقة عمل باستخدام امتداد[**الرسوم البيانية**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) مجموعة. كل عنصر في[**الرسوم البيانية**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) تمثل المجموعة أ[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) هدف. أ[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)يقوم الكائن بتغليف جميع كائنات التخطيط الأخرى المطلوبة لتخصيص مظهر المخطط. يوضح القسم التالي كيفية استخدام بعض كائنات التخطيط الأساسية لإنشاء مخطط بسيط.

### **إنشاء مخطط باستخدام Aspose.Cells**

**خطوات:**

1.  أضف بعض البيانات إلى خلايا ورقة العمل بامتداد[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) أشياء[**ضع القيمة**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)طريقة.
 سيتم استخدام هذا كمصدر بيانات للمخطط.
1.  أضف مخططًا إلى ورقة العمل عن طريق استدعاء[**الرسوم البيانية**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) المجموعة[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) طريقة مغلفة في[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)هدف.
1.  حدد نوع الرسم البياني بامتداد[**نوع التخطيط**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)تعداد.
 على سبيل المثال ، يستخدم المثال أدناه الامتداد[**نوع المخطط. الهرم**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)القيمة كنوع المخطط.
1.  الوصول إلى ملف[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) كائن من[**الرسوم البيانية**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)جمع عن طريق تمرير الفهرس الخاص به.
1.  استخدم أيًا من كائنات الرسوم البيانية المغلفة في ملف[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)كائن لإدارة المخطط.
 يستخدم المثال أدناه ملف[**السلسلة**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)رسم بياني لتحديد مصدر بيانات المخطط.

عند إضافة بيانات المصدر إلى المخطط ، يمكن أن يكون مصدر البيانات نطاقًا من الخلايا (مثل "A1: C3") ، أو سلسلة من الخلايا غير المتجاورة (مثل "A1 ، A3 ، A5") ، أو سلسلة من القيم (مثل "1،2،3").

تتيح لك هذه الخطوات العامة إنشاء أي نوع من المخططات. استخدم كائنات مخططات مختلفة لإنشاء مخططات مختلفة.

 من الممكن إنشاء العديد من أنواع الرسوم البيانية المختلفة باستخدام Aspose.Cells. جميع الرسوم البيانية القياسية التي يدعمها Aspose.Cells محددة مسبقًا في التعداد المسمى[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

أنواع المخططات المحددة مسبقًا هي:

|**أنواع المخططات**|**وصف**|
|:- |:- |
|عمودي|يمثل مخطط عمودي متفاوت المسافات|
|العمود مكدسة|يمثل مخطط عمودي مكدس|
|عمود 100 نسبة مكدسة|يمثل مخطط عمودي مكدس بنسبة 100٪|
|Column3D العنقودية|يمثل مخطط عمودي مجمع ثلاثي الأبعاد|
|العمود 3D مكدسة|يمثل مخطط عمودي مكدس ثلاثي الأبعاد|
|عمود 3 D100Percent مكدسة|يمثل مخططًا عموديًا مكدسًا بنسبة 100٪ ثلاثي الأبعاد|
|العمود 3 د|يمثل التخطيط العمودي ثلاثي الأبعاد|
|شريط|يمثل مخطط شريطي متفاوت المسافات|
|بار مكدسة|يمثل مخطط شريطي مكدس|
|شريط 100٪ مكدسة|يمثل مخطط شريطي مكدس بنسبة 100٪|
|شريط ثلاثي الأبعاد متفاوت|يمثل مخطط شريطي ثلاثي الأبعاد مجمع|
|Bar3D مكدسة|يمثل مخطط شريطي مكدس ثلاثي الأبعاد|
|شريط ثلاثي الأبعاد 100٪ مكدس|يمثل مخطط شريطي مكدس بنسبة 100٪ ثلاثي الأبعاد|
|خط|يمثل الخط البياني|
|LineStacked|يمثل مخطط خطي مكدس|
|Line100Percent مكدس|يمثل مخطط خطي مكدس بنسبة 100٪|
|LineWithDataMarkers|يمثل مخطط خطي بعلامات بيانات|
|LineStackedWithDataMarkers|يمثل مخططًا خطيًا مكدسًا بعلامات بيانات|
|Line100PercentStackedWithDataMarkers|يمثل مخططًا خطيًا مكدسًا بنسبة 100٪ بعلامات بيانات|
|Line3D|يمثل مخطط خطي ثلاثي الأبعاد|
|فطيرة|يمثل الرسم البياني الدائري|
|Pie3D|يمثل مخطط دائري ثلاثي الأبعاد|
|فطيرة فطيرة|يمثل مخطط دائري دائري|
|انفجرت الفطيرة|يمثل مخطط دائري مجزأ|
|انفجرت Pie3D|يمثل مخطط دائري مجسم ثلاثي الأبعاد|
|بي بار|يمثل مخطط شريطي دائري|
|مبعثر|يمثل الرسم البياني المبعثر|
|ScatterConnectedByCurvesWithDataMarker|يمثل مخطط مبعثر متصل بمنحنيات وعلامات بيانات|
|ScatterConnectedByCurvesWithoutDataMarker|يمثل مخطط مبعثر متصل بمنحنيات ، بدون علامات بيانات|
|ScatterConnectedByLinesWithDataMarker|يمثل مخطط مبعثر متصل بخطوط ، بعلامات بيانات|
|ScatterConnectedByLinesWithoutDataMarker|يمثل مخطط مبعثر متصل بخطوط ، بدون علامات بيانات|
|منطقة|يمثل مخطط المنطقة|
|المنطقة مكدسة|يمثل مخطط مساحي مكدس|
|مساحة 100٪ مكدسة|يمثل مخطط مساحي مكدس بنسبة 100٪|
|Area3D|يمثل مخطط منطقة ثلاثي الأبعاد|
|Area3D مكدس|يمثل مخطط مساحي مكدس ثلاثي الأبعاد|
|Area3D100Percent مكدس|يمثل مخطط مساحي مكدس بنسبة 100٪ ثلاثي الأبعاد|
|الدونات|يمثل الشكل الدائري المجوف|
|انفجرت العجين|يمثل مخطط دائري مجوف|
|رادار|يمثل الرسم البياني النسيجي|
|RadarWithDataMarkers|يمثل مخطط نسيجي بعلامات بيانات|
|الرادار|يمثل الرسم البياني النسيجي المملوء|
|Surface3D|يمثل مخطط سطحي ثلاثي الأبعاد|
|SurfaceWireframe3D|يمثل مخطط سطحي ثلاثي الأبعاد بإطار سلكي|
|SurfaceContour|يمثل مخطط كونتور|
|SurfaceContourWireframe|يمثل مخطط محيط الإطار السلكي|
|فقاعة|يمثل مخطط فقاعي|
|فقاعة ثلاثية الأبعاد|يمثل مخطط فقاعي ثلاثي الأبعاد|
|اسطوانة|يمثل مخطط اسطوانة|
|اسطوانة مكدسة|يمثل مخطط أسطواني مكدس|
|اسطوانة 100٪ مكدسة|يمثل مخطط أسطواني مكدس بنسبة 100٪|
|شريط اسطواني|يمثل مخطط شريطي أسطواني.|
|شريط أسطواني مكدس|يمثل مخطط شريطي أسطواني مكدس|
|شريط أسطواني 100٪ مكدس|يمثل مخطط شريطي أسطواني مكدس بنسبة 100٪|
|عمود أسطواني ثلاثي الأبعاد|يمثل مخطط عمودي أسطواني ثلاثي الأبعاد|
|مخروط|يمثل مخطط مخروطي|
|مخروط|يمثل مخطط مخروطي مكدس|
|مخروط 100٪ مكدسة|يمثل 100٪ مخطط مخروطي مكدس|
|مخروطي الشكل|يمثل مخطط شريطي مخروطي الشكل|
|مخروطي الشكل مكدس|يمثل مخطط شريطي مخروطي مكدس|
|ConicalBar 100Percent مكدسة|يمثل مخطط شريطي مخروطي مكدس بنسبة 100٪|
|عمود مخروطي ثلاثي الأبعاد|يمثل مخطط عمودي مخروطي ثلاثي الأبعاد|
|هرم|يمثل مخطط هرم|
|الهرم مكدسة|يمثل مخطط هرم مكدس|
|الهرم 100٪ مكدسة|يمثل مخطط هرمي مكدس بنسبة 100٪|
|هرم بار|يمثل مخطط شريطي هرمي|
|PyramidBar مكدس|يمثل مخطط شريطي هرمي مكدس|
|PyramidBar100Percent مكدسة|يمثل مخطط شريطي هرمي مكدس بنسبة 100٪|
|الهرم عمود 3 د|يمثل مخطط عمودي هرمي ثلاثي الأبعاد|
{{% alert color="primary" %}}

عند تعيين نطاق من الخلايا كمصدر بيانات ، يمكنك فقط تعيين النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال ، "A1: C3" صالح بينما "C3: A1" غير صالح.

{{% /alert %}}

#### **مخطط هرمي**

عند تنفيذ رمز المثال ، تتم إضافة مخطط هرمي إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **خط الرسم البياني**

 في المثال أعلاه ، قم ببساطة بتغيير ملف[**نوع التخطيط**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) إلى*خط*ينشئ مخططًا خطيًا. يتم توفير المصدر الكامل أدناه. عند تنفيذ الكود ، يتم إضافة مخطط خطي إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **مخطط فقاعي**

 من أجل إنشاء مخطط فقاعي ، فإن ملف[**نوع التخطيط**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) يجب ضبطه على[**نوع المخطط. فقاعة**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)وبعض الخصائص الإضافية مثل BubbleSizes و Values & XValues يجب تعيينها وفقًا لذلك. عند تنفيذ التعليمات البرمجية التالية ، تتم إضافة مخطط فقاعي إلى ورقة العمل.

#### **خط مع مخطط علامة البيانات**

 من أجل إنشاء خط مع مخطط علامة البيانات ،[**نوع التخطيط**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)يجب ضبطه على*ChartType.LineWithDataMarkers*وبعض الخصائص الإضافية مثل منطقة الخلفية ، وعلامات السلسلة ، والقيم ، والقيم X تحتاج إلى تعيينها وفقًا لذلك. عند تنفيذ الكود التالي ، يتم إضافة خط مع مخطط علامة البيانات إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **موضوعات مسبقة**
- [قراءة مخططات Excel 2016 والتعامل معها](/cells/ar/net/read-and-manipulate-excel-2016-charts/)
- [إدارة محاور مخططات Excel](/cells/ar/net/chart-axes/)
- [ضبط مظهر المخطط](/cells/ar/net/setting-chart-appearance/)
- [أنواع المخططات](/cells/ar/net/chart-types/)
- [تخصيص الرسوم البيانية](/cells/ar/net/customizing-charts/)
- [تعيين مصدر البيانات للرسم البياني](/cells/ar/net/data-formatting-in-charts/)
- [إدارة DataLabels لمخططات Excel](/cells/ar/net/insert-datalabels-to-chart/)
- [إنشاء مخطط عن طريق معالجة العلامات الذكية](/cells/ar/net/generate-chart-by-processing-smart-markers/)
- [احصل على ورقة عمل الرسم البياني](/cells/ar/net/get-worksheet-of-the-chart/)
- [إدارة وسيلة إيضاح مخططات Excel](/cells/ar/net/chart-legend/)
- [معالجة حجم المركز ومخطط المصمم](/cells/ar/net/manipulate-position-size-and-designer-chart/)
- [إنشاء مخطط دائري بخطوط سابقة](/cells/ar/net/creating-pie-chart-with-leader-lines/)
- [الأشكال في المخططات](/cells/ar/net/controls-in-charts/)
- [إدارة عناوين مخططات Excel](/cells/ar/net/chart-and-axis-titles/)
- [عرض المخطط](/cells/ar/net/chart-rendering/)
- [احصل على نص معادلة خط اتجاه المخطط](/cells/ar/net/get-equation-text-of-chart-trendline/)
