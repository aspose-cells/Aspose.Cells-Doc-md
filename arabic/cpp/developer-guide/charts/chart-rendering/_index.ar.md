---
title: عرض الرسم البياني
type: docs
weight: 30
url: /ar/cpp/chart-rendering/
---
##  **إنشاء الرسوم البيانية**

Aspose.Cells دعم واجهات برمجة التطبيقات (APIs) لإنشاء مجموعة حقيقية من مخططات Excel كما هو مفصل تحت الموضوع[إنشاء وتخصيص مخططات Excel](/cells/ar/cpp/creating-and-customizing-charts/). من أجل توضيح استخدام Aspose.Cells APIs لعرض المخططات في صورة وتنسيق PDF، سنقوم بإنشاء مخطط من النوع عمود وفقًا للمقتطف التالي.

{{< highlight "cpp" >}}

Aspose::Cells::Startup();

// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");

// Create a new workbook
Workbook workbook;

// Get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// Adding sample values to cells
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"B1").PutValue(4);
worksheet.GetCells().Get(u"B2").PutValue(20);
worksheet.GetCells().Get(u"B3").PutValue(50);

// Adding a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// Accessing the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.GetNSeries().Add(u"A1:B3", true);

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";
chart.ToImage(outputChartImage, ImageType::Png);

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

Aspose::Cells::Cleanup();

{{< /highlight >}}

##  **تقديم المخططات**

تدعم واجهات برمجة التطبيقات Aspose.Cells تحويل مخططات Excel إلى صور وتنسيقات PDF دون الحاجة إلى أي أدوات أو تطبيقات إضافية. من أجل توفير دعم العرض، كشفت فئة Chart عن أساليب ToImage وToPdf مع وجود أحمال زائدة لتناسب متطلبات التطبيق بشكل أفضل.

###  **تقديم المخططات إلى الصور**

تحتوي طريقة Chart.toImage على الكثير من الأحمال الزائدة لدعم العرض البسيط والمتقدم. إذا كانت متطلبات التطبيق هي عرض المخطط بأبعاده الافتراضية، فنقترح عليك استخدام طريقة Chart.toImage على النحو التالي.

{{< highlight "cpp" >}}

// Path of output image file
U16String outputChartImage = outDir + u"out1image.png";

// Saving the chart to image file
chart.ToImage(outputChartImage, ImageType::Png);

{{< /highlight >}}

###  **تقديم الرسم البياني إلى PDF**

من أجل تقديم المخطط إلى تنسيق PDF، كشفت واجهات برمجة التطبيقات Aspose.Cells عن طريقة Chart.ToPdf مع القدرة على تخزين PDF الناتج على مسار القرص أو الدفق.

{{< highlight "cpp" >}}

// Path of output pdf file
U16String outputPdfFile = outDir + u"out1pdf.pdf";

// Saving chart to PDF
chart.ToPdf(outputPdfFile);

{{< /highlight >}}

##  **أنواع المخططات المدعومة للعرض**

هناك بعض أنواع المخططات غير المدعومة حاليًا للعرض. تحتوي أنواع المخططات هذه على**N** في **مدعوم**عمود الجدول أدناه.

|**نوع التخطيط**|**النوع الفرعي للرسم البياني**|**أيد**|
| :- | :- | :- |
|**عمود**|عمود|*ص**|
| |عمود مكدس|*ص**|
| |عمود100%مكدس|*ص**|
| |Column3Dمجمع|*ص**|
| |Column3DStacked|*ص**|
| |العمود3D100٪مكدس|*ص**|
| |عمود3D|*ص**|
|**حاجِز**|حاجِز|*ص**|
| |BarStacked|*ص**|
| |شريط مكدس بنسبة 100%|*ص**|
| |Bar3Dمجمع|*ص**|
| |Bar3DStacked|*ص**|
| |شريط3D100%مكدس|*ص**|
|**خط**|خط|*ص**|
| |LineStacked|*ص**|
| |Line100%مكدس|*ص**|
| |LineWithDataMarkers|*ص**|
| |LineStackedWithDataMarkers|*ص**|
| |Line100%مكدس مع علامات البيانات|*ص**|
| |Line3D|*ص**|
|**فطيرة**|فطيرة|*ص**|
| |فطيرة3D|*ص**|
| |فطيرة فطيرة|*ص**|
| |فطيرة انفجرت|*ص**|
| |Pie3DExploded|*ص**|
| |بيبار|*ص**|
|**مبعثر**|مبعثر|*ص**|
| |مبعثر متصل بواسطة منحنيات مع DataMarker|*ص**|
| |مبعثر متصل بواسطة منحنيات بدون علامة البيانات|*ص**|
| |ScatterConnectedByLinesWithDataMarker|*ص**|
| |ScatterConnectedByLinesWithoutDataMarker|*ص**|
|**منطقة**|منطقة|*ص**|
| |منطقة مكدسة|*ص**|
| |المساحة 100%مكدسة|*ص**|
| |منطقة3D|*ص**|
| |Area3DStacked|*ص**|
| |المساحة 3D100%مكدسة|*ص**|
|**كعكة محلاة**|كعكة محلاة|*ص**|
| |دوناتانفجرت|*ص**|
|**رادار**|رادار|*ص**|
| |الرادار مع علامات البيانات|*ص**|
| |رادار معبأ|*ص**|
|**سطح**|سطح3D|N|
| |SurfaceWireframe3D|N|
| |SurfaceContour|N|
| |SurfaceContourWireframe|N|
|**فقاعة**|فقاعة|*ص**|
| |Bubble3D|N|
|مخزون|StockHighLowClose|*ص**|
| |ستوك أوبن هاي لو كلوز|*ص**|
| |حجم المخزون مرتفع، منخفض، إغلاق|*ص**|
| |حجم المخزون، فتح، ارتفاع، انخفاض، إغلاق|*ص**|
|**اسطوانة**|اسطوانة|*ص**|
| |CylinderStacked|*ص**|
| |الأسطوانة مكدسة بنسبة 100%|*ص**|
| |شريط اسطواني|*ص**|
| |CylindricalBarStacked|*ص**|
| |شريط أسطواني مكدس بنسبة 100%|*ص**|
| |عمود أسطواني3D|*ص**|
|**مخروط**|مخروط|*ص**|
| |ConeStacked|*ص**|
| |مخروطي100%مكدس|*ص**|
| |ConicalBar|*ص**|
| |ConicalBarStacked|*ص**|
| |شريط مخروطي بنسبة 100% مكدس|*ص**|
| |ConicalColumn3D|*ص**|
|**هرم**|هرم|*ص**|
| |الهرممكدس|*ص**|
| |الهرم مكدس بنسبة 100%|*ص**|
| |PyramidBar|*ص**|
| |PyramidBarStacked|*ص**|
| |PyramidBar100%مكدس|*ص**|
| |الهرم العمود3D|*ص**|
|**BoxWhisker**|BoxWhisker|Y|
|**قمع**|قمع|*ص**|
|**باريتولين**|باريتولين|*ص**|
|**أمة الله**|أمة الله|*ص**|
|**خريطة هيكلية**|خريطة هيكلية|*ص**|
|**شلال**|شلال|*ص**|
|**الرسم البياني**|الرسم البياني|Y|
|**خريطة**|خريطة|*ن**|

{{% alert color="primary" %}}

في حالة محاولتك تقديم أنواع المخططات غير المدعومة إلى صورة أو PDF، فقد ينتهي بك الأمر بصور بحجم 0 أو PDF فارغة.

{{% /alert %}}
