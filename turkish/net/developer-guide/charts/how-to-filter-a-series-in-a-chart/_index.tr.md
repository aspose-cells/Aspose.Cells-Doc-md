---
title: Grafik Verisini Filtreleme İçin Üç Yöntem
description: Aspose.Cells for .NET kullanarak Excel de grafikleri filtreleme konusunda nasıl bilgi alacağınızı öğrenin. Kapsamlı rehberimiz, grafiklere filtre uygulama, grafik öğelerini özelleştirme ve daha iyi bilgiler ve bilinçli karar verme için veri analiz araçlarını nasıl kullanacağınızı gösterecektir.
keywords: Aspose.Cells for .NET, Excel de Grafikleri Filtreleme, Veri Analizi, Karar Alma, Görselleştirme.
type: docs
weight: 2210
url: /tr/net/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. Bir grafik oluşturmak için serileri filtreleme**

### **Excel'de bir grafikten serileri filtreleme adımları**
Excel'de, belirli serileri filtreleyebilir, bu filtrelenmiş serilerin grafikte gösterilmemesine neden olabilir. Orijinal grafik **Şekil 1**'de gösterilir. Ancak **Testseries2** ve **Testseries4**'ü filtrelediğimizde grafik **Şekil 2**'de gösterildiği gibi görünecektir.

Aspose.Cells'te benzer bir işlem gerçekleştirebiliriz. Bu gibi bir [örnek](seriesFiltered.xlsx) dosyada, **Testseries2** ve **Testseries4**'ü filtrelemek istiyorsak, aşağıdaki kodu çalıştırabiliriz. Ayrıca, tüm seçilen serileri depolamak için bir ([NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) listesi ve filtrelenen serileri depolamak için başka bir ([FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/)) listesi tutacağız.

Lütfen **unutmayın** ki kodda **chart.NSeries[0].IsFiltered = true;** belirlendiğinde, [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) 'deki ilk seri kaldırılır ve uygun konuma yerleştirilir  [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filteredSeries/) içerisinde. Sonuç olarak, önceki **NSeries[1]** liste içindeki yeni ilk öğe haline gelir ve tüm sonraki seriler bir pozisyon ileri kayar. Bu, ardından **chart.NSeries[1].IsFiltered = true;** çalıştırırsak, aslında orijinal üçüncü seriyi kaldırır. Bunun bazen kafa karışıklığına yol açabileceğine dikkat edilmelidir, bu nedenle serileri sondan başa silme işlemini öneririz.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Örnek Kod**
Aşağıdaki örnek kodu [örnek Excel dosyasını](seriesFiltered.xlsx) yükler.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "seriesFiltered.cs" >}}

## **2. Veriyi filtrele ve grafiği değiştirmesine izin ver**

Verinizi filtrelemek, çok sayıda veri ile grafik filtrelerini yönetmenin harika bir yoludur. Veriyi filtrelediğinizde, grafik değişir. Karşılaşacağımız bir sorun, filtrelediğinizde gizli satırları alırsınız ve bazen grafik bu gizli satırlardan çıkar.

![todo:image_alt_text](Figure3.png)

### **Excel'de Grafikteki Değişikliği Uygulamak İçin Veri Filtrelerini Kullanma Adımları**

1. Veri aralığınızın içine tıklayın.
2. **Veri** sekmesine tıklayın ve Filtreleri açmak için Filtreleri tıklayın. Başlık satırınızın açılır oklarının olması gerekecektir.
3. **Ekle** sekmesine giderek sütun grafiği seçerek bir grafik oluşturun.
4. Verilerinizi veri içindeki açılır oklar kullanarak filtreleyin. Grafik Filtreleri kullanmayın.

### **Örnek Kod**
Aşağıdaki örnek kod, Aspose.Cells kullanarak aynı özelliği gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "DataFilters.cs" >}}

## **3. Verileri bir Tablo kullanarak filtreleyin ve grafiği değiştirin**

Tablo kullanımı, bir aralık kullanmakla bir yöntem 2'ye benzer, ancak tabloların aralıklara göre avantajları vardır. Aralığınızı bir Tablo'ya değiştirip veri eklediğinizde, grafik otomatik olarak güncellenir. Bir aralıkta veri kaynağını değiştirmeniz gerekecektir.

### **Excel'de tablo olarak biçimlendir**

Veri içine tıklayın ve **CTRL + T** kullanın veya Ana sekme, **Tablo Olarak Biçimlendir**i kullanın

![todo:image_alt_text](Figure4.png)

### **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](TableFilters.xlsx) Aspose.Cells kullanarak aynı özelliği gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "TableFilters.cs" >}}
