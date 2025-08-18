---
title: Grafik Verisini Filtreleme İçin Üç Yöntem
description: Excel de grafikleri Aspose.Cells for Python via .NET kullanarak filtrelemeyi nasıl yapacağınızı öğrenin. Kapsamlı rehberimiz, grafikleri filtreleme, grafik öğelerini özelleştirme ve daha iyi içgörüler ile bilinçli kararlar almak için veri analizi araçlarını kullanmayı gösterecek.
keywords: Aspose.Cells for Python via .NET, Excel de Grafik Filtreleme, Veri Analizi, Karar Verme, Görselleştirme.
type: docs
weight: 2210
url: /tr/python-net/filtering-charts-in-excel/
---


## **1. Bir grafik oluşturmak için serileri filtreleme**

### **Excel'de bir grafikten serileri filtreleme adımları**
Excel'de, belirli serileri filtreleyebilir, bu filtrelenmiş serilerin grafikte gösterilmemesine neden olabilir. Orijinal grafik **Şekil 1**'de gösterilir. Ancak **Testseries2** ve **Testseries4**'ü filtrelediğimizde grafik **Şekil 2**'de gösterildiği gibi görünecektir.

Aspose.Cells for Python via .NET'de, benzer işlemleri gerçekleştirebiliriz. Bu örnekteki gibi bir [örnek](seriesFiltered.xlsx) dosyası için, eğer **Testseries2** ve **Testseries4**'ü filtrelemek istersek, aşağıdaki kodu çalıştırabiliriz. Ek olarak, iki liste tutacağız: biri ([n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/)), tüm seçilen serileri depolamak için, diğeri ([filtered_n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/filtered_n_series/)), filtrelenmiş serileri saklamak için.

Lütfen **not** edin ki, kodda, **chart.nSeries[0].is_filtered = TRUE;** ayarlandığında, [n_series](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/n_series/) içindeki ilk seri kaldırılır ve uygun konuma **filtered_n_series** içinde yerleştirilir. Daha sonra, önceki **nSeries[1]** yeni listenin ilk öğesi haline gelir ve tüm sonraki seriler bir pozisyon kayar. Bu durumda, **chart.nSeries[1].is_filtered = TRUE;** çalıştırırsak, orijinal üçüncü seriyi kaldırmış oluruz. Bu bazen karışıklığa neden olabilir, bu yüzden kodda gösterilen işlemi, serileri sondan başa doğru silmeyi öneririz.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Örnek Kod**
Aşağıdaki örnek kodu [örnek Excel dosyasını](seriesFiltered.xlsx) yükler.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-seriesFiltered.py" >}}

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-DataFilters.py" >}}

## **3. Verileri bir Tablo kullanarak filtreleyin ve grafiği değiştirin**

Tablo kullanımı, bir aralık kullanmakla bir yöntem 2'ye benzer, ancak tabloların aralıklara göre avantajları vardır. Aralığınızı bir Tablo'ya değiştirip veri eklediğinizde, grafik otomatik olarak güncellenir. Bir aralıkta veri kaynağını değiştirmeniz gerekecektir.

### **Excel'de tablo olarak biçimlendir**

Veri içine tıklayın ve **CTRL + T** kullanın veya Ana sekme, **Tablo Olarak Biçimlendir**i kullanın

![todo:image_alt_text](Figure4.png)

### **Örnek Kod**
Aşağıdaki örnek kod, [örnek Excel dosyasını](TableFilters.xlsx) Aspose.Cells kullanarak aynı özelliği gösterir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-TableFilters.py" >}}
