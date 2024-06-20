---
title: Grafik Rendeleme
linktitle: Görüntü veya Pdf ye
type: docs
weight: 40
url: /tr/java/chart-rendering/
---

## **Grafikler Oluşturma**

Aspose.Cells API'leri, [Excel Grafikleri Oluşturma ve Özelleştirme](/cells/tr/java/creating-and-customizing-charts/) başlığı altında detaylı olarak açıklanan çeşitli Excel grafiklerini oluşturmayı destekler. Aspose.Cells API'lerinin kullanımını göstermek için, resim ve PDF formatında grafikleri oluşturacak olan bir sütun tipinde bir grafik oluşturacağız.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Grafikleri Oluşturma**

Aspose.Cells API'leri, ek araç veya uygulamalar gerekmeden Excel Grafiklerini görüntü ve PDF formatına dönüştürmeyi destekler. Rendeleme desteği sağlamak için, [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) sınıfı çeşitli aşırı yüklemelerle [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) ve [**toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) yöntemlerini sunmuştur bu, uygulama gereksinimlerine en uygun hale getirebilmek için.

### **Grafikleri Görüntüye Dönüştürme**

[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) yöntemi, basit ve gelişmiş renderelemeyi desteklemek için çeşitli aşırı yüklemelere sahiptir. Uygulama gereksinimi grafikleri varsayılan boyutlarında rendere etmekse, aşağıdaki [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) yöntemini kullanmanızı öneririz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

Ayrıca, gelişmiş ayarlarla grafikleri görüntülemek de mümkündür. Aspose.Cells API'leri, aşırı yüklemeli bir [**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) yöntemini sunmuştur ve bu yöntem, çözünürlük, rendereleme ipuçları, görüntü formatı vb. gibi parametreleri belirtmenizi sağlayan bir [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) örneğini kabul edebilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Grafiği PDF'ye Dönüştürme**

Grafiğin PDF formatına rendeleme yapmak için Aspose.Cells API'leri, sonucu diske veya OutputStream örneğine kaydetme yeteneğine sahip [**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) yöntemi sunmuştur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Görüntüleme için Desteklenen Grafik Türleri**

Şu anda desteklenmeyen birkaç grafik türü bulunmaktadır. Bu tür grafik tipleri aşağıdaki tablonun **Desteklenen** sütununda **N** içerir.

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
- [SVG Biçiminde Grafikleri Görüntüye Dönüştürme](/cells/tr/java/converting-chart-to-image-in-svg-format/)
- [İstenen Sayfa Boyutunda Grafik PDF Oluşturma](/cells/tr/java/create-chart-pdf-with-desired-page-size/)
- [Görünüm Kutusu Özelliği ile Grafiksel Bir Ortama Tabloyu Dışa Aktarma](/cells/tr/java/export-chart-to-svg-with-viewbox-attribute/)
