---
title: Grafikten Görüntü
description: Aspose.Cells for .NET kullanarak bir grafiği JPEG veya PNG gibi bir görüntü formatına dönüştürmeyi nasıl yapılır öğrenin. Rehberimiz Microsoft Excel den bir grafik dışa aktarmanın ve daha sonra ayrı bir görüntü olarak kaydetmenin nasıl yapılacağını gösterecektir.
keywords: Aspose.Cells for .NET, Grafikten Görüntü, Microsoft Excel, Görüntü Dönüşümü, Dışa Aktarma, Ayrı Görüntü.
linktitle: Grafikten Görüntü
type: docs
weight: 46
url: /tr/net/chart-to-image/
---

## **Grafikleri Oluşturma**

Aspose.Cells API'ları, Excel Grafiklerini ek araç veya uygulamalara ihtiyaç duymadan görüntü formatlarına dönüştürmeyi destekler. Görüntüleme desteği sağlamak için [**Chart**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) sınıfında bir dizi [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) yöntemi açığa çıkardı.

### **Grafikleri Görüntüye Dönüştürme**

[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) yöntemi, hem basit hem de gelişmiş görüntülemeyi desteklemek için bir dizi aşırı yükleme sunar. Uygulama gereksinimi grafik boyutlarında ise, [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) yöntemini kullanmanızı öneririz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

Grafikleri gelişmiş ayarlarla görüntülemek de mümkündür. Aspose.Cells API'ları, [**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) yönteminin bir aşırı yükleme sürümünü açığa çıkarmış ve çözünürlük, yumuşatma modu, görüntü formatı vb. gibi parametreleri belirtmeyi sağlayan bir [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) örneğini kabul edebilecek bir sürümünü kabul etmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

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
- [Grafiği PDF'ye Dönüştürme](/cells/tr/net/chart-to-pdf/)
{{< app/cells/assistant language="csharp" >}}
