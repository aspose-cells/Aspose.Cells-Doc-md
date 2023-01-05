---
title: تخصيص الرسوم البيانية
type: docs
weight: 15
url: /ar/java/creating-and-customizing-charts/
---
## **إنشاء الرسوم البيانية**

من الممكن إضافة مجموعة متنوعة من المخططات إلى جداول البيانات باستخدام Aspose.Cells. يوفر Aspose.Cells العديد من كائنات الرسوم البيانية المرنة. يناقش هذا الموضوع Aspose.Cells 'كائنات الرسوم البيانية.

### **ببساطة إنشاء الرسم البياني**

من السهل إنشاء مخطط باستخدام Aspose.Cells باستخدام رموز الأمثلة التالية:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **أشياء يجب معرفتها لإنشاء مخطط**

قبل إنشاء المخططات ، من المهم فهم بعض المفاهيم الأساسية المفيدة عند إنشاء الرسوم البيانية باستخدام Aspose.Cells.

#### **كائنات الرسوم البيانية**

 يوفر Aspose.Cells مجموعة خاصة من الفئات المستخدمة لإنشاء كافة أنواع المخططات. تستخدم هذه الفئات للإنشاء**رسم الأشياء**، والتي تعمل بمثابة اللبنات الأساسية للمخطط. كائنات التخطيط مذكورة أدناه:

- [**محور**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis)، محور الرسم البياني.
- [**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)، مخطط Excel واحد.
- [**منطقة الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea)، منطقة المخطط في ورقة العمل.
- [**جدول البيانات**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable)، جدول بيانات الرسم البياني.
- [**إطار الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame)، كائن الإطار في الرسم البياني.
- [**تشارت بوينت**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)، نقطة واحدة في سلسلة في مخطط.
- [**مجموعة ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection)، مجموعة تحتوي على جميع النقاط في سلسلة واحدة.
- [**جمع الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) ، مجموعة من[**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)أشياء.
-  DataLabels ، DataLabels لملف[**مسلسل**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**تشارت بوينت**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**خط الاتجاه**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)، إلخ.
- [**ملء**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat)، تعبئة الشكل لشكل.
- [**الأرض**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor)، أرضية مخطط ثلاثي الأبعاد.
- [**عنوان تفسيري**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend)، وسيلة إيضاح الرسم البياني.
- [**خط**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)، خط الرسم البياني.
- [**السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) ، مجموعة من[**مسلسل**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)أشياء.
- [**مسلسل**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)، يمثل سلسلة بيانات مفردة في مخطط.
- [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels)، تسميات علامات التجزئة المرتبطة بعلامات التجزئة علي محور المخطط.
- [**لقب**](https://reference.aspose.com/cells/java/com.aspose.cells/Title)، عنوان مخطط أو محور.
- [**خط الاتجاه**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)، خط اتجاه في الرسم البياني.
- [**مجموعة TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection)، مجموعة من كافة كائنات خط الاتجاه لسلسلة البيانات المحددة.
- [**الجدران**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)، جدران مخطط ثلاثي الأبعاد.

#### **استخدام كائنات الرسوم البيانية**

كما هو مذكور أعلاه ، فإن جميع كائنات الرسوم البيانية هي أمثلة لفئاتها وتوفر خصائص وطرق محددة لأداء مهام محددة. استخدم كائنات المخططات لإنشاء المخططات.

أضف أي نوع من المخططات إلى ورقة عمل باستخدام امتداد[**جمع الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) مجموعة. كل عنصر في[**جمع الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) تمثل المجموعة أ[**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) موضوع. أ[**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)يقوم الكائن بتغليف جميع كائنات الرسوم البيانية المطلوبة لتخصيص مظهر المخطط. يوضح القسم التالي كيفية استخدام بعض كائنات التخطيط الأساسية لإنشاء مخطط بسيط.

### **إنشاء مخطط بسيط**

 من الممكن إنشاء العديد من أنواع الرسوم البيانية المختلفة باستخدام Aspose.Cells. جميع الرسوم البيانية القياسية التي يدعمها Aspose.Cells محددة مسبقًا في التعداد المسمى[**نوع التخطيط**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). أنواع المخططات المحددة مسبقًا هي:

|**أنواع المخططات**|**وصف**|
|:- |:- |
|عمود|يمثل المخطط العمودي متفاوت المسافات|
|العمود مكدسة|يمثل مخطط عمودي مكدس|
|عمود 100 نسبة مكدسة|يمثل مخطط عمودي مكدس بنسبة 100٪|
|Column3D العنقودية|يمثل مخطط عمودي مجمع ثلاثي الأبعاد|
|العمود 3D مكدسة|يمثل مخطط عمودي مكدس ثلاثي الأبعاد|
|عمود 3 D100Percent مكدسة|يمثل مخطط عمودي مكدس بنسبة 100٪ ثلاثي الأبعاد|
|العمود 3 د|يمثل مخطط عمودي ثلاثي الأبعاد|
|شريط|يمثل مخطط شريطي متفاوت المسافات|
|بار مكدسة|يمثل مخطط شريطي مكدس|
|شريط 100٪ مكدسة|يمثل مخطط شريطي مكدس بنسبة 100٪|
|شريط ثلاثي الأبعاد متفاوت|يمثل مخطط شريطي ثلاثي الأبعاد متفاوت المسافات|
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
|مبعثر|يمثل المخطط المبعثر|
|ScatterConnectedByCurvesWithDataMarker|يمثل المخطط المبعثر المتصل بالمنحنيات وعلامات البيانات|
|ScatterConnectedByCurvesWithoutDataMarker|يمثل المخطط المبعثر المتصل بمنحنيات ، بدون علامات بيانات|
|ScatterConnectedByLinesWithDataMarker|يمثل المخطط المبعثر المتصل بخطوط ، بعلامات البيانات|
|ScatterConnectedByLinesWithoutDataMarker|يمثل المخطط المبعثر المتصل بخطوط ، بدون علامات بيانات|
|منطقة|يمثل مخطط المنطقة|
|المنطقة مكدسة|يمثل مخطط مساحي مكدس|
|مساحة 100٪ مكدسة|يمثل مخطط مساحي مكدس بنسبة 100٪|
|Area3D|يمثل مخطط منطقة ثلاثي الأبعاد|
|Area3D مكدس|يمثل مخطط مساحي مكدس ثلاثي الأبعاد|
|Area3D100Percent مكدس|يمثل مخطط مساحي مكدس بنسبة 100٪ ثلاثي الأبعاد|
|الدونات|يمثل الشكل الدائري المجوف|
|انفجرت العجين|يمثل مخطط دائري مجوف|
|رادار|يمثل المخطط النسيجي|
|RadarWithDataMarkers|يمثل المخطط النسيجي بعلامات بيانات|
|الرادار|يمثل الرسم البياني النسيجي المملوء|
|Surface3D|يمثل مخطط سطحي ثلاثي الأبعاد|
|SurfaceWireframe3D|يمثل المخطط السطحي للإطار السلكي ثلاثي الأبعاد|
|SurfaceContour|يمثل مخطط كونتور|
|SurfaceContourWireframe|يمثل مخطط محيط الإطار السلكي|
|فقاعة|يمثل مخطط فقاعي|
|فقاعة ثلاثية الأبعاد|يمثل مخطط فقاعي ثلاثي الأبعاد|
|اسطوانة|يمثل مخطط اسطوانة|
|اسطوانة مكدسة|يمثل مخطط أسطواني مكدس|
|اسطوانة 100٪ مكدسة|يمثل مخطط أسطواني مكدس بنسبة 100٪|
|أسطواني بار|يمثل مخطط شريطي أسطواني.|
|أسطواني بار مكدس|يمثل مخطط شريطي أسطواني مكدس|
|شريط أسطواني 100٪ مكدس|يمثل مخطط شريطي أسطواني مكدس بنسبة 100٪|
|عمود أسطواني ثلاثي الأبعاد|يمثل مخطط عمودي أسطواني ثلاثي الأبعاد|
|مخروط|يمثل مخطط مخروطي|
|مخروط|يمثل مخطط مخروطي مكدس|
|مخروط 100٪ مكدسة|يمثل 100٪ مخطط مخروطي مكدس|
|مخروطي الشكل|يمثل مخطط شريطي مخروطي الشكل|
|مخروطي الشكل مكدس|يمثل مخطط شريطي مخروطي مكدس|
|مخروطي الشكل 100٪ مكدس|يمثل مخطط شريطي مخروطي مكدس بنسبة 100٪|
|عمود مخروطي ثلاثي الأبعاد|يمثل مخطط عمودي مخروطي ثلاثي الأبعاد|
|هرم|يمثل مخطط هرم|
|الهرم مكدسة|يمثل مخطط هرم مكدس|
|الهرم 100٪ مكدسة|يمثل مخطط هرمي مكدس بنسبة 100٪|
|هرم بار|يمثل المخطط الشريطي الهرمي|
|PyramidBar مكدس|يمثل مخطط شريطي هرمي مكدس|
|PyramidBar100Percent مكدسة|يمثل مخطط شريطي هرمي مكدس بنسبة 100٪|
|الهرم عمود 3 د|يمثل مخطط عمودي هرمي ثلاثي الأبعاد|
لإنشاء مخطط باستخدام Aspose.Cells:

1.  أضف بعض البيانات إلى خلايا ورقة العمل بامتداد[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) أشياء[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)طريقة.
 سيتم استخدام هذا كمصدر بيانات للمخطط.
1.  أضف مخططًا إلى ورقة العمل عن طريق استدعاء[**جمع الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) المجموعة[*يضيف*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) ) ، مغلف في ملف[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)موضوع.
1.  حدد نوع الرسم البياني بامتداد[**نوع التخطيط**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)تعداد.
 على سبيل المثال ، يستخدم المثال الامتداد[**نوع المخطط**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)القيمة كنوع المخطط.
1.  الوصول إلى ملف[**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) كائن من[**جمع الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)جمع عن طريق تمرير الفهرس الخاص به.
1.  استخدم أيًا من كائنات الرسوم البيانية المغلفة في ملف[**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)كائن لإدارة المخطط.
 يستخدم المثال أدناه ملف[**السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)رسم بياني لتحديد مصدر بيانات المخطط.

عند إضافة بيانات المصدر إلى المخطط ، يمكن أن يكون مصدر البيانات نطاقًا من الخلايا (مثل "A1: C3") ، أو سلسلة من الخلايا غير المتجاورة (مثل "A1 ، A3 ، A5") ، أو سلسلة من القيم (مثل "1،2،3").

{{% alert color="primary" %}}

عند تعيين نطاق من الخلايا كمصدر بيانات ، يمكنك فقط تعيين النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال ، "A1: C3" صالح بينما "C3: A1" غير صالح.

{{% /alert %}}

تتيح لك هذه الخطوات العامة إنشاء أي نوع من المخططات. استخدم كائنات مخططات مختلفة لإنشاء مخططات مختلفة.

عند تنفيذ رمز المثال ، تتم إضافة مخطط هرمي إلى ورقة العمل كما هو موضح أدناه.

**مخطط هرمي مع مصدر البيانات الخاص به**

![ما يجب القيام به: image_بديل_نص](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

 لإنشاء مخطط فقاعي ، فإن ملف[**نوع التخطيط**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)يجب ضبطه على[**نوع المخطط**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)وبعض الخصائص الإضافية مثل BubbleSizes و Values & XValues يجب تعيينها وفقًا لذلك. عند تنفيذ الكود التالي ، تتم إضافة مخطط فقاعي إلى ورقة العمل كما هو موضح أدناه.

**مخطط فقاعي مع مصدر البيانات الخاص به**

![ما يجب القيام به: image_بديل_نص](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **خط مع مخطط علامة البيانات**

لإنشاء خط بمخطط علامة البيانات ، يتم إنشاء ملف[**نوع التخطيط**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)يجب ضبطه على[**نوع المخطط. LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) وبعض الخصائص الإضافية مثل منطقة الخلفية ، وعلامات السلسلة ، والقيم ، والقيم X تحتاج إلى تعيينها وفقًا لذلك. عند تنفيذ الكود التالي ، يتم إضافة خط مع مخطط علامة البيانات إلى ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **إنشاء الرسوم البيانية المخصصة**

حتى الآن ، عندما ناقشنا المخططات ، نظرنا إلى المخططات القياسية التي تحتوي على إعدادات التنسيق القياسية الخاصة بها. نحن نحدد مصدر البيانات فقط ، ونضع بعض الخصائص ويتم إنشاء المخطط باستخدام إعدادات التنسيق الافتراضية الخاصة به. لكن Aspose.Cells يدعم أيضًا إنشاء مخططات مخصصة تسمح للمطورين بإنشاء مخططات باستخدام إعدادات التنسيق الخاصة بهم.

### **إنشاء الرسوم البيانية المخصصة**

يمكن للمطورين إنشاء مخططات مخصصة في وقت التشغيل باستخدام Aspose.Cells بسيط API.

 يتكون المخطط من سلسلة بيانات. يتم تمثيل كل سلسلة بيانات في Aspose.Cells بواسطة أ[**مسلسل**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) كائن في حين أن[**السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) الكائن بمثابة مجموعة من[**مسلسل**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)أشياء. عند إنشاء مخطط مخصص ، يتمتع المطورون بحرية استخدام أنواع مختلفة من المخططات لسلسلة بيانات مختلفة (مجمعة في ملف[**السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)موضوع).

{{% alert color="primary" %}}

 يدعم Aspose.Cells حاليًا المخططات المخصصة فقط التي تجمع المخططات الدائرية والخطية والعمودية والمكدسة العمودية ولكن سيتم دعم المزيد من المخططات في الإصدارات المستقبلية. للحصول على قائمة كاملة بالمخططات القياسية التي يدعمها Aspose.Cells ، اقرأ ملف[أنواع المخططات](/cells/ar/java/chart-types/) مقالة - سلعة.

{{% /alert %}}

يوضح رمز المثال أدناه كيفية إنشاء مخططات مخصصة. في هذا المثال ، سنستخدم مخططًا عموديًا لسلسلة البيانات الأولى ومخطط خطي للسلسلة الثانية. والنتيجة هي أننا نضيف مخططًا عموديًا ، جنبًا إلى جنب مع مخطط خطي ، إلى ورقة العمل.

**مخطط مخصص يجمع بين المخططات العمودية والخطية**

![ما يجب القيام به: image_بديل_نص](creating-and-customizing-charts_3.png)

**مثال البرمجة**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

للاطلاع على قائمة بأنواع المخططات المدعومة ، اقرأ ملف[أنواع المخططات](/cells/ar/java/chart-types/) مقالة - سلعة.

{{% /alert %}}

