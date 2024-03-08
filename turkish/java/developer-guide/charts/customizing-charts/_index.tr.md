---
title: Grafikleri Özelleştirme
type: docs
weight: 15
url: /tr/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---
##  **Grafik Oluşturma**

Aspose.Cells ile elektronik tablolara çeşitli grafikler eklemek mümkündür. Aspose.Cells, birçok esnek grafik nesnesi sağlar. Bu konu Aspose.Cells' grafik nesnelerini ele almaktadır.

###  **Basitçe Grafik Oluşturma**

Aşağıdaki örnek kodlarla Aspose.Cells ile bir grafik oluşturmak kolaydır:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


###  **Grafik Oluşturmak İçin Bilinmesi Gerekenler**

Grafik oluşturmadan önce, Aspose.Cells'i kullanarak grafik oluştururken yardımcı olacak bazı temel kavramları anlamak önemlidir.

####  **Grafik Nesneleri**

Aspose.Cells, her türlü grafiği oluşturmak için kullanılan özel bir sınıf seti sağlar. Bu sınıflar, grafiğin yapı taşları olarak görev yapan *grafik nesneleri** oluşturmak için kullanılır. Grafik nesneleri aşağıda listelenmiştir:

- [**Eksen**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), bir grafiğin ekseni.
- [**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), tek bir Excel grafiği.
- [**GrafikAlan**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), çalışma sayfasındaki grafik alanı.
- [**GrafikVeriTablosu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), bir grafik veri tablosu.
- [**Grafik Çerçevesi**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), grafikteki çerçeve nesnesi.
- [**Harita Noktası**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), bir grafikteki serideki tek bir nokta.
- [**ChartPointKoleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), tek bir serideki tüm noktaları içeren bir koleksiyon.
- [**Grafik Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) , koleksiyonu[**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)nesneler.
-  DataLabels, belirtilenler için DataLabels[**Seri**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**Harita Noktası**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Trend çizgisi**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), vesaire.
- [**Doldurma Biçimi**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), bir şeklin biçimini doldurun.
- [**Zemin**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), 3 boyutlu bir grafiğin tabanı.
- [**Efsane**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), grafik efsanesi.
- [**Astar**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), grafik çizgisi.
- [**SeriKoleksiyon**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) , koleksiyonu[**Seri**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)nesneler.
- [**Seri**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)bir grafikteki tek bir veri serisini temsil eder.
- [**Onay Etiketleri**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), bir grafik eksenindeki onay işaretleriyle ilişkili onay işareti etiketleri.
- [**Başlık**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), bir grafiğin veya eksenin başlığı.
- [**Trend çizgisi**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), bir grafikteki eğilim çizgisi.
- [**Trend Çizgisi Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), belirtilen veri serisine ilişkin tüm Eğilim Çizgisi nesnelerinin bir koleksiyonu.
- [**Duvarlar**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), 3 boyutlu bir grafiğin duvarları.

####  **Grafik Nesnelerini Kullanma**

Yukarıda belirtildiği gibi, tüm grafik nesneleri kendi sınıflarının örnekleridir ve belirli görevleri gerçekleştirmek için belirli özellikler ve yöntemler sağlar. Grafikler oluşturmak için grafik nesnelerini kullanın.

 kullanarak herhangi bir grafik türünü çalışma sayfasına ekleyin.[**Grafik Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) Toplamak. İçindeki her öğe[**Grafik Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) koleksiyon bir temsil eder[**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) nesne. A[**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)nesne, grafiğin görünümünü özelleştirmek için gereken tüm Grafik Nesnelerini kapsar. Bir sonraki bölümde basit bir grafik oluşturmak için birkaç temel grafik nesnesinin nasıl kullanılacağı gösterilmektedir.

###  **Basit Grafik Oluşturma**

Aspose.Cells ile birçok farklı türde grafik oluşturmak mümkündür. Aspose.Cells tarafından desteklenen tüm standart grafikler, adlı bir numaralandırmada önceden tanımlanmıştır.[**Grafik tipi**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). Önceden tanımlanmış grafik türleri şunlardır:

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
|RadarWithDataMarkers|Radar Grafiği'ni veri işaretleyicileriyle temsil eder|
|RadarDolu|Dolu Radar Grafiği'ni temsil eder|
|Yüzey3D|3D Yüzey Grafiğini temsil eder|
|Yüzey Tel Çerçeve3D|Tel Çerçeve 3B Yüzey Grafiği'ni temsil eder|
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
|PiramitBar|Piramit Çubuk Grafiği'ni temsil eder|
|PiramitBarYığılmış|Yığılmış Piramit Çubuk Grafiği temsil eder|
|PiramitBar100YüzdeYığınlanmış|%100 Yığılmış Piramit Çubuk Grafiği temsil eder|
|PiramitSütun3D|3D Piramit Sütun Grafiği'ni temsil eder|
Aspose.Cells'i kullanarak bir grafik oluşturmak için:

1. Çalışma sayfası hücrelerine bazı verileri şununla ekleyin:[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) nesnenin[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)yöntem.
 Bu, grafiğin veri kaynağı olarak kullanılacaktır.
1.  çağırarak çalışma sayfasına bir grafik ekleyin.[**Grafik Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) Koleksiyonun[*eklemek*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) ) yöntemi, kapsüllenmiş[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)nesne.
1.  Grafiğin türünü şununla belirtin:[**Grafik tipi**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)numaralandırma.
 Örneğin, örnek şunu kullanır:[**ChartType.PİRAMİT**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)grafik türü olarak değer.
1.  Yeniye erişin[**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) gelen nesne[**Grafik Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)indeksini geçerek koleksiyon.
1.  Kapsüllenmiş grafik nesnelerinden herhangi birini kullanın.[**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)Grafiği yönetmek için nesne.
 Aşağıdaki örnek şunu kullanır:[**SeriKoleksiyon**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)Grafiğin veri kaynağını belirtmek için grafik nesnesi.

Grafiğe kaynak verileri eklerken, veri kaynağı bir hücre aralığı ("A1:C3" gibi), veya bitişik olmayan hücrelerin bir dizisi ("A1, A3, A5" gibi) veya bir hücre dizisi olabilir. değerler ("1,2,3" gibi).

{{% alert color="primary" %}}

Veri kaynağı olarak bir hücre aralığı atadığınızda aralığı yalnızca sol üstten sağ alta kadar ayarlayabilirsiniz. Örneğin, "A1:C3" geçerlidir, "C3:A1" ise geçersizdir.

{{% /alert %}}

Bu genel adımlar her türde grafik oluşturmanıza olanak tanır. Farklı grafikler oluşturmak için farklı grafik nesneleri kullanın.

Örnek kod çalıştırıldığında çalışma sayfasına aşağıda gösterildiği gibi bir piramit grafiği eklenir.

**Veri kaynağıyla birlikte piramit grafiği**

![yapılacak şey:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

Kabarcık grafiği oluşturmak için[**Grafik tipi**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)olarak ayarlanması gerekiyor[**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)ve BubbleSizes, Values & XValues gibi birkaç ekstra özelliğin buna göre ayarlanması gerekir. Aşağıdaki kodu çalıştırdıktan sonra çalışma sayfasına aşağıda gösterildiği gibi bir kabarcık grafiği eklenir.

**Veri kaynağıyla birlikte kabarcık grafiği**

![yapılacak şey:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

####  **Veri İşaretleyici Grafiği ile Çizgi**

Veri işaretçisi grafiğiyle bir çizgi oluşturmak için[**Grafik tipi**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)olarak ayarlanması gerekiyor[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) ve arka plan alanı, Seri İşaretleyicileri, Değerler ve XValues gibi birkaç ekstra özelliğin buna göre ayarlanması gerekir. Aşağıdaki kodun çalıştırılmasıyla çalışma sayfasına veri işaretçisi grafiğinin bulunduğu bir satır eklenir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

##  **Özel Grafikler Oluşturma**

Şu ana kadar grafikleri tartışırken, standart biçimlendirme ayarlarına sahip standart grafiklere baktık. Yalnızca veri kaynağını tanımlıyoruz, birkaç özelliği ayarlıyoruz ve grafik varsayılan format ayarlarıyla oluşturuluyor. Ancak Aspose.Cells, geliştiricilerin kendi format ayarlarıyla grafikler oluşturmasına olanak tanıyan özel grafikler oluşturmayı da destekler.

###  **Özel Grafikler Oluşturma**

Geliştiriciler, Aspose.Cells basit API'i kullanarak çalışma zamanında özel grafikler oluşturabilir.

 Bir grafik bir veri serisinden oluşur. Aspose.Cells'deki her veri serisi bir ile temsil edilir[**Seri**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) nesne ise[**SeriKoleksiyon**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) nesne bir koleksiyon görevi görür[**Seri**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)nesneler. Özel bir grafik oluştururken geliştiriciler, farklı veri serileri için (bir dosyada toplanan) farklı türde grafikler kullanma özgürlüğüne sahiptir.[**SeriKoleksiyon**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)nesne).

{{% alert color="primary" %}}

 Şu anda Aspose.Cells yalnızca pasta, çizgi, sütun ve sütun yığını grafiklerini birleştiren özel grafikleri desteklemektedir ancak gelecek sürümlerde daha fazla grafik desteklenecektir. Aspose.Cells'in desteklediği standart grafiklerin tam listesi için[Grafik Türleri](/cells/tr/java/chart-types/) madde.

{{% /alert %}}

Aşağıdaki örnek kod, özel grafiklerin nasıl oluşturulacağını gösterir. Bu örnekte ilk veri serisi için sütun grafiği, ikinci seri için ise çizgi grafiği kullanacağız. Sonuç olarak, çalışma sayfasına çizgi grafikle birleştirilmiş bir sütun grafiği ekliyoruz.

**Sütun ve çizgi grafiklerini birleştiren özel grafik**

![yapılacak şey:image_alt_text](creating-and-customizing-charts_3.png)

**Programlama Örneği**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Desteklenen grafik türlerinin listesini görmek için[Grafik Türleri](/cells/tr/java/chart-types/) madde.

{{% /alert %}}

