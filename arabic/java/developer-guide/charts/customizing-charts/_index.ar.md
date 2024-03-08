---
title: تخصيص الرسوم البيانية
type: docs
weight: 15
url: /ar/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---
##  **إنشاء الرسوم البيانية**

من الممكن إضافة مجموعة متنوعة من المخططات إلى جداول البيانات باستخدام Aspose.Cells. يوفر Aspose.Cells العديد من كائنات الرسوم البيانية المرنة. يناقش هذا الموضوع كائنات التخطيط Aspose.Cells.

###  **ببساطة إنشاء مخطط**

من السهل إنشاء مخطط بالرقم Aspose.Cells باستخدام رموز الأمثلة التالية:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


###  **أشياء يجب معرفتها لإنشاء مخطط**

قبل إنشاء المخططات، من المهم فهم بعض المفاهيم الأساسية التي تكون مفيدة عند إنشاء المخططات باستخدام Aspose.Cells.

####  **رسم الكائنات**

Aspose.Cells يوفر مجموعة خاصة من الفئات المستخدمة لإنشاء جميع أنواع المخططات. تُستخدم هذه الفئات لإنشاء *كائنات الرسم البياني**، والتي تعمل كعناصر بناء للرسم البياني. كائنات التخطيط مدرجة أدناه:

- [**محور**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis)، محور المخطط.
- [**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)، مخطط Excel واحد.
- [**منطقة الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea)، منطقة المخطط في ورقة العمل.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable)، جدول بيانات الرسم البياني.
- [**إطار الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame)، كائن الإطار في المخطط.
- [**تشارتبوينت**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint)، نقطة واحدة في سلسلة في المخطط.
- [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection)، مجموعة تحتوي على جميع النقاط في سلسلة واحدة.
- [**مجموعة الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) ، مجموعة من[**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)أشياء.
-  DataLabels، DataLabels للمحدد[**مسلسل**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**تشارتبوينت**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**خط الاتجاه**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)، إلخ.
- [**تنسيق التعبئة**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat)، تعبئة التنسيق للشكل.
- [**أرضية**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor)، أرضية مخطط ثلاثي الأبعاد.
- [**أسطورة**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend)، وسيلة إيضاح الرسم البياني.
- [**خط**](https://reference.aspose.com/cells/java/com.aspose.cells/Line)، خط الرسم البياني.
- [**مجموعة السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) ، مجموعة من[**مسلسل**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)أشياء.
- [**مسلسل**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)يمثل سلسلة بيانات واحدة في مخطط.
- [**علامات التجزئة**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels)، تسميات علامات التجزئة المرتبطة بعلامات التجزئة على محور المخطط.
- [**عنوان**](https://reference.aspose.com/cells/java/com.aspose.cells/Title)، عنوان المخطط أو المحور.
- [**خط الاتجاه**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline)، خط الاتجاه في الرسم البياني.
- [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection)، مجموعة من كافة كائنات خط الاتجاه لسلسلة البيانات المحددة.
- [**الجدران**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls)، جدران مخطط ثلاثي الأبعاد.

####  **استخدام كائنات التخطيط**

كما هو مذكور أعلاه، فإن كافة كائنات التخطيط هي مثيلات لفئاتها الخاصة وتوفر خصائص وأساليب محددة لتنفيذ مهام محددة. استخدم كائنات التخطيط لإنشاء المخططات.

 أضف أي نوع من المخططات إلى ورقة العمل باستخدام[**مجموعة الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) مجموعة. كل عنصر في[**مجموعة الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) جمع يمثل أ[**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) هدف. أ[**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)يقوم الكائن بتغليف كافة كائنات التخطيط المطلوبة لتخصيص مظهر المخطط. يوضح القسم التالي كيفية استخدام بعض كائنات التخطيط الأساسية لإنشاء مخطط بسيط.

###  **إنشاء مخطط بسيط**

من الممكن إنشاء العديد من أنواع المخططات المختلفة باستخدام Aspose.Cells. جميع المخططات القياسية التي يدعمها Aspose.Cells محددة مسبقًا في تعداد يسمى[**نوع التخطيط**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). أنواع المخططات المحددة مسبقًا هي:

|**أنواع المخططات**|**وصف**|
| :- | :- |
|عمود|يمثل المخطط العمودي متفاوت المسافات|
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
|مبعثر|يمثل المخطط المبعثر|
|مبعثر متصل بواسطة منحنيات مع DataMarker|يمثل المخطط المبعثر المتصل بالمنحنيات، مع علامات البيانات|
|مبعثر متصل بواسطة منحنيات بدون علامة البيانات|يمثل المخطط المبعثر المتصل بواسطة المنحنيات، بدون علامات البيانات|
|ScatterConnectedByLinesWithDataMarker|يمثل المخطط المبعثر المتصل بالخطوط، مع علامات البيانات|
|ScatterConnectedByLinesWithoutDataMarker|يمثل المخطط المبعثر المتصل بالخطوط، بدون علامات البيانات|
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
|SurfaceWireframe3D|يمثل المخطط السطحي ثلاثي الأبعاد للإطار السلكي|
|SurfaceContour|يمثل مخطط كفاف|
|SurfaceContourWireframe|يمثل مخطط محيطي سلكي|
|فقاعة|يمثل مخطط الفقاعة|
|Bubble3D|يمثل مخطط فقاعي ثلاثي الأبعاد|
|اسطوانة|يمثل مخطط الاسطوانة|
|CylinderStacked|يمثل مخطط اسطوانة مكدسة|
|الأسطوانة مكدسة بنسبة 100%|يمثل مخططًا أسطوانيًا مكدسًا بنسبة 100%|
|شريط اسطواني|يمثل مخطط شريطي أسطواني.|
|CylindricalBarStacked|يمثل مخطط شريطي أسطواني مكدس|
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
لإنشاء مخطط باستخدام Aspose.Cells:

1. أضف بعض البيانات إلى خلايا ورقة العمل باستخدام الملحق[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) أشياء[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)طريقة.
 سيتم استخدام هذا كمصدر بيانات للمخطط.
1.  أضف مخططًا إلى ورقة العمل عن طريق استدعاء[**مجموعة الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) المجموعة[*يضيف*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) ) الطريقة، مغلفة في[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)هدف.
1.  حدد نوع المخطط باستخدام[**نوع التخطيط**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)تعداد.
 على سبيل المثال، يستخدم المثال[**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)القيمة كنوع المخطط.
1.  الوصول إلى الجديد[**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) كائن من[**مجموعة الرسم البياني**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)جمع عن طريق تمرير فهرسها.
1.  استخدم أيًا من كائنات التخطيط المغلفة في[**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)كائن لإدارة المخطط.
 يستخدم المثال أدناه[**مجموعة السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)كائن التخطيط لتحديد مصدر بيانات المخطط.

عند إضافة بيانات المصدر إلى المخطط، يمكن أن يكون مصدر البيانات عبارة عن نطاق من الخلايا (مثل "A1:C3")، أو تسلسل من الخلايا غير المتجاورة (مثل "A1، A3، A5")، أو تسلسل من الخلايا القيم (مثل "1،2،3").

{{% alert color="primary" %}}

عندما تقوم بتعيين نطاق من الخلايا كمصدر بيانات، يمكنك فقط تعيين النطاق من أعلى اليسار إلى أسفل اليمين. على سبيل المثال، "A1:C3" صالح بينما "C3:A1" غير صالح.

{{% /alert %}}

تسمح لك هذه الخطوات العامة بإنشاء أي نوع من المخططات. استخدم كائنات تخطيطية مختلفة لإنشاء مخططات مختلفة.

عند تنفيذ رمز المثال، تتم إضافة مخطط هرمي إلى ورقة العمل كما هو موضح أدناه.

**مخطط هرمي مع مصدر البيانات الخاص به**

![ما يجب القيام به:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

 لإنشاء مخطط فقاعي، استخدم[**نوع التخطيط**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)يجب أن يتم ضبطه على[**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)ويجب تعيين بعض الخصائص الإضافية مثل BubbleSizes وValues وXValues وفقًا لذلك. عند تنفيذ التعليمات البرمجية التالية، تتم إضافة مخطط فقاعي إلى ورقة العمل كما هو موضح أدناه.

**مخطط فقاعي مع مصدر البيانات الخاص به**

![ما يجب القيام به:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

####  **يتماشى مع مخطط علامة البيانات**

لإنشاء خط باستخدام مخطط علامة البيانات، قم بإنشاء خط[**نوع التخطيط**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)يجب أن يتم ضبطه على[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) ويجب تعيين عدد قليل من الخصائص الإضافية مثل منطقة الخلفية وعلامات السلسلة والقيم وقيم X وفقًا لذلك. عند تنفيذ التعليمات البرمجية التالية، تتم إضافة سطر به مخطط علامة البيانات إلى ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

##  **إنشاء مخططات مخصصة**

حتى الآن، عندما ناقشنا المخططات، نظرنا إلى المخططات القياسية التي تحتوي على إعدادات التنسيق القياسية الخاصة بها. نقوم فقط بتعريف مصدر البيانات، وتعيين بعض الخصائص، ويتم إنشاء المخطط باستخدام إعدادات التنسيق الافتراضية الخاصة به. لكن Aspose.Cells يدعم أيضًا إنشاء مخططات مخصصة تسمح للمطورين بإنشاء مخططات باستخدام إعدادات التنسيق الخاصة بهم.

###  **إنشاء مخططات مخصصة**

يمكن للمطورين إنشاء مخططات مخصصة في وقت التشغيل باستخدام Aspose.Cells بسيط API.

 يتكون المخطط من سلسلة بيانات. يتم تمثيل كل سلسلة بيانات في Aspose.Cells بواسطة أ[**مسلسل**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) الكائن في حين أن[**مجموعة السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) الكائن بمثابة مجموعة من[**مسلسل**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)أشياء. عند إنشاء مخطط مخصص، يتمتع المطورون بحرية استخدام أنواع مختلفة من المخططات لسلاسل بيانات مختلفة (يتم جمعها في ملف[**مجموعة السلسلة**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)هدف).

{{% alert color="primary" %}}

 يدعم Aspose.Cells حاليًا فقط المخططات المخصصة التي تجمع بين المخططات الدائرية والخطية والعمودية ومكدس الأعمدة ولكن سيتم دعم المزيد من المخططات في الإصدارات المستقبلية. للحصول على قائمة كاملة بالمخططات القياسية التي يدعمها Aspose.Cells، اقرأ[أنواع المخططات](/cells/ar/java/chart-types/) شرط.

{{% /alert %}}

يوضح رمز المثال أدناه كيفية إنشاء مخططات مخصصة. في هذا المثال، سنستخدم مخططًا عموديًا لسلسلة البيانات الأولى ومخططًا خطيًا للسلسلة الثانية. والنتيجة هي أننا نضيف مخططًا عموديًا، مقترنًا بمخطط خطي، إلى ورقة العمل.

**مخطط مخصص يجمع بين المخططات العمودية والخطية**

![ما يجب القيام به:image_alt_text](creating-and-customizing-charts_3.png)

**مثال البرمجة**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

للاطلاع على قائمة بأنواع المخططات المدعومة، اقرأ[أنواع المخططات](/cells/ar/java/chart-types/) شرط.

{{% /alert %}}

