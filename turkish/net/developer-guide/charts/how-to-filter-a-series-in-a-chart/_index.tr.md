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

Aspose.Cells'te benzer bir işlem yapabiliriz. Bu tarz bir [örnek](seriesFiltered.xlsx) dosya için, **Testseries2** ve **Testseries4**'ü hariç tutmak istediğimizde aşağıdaki kodu çalıştırabiliriz. Ayrıca, iki liste tutarız: tüm seçilen serileri depolayan bir ([NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/)) list ve filtrelenmiş serileri depolayan başka ([FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filterednseries/)) list.

Lütfen **not** edin ki, kodda, **chart.NSeries[0].IsFiltered = true;** ayarlandığında, [NSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/nseries/) içindeki ilk seriden çıkartılır ve uygun pozisyona [FilteredNSeries](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/filterednseries/) içine yerleştirilir. Ardından, önceki **NSeries[1]** yeni listenin ilk ögesi olur ve sonraki seriler bir sıra sağa kayar. Bu durumda, sonra **chart.NSeries[1].IsFiltered = true;** yaparsak, orijinal üçüncü seri kaldırılmış olur. Bu bazen karışıklığa yol açabilir, bu yüzden kodda yapılan işlemi sondan başa doğru serileri silerek takip etmeniz önerilir.

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
{{< app/cells/assistant language="csharp" >}}
