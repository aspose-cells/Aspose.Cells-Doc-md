---
title: Grafik Oluşturun ve Yönetin
description: Microsoft Excel'de grafikler oluşturmak için Aspose.Cells for .NET'i nasıl kullanacağınızı öğrenin. Kılavuzumuz, oluşturulabilecek farklı grafik türlerinin yanı sıra bunların görünüm ve biçimlendirmelerinin nasıl özelleştirileceğini de gösterecektir.
keywords: Aspose.Cells for .NET, Chart Creation, Microsoft Excel, Chart Types, Customization, Appearance, Formatting.
linktitle: Grafikler
type: docs
weight: 130
url: /tr/net/creating-charts/
description: Excel için CSharp'ta ve ODS dosyalarında bir grafik oluşturun.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

Aspose.Cells ile elektronik tablolara çeşitli grafikler eklemek mümkündür. Aspose.Cells, birçok esnek grafik nesnesi sağlar. Bu konu Aspose.Cells' grafik nesnelerini ele almaktadır.

{{% /alert %}}

##  **Grafik Oluşturma**

###  **Basitçe Grafik Oluşturma**
Aşağıdaki örnek kodlarla Aspose.Cells ile bir grafik oluşturmak kolaydır:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

###  **Grafik Oluştururken Bilinmesi Gerekenler**

Grafik oluşturmadan önce, Aspose.Cells'i kullanarak grafik oluştururken yardımcı olacak bazı temel kavramları anlamak önemlidir.

####  **Grafik Nesneleri**

 Aspose.Cells, özel bir sınıf seti sağlar.[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts)Aspose.Cells tarafından desteklenen grafikleri oluşturmak için kullanılan ad alanı. Bu sınıflar, grafiğin yapı taşları olarak görev yapan *grafik nesneleri** oluşturmak için kullanılır. Grafik nesneleri aşağıda listelenmiştir:

- Seriler, bir grafikteki tek bir veri serisi.
- Eksen, bir grafiğin ekseni.
- Grafik, tek bir Excel grafiği.
- ChartArea, çalışma sayfasındaki grafik alanı.
- ChartDataTable, bir grafik veri tablosu.
- ChartFrame, grafikteki çerçeve nesnesi.
- ChartPoint, bir grafikteki serideki tek nokta.
- ChartPointCollection, tek bir serideki tüm noktaları içeren bir koleksiyon.
- Charts, Chart nesnelerinin bir koleksiyonudur.
- DataLabels, belirtilen seriye ait tüm DataLabel nesnelerinin koleksiyonudur.
- FillFormat, bir şeklin doldurma biçimi.
- Zemin, 3 boyutlu bir grafiğin zemini.
- Efsane, grafik efsanesi.
- Çizgi, grafik çizgisi.
- SeriesCollection, Series nesnelerinin bir koleksiyonudur.
- TickLabels, grafik eksenindeki onay işaretleriyle ilişkili onay işareti etiketleri.
- Başlık, bir grafiğin veya eksenin başlığı.
- Trend çizgisi, grafikteki trend çizgisi.
- TrendlineCollection, belirtilen veri serisi için tüm Trendline nesnelerinin bir koleksiyonudur.
- Duvarlar, 3 boyutlu bir grafiğin duvarları.

####  **Grafik Nesnelerini Kullanma**

Yukarıda belirtildiği gibi, tüm grafik nesneleri kendi sınıflarının örnekleridir ve belirli görevleri gerçekleştirmek için belirli özellikler ve yöntemler sağlar. Grafikler oluşturmak için grafik nesnelerini kullanın.

 kullanarak herhangi bir grafik türünü çalışma sayfasına ekleyin.[**Grafikler**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) Toplamak. İçindeki her öğe[**Grafikler**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) koleksiyon bir temsil eder[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) nesne. A[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)nesne, grafiğin görünümünü özelleştirmek için gereken diğer tüm grafik nesnelerini kapsar. Bir sonraki bölümde basit bir grafik oluşturmak için birkaç temel grafik nesnesinin nasıl kullanılacağı gösterilmektedir.

###  **Aspose.Cells'i Kullanarak Grafik Oluşturun**

**Adımlar:**

1. Çalışma sayfası hücrelerine bazı verileri şununla ekleyin:[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) nesnenin[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)yöntem.
 Bu, grafiğin veri kaynağı olarak kullanılacaktır.
1.  çağırarak çalışma sayfasına bir grafik ekleyin.[**Grafikler**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) Koleksiyonun[**Eklemek**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) yöntemi, kapsüllenmiş[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)nesne.
1.  Grafiğin türünü şununla belirtin:[**Grafik tipi**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)numaralandırma.
 Örneğin, aşağıdaki örnekte[**ChartType.Pyramid**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)grafik türü olarak değer.
1.  Yeniye erişin[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) gelen nesne[**Grafikler**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)indeksini geçerek koleksiyon.
1.  Kapsüllenmiş grafik nesnelerinden herhangi birini kullanın.[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)Grafiği yönetmek için nesne.
 Aşağıdaki örnek şunu kullanır:[**SeriKoleksiyon**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)Grafiğin veri kaynağını belirtmek için grafik nesnesi.

Grafiğe kaynak verileri eklerken, veri kaynağı bir hücre aralığı ("A1:C3" gibi), veya bitişik olmayan hücrelerin bir dizisi ("A1, A3, A5" gibi) veya bir hücre dizisi olabilir. değerler ("1,2,3" gibi).

Bu genel adımlar her türde grafik oluşturmanıza olanak tanır. Farklı grafikler oluşturmak için farklı grafik nesneleri kullanın.

Aspose.Cells ile birçok farklı türde grafik oluşturmak mümkündür. Aspose.Cells tarafından desteklenen tüm standart grafikler, adlı bir numaralandırmada önceden tanımlanmıştır.[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

Önceden tanımlanmış grafik türleri şunlardır:

|**Grafik Türleri**|**Tanım**|
| :- | :- |
|Kolon|Kümelenmiş Sütun Grafiği'ni temsil eder|
|SütunYığılmış|Yığılmış Sütun Grafiği temsil eder|
|SütunYüzde100Yığılmış|%100 Yığılmış Sütun Grafiği temsil eder|
|Sütun3DKümelenmiş|3B Kümelenmiş Sütun Grafiği'ni temsil eder|
|Sütun3DSığılmış|3B Yığılmış Sütun Grafiği temsil eder|
|Sütun3D100YüzdeYığınlanmış|3D %100 Yığılmış Sütun Grafiği temsil eder|
|Sütun3D|3B Sütun Grafiği'ni temsil eder|
|Çubuk|Kümelenmiş Çubuk Grafiği temsil eder|
|BarYığılmış|Yığılmış Çubuk Grafiği temsil eder|
|Bar100PercentYığılmış|%100 Yığılmış Çubuk Grafiği temsil eder|
|Bar3DKümelenmiş|3B Kümelenmiş Çubuk Grafiği temsil eder|
|Bar3DSığılmış|3B Yığılmış Çubuk Grafiği temsil eder|
|Bar3D100YüzdeYığınlanmış|3D %100 Yığılmış Çubuk Grafiği temsil eder|
|Astar|Çizgi Grafiğini temsil eder|
|HatYığılmış|Yığılmış Çizgi Grafiği temsil eder|
|Line100PercentYığılmış|%100 Yığılmış Çizgi Grafiğini temsil eder|
|LineWithDataMarkers|Çizgi Grafiğini veri işaretçileriyle temsil eder|
|LineStackedWithDataMarkers|Veri işaretçileriyle Yığılmış Çizgi Grafiğini temsil eder|
|Line100PercentStackedWithDataMarkers|Veri işaretçileriyle %100 Yığılmış Çizgi Grafiğini temsil eder|
|Hat3D|3D Çizgi Grafiğini temsil eder|
|Turta|Pasta Grafiğini temsil eder|
|Pasta3D|3D Pasta Grafiğini temsil eder|
|TurtaPasta|Pasta Grafiği Pastasını temsil eder|
|Pasta Patladı|Patlatılmış Pasta Grafiği'ni temsil eder|
|Pie3DEpatladı|3B Patlatılmış Pasta Grafiği'ni temsil eder|
|Pasta Barı|Pasta Grafiği Çubuğu'nu temsil eder|
|Dağılım|Dağılım Grafiği'ni temsil eder|
|ScatterConnectedByCurvesWithDataMarker|Veri işaretçileriyle eğrilerle birbirine bağlanan Dağılım Grafiği'ni temsil eder|
|ScatterConnectedByCurvesWithoutDataMarker|Veri işaretçileri olmadan, eğrilerle birbirine bağlanan Dağılım Grafiği'ni temsil eder|
|ScatterConnectedByLinesWithDataMarker|Veri işaretçileriyle çizgilerle birbirine bağlanan Dağılım Grafiği'ni temsil eder|
|ScatterConnectedByLinesWithoutDataMarker|Veri işaretçileri olmadan çizgilerle birbirine bağlanan Dağılım Grafiği'ni temsil eder|
|Alan|Alan Grafiğini temsil eder|
|AlanYığılmış|Yığılmış Alan Grafiğini Temsil Eder|
|Alan100YüzdeYığınlanmış|%100 Yığılmış Alan Grafiğini temsil eder|
|Alan3D|3D Alan Grafiğini temsil eder|
|Alan3Dyığılmış|3B Yığılmış Alan Grafiği'ni temsil eder|
|Alan3D100YüzdeYığınlanmış|3D %100 Yığılmış Alan Grafiğini temsil eder|
|Tatlı çörek|Halka Tablosunu temsil eder|
|DonutPatladı|Patlatılmış Halka Tablosunu Temsil Eder|
|Radar|Radar Grafiği'ni temsil eder|
|RadarWithDataMarkers|Veri işaretçileriyle Radar Grafiği'ni temsil eder|
|RadarDolu|Dolu Radar Grafiği'ni temsil eder|
|Yüzey3D|3D Yüzey Grafiğini temsil eder|
|Yüzey Tel Çerçeve3D|Tel Çerçeve 3D Yüzey Grafiği'ni temsil eder|
|YüzeyKontur|Kontur Grafiği'ni temsil eder|
|YüzeyKonturTel Çerçeve|Tel Çerçeve Kontur Grafiği'ni temsil eder|
|Kabarcık|Kabarcık Grafiği'ni temsil eder|
|Kabarcık3D|3D Kabarcık Grafiğini temsil eder|
|Silindir|Silindir Tablosunu temsil eder|
|SilindirYığılmış|Yığılmış Silindir Tablosunu Temsil Eder|
|SilindirYüzde100Yığılmış|%100 Yığılmış Silindir Tablosunu temsil eder|
|SilindirikBar|Silindirik Çubuk Grafiği temsil eder.|
|SilindirikBarYığılmış|Yığılmış Silindirik Çubuk Grafiği temsil eder|
|SilindirikBar100PercentYığılmış|%100 Yığılmış Silindirik Çubuk Grafiği temsil eder|
|Silindirik Sütun3D|3B Silindirik Sütun Grafiği'ni temsil eder|
|Koni|Koni Grafiği temsil eder|
|KoniYığılmış|Yığılmış Koni Grafiği temsil eder|
|KoniYüzde100Yığılmış|%100 Yığılmış Koni Grafiği temsil eder|
|KonikBar|Konik Çubuk Grafiği temsil eder|
|KonikBarYığılmış|Yığılmış Konik Çubuk Grafiği temsil eder|
|KonikBar100YüzdeYığınlanmış|%100 Yığılmış Konik Çubuk Grafiği temsil eder|
|Konik Sütun3D|3D Konik Sütun Grafiği'ni temsil eder|
|Piramit|Piramit Grafiği temsil eder|
|PiramitYığılmış|Yığılmış Piramit Grafiği Temsil Edilir|
|PiramitYüzde100Yığılmış|%100 Yığılmış Piramit Grafiği temsil eder|
|PiramitBar|Piramit Çubuk Grafiği temsil eder|
|PiramitBarYığılmış|Yığılmış Piramit Çubuk Grafiği temsil eder|
|PiramitBar100YüzdeYığınlanmış|%100 Yığılmış Piramit Çubuk Grafiği temsil eder|
|PiramitSütun3D|3D Piramit Sütun Grafiği'ni temsil eder|
{{% alert color="primary" %}}

Veri kaynağı olarak bir hücre aralığı atadığınızda aralığı yalnızca sol üstten sağ alta kadar ayarlayabilirsiniz. Örneğin, "A1:C3" geçerlidir, "C3:A1" ise geçersizdir.

{{% /alert %}}

####  **Piramit Grafiği**

Örnek kod çalıştırıldığında çalışma sayfasına bir piramit grafiği eklenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

####  **Çizgi grafik**

 Yukarıdaki örnekte, yalnızca[**Grafik tipi**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) ile*Astar*çizgi grafiği oluşturur. Kaynağın tamamı aşağıda verilmiştir. kod yürütüldüğünde çalışma sayfasına bir çizgi grafik eklenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

####  **Kabarcık Grafiği**

 Kabarcık grafiği oluşturmak için[**Grafik tipi**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) olarak ayarlanması gerekiyor[**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)ve BubbleSizes, Values & XValues gibi birkaç ekstra özelliğin buna göre ayarlanması gerekir. Aşağıdaki kodu çalıştırdıktan sonra çalışma sayfasına bir kabarcık grafiği eklenir.

####  **Veri İşaretleyici Grafiği ile Çizgi**

 Veri işaretçisi grafiğiyle bir çizgi oluşturmak için,[**Grafik tipi**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)olarak ayarlanması gerekiyor*ChartType.LineWithDataMarkers*ve arka plan alanı, Seri İşaretleyicileri, Değerler ve XDeğerleri gibi birkaç ekstra özelliğin buna göre ayarlanması gerekir. Aşağıdaki kodun çalıştırılmasıyla çalışma sayfasına veri işaretçisi grafiğinin bulunduğu bir satır eklenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

##  **İleri konular**
- [Excel 2016 Grafiklerini Okuyun ve Değiştirin](/cells/tr/net/read-and-manipulate-excel-2016-charts/)
- [Excel Grafiklerinin Eksenlerini Yönetme](/cells/tr/net/chart-axes/)
- [Grafik Görünümünü Ayarlama](/cells/tr/net/setting-chart-appearance/)
- [Grafik Türleri](/cells/tr/net/chart-types/)
- [Grafikleri Özelleştirme](/cells/tr/net/customizing-charts/)
- [Grafiğin Veri kaynağını ayarlayın](/cells/tr/net/data-formatting-in-charts/)
- [Excel Grafiklerinin DataLabel'lerini Yönetme](/cells/tr/net/insert-datalabels-to-chart/)
- [Akıllı İşaretleyicileri İşleyerek Grafik Oluşturun](/cells/tr/net/generate-chart-by-processing-smart-markers/)
- [Grafiğin Çalışma Sayfasını Alın](/cells/tr/net/get-worksheet-of-the-chart/)
- [Excel Grafiklerinin Efsanesini Yönetme](/cells/tr/net/chart-legend/)
- [Konum Boyutunu ve Tasarımcı Tablosunu Yönetin](/cells/tr/net/manipulate-position-size-and-designer-chart/)
- [Lider Çizgilerle Pasta Grafiği Oluşturma](/cells/tr/net/creating-pie-chart-with-leader-lines/)
- [Grafiklerdeki Şekiller](/cells/tr/net/controls-in-charts/)
- [Excel Grafiklerinin Başlıklarını Yönetme](/cells/tr/net/chart-and-axis-titles/)
- [Grafik Oluşturma](/cells/tr/net/chart-rendering/)
- [Grafik Trend Çizgisinin Denklem Metnini Alma](/cells/tr/net/get-equation-text-of-chart-trendline/)
