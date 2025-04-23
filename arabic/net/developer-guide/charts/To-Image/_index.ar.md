---
title: تحويل الرسم البياني إلى صورة
description: تعلم كيفية استخدام Aspose.Cells for .NET لتحويل الرسم البياني إلى تنسيق صورة مثل JPEG أو PNG. سيقوم دليلنا بشرح كيفية تصدير رسم بياني من Microsoft Excel وحفظه كصورة مستقلة للاستخدام والتعديل المستقبلي.
keywords: Aspose.Cells for .NET، تحويل الرسم البياني إلى صورة، Microsoft Excel، تحويل الصورة، التصدير، صورة مستقلة.
linktitle: تحويل الرسم البياني إلى صورة
type: docs
weight: 46
url: /ar/net/chart-to-image/
---

## **عرض الرسوم البيانية**

تدعم واجهات برمجة التطبيقات في Aspose.Cells تحويل الرسوم البيانية في Excel إلى صيغ صور دون الحاجة إلى أي أدوات أو تطبيقات إضافية. من أجل توفير دعم العرض، فإن فئة [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) قد عرضت طرق مع مجموعة متنوعة من الحمولات لتناسب أفضل متطلبات التطبيق.

### **عرض الرسوم البيانية كصور**

تحتوي طريقة [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) على مجموعة متنوعة من الحمولات لدعم العرض البسيط وكذلك العرض المتقدم. إذا كان متطلب التطبيق هو عرض الرسم البياني في أبعاده الافتراضية، نقترح عليك استخدام الطريقة [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) على النحو التالي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

من الممكن أيضًا عرض الرسوم البيانية إلى صور باستخدام إعدادات متقدمة. لقد عرضت واجهات برمجة التطبيقات في Aspose.Cells إصدارًا زائدًا من طريقة [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) التي يمكن أن تقبل مثيلًا لـ [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)، مع السماح بتحديد معلمات مثل الدقة، وضع التنعيم، تنسيق الصورة، وما إلى ذلك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

## **أنواع الرسوم البيانية المدعومة للعرض**

هناك بعض أنواع الرسوم البيانية التي لا تتم دعمها حاليًا للعرض. تحتوي مثل هذه الأنواع على **N** في العمود **مدعوم** للجدول أدناه.

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
- [تحويل الرسم البياني إلى PDF](/cells/ar/net/chart-to-pdf/)
{{< app/cells/assistant language="csharp" >}}
