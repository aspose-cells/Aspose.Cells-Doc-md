---
title: عرض المخطط
linktitle: إلى صورة أو PDF
type: docs
weight: 40
url: /ar/java/chart-rendering/
---
## **إنشاء الرسوم البيانية**

 دعم Aspose.Cells APIs لإنشاء حقيقة من مخططات Excel كما هو مفصل تحت الموضوع[إنشاء وتخصيص مخططات Excel](/cells/ar/java/creating-and-customizing-charts/). لتوضيح استخدام واجهات برمجة تطبيقات Aspose.Cells لعرض المخططات في صورة وتنسيق PDF ، سنقوم بإنشاء مخطط من النوع Column وفقًا للمقتطف التالي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **تقديم المخططات**

 تدعم واجهات برمجة تطبيقات Aspose.Cells تحويل مخططات Excel إلى صور وتنسيقات PDF دون الحاجة إلى أي أدوات أو تطبيقات إضافية. من أجل تقديم الدعم ، فإن[**جدول**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)لقد كشفت الطبقة[**إلى الصورة**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) & [**toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) طرق ذات حمولات زائدة لتناسب متطلبات التطبيق على أفضل وجه.

### **تقديم المخططات للصور**

 ال[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) لديها حقيقة من الأحمال الزائدة لدعم التقديم البسيط والمتقدم. إذا كانت متطلبات التطبيق هي عرض المخطط بأبعاده الافتراضية ، فنحن نقترح عليك استخدام ملف[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) الطريقة على النحو التالي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

من الممكن أيضًا عرض المخططات على الصور باستخدام الإعدادات المتقدمة. كشفت واجهات برمجة التطبيقات Aspose.Cells عن إصدار التحميل الزائد من[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions) ) التي يمكن أن تقبل مثيل[**خيارات ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)مع السماح بتحديد معلمات مثل الدقة وتلميحات العرض وتنسيق الصورة وما إلى ذلك.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **تقديم مخطط إلى PDF**

 من أجل تقديم المخطط إلى تنسيق PDF ، كشفت واجهات برمجة التطبيقات Aspose.Cells تنسيق[**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) مع القدرة على تخزين الناتج PDF على مسار القرص أو مثيل OutputStream.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **أنواع الرسوم البيانية المدعومة للتقديم**

 هناك عدد قليل من أنواع المخططات التي لا يتم دعمها حاليًا للعرض. تحتوي هذه الأنواع من المخططات على ملفات** N ** في**عمود ** المدعوم من الجدول أدناه.

|**نوع التخطيط**|**النوع الفرعي للمخطط**|**أيد**|
|:- |:- |:- |
|**عمود**|عمود|** نعم **|
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
|**سطح - المظهر الخارجي**|Surface3D|ن|
||SurfaceWireframe3D|ن|
||SurfaceContour|ن|
||SurfaceContourWireframe|ن|
|**فقاعة**|فقاعة|** نعم **|
||فقاعة ثلاثية الأبعاد|ن|
|**مخزون**|StockHighLowClose|** نعم **|
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

في حالة محاولة تقديم أنواع المخططات غير المدعومة إلى صورة أو PDF ، فقد ينتهي بك الأمر بصور بحجم 0 أو PDF فارغًا.

{{% /alert %}}


## **موضوعات مسبقة**
- [تحويل الرسم البياني إلى صورة بتنسيق SVG](/cells/ar/java/converting-chart-to-image-in-svg-format/)
- [قم بإنشاء مخطط PDF بحجم الصفحة المطلوب](/cells/ar/java/create-chart-pdf-with-desired-page-size/)
- [تصدير المخطط إلى SVG مع سمة viewBox](/cells/ar/java/export-chart-to-svg-with-viewbox-attribute/)
