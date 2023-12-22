---
title: الرسم البياني للصورة
description: تعرف على كيفية استخدام Aspose.Cells for .NET لتحويل مخطط إلى تنسيق صورة، مثل JPEG أو PNG. سيوضح دليلنا كيفية تصدير مخطط من Microsoft Excel وحفظه كصورة مستقلة لمزيد من الاستخدام والمعالجة.
keywords: Aspose.Cells for .NET, Chart to Image, Microsoft Excel, Image Conversion, Export, Standalone Image.
linktitle: الرسم البياني للصورة
type: docs
weight: 46
url: /ar/net/chart-to-image/
---
##  **تقديم المخططات**

 Aspose.Cells دعم واجهات برمجة التطبيقات لتحويل مخططات Excel إلى تنسيقات صور دون الحاجة إلى أي أدوات أو تطبيقات إضافية. من أجل تقديم الدعم، و[**جدول**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) لقد كشفت الطبقة[**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) طرق مع حقيقة الأحمال الزائدة لتناسب متطلبات التطبيق بشكل أفضل.

###  **تقديم المخططات إلى الصور**

 ال[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) تحتوي الطريقة على عدد كبير من الأحمال الزائدة لدعم العرض البسيط والمتقدم. إذا كانت متطلبات التطبيق هي عرض المخطط بأبعاده الافتراضية، فنقترح عليك استخدام[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)الطريقة على النحو التالي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 من الممكن أيضًا عرض المخططات على الصور باستخدام الإعدادات المتقدمة. كشفت واجهات برمجة التطبيقات Aspose.Cells عن إصدار التحميل الزائد من[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) الطريقة التي يمكن أن تقبل مثيل[**خيارات الصورة أو الطباعة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)، مع السماح بتحديد المعلمات مثل الدقة ووضع التجانس وتنسيق الصورة وما إلى ذلك.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

##  **أنواع المخططات المدعومة للعرض**

 هناك بعض أنواع المخططات غير المدعومة حاليًا للعرض. تحتوي أنواع المخططات هذه على**N** في **مدعوم** عمود الجدول أدناه.

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
|**مخزون**|StockHighLowClose|*ص**|
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

##  **مواضيع متقدمة**
- [تحويل الرسم البياني إلى PDF](/cells/ar/net/chart-to-pdf/)
