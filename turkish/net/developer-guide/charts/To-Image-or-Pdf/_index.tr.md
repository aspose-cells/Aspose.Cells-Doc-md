---
title: Grafik Oluşturma
linktitle: Görüntüye veya Pdf'ye
type: docs
weight: 45
url: /tr/net/chart-rendering/
---
## **Oluşturma Grafikleri**

 Aspose.Cells API'ler, Excel Grafiklerini herhangi bir ek araç veya uygulama gerektirmeden resimlere ve PDF biçimlerine dönüştürmeyi destekler. Render desteği sağlamak için,[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) sınıf açığa çıktı[**Hayal etmek**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)uygulama gereksinimlerine en iyi uyacak şekilde aşırı yükleme verisine sahip yöntemler.

### **Grafikleri Görüntülere Dönüştürme**

 bu[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) & [**ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index) yöntem, hem basit hem de gelişmiş işlemeyi desteklemek için çeşitli aşırı yüklemelere sahiptir. Uygulama gereksinimi, grafiği varsayılan boyutlarında oluşturmaksa,[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)aşağıdaki gibi yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 Grafikleri gelişmiş ayarlarla görüntülere dönüştürmek de mümkündür. Aspose.Cells API'ler, bir aşırı yük sürümünü kullanıma sundu[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) örneğini kabul edebilecek bir yöntem[**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), çözünürlük, yumuşatma modu, görüntü formatı vb. gibi parametreleri belirlemeye izin verirken.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

### **Grafiği PDF'e Dönüştürme**

 Grafiği PDF formatına dönüştürmek için Aspose.Cells API'leri[**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)Elde edilen PDF'yi disk yolunda veya Akışta saklama yeteneğine sahip bir yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

## **Oluşturma için Desteklenen Grafik Türleri**

 Şu anda işleme için desteklenmeyen birkaç grafik türü vardır. Bu tür grafik türleri şunları içerir:** içinde N****Aşağıdaki tablonun desteklenen** sütunu.

|**Grafik türü**|**Grafik alt türü**|**desteklenen**|
|:- |:- |:- |
|**Kolon**|Kolon|**e**|
||SütunYığılmış|**e**|
||Sütun100YığılmışYüzde|**e**|
||Sütun3Dkümelenmiş|**e**|
||Sütun3DSığılmış|**e**|
||Sütun3D100YığılmışYüzde|**e**|
||Sütun3D|**e**|
|**Çubuk**|Çubuk|**e**|
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

Desteklenmeyen grafik türlerini görüntüye veya PDF'ye dönüştürmeye çalışırsanız, 0 boyutlu görüntüler veya boş PDF ile karşılaşabilirsiniz.

{{% /alert %}}

## **ileri konular**
- [Grafiği İstenilen Sayfa Boyutuyla PDF'ye Dönüştürün](/cells/tr/net/chart-to-pdf/)
