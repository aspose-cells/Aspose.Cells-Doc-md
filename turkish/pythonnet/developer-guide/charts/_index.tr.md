---
title: Çizim Oluştur ve Yönet
description: Aspose.Cells for Python via .NET kullanarak Microsoft Excel de grafikler oluşturmayı öğrenin. Kılavuzumuz, oluşturulabilecek farklı grafik türlerini ve görüntüleme ile biçimlendirmeyi nasıl özelleştireceğinizi gösterecek.
keywords: Aspose.Cells for Python via .NET, Grafik Oluşturma, Microsoft Excel, Grafik Türleri, Özelleştirme, Görünüm, Biçimlendirme.
linktitle: Grafikler
type: docs
weight: 130
url: /tr/python-net/creating-charts/
description: Excel ve ODS dosyaları için bir grafik oluşturun.
keywords: bir grafik oluştur, bir çizelge yap 
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET ile elektronik tablolarınıza çeşitli grafikler eklemek mümkündür. Aspose.Cells for Python via .NET birçok esnek grafik nesnesi sağlar. Bu konu, Aspose.Cells'in grafik nesnelerini tartışır.

{{% /alert %}}

## **Grafikler Oluşturma**

### **Basitçe bir Grafik Oluşturma**
Aspose.Cells for Python via .NET ile grafik oluşturmak oldukça basittir; aşağıdaki örnek kodlarla yapılabilir:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateColumnChart-1.py" >}}

### **Bir Grafik Oluşturmak için Bilinmesi Gerekenler**

Grafik oluşturmadan önce, Aspose.Cells for Python via .NET kullanarak grafik oluştururken yararlı olacak bazı temel kavramları anlamak önemlidir.

#### **Grafikleme Nesneleri**

Aspose.Cells for Python via .NET, desteklenen grafiklerin oluşturulmasında kullanılan [**Aspose.Cells.Charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts) isim alanında özel bir sınıf kümesi sağlar. Bu sınıflar, **grafik nesneleri** oluşturmak için kullanılır ve grafik yapım blokları görevi görür. Grafik nesneleri aşağıda listelenmiştir:

- Seri, bir grafikte tek veri serisi.
- Eksen, bir grafik eksenleri.
- Grafik, tek bir Excel grafiği.
- GrafikAlanı, çalışma sayfasındaki grafik alanı.
- GrafikVeriTablosu, bir grafik veri tablosu.
- GrafikÇerçeve, bir grafikteki çerçeve nesnesi.
- GrafikNokta, bir grafikteki seri içindeki tek bir nokta.
- GrafikNoktaKoleksiyonu, bir serideki tüm noktaları içeren bir koleksiyon.
- Grafikler, Grafik nesnelerinin bir koleksiyonu.
- VeriEtiketleri, belirtilen seri için tüm VeriEtiketi nesnelerinin bir koleksiyonu.
- DoldurBiçimi, bir şeklin doldurulma biçimi.
- Zemin, 3B bir grafik zemini.
- Efsane, grafik efsanesi.
- Çizgi, grafik çizgisi.
- SeriKoleksiyonu, Seri nesnelerinin bir koleksiyonu.
- İşaretEtiketleri, bir grafik eksenindeki işaret etiketleri ile ilişkili olan işaret etiketi etiketleri.
- Başlık, bir grafik veya eksenin başlığı.
- Trend Çizgisi, bir grafikteki bir trend çizgisi.
- Trend Çizgisi Koleksiyonu, belirtilen veri serisi için tüm Trend Çizgisi nesnelerinin bir koleksiyonu.
- Duvarlar, 3D bir grafikte duvarlar.

#### **Grafik Nesneleri Kullanma**

Yukarıda belirtildiği gibi, tüm grafik nesneleri, ilgili sınıfların örnekleridir ve belirli görevleri yerine getirmek için belirli özellikler ve metotlar sağlar. Grafik nesnelerini kullanarak grafikler oluşturun.

Herhangi bir türde bir grafik, [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/charts) koleksiyonunu kullanarak bir çalışma sayfasına ekleyin. [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/charts) koleksiyonundaki her öğe bir [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) nesnesini temsil eder. Bir [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) nesnesi, grafik görünümünü özelleştirmek için gereken diğer tüm grafik nesnelerini kapsar. Sonraki bölüm, basit bir grafik oluşturmak için birkaç temel grafik nesnesini nasıl kullanacağınızı gösterir.

### **Aspose.Cells for Python via .NET kullanarak Grafik Oluşturma**

**Adımlar:**

1. Çalışma sayfası hücrelerine biraz veri ekleyin [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) nesnesinin [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value) metodu ile.
   Bu, grafik veri kaynağı olarak kullanılacaktır.
1. [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection/add) nesnesine kapsüllenmiş olan [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection) koleksiyonunun [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection/add) metodu çağrılarak bir grafik çalışma sayfasına ekleyin.
1. Grafik türünü [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) numaralandırma ile belirtin.
   Örneğin, aşağıdaki örnek, grafik türü olarak [**ChartType.PYRAMID**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype/) değerini kullanır.
1. Yeni [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) nesnesine, endeksini geçirerek [**charts**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartcollection) koleksiyonundan erişin.
1. Grafiği yönetmek için [**Chart**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart) nesnesine kapsüllenmiş olan herhangi bir grafik nesnesini kullanın.
   Aşağıdaki örnek, [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) grafik nesnesini grafik veri kaynağını belirtmek için kullanır.

Grafik verisini eklerken, veri kaynağı hücre aralığı (örneğin "A1:C3") veya ardışık olmayan hücrelerin dizisi (örneğin "A1, A3, A5") veya değerlerin dizisi (örneğin "1,2,3") olabilir.

Bu genel adımlar, herhangi bir türde bir grafik oluşturmanıza olanak tanır. Farklı grafikler oluşturmak için farklı grafik nesnelerini kullanın.

Aspose.Cells for Python via .NET ile birçok farklı türde grafik oluşturmak mümkündür. Aspose.Cells for Python via .NET tarafından desteklenen tüm standart grafikler, [**Aspose.Cells.Charts.ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) adlı bir enumda önceden tanımlanmıştır.

Önceden tanımlanmış grafik tipleri:

|**Grafik Tipleri**|**Açıklama**|
| :- | :- |
|Column|Temsil Edilen Kümeleme Sutun Grafiği|
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
|ScatterConnectedByCurvesWithDataMarker|Eğrilerle Bağlı Veri İşaretleri Bulunan Saçılma Grafiğini Temsil Eder|
|ScatterConnectedByCurvesWithoutDataMarker|Eğrilerle Bağlı Veri İşaretleri Bulunmayan Saçılma Grafiğini Temsil Eder|
|ScatterConnectedByLinesWithDataMarker|Çizgilerle Bağlı Veri İşaretleri Bulunan Saçılma Grafiğini Temsil Eder|
|ScatterConnectedByLinesWithoutDataMarker|Çizgilerle Bağlı Veri İşaretleri Bulunmayan Saçılma Grafiğini Temsil Eder|
|Area|Alan Grafiğini Temsil Eder|
|AreaStacked|Yığılmış Alan Grafiğini Temsil Eder|
|Area100PercentStacked|100% Yığılmış Alan Grafiğini Temsil Eder|
|Area3D|3D Alan Grafiğini Temsil Eder|
|Area3DStacked|3D Yığılmış Alan Grafiğini Temsil Eder|
|Area3D100PercentStacked|3D 100% Yığılmış Alan Grafiğini Temsil Eder|
|Doughnut|Donut Grafiğini Temsil Eder|
|DoughnutExploded|Exploded Doughnut Chartını Temsil Ediyor|
|Radar|Radar Grafiğini Temsil Ediyor|
|RadarWithDataMarkers|Veri İşaretçileri olan Radar Grafiğini Temsil Ediyor|
|RadarFilled|Dolu Radar Grafiğini Temsil Ediyor|
|Surface3D|3 boyutlu Yüzey Grafiğini Temsil Ediyor|
|SurfaceWireframe3D|Tel Kafesli 3 Boyutlu Yüzey Grafiğini Temsil Ediyor|
|SurfaceContour|Kontur Grafiğini Temsil Ediyor|
|SurfaceContourWireframe|Tel Kafesli Kontur Grafiğini Temsil Ediyor|
|Bubble|Balon Grafiğini Temsil Ediyor|
|Bubble3D|3 Boyutlu Balon Grafiğini Temsil Ediyor|
|Cylinder|Silindir Grafiğini Temsil Ediyor|
|CylinderStacked|Yığılmış Silindir Grafiğini Temsil Ediyor|
|Cylinder100PercentStacked|100% Yığılmış Silindir Grafiğini Temsil Ediyor|
|CylindericalBar|Silindirik Çubuk Grafiğini Temsil Ediyor|
|CylindericalBarStacked|Yığılmış Silindirik Çubuk Grafiğini Temsil Ediyor|
|CylindericalBar100PercentStacked|100% Yığılmış Silindirik Çubuk Grafiğini Temsil Ediyor|
|CylindericalColumn3D|3 Boyutlu Silindirik Sütun Grafiğini Temsil Ediyor|
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
|PyramidBar|Piramit Çubuk Grafiğini Temsil Ediyor|
|PyramidBarStacked|Stacked Piramit Çubuk Grafiğini Temsil Ediyor|
|PyramidBar100PercentStacked|100% Yığılmış Piramit Çubuk Grafiğini Temsil Ediyor|
|PyramidColumn3D| 3D Piramit Sutun Grafiğini Temsil Eder|
{{% alert color="primary" %}}

Hücre aralığını veri kaynağı olarak atadığınızda, yalnızca sol üstten sağ alta doğru aralığı belirleyebilirsiniz. Örneğin, "A1:C3" geçerli iken "C3:A1" geçersizdir.

{{% /alert %}}

#### **Piramit Grafiği**

Örnek kod çalıştırıldığında, bir piramit grafiği çalışma sayfasına eklenir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreatePyramidChart-1.py" >}}

#### **Çizgi Grafiği**

Yukarıdaki örnekte, [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) yalnızca *Çizgi* olarak değiştirilerek bir çizgi grafiği oluşturulur. Tam kod aşağıda verilmiştir. Kod çalıştırıldığında, çalışma sayfasına bir çizgi grafiği eklenir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateLineChart-1.py" >}}

#### **Kabarcık Grafiği**

Bir kabarcık grafiği oluşturmak için, [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) [**ChartType.BUBBLE**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) olarak ayarlanmalı ve BubbleSizes, Values & XValues gibi ekstra özellikler uygun şekilde ayarlanmalıdır. Aşağıdaki kod çalıştırıldığında, bir kabarcık grafiği çalışma sayfasına eklenir.

#### **Veri İşaretçisi ile Çizgi Grafiği**

Veri işaretçisi ile çizgi grafiği oluşturmak için, [**ChartType**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/charttype) *ChartType.LineWithDataMarkers* olarak ayarlanmalı ve arka plan alanı, Seri İşaretçileri, Değerler & XDeğerler gibi ekstra özellikler uygun şekilde ayarlanmalıdır. Aşağıdaki kod çalıştırıldığında, veri işaretçili çizgi grafiği çalışma sayfasına eklenir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateLineWithDataMarkerChart-1.py" >}}

## **Gelişmiş Konular**
- [Excel 2016 Grafiklerini Okuma ve Değiştirme](/cells/tr/python-net/read-and-manipulate-excel-2016-charts/)
- [Excel Grafik Eksenlerini Yönetme](/cells/tr/python-net/chart-axes/)
- [Grafik Görünümünü Ayarlama](/cells/tr/python-net/setting-chart-appearance/)
- [Grafik Türleri](/cells/tr/python-net/chart-types/)
- [Grafikleri Özelleştirme](/cells/tr/python-net/customizing-charts/)
- [Grafiğin Veri Kaynağını Ayarlama](/cells/tr/python-net/data-formatting-in-charts/)
- [Excel Grafik Veri Etiketlerini Yönetme](/cells/tr/python-net/insert-datalabels-to-chart/)
- [Zeki İşaretleyicileri İşleyerek Grafiği Oluşturma](/cells/tr/python-net/generate-chart-by-processing-smart-markers/)
- [Grafiğin Çalışma Sayfasını Alma](/cells/tr/python-net/get-worksheet-of-the-chart/)
- [Excel Grafiklerinin Açıklamasını Yönetme](/cells/tr/python-net/chart-legend/)
- [Pozisyon Boyutunu ve Tasarımcı Grafiği Yönetme](/cells/tr/python-net/manipulate-position-size-and-designer-chart/)
- [Lider Çizgili Pasta Grafiği Oluşturma](/cells/tr/python-net/creating-pie-chart-with-leader-lines/)
- [Grafiplerde Şekiller](/cells/tr/python-net/controls-in-charts/)
- [Excel Grafik Başlıklarını Yönetme](/cells/tr/python-net/chart-and-axis-titles/)
- [Grafik Rendeleme](/cells/tr/python-net/chart-rendering/)
- [Grafik Eğrisi Trend Çizgisinin Denklem Metnini Alma](/cells/tr/python-net/get-equation-text-of-chart-trendline/)
