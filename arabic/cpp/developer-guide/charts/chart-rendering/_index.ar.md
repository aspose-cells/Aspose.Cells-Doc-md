---
title: عرض المخطط
type: docs
weight: 30
url: /ar/cpp/chart-rendering/
---
## **إنشاء الرسوم البيانية**

دعم Aspose.Cells APIs لإنشاء حقيقة من مخططات Excel كما هو مفصل تحت الموضوع[إنشاء وتخصيص مخططات Excel](/cells/ar/cpp/creating-and-customizing-charts/)لتوضيح استخدام واجهات برمجة تطبيقات Aspose.Cells لعرض المخططات بتنسيق صورة و PDF ، سننشئ مخططًا من النوع Column وفقًا للمقتطف التالي.

{{< highlight "cpp" >}}

     // Create a new workbook

	intrusive_ptr<IWorkbook> workbook = Factory::CreateIWorkbook();

	// Get first worksheet which is created by default

	intrusive_ptr<IWorksheet> worksheet = workbook->GetIWorksheets()->GetObjectByIndex(0);

	// Adding sample values to cells

	worksheet->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(50);

	worksheet->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(100);

	worksheet->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(150);

	worksheet->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(4);

	worksheet->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(20);

	worksheet->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(50);

	// Adding a chart to the worksheet

	int chartIndex = worksheet->GetICharts()->Add(Aspose::Cells::Charts::ChartType::ChartType_Column, 5, 0, 20, 8);

	// Accessing the instance of the newly added chart

	intrusive_ptr<Aspose::Cells::Charts::IChart> chart = worksheet->GetICharts()->GetObjectByIndex(chartIndex);

	// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"

	chart->GetNISeries()->Add(new String("A1:B3"), true);

{{< /highlight >}}

## **تقديم المخططات**

تدعم واجهات برمجة التطبيقات Aspose.Cells تحويل مخططات Excel إلى صور وتنسيقات PDF دون الحاجة إلى أي أدوات أو تطبيقات إضافية. من أجل توفير دعم العرض ، كشفت فئة الرسم البياني طرق ToImage & ToPdf مع حقيقة من الأحمال الزائدة لتناسب متطلبات التطبيق على أفضل وجه.

### **تقديم المخططات للصور**

طريقة Chart.toImage لديها حقيقة من الأحمال الزائدة لدعم التصيير البسيط والمتقدم. إذا كان مطلب التطبيق هو عرض المخطط بأبعاده الافتراضية ، فإننا نقترح عليك استخدام طريقة Chart.toImage على النحو التالي.

{{< highlight "cpp" >}}

 // Output directory path

StringPtr outDir = new String("..\\Data\\02_OutputDirectory\\");

// Path of output image file

StringPtr outputChartImage = outDir->StringAppend(new String("out1image.png"));

// Saving the chart to image file

chart->ToImage(outputChartImage, Aspose::Cells::System::Drawing::Imaging::ImageFormat::GetPng());

{{< /highlight >}}

### **تقديم مخطط إلى PDF**

من أجل تقديم المخطط إلى تنسيق PDF ، كشفت واجهات برمجة التطبيقات Aspose.Cells عن طريقة Chart.ToPdf مع القدرة على تخزين ملف PDF الناتج على مسار القرص أو التدفق.

{{< highlight "cpp" >}}

 // Path of output pdf file

StringPtr outputPdfFile = outDir->StringAppend(new String("out1pdf.pdf"));

// Saving chart to PDF

chart->ToPdf(outputPdfFile);

{{< /highlight >}}

## **أنواع الرسوم البيانية المدعومة للتقديم**

هناك عدد قليل من أنواع المخططات التي لا يتم دعمها حاليًا للعرض. تحتوي هذه الأنواع من المخططات على ملفات**N ** في**عمود ** المدعوم من الجدول أدناه.

|**نوع التخطيط**|**النوع الفرعي للمخطط**|**أيد**|
|:- |:- |:- |
|**عمودي**|عمودي|** نعم **|
||العمود مكدسة|** نعم **|
||عمود 100 نسبة مكدسة|** نعم **|
||Column3D العنقودية|** نعم **|
||العمود 3D مكدسة|** نعم **|
||عمود 3 D100Percent مكدسة|** نعم **|
||العمود 3 د|** نعم **|
|**شريط**|شريط|** نعم **|
||بار مكدسة|** نعم **|
||شريط 100٪ مكدسة|** نعم **|
||شريط ثلاثي الأبعاد متفاوت|** نعم **|
||Bar3D مكدسة|** نعم **|
||شريط ثلاثي الأبعاد 100٪ مكدس|** نعم **|
|**خط**|خط|** نعم **|
||LineStacked|** نعم **|
||Line100Percent مكدس|** نعم **|
||LineWithDataMarkers|** نعم **|
||LineStackedWithDataMarkers|** نعم **|
||Line100PercentStackedWithDataMarkers|** نعم **|
||Line3D|** نعم **|
|**فطيرة**|فطيرة|** نعم **|
||Pie3D|** نعم **|
||فطيرة فطيرة|** نعم **|
||انفجرت الفطيرة|** نعم **|
||انفجرت Pie3D|** نعم **|
||بي بار|** نعم **|
|**مبعثر**|مبعثر|** نعم **|
||ScatterConnectedByCurvesWithDataMarker|** نعم **|
||ScatterConnectedByCurvesWithoutDataMarker|** نعم **|
||ScatterConnectedByLinesWithDataMarker|** نعم **|
||ScatterConnectedByLinesWithoutDataMarker|** نعم **|
|**منطقة**|منطقة|** نعم **|
||المنطقة مكدسة|** نعم **|
||مساحة 100٪ مكدسة|** نعم **|
||Area3D|** نعم **|
||Area3D مكدس|** نعم **|
||Area3D100Percent مكدس|** نعم **|
|**الدونات**|الدونات|** نعم **|
||انفجرت العجين|** نعم **|
|**رادار**|رادار|** نعم **|
||RadarWithDataMarkers|** نعم **|
||الرادار|** نعم **|
|**سطح**|Surface3D|ن|
||SurfaceWireframe3D|ن|
||SurfaceContour|ن|
||SurfaceContourWireframe|ن|
|**فقاعة**|فقاعة|** نعم **|
||فقاعة ثلاثية الأبعاد|ن|
|مخزون|StockHighLowClose|** نعم **|
||مخزون OpenHighLowClose|** نعم **|
||حجم المخزن HighLowClose|** نعم **|
||حجم المخزون OpenHighLowClose|** نعم **|
|**اسطوانة**|اسطوانة|** نعم **|
||اسطوانة مكدسة|** نعم **|
||اسطوانة 100٪ مكدسة|** نعم **|
||أسطواني بار|** نعم **|
||أسطواني بار مكدس|** نعم **|
||شريط أسطواني 100٪ مكدس|** نعم **|
||عمود أسطواني ثلاثي الأبعاد|** نعم **|
|**مخروط**|مخروط|** نعم **|
||مخروط|** نعم **|
||مخروط 100٪ مكدسة|** نعم **|
||مخروطي الشكل|** نعم **|
||مخروطي الشكل مكدس|** نعم **|
||مخروطي الشكل 100٪ مكدس|** نعم **|
||عمود مخروطي ثلاثي الأبعاد|** نعم **|
|**هرم**|هرم|** نعم **|
||الهرم مكدسة|** نعم **|
||الهرم 100٪ مكدسة|** نعم **|
||هرم بار|** نعم **|
||PyramidBar مكدس|** نعم **|
||PyramidBar100Percent مكدسة|** نعم **|
||الهرم عمود 3 د|** نعم **|
|**BoxWhisker**|BoxWhisker|ص|
|**قمع**|قمع|** نعم **|
|**باريتولين**|باريتولين|** نعم **|
|**أمة الله**|أمة الله|** نعم **|
|**مخطط Treemap**|مخطط Treemap|** نعم **|
|**شلال**|شلال|** نعم **|
|**الرسم البياني**|الرسم البياني|ص|
|**خريطة**|خريطة|**ن**|

{{% alert color="primary" %}}

في حالة محاولة عرض أنواع المخططات غير المدعومة على صورة أو ملف PDF ، فقد ينتهي بك الأمر مع 0 صور بحجم أو ملف PDF فارغ.

{{% /alert %}}
