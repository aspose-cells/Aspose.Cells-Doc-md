---
title: Grafik Verilerini filtrelemek için üç yöntem
description: Aspose.Cells for .NET numaralı telefonu kullanarak Excel'de grafikleri nasıl filtreleyeceğinizi öğrenin. Kapsamlı kılavuzumuz, daha iyi içgörüler ve bilinçli karar verme için grafiklere filtrelerin nasıl uygulanacağını, grafik öğelerinin nasıl özelleştirileceğini ve veri analizi araçlarının nasıl kullanılacağını gösterecektir.
keywords: Aspose.Cells for .NET, Filtering Charts in Excel, Data Analysis, Decision Making, Visualization.
type: docs
weight: 2210
url: /tr/net/filtering-charts-in-excel/
---
{{% alert color="primary" %}}

##  **1. Grafiği oluşturmak için serileri filtrelemek**

###  **Excel'deki bir grafikteki serileri filtreleme adımları**
 Excel'de, bir grafikten belirli serileri filtreleyerek filtrelenen serilerin grafikte görüntülenmemesine neden olabiliriz. Orijinal grafik şurada gösterilmiştir:**Şekil 1**. Ancak **Testseries2'yi filtrelediğimizde** ve *Testseries4**, grafik *Şekil 2**'de gösterildiği gibi görünecektir.

 Aspose.Cells'de de benzer işlemi gerçekleştirebiliriz. bir için[örnek](seriesFiltered.xlsx) filtrelemek istiyorsak bunun gibi bir dosya**Test serisi2** ve *Testseries4** ile aşağıdaki kodu çalıştırabiliriz. Ek olarak iki liste tutacağız: bir ([NSerisi](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) seçilen tüm serileri ve diğerini ([FiltrelenmişNSerisi](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)) filtrelenen seriyi saklamak için.

Lütfen**Not** bunu ayarladığımızda kodda**chart.NSeries[0].IsFiltered = true;**, [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)'deki ilk seri kaldırılacak ve [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/) içinde uygun konuma yerleştirildi. Daha sonra, önceki **NSerisi[1]** listedeki yeni ilk öğe olacak ve sonraki tüm seriler bir sıra ileri kayacaktır. Bu, daha sonra *chart.NSeries[1].IsFiltered = true;** komutunu çalıştırırsak, orijinal üçüncü seriyi etkili bir şekilde kaldırdığımız anlamına gelir. Bu bazen karışıklığa neden olabilir, bu nedenle koddaki seriyi baştan sona silen işlemi takip etmenizi öneririz.

![yapılacak şey:image_alt_text](Figure1.png)

![yapılacak şey:image_alt_text](Figure2.png)

###  **Basit kod**
 Aşağıdaki örnek kod,[örnek Excel dosyası](seriesFiltered.xlsx).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

##  **2. Verileri filtreleyin ve grafiğin değişmesine izin verin**

Verilerinizi filtrelemek, çok fazla veri içeren grafik filtrelerini işlemenin harika bir yoludur. Verileri filtrelediğinizde grafik değişecektir. Ele almamız gereken bir konu da grafiğin ekranda kalmasını sağlamaktır. Filtrelediğinizde gizli satırlar elde edersiniz ve bazen grafik de bu gizli satırlarda olur.

![yapılacak şey:image_alt_text](Figure3.png)

###  **Excel'deki grafiği değiştirmek için Veri Filtrelerini kullanma adımları**

1. Veri aralığınızın içine tıklayın.
 2. öğesine tıklayın**Veri** sekmesine gidin ve Filtreler'e tıklayarak Filtreler'i açın. Başlık satırınızda aşağı açılan oklar bulunur.
 3. Şuraya giderek bir grafik oluşturun:**Sokmak** sekmesine tıklayın ve bir sütun grafiği seçin.
4. Şimdi verilerdeki açılır okları kullanarak verilerinizi filtreleyin. Grafik Filtrelerini kullanmayın.

###  **Basit kod**
Aşağıdaki örnek kod, Aspsoe.Cells kullanılarak aynı özelliği göstermektedir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

##  **3. Verileri bir Tablo kullanarak filtreleyin ve grafiğin değişmesine izin verin**

Tablo kullanmak, Aralık kullanan Yöntem 2'ye benzer, ancak tablolarla aralıklara göre avantajlara sahipsiniz. Aralığınızı Tablo olarak değiştirip veri eklediğinizde grafik otomatik olarak güncellenir. Bir aralıkla veri kaynağını değiştirmeniz gerekecektir.

###  **Excel'de tablo olarak biçimlendirme**

 Verilerinizin içine tıklayın ve kullanın**CTRL + T** veya Ana Sayfa sekmesini kullanın,**Tablo Olarak Biçimlendir**

![yapılacak şey:image_alt_text](Figure4.png)

###  **Basit kod**
 Aşağıdaki örnek kod,[örnek Excel dosyası](TableFilters.xlsx) Aspsoe.Cells kullanılarak aynı özelliği gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}