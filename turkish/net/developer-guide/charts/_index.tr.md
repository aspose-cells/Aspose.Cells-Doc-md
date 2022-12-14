---
title: Grafik Oluştur ve Yönet
linktitle: Grafikler
type: docs
weight: 130
url: /tr/net/creating-charts/
description: CSharp for Excel ve ODS dosyalarında bir grafik oluşturun.
keywords: create a chart, make a graph 
---
{{% alert color="primary" %}}

Aspose.Cells ile elektronik tablolara çeşitli grafikler eklemek mümkündür. Aspose.Cells birçok esnek grafik nesnesi sağlar. Bu konu, Aspose.Cells' grafik nesnelerini ele almaktadır.

{{% /alert %}}

## **Grafik Oluşturma**

### **Basitçe Grafik Oluşturma**
Aşağıdaki örnek kodlarla Aspose.Cells ile bir grafik oluşturmak basittir:
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateColumnChart-1.cs" >}}

### **Grafik Oluşturmak İçin Bilinmesi Gerekenler**

Grafikleri oluşturmadan önce, Aspose.Cells'i kullanarak grafikler oluştururken yardımcı olan bazı temel kavramları anlamak önemlidir.

#### **Grafik Nesneleri**

Aspose.Cells, özel bir dizi sınıf sağlar.[**Aspose.Cells.Charts**](https://reference.aspose.com/cells/net/aspose.cells.charts) Aspose.Cells tarafından desteklenen grafikleri oluşturmak için kullanılan ad alanı. Bu sınıflar, oluşturmak için kullanılır**grafik nesneleri**, grafik yapı taşları olarak işlev görür. Grafik nesneleri aşağıda listelenmiştir:

- Seri, grafikteki tek bir veri serisi.
- Eksen, bir grafiğin ekseni.
- Grafik, tek bir Excel grafiği.
- ChartArea, çalışma sayfasındaki grafik alanı.
- ChartDataTable, bir grafik veri tablosu.
- ChartFrame, bir grafikteki çerçeve nesnesi.
- ChartPoint, grafikteki bir dizideki tek nokta.
- ChartPointCollection, bir dizideki tüm noktaları içeren bir koleksiyon.
- Grafikler, Grafik nesnelerinin bir koleksiyonu.
- DataLabels, belirtilen seri için tüm DataLabel nesnelerinin koleksiyonu.
- FillFormat, bir şekil için dolgu formatı.
- Zemin, bir 3D grafiğin zemini.
- Efsane, grafik efsanesi.
- Çizgi, grafik çizgisi.
- SeriesCollection, Series nesnelerinden oluşan bir koleksiyon.
- TickLabels, bir grafik eksenindeki değer işaretleriyle ilişkili onay işareti etiketleri.
- Başlık, grafiğin veya eksenin başlığı.
- Eğilim çizgisi, grafikteki bir eğilim çizgisi.
- TrendlineCollection, belirtilen veri serisi için tüm Trendline nesnelerinin bir koleksiyonu.
- Duvarlar, bir 3D grafiğin duvarları.

#### **Grafik Nesnelerini Kullanma**

Yukarıda bahsedildiği gibi, tüm grafik oluşturma nesneleri ilgili sınıflarının örnekleridir ve belirli görevleri gerçekleştirmek için belirli özellikler ve yöntemler sağlar. Grafikler oluşturmak için grafik nesnelerini kullanın.

kullanarak bir çalışma sayfasına herhangi bir grafik türü ekleyin.[**Grafikler**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) Toplamak. İçindeki her öğe[**Grafikler**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/charts) koleksiyon temsil eder[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) nesne. A[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)nesne, grafiğin görünümünü özelleştirmek için gereken diğer tüm grafik oluşturma nesnelerini kapsar. Bir sonraki bölüm, basit bir grafik oluşturmak için birkaç temel grafik nesnesinin nasıl kullanılacağını gösterir.

### **Aspose.Cells Kullanarak Grafik Oluşturun**

**Adımlar:**

1.  ile çalışma sayfası hücrelerine bazı veriler ekleyin.[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) nesnenin[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index)yöntem.
 Bu, grafiğin veri kaynağı olarak kullanılacaktır.
1.  Çağırarak çalışma sayfasına bir grafik ekleyin.[**Grafikler**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection) koleksiyonun[**Ekle**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection/methods/add) kapsüllenmiş yöntem,[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)nesne.
1.  ile grafiğin türünü belirtin.[**Grafik türü**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)numaralandırma.
 Örneğin, aşağıdaki örnekte[**ChartType.Piramit**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)grafik türü olarak değer.
1.  Yeniye erişin[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart) gelen nesne[**Grafikler**](https://reference.aspose.com/cells/net/aspose.cells.charts/chartcollection)indeksini geçerek koleksiyon.
1.  Kapsüllenmiş grafik nesnelerinden herhangi birini kullanın.[**Çizelge**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart)grafiği yönetmek için nesne.
 Aşağıdaki örnek,[**Seri Koleksiyonu**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)grafiğin veri kaynağını belirtmek için grafik nesnesi.

Grafiğe kaynak verileri eklerken, veri kaynağı bir hücre aralığı ("A1:C3" gibi) veya bitişik olmayan bir hücre dizisi ("A1, A3, A5" gibi) veya bir dizi olabilir. değerler ("1,2,3" gibi).

Bu genel adımlar, herhangi bir türde grafik oluşturmanıza olanak sağlar. Farklı grafikler oluşturmak için farklı grafik nesneleri kullanın.

 Aspose.Cells ile birçok farklı türde grafik oluşturmak mümkündür. Aspose.Cells tarafından desteklenen tüm standart grafikler, adlı bir numaralandırmada önceden tanımlanmıştır.[**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype).

Önceden tanımlanmış grafik türleri şunlardır:

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
|DağılımConnectedByCurvesWithDataMarker|Veri işaretçileri ile eğrilerle bağlantılı Dağılım Grafiğini temsil eder|
|ScatterConnectedByCurvesWithoutDataMarker|Veri işaretleri olmadan, eğrilerle birbirine bağlı Dağılım Grafiğini temsil eder|
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
|Radar|Radar Grafiğini Temsil Eder|
|RadarWithDataMarkers|Veri işaretçileri ile Radar Grafiği temsil eder|
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
{{% alert color="primary" %}}

Veri kaynağı olarak bir hücre aralığı atadığınızda, aralığı yalnızca sol üstten sağ alta ayarlayabilirsiniz. Örneğin, "A1:C3" geçerlidir, "C3:A1" geçersizdir.

{{% /alert %}}

#### **Piramit Grafiği**

Örnek kod yürütüldüğünde, çalışma sayfasına bir piramit grafiği eklenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreatePyramidChart-1.cs" >}}

#### **Çizgi grafik**

 Yukarıdaki örnekte, basitçe değiştirmek[**Grafik türü**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) ile*Astar*bir çizgi grafiği oluşturur. Tam kaynak aşağıda verilmiştir. kod yürütüldüğünde, çalışma sayfasına bir çizgi grafik eklenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateLineChart-1.cs" >}}

#### **Kabarcık Grafiği**

 Balon grafiği oluşturmak için,[**Grafik türü**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype) olarak ayarlanması gerekir[**ChartType.Bubble**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)ve BubbleSizes, Values & XValues gibi birkaç ekstra özelliğin buna göre ayarlanması gerekir. Aşağıdaki kodu çalıştırdıktan sonra, çalışma sayfasına bir balon grafiği eklenir.

#### **Veri İşareti Grafiği ile Çizgi**

 Veri işaretleyici grafiği ile bir çizgi oluşturmak için,[**Grafik türü**](https://reference.aspose.com/cells/net/aspose.cells.charts/charttype)olarak ayarlanması gerekir*ChartType.LineWithDataMarkers*ve arka plan alanı, Seri İşaretleyiciler, Değerler ve XValues gibi birkaç ekstra özelliğin buna göre ayarlanması gerekir. Aşağıdaki kodu çalıştırdıktan sonra, çalışma sayfasına veri işaretçi grafiğini içeren bir satır eklenir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-CreateLineWithDataMarkerChart-1.cs" >}}

## **ileri konular**
- [Excel 2016 Grafiklerini Okuyun ve İşleyin](/cells/tr/net/read-and-manipulate-excel-2016-charts/)
- [Excel Grafiklerinin Eksenlerini Yönetin](/cells/tr/net/chart-axes/)
- [Ayar Tablosu Görünümü](/cells/tr/net/setting-chart-appearance/)
- [Grafik Türleri](/cells/tr/net/chart-types/)
- [Grafikleri Özelleştirme](/cells/tr/net/customizing-charts/)
- [Grafik için Veri kaynağını ayarla](/cells/tr/net/data-formatting-in-charts/)
- [Excel Grafiklerinin Veri Etiketlerini Yönetme](/cells/tr/net/insert-datalabels-to-chart/)
- [Akıllı İşaretleyicileri İşleyerek Grafik Oluşturun](/cells/tr/net/generate-chart-by-processing-smart-markers/)
- [Grafiğin Çalışma Sayfasını Alın](/cells/tr/net/get-worksheet-of-the-chart/)
- [Legend of Excel Charts'ı yönetin](/cells/tr/net/chart-legend/)
- [Pozisyon Boyutunu ve Tasarımcı Grafiğini İşleyin](/cells/tr/net/manipulate-position-size-and-designer-chart/)
- [Lider Çizgilerle Pasta Grafiği Oluşturma](/cells/tr/net/creating-pie-chart-with-leader-lines/)
- [Grafiklerdeki Şekiller](/cells/tr/net/controls-in-charts/)
- [Excel Grafiklerinin Başlıklarını Yönetin](/cells/tr/net/chart-and-axis-titles/)
- [Grafik Oluşturma](/cells/tr/net/chart-rendering/)
- [Grafik Eğilim Çizgisinin Denklem Metnini Alın](/cells/tr/net/get-equation-text-of-chart-trendline/)
