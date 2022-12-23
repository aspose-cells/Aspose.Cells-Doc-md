---
title: Grafik Oluşturma
linktitle: Görüntüye veya Pdf'ye
type: docs
weight: 40
url: /tr/java/chart-rendering/
---
## **Grafik Oluşturma**

 Aspose.Cells API'ler, konu altında ayrıntılı olarak açıklandığı gibi çeşitli Excel grafikleri oluşturmayı destekler[Excel Grafikleri Oluşturma ve Özelleştirme](/cells/tr/java/creating-and-customizing-charts/). Grafikleri görüntü & PDF biçiminde işlemek için Aspose.Cells API'lerinin kullanımını göstermek için, aşağıdaki parçacığa göre Sütun türünde bir grafik oluşturacağız.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-CreateChart-CreateChart.java" >}}

## **Oluşturma Grafikleri**

 Aspose.Cells API'leri, Excel Grafiklerini herhangi bir ek araç veya uygulama gerektirmeden resimlere ve PDF biçimlerine dönüştürmeyi destekler. Render desteği sağlamak için,[**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)sınıf açığa çıktı[**Hayal etmek**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) & [**topdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) uygulama gereksinimlerine en iyi şekilde uyacak aşırı yükleme verisine sahip yöntemler.

### **Grafikleri Görüntülere Dönüştürme**

 bu[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) yöntemi, basit ve gelişmiş işlemeyi desteklemek için çeşitli aşırı yüklemelere sahiptir. Uygulama gereksinimi, grafiği varsayılan boyutlarında oluşturmaksa,[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions)) yöntemi aşağıdaki gibidir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-RenderChartsToImages-RenderChartsToImages.java" >}}

Grafikleri gelişmiş ayarlarla görüntülere dönüştürmek de mümkündür. Aspose.Cells API'ler, bir aşırı yük sürümünü kullanıma sundu[**Chart.toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toImage(java.io.OutputStream,%20com.aspose.cells.ImageOrPrintOptions) ) örneğini kabul edebilecek yöntem[**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)Çözünürlük, işleme ipuçları, görüntü formatı vb. gibi parametreleri belirlemeye izin verirken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-ChartRendering-ChartRendering.java" >}}

### **Tabloyu PDF'e Oluşturma**

 Grafiği PDF biçimine dönüştürmek için Aspose.Cells API'leri[**Chart.toPdf**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#toPdf(java.io.OutputStream)) elde edilen PDF'i disk yolunda veya bir OutputStream örneğinde saklama yeteneğine sahip yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-chartsRenderChartsToPdf-RenderChartsToPdf.java" >}}

## **Oluşturma için Desteklenen Grafik Türleri**

 Şu anda işleme için desteklenmeyen birkaç grafik türü vardır. Bu tür grafik türleri şunları içerir:** içinde N****Aşağıdaki tablonun desteklenen** sütunu.

|**Grafik tipi**|**Grafik alt türü**|**desteklenen**|
|:- |:- |:- |
|**Kolon**|Kolon|**e**|
||SütunYığılmış|**e**|
||Sütun100YığılmışYüzde|**e**|
||Sütun3Dkümelenmiş|**e**|
||Sütun3DSığılmış|**e**|
||Sütun3D100YığılmışYüzde|**e**|
||Sütun3D|**e**|
|**Bar**|Bar|**e**|
||Çubuk Yığılmış|**e**|
||Bar100YığılmışYüzde|**e**|
||Bar3Dkümelenmiş|**e**|
||Bar3DSyığılmış|**e**|
||Bar3D100YığılmışYüzde|**e**|
|**Astar**|Astar|**e**|
||Sıra Yığılmış|**e**|
||Line100PercentYığılmış|**e**|
||LineWithDataMarkers|**e**|
||LineStackedWithDataMarkers|**e**|
||Line100PercentStackedWithDataMarkers|**e**|
||Çizgi3D|**e**|
|**Turta**|Turta|**e**|
||Pasta3D|**e**|
||Turta Turtası|**e**|
||PastaPatladı|**e**|
||Pie3DEpatladı|**e**|
||pasta çubuğu|**e**|
|**Dağılım**|Dağılım|**e**|
||DağılımConnectedByCurvesWithDataMarker|**e**|
||ScatterConnectedByCurvesWithoutDataMarker|**e**|
||ScatterConnectedByLinesWithDataMarker|**e**|
||ScatterConnectedByLinesWithoutDataMarker|**e**|
|**Alan**|Alan|**e**|
||Yığılmış Alan|**e**|
||Alan100YığılmışYüzde|**e**|
||Alan3D|**e**|
||Alan3Dyığınlanmış|**e**|
||Alan3D100YığılmışYüzde|**e**|
|**Tatlı çörek**|Tatlı çörek|**e**|
||DonutPatladı|**e**|
|**Radar**|Radar|**e**|
||RadarWithDataMarkers|**e**|
||Radar Dolu|**e**|
|**Yüzey**|Yüzey3D|N|
||SurfaceWireframe3D|N|
||Yüzey Konturu|N|
||Yüzey Kontur Tel Kafes|N|
|**kabarcık**|kabarcık|**e**|
||Bubble3D|N|
|**Stoklamak**|StokYüksekDüşükKapat|**e**|
||StokAçıkYüksekDüşükKapat|**e**|
||StokHacimYüksekDüşükKapat|**e**|
||Stok HacmiAçıkYüksekDüşükKapalı|**e**|
|**silindir**|silindir|**e**|
||Silindir Yığılmış|**e**|
||Cylinder100PercentYığılmış|**e**|
||Silindirik Çubuk|**e**|
||Silindirik ÇubukYığılmış|**e**|
||SilindirikÇubukYüzde100Yığılmış|**e**|
||Silindirik Sütun3D|**e**|
|**koni**|koni|**e**|
||koni yığılmış|**e**|
||Koni100YüzdeYığılmış|**e**|
||Konik Çubuk|**e**|
||Konik ÇubukYığılmış|**e**|
||ConicalBar100PercentYığılmış|**e**|
||Konik Sütun3D|**e**|
|**Piramit**|Piramit|**e**|
||PiramitYığılmış|**e**|
||Piramit100YüzdeYığılmış|**e**|
||PiramitBar|**e**|
||PiramitÇubuğuYığılmış|**e**|
||PiramitBar100PercentYığınlanmış|**e**|
||PiramitSütun3D|**e**|
|**KutuBıyık**|KutuBıyık|Y|
|**Huni**|Huni|**e**|
|**ParetoLine**|ParetoLine|**e**|
|**güneş patlaması**|güneş patlaması|**e**|
|**ağaç haritası**|ağaç haritası|**e**|
|**Şelale**|Şelale|**e**|
|**histogram**|histogram|Y|
|**Harita**|Harita|**N**|

{{% alert color="primary" %}}

Desteklenmeyen grafik türlerini resim veya PDF'e dönüştürmeye çalışırsanız, 0 boyutlu resimler veya boş PDF ile sonuçlanabilirsiniz.

{{% /alert %}}


## **ileri konular**
- [Grafiği SVG Formatında Resme Dönüştürme](/cells/tr/java/converting-chart-to-image-in-svg-format/)
- [İstenilen Sayfa Boyutuyla Grafik PDF Oluşturun](/cells/tr/java/create-chart-pdf-with-desired-page-size/)
- [Grafiği viewBox özniteliğiyle SVG'e aktarın](/cells/tr/java/export-chart-to-svg-with-viewbox-attribute/)
