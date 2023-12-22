---
title: Grafikten Görüntüye
description: Bir grafiği JPEG veya PNG gibi bir görüntü biçimine dönüştürmek için Aspose.Cells for .NET'i nasıl kullanacağınızı öğrenin. Kılavuzumuz, Microsoft Excel'den bir grafiğin nasıl dışa aktarılacağını ve daha sonra kullanmak ve değiştirmek üzere bağımsız bir görüntü olarak nasıl kaydedileceğini gösterecektir.
keywords: Aspose.Cells for .NET, Chart to Image, Microsoft Excel, Image Conversion, Export, Standalone Image.
linktitle: Grafikten Görüntüye
type: docs
weight: 46
url: /tr/net/chart-to-image/
---
##  **İşleme Grafikleri**

 Aspose.Cells API'ler, herhangi bir ek araç veya uygulama gerektirmeden Excel Grafiklerini görüntü formatlarına dönüştürmeyi destekler. Render desteği sağlamak amacıyla,[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) sınıf açığa çıktı[**Hayal etmek**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) Uygulama gereksinimlerine en iyi şekilde uyum sağlamak için çeşitli aşırı yüklemelere sahip yöntemler.

###  **Grafikleri Görsellere Dönüştürme**

[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) yöntem, basit ve gelişmiş oluşturmayı desteklemek için çok sayıda aşırı yüklemeye sahiptir. Uygulama gereksinimi grafiğin varsayılan boyutlarında oluşturulmasıysa,[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index)yöntem aşağıdaki gibidir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImage.cs" >}}

 Gelişmiş ayarlarla grafikleri görsellere dönüştürmek de mümkündür. Aspose.Cells API'ler aşırı yükleme sürümünü açığa çıkardı[**Chart.ToImage**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/toimage/index) örneğini kabul edebilecek bir yöntem[**Görüntü Veya Yazdırma Seçenekleri**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)çözünürlük, yumuşatma modu, görüntü formatı vb. gibi parametrelerin belirtilmesine izin verir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToImageWithAdvancedOptions.cs" >}}

##  **İşleme için Desteklenen Grafik Türleri**

 Şu anda oluşturma için desteklenmeyen birkaç grafik türü vardır. Bu tür grafik türleri şunları içerir:****Desteklenen bölümündeki N**** aşağıdaki tablonun sütunu.

|**Grafik tipi**|**Grafik alt türü**|**Destekleniyor**|
| :- | :- | :- |
|**Kolon**|Kolon|*Evet**|
| |SütunYığılmış|*Evet**|
| |SütunYüzde100Yığılmış|*Evet**|
| |Sütun3DKümelenmiş|*Evet**|
| |Sütun3DSığılmış|*Evet**|
| |Sütun3D100YüzdeYığınlanmış|*Evet**|
| |Sütun3D|*Evet**|
|**Çubuk**|Çubuk|*Evet**|
| |BarYığılmış|*Evet**|
| |Bar100PercentYığılmış|*Evet**|
| |Bar3DKümelenmiş|*Evet**|
| |Bar3DSığılmış|*Evet**|
| |Bar3D100YüzdeYığınlanmış|*Evet**|
|**Astar**|Astar|*Evet**|
| |HatYığılmış|*Evet**|
| |Line100PercentYığılmış|*Evet**|
| |LineWithDataMarkers|*Evet**|
| |LineStackedWithDataMarkers|*Evet**|
| |Line100PercentStackedWithDataMarkers|*Evet**|
| |Hat3D|*Evet**|
|**Turta**|Turta|*Evet**|
| |Pasta3D|*Evet**|
| |TurtaPasta|*Evet**|
| |Pasta Patladı|*Evet**|
| |Pie3DEpatladı|*Evet**|
| |Pasta Barı|*Evet**|
|**Dağılım**|Dağılım|*Evet**|
| |ScatterConnectedByCurvesWithDataMarker|*Evet**|
| |ScatterConnectedByCurvesWithoutDataMarker|*Evet**|
| |ScatterConnectedByLinesWithDataMarker|*Evet**|
| |ScatterConnectedByLinesWithoutDataMarker|*Evet**|
|**Alan**|Alan|*Evet**|
| |AlanYığılmış|*Evet**|
| |Alan100YüzdeYığınlanmış|*Evet**|
| |Alan3D|*Evet**|
| |Alan3Dyığılmış|*Evet**|
| |Alan3D100YüzdeYığınlanmış|*Evet**|
|**Tatlı çörek**|Tatlı çörek|*Evet**|
| |DonutPatladı|*Evet**|
|**Radar**|Radar|*Evet**|
| |RadarWithDataMarkers|*Evet**|
| |RadarDolu|*Evet**|
|**Yüzey**|Yüzey3D|N|
| |Yüzey Tel Çerçeve3D|N|
| |YüzeyKontur|N|
| |YüzeyKonturTel Çerçeve|N|
|**Kabarcık**|Kabarcık|*Evet**|
| |Kabarcık3D|N|
|**Stoklamak**|StokYüksekDüşükKapat|*Evet**|
| |HisseAçıkYüksekDüşükKapat|*Evet**|
| |Hisse HacmiYüksekDüşükKapat|*Evet**|
| |Hisse HacmiAçıkYüksekDüşükKapanış|*Evet**|
|**Silindir**|Silindir|*Evet**|
| |SilindirYığılmış|*Evet**|
| |SilindirYüzde100Yığılmış|*Evet**|
| |SilindirikBar|*Evet**|
| |SilindirikBarYığılmış|*Evet**|
| |SilindirikBar100PercentYığılmış|*Evet**|
| |Silindirik Sütun3D|*Evet**|
|**Koni**|Koni|*Evet**|
| |KoniYığılmış|*Evet**|
| |KoniYüzde100Yığılmış|*Evet**|
| |KonikBar|*Evet**|
| |KonikBarYığılmış|*Evet**|
| |KonikBar100YüzdeYığınlanmış|*Evet**|
| |Konik Sütun3D|*Evet**|
|**Piramit**|Piramit|*Evet**|
| |PiramitYığılmış|*Evet**|
| |PiramitYüzde100Yığılmış|*Evet**|
| |PiramitBar|*Evet**|
| |PiramitBarYığılmış|*Evet**|
| |PiramitBar100YüzdeYığınlanmış|*Evet**|
| |PiramitSütun3D|*Evet**|
|**Kutu Bıyık**|Kutu Bıyık|Y|
|**Huni**|Huni|*Evet**|
|**Pareto Hattı**|Pareto Hattı|*Evet**|
|**Güneş patlaması**|Güneş patlaması|*Evet**|
|**Ağaç haritası**|Ağaç haritası|*Evet**|
|**Şelale**|Şelale|*Evet**|
|**Histogram**|Histogram|Y|
|**Harita**|Harita|*N**|

{{% alert color="primary" %}}

Desteklenmeyen grafik türlerini görsele veya PDF'e dönüştürmeye çalışırsanız, 0 boyutlu görsellerle veya boş PDF ile karşılaşabilirsiniz.

{{% /alert %}}

##  **İleri konular**
- [Grafiği PDF'e dönüştür](/cells/tr/net/chart-to-pdf/)
