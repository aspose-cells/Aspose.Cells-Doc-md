---
title: Grafikten Görüntü
description: Aspose.Cells for Python via .NET kullanarak bir grafiği JPEG veya PNG gibi görüntü formatına dönüştürmeyi öğrenin. Kılavuzumuz, Microsoft Excel den bir grafik dışa aktarma ve onu bağımsız bir görsel olarak kaydetme adımlarını gösterecek.
keywords: Aspose.Cells for Python via .NET, Grafikleri Görsele Dönüştürme, Microsoft Excel, Görüntü Dönüşümü, Dışa Aktarma, Bağımsız Görsel.
linktitle: Grafikten Görüntü
type: docs
weight: 46
url: /tr/python-net/chart-to-image/
---

## **Grafikleri Oluşturma**

Aspose.Cells for Python via .NET API’leri, Excel Grafiklerini ek herhangi bir ek araç veya uygulama olmadan görüntü formatlarına dönüştürmeyi destekler. Render desteği sağlamak için, [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) sınıfı çeşitli overload’lara sahip [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) yöntemlerini açığa çıkarır, böylece uygulama gereksinimlerine en iyi şekilde uyabilir.

### **Grafikleri Görüntüye Dönüştürme**

[**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) yöntemi, hem basit hem de gelişmiş görüntülemeyi desteklemek için bir dizi aşırı yükleme sunar. Uygulama gereksinimi grafik boyutlarında ise, [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) yöntemini kullanmanızı öneririz.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImage.py" >}}

Grafiklerin gelişmiş ayarlarla görselleştirilmesi de mümkündür. Aspose.Cells for Python via .NET API’leri, [**Chart.to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_image) yönteminin overload versiyonunu açığa çıkararak, [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/) örneği kabul edebilir ve çözünürlük, yumuşatma modu, görüntü formatı gibi parametreleri belirtebilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.py" >}}

## **Görüntüleme için Desteklenen Grafik Türleri**

Şu anda görüntüleme için desteklenmeyen birkaç grafik türü vardır. Bu tür grafikler, aşağıdaki tablonun **Desteklenen** sütununda **N** içerir.

|**Grafik türü**|**Grafik alt türü**|**Desteklenen**|
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

Görüntüye veya PDF'ye dönüştürmeye çalıştığınızda, desteklenmeyen grafik türlerini 0 boyutlu görüntüler veya boş PDF'lerle sonuçlanabilirsiniz.

{{% /alert %}}

## **Gelişmiş Konular**
- [Grafiği PDF'ye Dönüştürme](/cells/tr/python-net/chart-to-pdf/)
