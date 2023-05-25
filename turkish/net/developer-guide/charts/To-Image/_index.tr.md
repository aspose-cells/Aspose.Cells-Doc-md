---
title: Grafikten Görüntüye
linktitle: Grafikten Görüntüye
type: docs
weight: 46
url: /tr/net/chart-to-image/
---
##  **Oluşturma Grafikleri**

 Aspose.Cells API'ler, herhangi bir ek araç veya uygulama gerektirmeden Excel Grafiklerini resim biçimlerine dönüştürmeyi destekler. Render desteği sağlamak için,[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) sınıf açığa çıktı[**Hayal etmek**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) uygulama gereksinimlerine en iyi uyacak şekilde aşırı yükleme verisine sahip yöntemler.

###  **Grafikleri Görüntülere Dönüştürme**

 bu[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) yöntem, hem basit hem de gelişmiş işlemeyi desteklemek için çeşitli aşırı yüklemelere sahiptir. Uygulama gereksinimi, grafiği varsayılan boyutlarında oluşturmaksa,[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)aşağıdaki gibi yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 Grafikleri gelişmiş ayarlarla görüntülere dönüştürmek de mümkündür. Aspose.Cells API'ler, bir aşırı yük sürümünü kullanıma sundu[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) örneğini kabul edebilecek bir yöntem[**ResimVeyaBaskıSeçenekleri**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), çözünürlük, yumuşatma modu, görüntü formatı vb. gibi parametreleri belirlemeye izin verirken.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

##  **Oluşturma için Desteklenen Grafik Türleri**

 Şu anda işleme için desteklenmeyen birkaç grafik türü vardır. Bu tür grafik türleri şunları içerir:****Desteklenen içinde N**** aşağıdaki tablonun sütunu.

|**Grafik tipi**|**Grafik alt türü**|**desteklenen**|
| :- | :- | :- |
|**Kolon**|Kolon|*Y**|
| |SütunYığılmış|*Y**|
| |Sütun100YüzdeYığılmış|*Y**|
| |Sütun3Dkümelenmiş|*Y**|
| |Sütun3DSığılmış|*Y**|
| |Sütun3D100YığılmışYüzde|*Y**|
| |Sütun3D|*Y**|
|**Çubuk**|Çubuk|*Y**|
| |Çubuk Yığılmış|*Y**|
| |Bar100YığılmışYüzde|*Y**|
| |Bar3Dkümelenmiş|*Y**|
| |Bar3DSyığılmış|*Y**|
| |Bar3D100YığılmışYüzde|*Y**|
|**Astar**|Astar|*Y**|
| |Sıra Yığılmış|*Y**|
| |Line100PercentYığılmış|*Y**|
| |LineWithDataMarkers|*Y**|
| |LineStackedWithDataMarkers|*Y**|
| |Line100PercentStackedWithDataMarkers|*Y**|
| |Çizgi3D|*Y**|
|**Turta**|Turta|*Y**|
| |Pasta3D|*Y**|
| |Turta Turtası|*Y**|
| |PastaPatladı|*Y**|
| |Pie3DEpatladı|*Y**|
| |pasta çubuğu|*Y**|
|**Dağılım**|Dağılım|*Y**|
| |DağılımConnectedByCurvesWithDataMarker|*Y**|
| |ScatterConnectedByCurvesWithoutDataMarker|*Y**|
| |ScatterConnectedByLinesWithDataMarker|*Y**|
| |ScatterConnectedByLinesWithoutDataMarker|*Y**|
|**Alan**|Alan|*Y**|
| |Yığılmış Alan|*Y**|
| |Alan100YığılmışYüzde|*Y**|
| |Alan3D|*Y**|
| |Alan3Dyığınlanmış|*Y**|
| |Alan3D100YığılmışYüzde|*Y**|
|**Tatlı çörek**|Tatlı çörek|*Y**|
| |DonutPatladı|*Y**|
|**Radar**|Radar|*Y**|
| |RadarWithDataMarkers|*Y**|
| |Radar Dolu|*Y**|
|**Yüzey**|Yüzey3D|N|
| |SurfaceWireframe3D|N|
| |Yüzey Konturu|N|
| |Yüzey Kontur Tel Kafes|N|
|**kabarcık**|kabarcık|*Y**|
| |Bubble3D|N|
|**Stoklamak**|StokYüksekDüşükKapat|*Y**|
| |StokAçıkYüksekDüşükKapat|*Y**|
| |StokHacimYüksekDüşükKapat|*Y**|
| |Stok HacmiAçıkYüksekDüşükKapalı|*Y**|
|**silindir**|silindir|*Y**|
| |Silindir Yığılmış|*Y**|
| |Cylinder100PercentYığılmış|*Y**|
| |Silindirik Çubuk|*Y**|
| |Silindirik ÇubukYığılmış|*Y**|
| |SilindirikÇubukYüzde100Yığılmış|*Y**|
| |Silindirik Sütun3D|*Y**|
|**koni**|koni|*Y**|
| |koni yığılmış|*Y**|
| |Koni100YüzdeYığılmış|*Y**|
| |Konik Çubuk|*Y**|
| |Konik ÇubukYığılmış|*Y**|
| |ConicalBar100PercentYığılmış|*Y**|
| |Konik Sütun3D|*Y**|
|**Piramit**|Piramit|*Y**|
| |PiramitYığılmış|*Y**|
| |Piramit100YüzdeYığılmış|*Y**|
| |PiramitBar|*Y**|
| |PiramitÇubuğuYığılmış|*Y**|
| |PiramitBar100PercentYığınlanmış|*Y**|
| |PiramitSütun3D|*Y**|
|**KutuBıyık**|KutuBıyık|Y|
|**Huni**|Huni|*Y**|
|**ParetoLine**|ParetoLine|*Y**|
|**güneş patlaması**|güneş patlaması|*Y**|
|**ağaç haritası**|ağaç haritası|*Y**|
|**Şelale**|Şelale|*Y**|
|**histogram**|histogram|Y|
|**Harita**|Harita|*N**|

{{% alert color="primary" %}}

Desteklenmeyen grafik türlerini resim veya PDF'e dönüştürmeye çalışırsanız, 0 boyutlu resimler veya boş PDF ile sonuçlanabilirsiniz.

{{% /alert %}}

##  **ileri konular**
- [Grafiği PDF'e Dönüştür](/cells/tr/net/chart-to-pdf/)
