---
title: تقديم الرسم البياني
linktitle: إلى صورة أو Pdf
type: docs
weight: 40
url: /ar/java/chart-rendering/
---

## **إنشاء الرسوم البيانية**

تدعم واجهات برمجة التطبيقات (APIs) لـ Aspose.Cells إنشاء مجموعة متنوعة من الرسوم البيانية في Excel كما هو مفصل في الموضوع [إنشاء وتخصيص رسوم بيانية في Excel](/cells/ar/java/creating-and-customizing-charts/) . من أجل توضيح استخدام واجهات برمجة التطبيقات (APIs) لـ Aspose.Cells لتقديم الرسوم البيانية بصيغة صورة و PDF ، سوف نقوم بإنشاء رسم بياني من نوع Column وفقًا للكود المصغر التالي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **عرض الرسوم البيانية**

تدعم واجهات برمجة التطبيقات الخاصة بـ Aspose.Cells تحويل الرسوم البيانية في Excel إلى صور وتنسيقات PDF دون الحاجة إلى أدوات أو تطبيقات إضافية. من أجل توفير دعم الرسم، فقد قدمت فئة [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) طرق [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) و [**toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf-java.io.OutputStream-) بمجموعة متنوعة من الأوزان لتناسب أفضل متطلبات التطبيق.

### **عرض الرسوم البيانية كصور**

لطريقة [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) مجموعة من الأوزان لدعم التقديم البسيط والمتقدم. إذا كان متطلبات التطبيق هي تقديم الرسم البياني في أبعاده الافتراضية، فإننا نقترح عليك استخدام الطريقة [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) كما يلي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

من الممكن أيضًا تقديم الرسوم البيانية إلى صور بإعدادات متقدمة. فقد قدمت واجهات برمجة التطبيقات الخاصة بـ Aspose.Cells إصدارًا من الطريقة [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage-java.io.OutputStream-com.aspose.cells.ImageOrPrintOptions-) زائد الأحمال التي يمكنها قبول مثيل [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) بالإضافة إلى السماح بتحديد معلمات مثل الدقة وتلميحات التقديم وتنسيق الصورة وما إلى ذلك.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **عرض الرسم البياني إلى PDF**

من أجل تقديم الرسم البياني إلى تنسيق PDF، فقد قدمت واجهات برمجة التطبيقات الخاصة بـ Aspose.Cells الطريقة [**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf-java.io.OutputStream-) مع القدرة على تخزين PDF الناتج على مسار القرص أو مثيل من OutputStream.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **أنواع الرسوم البيانية المدعومة للعرض**

هناك بعض أنواع الرسوم البيانية التي لا تحظى حاليًا بالدعم لعملية الرسم. تحتوي مثل هذه الأنواع على **N** في العمود **المدعوم** من الجدول أدناه.

|**نوع الرسم البياني**|**نوع الفرعي للرسم البياني**|**مدعوم**|
| :- | :- | :- |
|**Column**|Column|**Y**|
| |ColumnStacked|**Y**|
| |Column100PercentStacked|**Y**|
| |Column3DClustered|**Y**|
| |Column3DStacked|**Y**|
| |Column3D100PercentStacked|**Y**|
| |Column3D|**Y**|
|**Bar**|Bar|**Y**|
| |BarStacked|**Y**|
| |Bar100PercentStacked|**Y**|
| |Bar3DClustered|**Y**|
| |Bar3DStacked|**Y**|
| |Bar3D100PercentStacked|**Y**|
|**Line**|Line|**Y**|
| |LineStacked|**Y**|
| |Line100PercentStacked|**Y**|
| |LineWithDataMarkers|**Y**|
| |LineStackedWithDataMarkers|**Y**|
| |Line100PercentStackedWithDataMarkers|**Y**|
| |Line3D|**Y**|
|**Pie**|Pie|**Y**|
| |Pie3D|**Y**|
| |PiePie|**Y**|
| |PieExploded|**Y**|
| |Pie3DExploded|**Y**|
| |PieBar|**Y**|
|**Scatter**|Scatter|**Y**|
| |ScatterConnectedByCurvesWithDataMarker|**Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|**Y**|
| |ScatterConnectedByLinesWithDataMarker|**Y**|
| |ScatterConnectedByLinesWithoutDataMarker|**Y**|
|**Area**|Area|**Y**|
| |AreaStacked|**Y**|
| |Area100PercentStacked|**Y**|
| |Area3D|**Y**|
| |Area3DStacked|**Y**|
| |Area3D100PercentStacked|**Y**|
|**Doughnut**|Doughnut|**Y**|
| |DoughnutExploded|**Y**|
|**Radar**|Radar|**Y**|
| |RadarWithDataMarkers|**Y**|
| |RadarFilled|**Y**|
|**Surface**|Surface3D|N|
| |SurfaceWireframe3D|N|
| |SurfaceContour|N|
| |SurfaceContourWireframe|N|
|**Bubble**|Bubble|**Y**|
| |Bubble3D|N|
|**Stock**|StockHighLowClose|**Y**|
| |StockOpenHighLowClose|**Y**|
| |StockVolumeHighLowClose|**Y**|
| |StockVolumeOpenHighLowClose|**Y**|
|**Cylinder**|Cylinder|**Y**|
| |CylinderStacked|**Y**|
| |Cylinder100PercentStacked|**Y**|
| |CylindricalBar|**Y**|
| |CylindricalBarStacked|**Y**|
| |CylindricalBar100PercentStacked|**Y**|
| |CylindricalColumn3D|**Y**|
|**Cone**|Cone|**Y**|
| |ConeStacked|**Y**|
| |Cone100PercentStacked|**Y**|
| |ConicalBar|**Y**|
| |ConicalBarStacked|**Y**|
| |ConicalBar100PercentStacked|**Y**|
| |ConicalColumn3D|**Y**|
|**Pyramid**|Pyramid|**Y**|
| |PyramidStacked|**Y**|
| |Pyramid100PercentStacked|**Y**|
| |PyramidBar|**Y**|
| |PyramidBarStacked|**Y**|
| |PyramidBar100PercentStacked|**Y**|
| |PyramidColumn3D|**Y**|
|**BoxWhisker**|BoxWhisker|Y|
|**Funnel**|Funnel|**Y**|
|**ParetoLine**|ParetoLine|**Y**|
|**Sunburst**|Sunburst|**Y**|
|**Treemap**|Treemap|**Y**|
|**Waterfall**|Waterfall|**Y**|
|**Histogram**|Histogram|Y|
|**Map**|Map|**N**|

{{% alert color="primary" %}}

في حال محاولة عرض أنواع الرسوم البيانية غير المدعومة إلى صورة أو PDF، قد تنتهي بصور بحجم 0 أو PDF فارغة.

{{% /alert %}}


## **مواضيع متقدمة**
- [تحويل مخطط إلى صورة بتنسيق SVG](/cells/ar/java/converting-chart-to-image-in-svg-format/)
- [إنشاء رسم بياني PDF بحجم الصفحة المطلوب](/cells/ar/java/create-chart-pdf-with-desired-page-size/)
- [تصدير مخطط إلى SVG باستخدام سمة viewBox](/cells/ar/java/export-chart-to-svg-with-viewbox-attribute/)
{{< app/cells/assistant language="java" >}}
