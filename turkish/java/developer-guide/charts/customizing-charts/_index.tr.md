---
title: Grafikleri Özelleştirme
type: docs
weight: 15
url: /tr/java/creating-and-customizing-charts/
alias: [/java/customizing-charts/]
---

## **Grafikler Oluşturma**

Aspose.Cells ile elektronik tablolara çeşitli grafikler eklemek mümkündür. Aspose.Cells çok esnek grafik nesneleri sağlar. Bu konu, Aspose.Cells'in grafik nesnelerini tartışmaktadır.

### **Basitçe bir Grafik Oluşturma**

Aspose.Cells ile bir grafik oluşturmak oldukça basittir, aşağıdaki örnek kodlar ile:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-Charts-ManipulateChart-HowToCreateColumnChart-1.java" >}}


### **Grafi̇k Oluşturma İçin Bilmeni̇z Gerekenler**

Grafik oluşturmadan önce, Aspose.Cells kullanarak grafik oluştururken faydalı bazı temel kavramları anlamanız önemlidir.

#### **Grafikleme Nesneleri**

Aspose.Cells, her türlü grafik oluşturmak için kullanılan özel bir sınıf kümesi sağlar. Bu sınıflar, tüm türde grafikler oluşturmak için kullanılır ve grafik oluşturma blokları olarak hareket eder. Grafik nesneleri aşağıda listelenmiştir:

- [**Axis**](https://reference.aspose.com/cells/java/com.aspose.cells/Axis), bir grafik eksenidir.
- [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart), tek bir Excel grafiği.
- [**ChartArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartArea), çalışma sayfasındaki grafik alanıdır.
- [**ChartDataTable**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartDataTable), grafik veri tablosudur.
- [**ChartFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartFrame), bir grafikte çerçeve nesnesidir.
- Bir grafikte bir serideki tek bir nokta olan [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint).
- Bir koleksiyon olan ve bir serideki tüm noktaları içeren [**ChartPointCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPointCollection).
- [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) nesnelerinin bir koleksiyonu olan [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection).
- Belirtilen [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series), [**ChartPoint**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartPoint), [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline) için DataLabels.
- Bir şeklin doldurma biçimi olan [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/FillFormat).
- 3D grafiğin zemini olan [**Floor**](https://reference.aspose.com/cells/java/com.aspose.cells/Floor).
- Grafik gösterimli olan [**Legend**](https://reference.aspose.com/cells/java/com.aspose.cells/Legend).
- Grafikteki çizgi olan [**Line**](https://reference.aspose.com/cells/java/com.aspose.cells/Line).
- [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) nesnelerinin bir koleksiyonu olan [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection).
- Bir grafikte tek bir veri serisini temsil eden [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series).
- Bir grafik eksenindeki çizgi işaretleri ile ilişkili olan [**TickLabels**](https://reference.aspose.com/cells/java/com.aspose.cells/TickLabels).
- Bir grafik veya eksenin başlığı olan [**Title**](https://reference.aspose.com/cells/java/com.aspose.cells/Title).
- Bir grafikteki trend çizgisi olan [**Trendline**](https://reference.aspose.com/cells/java/com.aspose.cells/Trendline).
- Belirtilen veri serisi için tüm Trendline nesnelerinin bir koleksiyonu olan [**TrendlineCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/TrendlineCollection).
- 3D grafik duvarları olan [**Walls**](https://reference.aspose.com/cells/java/com.aspose.cells/Walls).

#### **Grafik Nesneleri Kullanma**

Yukarıda belirtildiği gibi, tüm grafik nesneleri, ilgili sınıfların örnekleridir ve belirli görevleri yerine getirmek için belirli özellikler ve metotlar sağlar. Grafik nesnelerini kullanarak grafikler oluşturun.

Herhangi bir türdeki grafiği bir çalışma sayfasına [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) koleksiyonunu kullanarak ekleyin. [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) koleksiyonundaki her öğe bir [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) nesnesini temsil eder. Bir [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) nesnesi, grafiğin görünümünü özelleştirmek için gereken tüm Çizim Nesnelerini kapsar. Bir sonraki bölüm, basit bir grafik oluşturmak için birkaç temel çizim nesnesinin nasıl kullanılacağını gösterir.

### **Basit Bir Grafik Oluşturma**

Aspose.Cells ile birçok farklı grafik türü oluşturmak mümkündür. Aspose.Cells tarafından desteklenen tüm standart grafikler, [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) adında bir numaralama içeren önceden tanımlanmıştır. Önceden tanımlanmış grafik tipleri şunlardır:

|**Grafik Tipleri**|**Açıklama**|
| :- | :- |
|Column|Kümelenmiş Sütun Grafiğini Temsil Eder|
|ColumnStacked|Tasvir Yığılmış Sutun Grafiği|
|Column100PercentStacked|Tasvir 100% Yığılmış Sutun Grafiği|
|Column3DClustered|Tasvir 3D Küme Sutun Grafiği|
|Column3DStacked|Tasvir 3D Yığılmış Sutun Grafiği|
|Column3D100PercentStacked|Tasvir 3D 100% Yığılmış Sutun Grafiği|
|Column3D|Tasvir 3D Sutun Grafiği|
|Bar|Tasvir Kümeleme Çubuk Grafiği|
|BarStacked|Yığın Çubuk Grafiğini Temsil Eder|
|Bar100PercentStacked|100% Yığılmış Çubuk Grafiğini Temsil Eder|
|Bar3DClustered|3D Küme Çubuk Grafiğini Temsil Eder|
|Bar3DStacked|3D Yığılmış Çubuk Grafiğini Temsil Eder|
|Bar3D100PercentStacked|3D 100% Yığılmış Çubuk Grafiğini Temsil Eder|
|Line|Çizgi Grafiğini Temsil Eder|
|LineStacked|Yığılmış Çizgi Grafiğini Temsil Eder|
|Line100PercentStacked|100% Yığılmış Çizgi Grafiğini Temsil Eder|
|LineWithDataMarkers|Veri İşaretleri Bulunan Çizgi Grafiğini Temsil Eder|
|LineStackedWithDataMarkers|Veri İşaretleri Bulunan Yığılmış Çizgi Grafiğini Temsil Eder|
|Line100PercentStackedWithDataMarkers|100% Yığılmış Veri İşaretleri Bulunan Çizgi Grafiğini Temsil Eder|
|Line3D|3D Çizgi Grafiğini Temsil Eder|
|Pie|Pasta Grafiğini Temsil Eder|
|Pie3D|3D Pasta Grafiğini Temsil Eder|
|PiePie|Pasta Grafiğinde Pasta Temsil Eder|
|PieExploded|Patlamış Pasta Grafiğini Temsil Eder|
|Pie3DExploded|3D Patlamış Pasta Grafiğini Temsil Eder|
|PieBar|Pasta Grafiğinde Çubuk Temsil Eder|
|Scatter|Saçılma Grafiğini Temsil Eder|
|ScatterConnectedByCurvesWithDataMarker|Eğrilerle Bağlı Saçılma Grafiğini, Veri İşaretleriyle Temsil Eder|
|ScatterConnectedByCurvesWithoutDataMarker|Eğrilerle Bağlı Saçılma Grafiğini, Veri İşaretleri olmadan Temsil Eder|
|ScatterConnectedByLinesWithDataMarker|Çizgilerle Bağlı Saçılma Grafiğini, Veri İşaretleriyle Temsil Eder|
|ScatterConnectedByLinesWithoutDataMarker|Çizgilerle Bağlı Saçılma Grafiğini, Veri İşaretleri olmadan Temsil Eder|
|Area|Alan Grafiğini Temsil Eder|
|AreaStacked|Yığılmış Alan Grafiğini Temsil Eder|
|Area100PercentStacked|100% Yığılmış Alan Grafiğini Temsil Eder|
|Area3D|3D Alan Grafiğini Temsil Eder|
|Area3DStacked|3D Yığılmış Alan Grafiğini Temsil Eder|
|Area3D100PercentStacked|3D 100% Yığılmış Alan Grafiğini Temsil Eder|
|Doughnut|Donut Grafiğini Temsil Eder|
|DoughnutExploded|Exploded Doughnut Chartını Temsil Ediyor|
|Radar| Radar Grafiğini Temsil Eder|
|RadarWithDataMarkers| Veri İşaretleriyle Radar Grafiğini Temsil Eder|
|RadarFilled|Dolu Radar Grafiğini Temsil Ediyor|
|Surface3D|3 boyutlu Yüzey Grafiğini Temsil Ediyor|
|SurfaceWireframe3D| Tel Çerçeveli 3 Boyutlu Yüzey Grafiğini Temsil Eder|
|SurfaceContour|Kontur Grafiğini Temsil Ediyor|
|SurfaceContourWireframe|Tel Kafesli Kontur Grafiğini Temsil Ediyor|
|Bubble|Balon Grafiğini Temsil Ediyor|
|Bubble3D|3 Boyutlu Balon Grafiğini Temsil Ediyor|
|Cylinder|Silindir Grafiğini Temsil Ediyor|
|CylinderStacked|Yığılmış Silindir Grafiğini Temsil Ediyor|
|Cylinder100PercentStacked|100% Yığılmış Silindir Grafiğini Temsil Ediyor|
|CylindricalBar| Silindirik Sütun Grafiğini Temsil Eder|
|CylindricalBarStacked| Yığılmış Silindirik Sütun Grafiğini Temsil Eder|
|CylindricalBar100PercentStacked| Yüzde 100 Yığılmış Silindirik Sütun Grafiğini Temsil Eder|
|CylindricalColumn3D| 3 Boyutlu Silindirik Sütun Grafiğini Temsil Eder|
|Cone|Konik Grafiğini Temsil Ediyor|
|ConeStacked|Yığılmış Konik Grafiğini Temsil Ediyor|
|Cone100PercentStacked|100% Yığılmış Konik Grafiğini Temsil Ediyor|
|ConicalBar|Konik Çubuk Grafiğini Temsil Ediyor|
|ConicalBarStackedStacked Konik Çubuk Grafiğini Temsil Ediyor|
|ConicalBar100PercentStacked|100% Yığılmış Konik Çubuk Grafiğini Temsil Ediyor|
|ConicalColumn3D|3 Boyutlu Konik Sütun Grafiğini Temsil Ediyor|
|Pyramid|Piramit Grafiğini Temsil Ediyor|
|PyramidStacked|Yığılmış Piramit Grafiğini Temsil Ediyor|
|Pyramid100PercentStacked|100% Yığılmış Piramit Grafiğini Temsil Ediyor|
|PyramidBar| Piramit Çubuk Grafiğini Temsil Eder|
|PyramidBarStacked|Stacked Piramit Çubuk Grafiğini Temsil Ediyor|
|PyramidBar100PercentStacked|100% Yığılmış Piramit Çubuk Grafiğini Temsil Ediyor|
|PyramidColumn3D| 3D Piramit Sutun Grafiğini Temsil Eder|
Aspose.Cells kullanarak bir grafik oluşturmak için:

1. Çalışma sayfası hücrelerine biraz veri ekleyin [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) nesnesinin [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Value) metodu ile.
   Bu, grafik veri kaynağı olarak kullanılacaktır.
1. [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) koleksiyonunun [*add*](https://reference.aspose.com/cells/java/com.aspose.cells/chartcollection#add-int-int-int-int-int-) metodunu çağırarak çalışma sayfasına bir grafik ekleyin, bu metod [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) nesnesine gömülüdür.
1. Grafik türünü [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) numaralandırma ile belirtin.
   Örneğin, örnek, grafik türü olarak [**ChartType.PYRAMID**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#PYRAMID) değerini kullanır.
1. Yeni [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) nesnesine, endeksini geçirerek [**ChartCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartCollection) koleksiyonundan erişin.
1. Grafiği yönetmek için [**Chart**](https://reference.aspose.com/cells/java/com.aspose.cells/Chart) nesnesine kapsüllenmiş olan herhangi bir grafik nesnesini kullanın.
   Aşağıdaki örnek, [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) grafik nesnesini grafik veri kaynağını belirtmek için kullanır.

Grafik verisini eklerken, veri kaynağı hücre aralığı (örneğin "A1:C3") veya ardışık olmayan hücrelerin dizisi (örneğin "A1, A3, A5") veya değerlerin dizisi (örneğin "1,2,3") olabilir.

{{% alert color="primary" %}}

Hücre aralığını bir veri kaynağı olarak atadığınızda, aralığı sadece sol üstten sağ alta ayarlayabilirsiniz. Örneğin, "A1:C3" geçerli iken, "C3:A1" geçersizdir.

{{% /alert %}}

Bu genel adımlar, herhangi bir türde bir grafik oluşturmanıza olanak tanır. Farklı grafikler oluşturmak için farklı grafik nesnelerini kullanın.

Örnek kod yürütüldüğünde, aşağıdaki gibi bir piramit grafik çalışma sayfasına eklenir.

**Veri kaynağı ile piramit grafik**

![todo:image_alt_text](creating-and-customizing-charts_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreatePyramidChart-HowToCreatePyramidChart.java" >}}

Balon Grafik oluşturmak için, [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) değerinin [**ChartType.BUBBLE**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#BUBBLE) olarak ayarlanması gerekmekte ve ayrıca, BalonBoyutları, Değerler ve XDeğerleri gibi ekstra özelliklerin buna göre ayarlanması gerekmektedir. Aşağıdaki kodu yürütme işlemi sonucunda, çalışma sayfasına bir balon grafik eklenir.

**Veri kaynağı ile balon grafik**

![todo:image_alt_text](creating-and-customizing-charts_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateBubbleChart-HowToCreateBubbleChart.java" >}}

#### **Veri İşaretçisi ile Çizgi Grafiği**

Bir veri işaretçili çizgi grafiği oluşturmak için, [**ChartType**](https://reference.aspose.com/cells/java/com.aspose.cells/ChartType) [**ChartType.LINE_WITH_DATA_MARKERS**](https://reference.aspose.com/cells/java/com.aspose.cells/charttype#LINE-WITH-DATA-MARKERS) olarak ayarlanmalı ve ayrıca, arka plan alanı, Seri İşaretçileri, Değerler & XDeğerleri gibi ekstra özellikler buna göre ayarlanmalıdır. Aşağıdaki kodu yürütme işlemi sonucunda, çalışma sayfasına bir veri işaretçili çizgi grafiği eklenir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-CreateLineWithDataMarkerChart-1.java" >}}

## **Özel Grafikler Oluşturma**

Şimdiye kadar grafikler hakkında konuştuğumuzda, standart biçimlendirme ayarlarına sahip standart grafikleri inceledik. Sadece veri kaynağını tanımlıyoruz, birkaç özellik belirliyoruz ve grafik varsayılan biçim ayarlarıyla oluşturuluyor. Ancak Apose.Cells, geliştiricilere kendi format ayarlarıyla grafik oluşturmalarını destekleyen özel grafikler oluşturmaya da olanak tanır.

### **Özel Grafikler Oluşturma**

Geliştiriciler, Aspose.Cells'in basit API'sını kullanarak çalışma zamanında özel grafikler oluşturabilirler.

Bir grafik, bir veri serisinden oluşur. Aspose.Cells'te her veri serisi bir [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) nesnesi tarafından temsil edilir, [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) nesnesi ise [**Series**](https://reference.aspose.com/cells/java/com.aspose.cells/Series) nesnelerinin bir koleksiyonunu hizmet eder. Özel bir grafik oluştururken, geliştiriciler farklı veri serileri için farklı grafik türlerini kullanma özgürlüğüne sahiptir (bir [**SeriesCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/SeriesCollection) nesnesinde toplanmış veri serileri için).

{{% alert color="primary" %}}

Şu anda Aspose.Cells, sadece turta, çizgi, sütun ve sütun yığını grafiklerini birleştiren özel grafikleri desteklemektedir ancak daha fazla grafik gelecekteki sürümlerde desteklenecektir. Aspose.Cells'in desteklediği standart grafiklerin tam listesi için [Grafik Türleri](/cells/tr/java/chart-types/) makalesini okuyun.

{{% /alert %}}

Aşağıdaki örnek kod, özel grafikler nasıl oluşturulurunu göstermektedir. Bu örnekte, birinci veri serisi için sütun grafik ve ikinci serisi için çizgi grafik kullanacağız. Sonuç olarak, çalışma sayfasına sütun grafik ve çizgi grafikle birlikte eklendi.

**Sütun ve çizgi grafiklerini birleştiren özel grafik**

![todo:image_alt_text](creating-and-customizing-charts_3.png)

**Programlama Örneği**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-HowToCreateCustomChart-HowToCreateCustomChart.java" >}}

{{% alert color="primary" %}}

Desteklenen grafik türlerinin bir listesini görmek için, [Grafik Türleri](/cells/tr/java/chart-types/) makalesini okuyun.

{{% /alert %}}

{{< app/cells/assistant language="java" >}}
