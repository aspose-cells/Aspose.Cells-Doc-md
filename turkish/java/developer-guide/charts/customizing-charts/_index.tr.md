---
title: Grafikleri Özelleştirme
type: docs
weight: 15
url: /tr/java/creating-and-customizing-charts/
---
## **Grafik Oluşturma**

Aspose.Cells ile elektronik tablolara çeşitli grafikler eklemek mümkündür. Aspose.Cells birçok esnek grafik nesnesi sağlar. Bu konu, Aspose.Cells' grafik nesnelerini ele almaktadır.

### **Basitçe Grafik Oluşturma**

Aşağıdaki örnek kodlarla Aspose.Cells ile bir grafik oluşturmak basittir:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **Grafik Oluşturmak İçin Bilmeniz Gerekenler**

Grafikleri oluşturmadan önce, Aspose.Cells'i kullanarak grafikler oluştururken yardımcı olan bazı temel kavramları anlamak önemlidir.

#### **Grafik Nesneleri**

 Aspose.Cells, her türlü grafiği oluşturmak için kullanılan özel bir sınıf seti sağlar. Bu sınıflar oluşturmak için kullanılır.**grafik nesneleri**, grafik yapı taşları olarak işlev görür. Grafik nesneleri aşağıda listelenmiştir:

- [**eksen**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), bir grafiğin ekseni.
- [**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), tek bir Excel grafiği.
- [**Harita Alanı**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), çalışma sayfasındaki grafik alanı.
- [**Grafik Veri Tablosu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), bir grafik veri tablosu.
- [**Grafik Çerçevesi**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), grafikteki çerçeve nesnesi.
- [**Harita Noktası**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), grafikteki bir dizideki tek bir nokta.
- [**Harita Noktası Toplama**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection), bir dizideki tüm noktaları içeren bir koleksiyon.
- [**Grafik Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) , koleksiyonu[**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)nesneler.
-  DataLabels, belirtilen için DataLabels[**Diziler**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**Harita Noktası**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**trend çizgisi**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), vb.
- [**Doldurma Biçimi**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat), bir şekil için dolgu biçimi.
- [**Zemin**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor), bir 3B grafiğin zemini.
- [**Efsane**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend), grafik efsanesi.
- [**Astar**](https://reference.aspose.com/cells/java/com.aspose.cells/Line), grafik çizgisi.
- [**Seri Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) , koleksiyonu[**Diziler**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)nesneler.
- [**Diziler**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), grafikteki tek bir veri serisini temsil eder.
- [**TikEtiketler**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels), bir grafik eksenindeki değer işaretleriyle ilişkili onay işareti etiketleri.
- [**Başlık**](https://reference.aspose.com/cells/java/com.aspose.cells/Title), grafiğin veya eksenin başlığı.
- [**trend çizgisi**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline), grafikte bir eğilim çizgisi.
- [**TrendlineKoleksiyon**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection), belirtilen veri serisi için tüm Trendline nesnelerinin bir koleksiyonu.
- [**Duvarlar**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls), bir 3B grafiğin duvarları.

#### **Grafik Nesnelerini Kullanma**

Yukarıda bahsedildiği gibi, tüm grafik oluşturma nesneleri ilgili sınıflarının örnekleridir ve belirli görevleri gerçekleştirmek için belirli özellikler ve yöntemler sağlar. Grafikler oluşturmak için grafik nesnelerini kullanın.

kullanarak bir çalışma sayfasına herhangi bir grafik türü ekleyin.[**Grafik Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) Toplamak. İçindeki her öğe[**Grafik Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) koleksiyon temsil eder[**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) nesne. A[**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)nesne, grafiğin görünümünü özelleştirmek için gereken tüm Grafik Nesnelerini içine alır. Bir sonraki bölüm, basit bir grafik oluşturmak için birkaç temel grafik nesnesinin nasıl kullanılacağını gösterir.

### **Basit Grafik Oluşturma**

 Aspose.Cells ile birçok farklı türde grafik oluşturmak mümkündür. Aspose.Cells tarafından desteklenen tüm standart grafikler, adlı bir numaralandırmada önceden tanımlanmıştır.[**Grafik türü**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType). Önceden tanımlanmış grafik türleri şunlardır:

|**Grafik Türleri**|**Tanım**|
|:- |:- |
|Kolon|Kümelenmiş Sütun Grafiğini Temsil Eder|
|SütunYığılmış|Yığılmış Sütun Grafiğini Temsil Eder|
|Sütun100YığılmışYüzde|%100 Yığılmış Sütun Grafiğini Temsil Eder|
|Sütun3Dkümelenmiş|3B Kümelenmiş Sütun Grafiğini Temsil Eder|
|Sütun3DSığılmış|3B Yığılmış Sütun Grafiğini Temsil Eder|
|Sütun3D100YığılmışYüzde|3B %100 Yığılmış Sütun Grafiğini Temsil Eder|
|Sütun3D|3B Sütun Grafiğini Temsil Eder|
|Çubuk|Kümelenmiş Çubuk Grafiği Temsil Eder|
|Çubuk Yığılmış|Yığılmış Çubuk Grafiği Temsil Eder|
|Bar100YığılmışYüzde|%100 Yığılmış Çubuk Grafiği Temsil Eder|
|Bar3Dkümelenmiş|3B Kümelenmiş Çubuk Grafiği Temsil Eder|
|Bar3DSyığılmış|3B Yığılmış Çubuk Grafiği Temsil Eder|
|Bar3D100YığılmışYüzde|3B %100 Yığılmış Çubuk Grafiği Temsil Eder|
|Astar|Çizgi Grafiği Temsil Eder|
|Sıra Yığılmış|Yığılmış Çizgi Grafiğini Temsil Eder|
|Line100PercentYığılmış|%100 Yığılmış Çizgi Grafiği Temsil Eder|
|LineWithDataMarkers|Veri işaretçileri ile Çizgi Grafiği temsil eder|
|LineStackedWithDataMarkers|Veri işaretçileriyle Yığılmış Çizgi Grafiği temsil eder|
|Line100PercentStackedWithDataMarkers|Veri işaretçileri ile %100 Yığılmış Çizgi Grafiğini temsil eder|
|Çizgi3D|3B Çizgi Grafiği Temsil Eder|
|Turta|Pasta grafiğini temsil eder|
|Pasta3D|3B Pasta Grafiği Temsil Eder|
|Turta Turtası|Pasta Grafiğinin Pastasını Temsil Eder|
|PastaPatladı|Patlatılmış Pasta Grafiğini Temsil Eder|
|Pie3DEpatladı|3B Patlatılmış Pasta Grafiği Temsil Eder|
|pasta çubuğu|Pasta Grafiği Çubuğunu Temsil Eder|
|Dağılım|Dağılım Tablosunu Temsil Eder|
|DağılımConnectedByCurvesWithDataMarker|Veri işaretçileri ile eğrilerle bağlanan Dağılım Grafiği'ni temsil eder|
|ScatterConnectedByCurvesWithoutDataMarker|Veri işaretçileri olmadan eğrilerle bağlanan Dağılım Grafiği'ni temsil eder|
|ScatterConnectedByLinesWithDataMarker|Veri işaretçileri ile çizgilerle bağlanan Dağılım Grafiğini temsil eder|
|ScatterConnectedByLinesWithoutDataMarker|Veri işaretçileri olmadan çizgilerle bağlanmış Dağılım Grafiğini temsil eder|
|Alan|Alan Grafiğini Temsil Eder|
|Yığılmış Alan|Yığılmış Alan Grafiğini Temsil Eder|
|Alan100YığılmışYüzde|%100 Yığılmış Alan Grafiğini Temsil Eder|
|Alan3D|3D Alan Grafiğini Temsil Eder|
|Alan3Dyığınlanmış|3B Yığılmış Alan Grafiğini Temsil Eder|
|Alan3D100YığılmışYüzde|3D %100 Yığılmış Alan Tablosunu Temsil Eder|
|Tatlı çörek|Halka Grafiğini Temsil Eder|
|DonutPatladı|Patlatılmış Halka Grafiğini Temsil Eder|
|Radar|Radar Tablosunu Temsil Eder|
|RadarWithDataMarkers|Radar Tablosunu veri işaretçileriyle temsil eder|
|Radar Dolu|Dolu Radar Grafiğini Temsil Eder|
|Yüzey3D|3D Yüzey Grafiğini Temsil Eder|
|SurfaceWireframe3D|Tel Kafes 3B Yüzey Grafiğini Temsil Eder|
|Yüzey Konturu|Kontur Grafiğini Temsil Eder|
|Yüzey Kontur Tel Kafes|Tel Kafes Kontur Grafiğini Temsil Eder|
|kabarcık|Kabarcık Tablosunu Temsil Eder|
|Bubble3D|3D Kabarcık Tablosunu Temsil Eder|
|silindir|Silindir Grafiğini Temsil Eder|
|Silindir Yığılmış|Yığılmış Silindir Grafiğini Temsil Eder|
|Cylinder100PercentYığılmış|%100 İstiflenmiş Silindir Grafiğini Temsil Eder|
|Silindirik Çubuk|Silindirik Çubuk Grafiği Temsil Eder.|
|Silindirik ÇubukYığılmış|Yığılmış Silindirik Çubuk Grafiği Temsil Eder|
|SilindirikÇubukYüzde100Yığılmış|%100 Yığılmış Silindirik Çubuk Grafiği Temsil Eder|
|Silindirik Sütun3D|3B Silindirik Sütun Grafiğini Temsil Eder|
|koni|Koni Grafiğini Temsil Eder|
|koni yığılmış|Yığılmış Koni Grafiğini Temsil Eder|
|Koni100YüzdeYığılmış|%100 Yığılmış Koni Grafiğini Temsil Eder|
|Konik Çubuk|Konik Çubuk Grafiğini Temsil Eder|
|Konik ÇubukYığılmış|Yığılmış Konik Çubuk Grafiğini Temsil Eder|
|ConicalBar100PercentYığılmış|%100 Yığılmış Konik Çubuk Grafiği Temsil Eder|
|Konik Sütun3D|3B Konik Sütun Grafiğini Temsil Eder|
|Piramit|Piramit Grafiğini Temsil Eder|
|PiramitYığılmış|Yığılmış Piramit Grafiğini Temsil Eder|
|Piramit100YüzdeYığılmış|%100 Yığılmış Piramit Grafiğini Temsil Eder|
|PiramitBar|Piramit Çubuk Grafiğini Temsil Eder|
|PiramitÇubuğuYığılmış|Yığılmış Piramit Çubuk Grafiğini Temsil Eder|
|PiramitBar100PercentYığınlanmış|%100 Yığılmış Piramit Çubuk Grafiğini Temsil Eder|
|PiramitSütun3D|3B Piramit Sütun Grafiğini Temsil Eder|
Aspose.Cells'i kullanarak bir grafik oluşturmak için:

1.  ile çalışma sayfası hücrelerine bazı veriler ekleyin.[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) nesnenin[**değer ayarla**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value)yöntem.
 Bu, grafiğin veri kaynağı olarak kullanılacaktır.
1.  Çağırarak çalışma sayfasına bir grafik ekleyin.[**Grafik Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) koleksiyonun[*Ekle*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add(int,%20int,%20int,%20int,%20int) ) yöntemi, kapsüllenmiş[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)nesne.
1.  ile grafiğin türünü belirtin.[**Grafik türü**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)numaralandırma.
 Örneğin, örnek kullanır[**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID)grafik türü olarak değer.
1.  Yeniye erişin[**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) gelen nesne[**Grafik Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection)indeksini geçerek koleksiyon.
1.  Kapsüllenmiş grafik nesnelerinden herhangi birini kullanın.[**Çizelge**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart)grafiği yönetmek için nesne.
 Aşağıdaki örnek,[**Seri Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)grafiğin veri kaynağını belirtmek için grafik nesnesi.

Grafiğe kaynak verileri eklerken, veri kaynağı bir hücre aralığı ("A1:C3" gibi) veya bitişik olmayan bir hücre dizisi ("A1, A3, A5" gibi) veya bir dizi olabilir. değerler ("1,2,3" gibi).

{{% alert color="primary" %}}

Veri kaynağı olarak bir hücre aralığı atadığınızda, aralığı yalnızca sol üstten sağ alta ayarlayabilirsiniz. Örneğin, "A1:C3" geçerlidir, "C3:A1" geçersizdir.

{{% /alert %}}

Bu genel adımlar, herhangi bir türde grafik oluşturmanıza olanak tanır. Farklı grafikler oluşturmak için farklı grafik nesneleri kullanın.

Örnek kod yürütüldüğünde, çalışma sayfasına aşağıda gösterildiği gibi bir piramit grafiği eklenir.

**Veri kaynağıyla birlikte piramit grafiği**

![yapılacaklar:resim_alternatif_Metin](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

 Balon grafiği oluşturmak için,[**Grafik türü**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)olarak ayarlanması gerekir[**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE)ve BubbleSizes, Values & XValues gibi birkaç ekstra özelliğin buna göre ayarlanması gerekir. Aşağıdaki kodu çalıştırdıktan sonra, çalışma sayfasına aşağıda gösterildiği gibi bir balon grafiği eklenir.

**Veri kaynağıyla birlikte balon grafiği**

![yapılacaklar:resim_alternatif_Metin](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **Veri İşareti Grafiği ile Çizgi**

Veri işaretleyici grafiğiyle bir çizgi oluşturmak için,[**Grafik türü**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType)olarak ayarlanması gerekir[**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE_WITH_DATA_MARKERS) ve arka plan alanı, Seri İşaretleyiciler, Değerler ve XValues gibi birkaç ekstra özelliğin buna göre ayarlanması gerekir. Aşağıdaki kodu çalıştırdıktan sonra, çalışma sayfasına veri işaretçi grafiği içeren bir satır eklenir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **Özel Grafikler Oluşturma**

Şimdiye kadar grafikleri tartıştığımızda, standart biçimlendirme ayarlarına sahip standart grafiklere baktık. Yalnızca veri kaynağını tanımlarız, birkaç özellik ayarlarız ve grafik, varsayılan biçim ayarlarıyla oluşturulur. Ancak Aspose.Cells, geliştiricilerin kendi format ayarlarıyla grafikler oluşturmasına olanak tanıyan özel grafikler oluşturmayı da destekler.

### **Özel Grafikler Oluşturma**

Geliştiriciler, Aspose.Cells basit API'i kullanarak çalışma zamanında özel grafikler oluşturabilir.

 Grafik, bir veri serisinden oluşur. Aspose.Cells'deki her veri serisi, bir[**Diziler**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) nesne oysa[**Seri Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) nesne koleksiyonu olarak hizmet eder[**Diziler**](https://reference.aspose.com/cells/java/com.aspose.cells/Series)nesneler. Özel bir grafik oluştururken, geliştiriciler farklı veri serileri için farklı türde grafikler kullanma özgürlüğüne sahiptir (bir[**Seri Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection)nesne).

{{% alert color="primary" %}}

 Şu anda Aspose.Cells yalnızca pasta, çizgi, sütun ve sütun yığını grafiklerini birleştiren özel grafikleri destekler, ancak gelecek sürümlerde daha fazla grafik desteklenecektir. Aspose.Cells'in desteklediği standart çizelgelerin tam listesi için şurayı okuyun:[Grafik Türleri](/cells/tr/java/chart-types/) makale.

{{% /alert %}}

Aşağıdaki örnek kod, özel grafiklerin nasıl oluşturulacağını gösterir. Bu örnekte, birinci veri serisi için bir sütun grafiği ve ikinci seri için bir çizgi grafiği kullanacağız. Sonuç olarak, çalışma sayfasına bir çizgi grafiğiyle birlikte bir sütun grafiği ekliyoruz.

**Sütun ve çizgi grafiklerini birleştiren özel grafik**

![yapılacaklar:resim_alternatif_Metin](creating-and-customizing-charts_3.png)

**Programlama Örneği**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Desteklenen grafik türlerinin listesini görmek için[Grafik Türleri](/cells/tr/java/chart-types/) makale.

{{% /alert %}}

