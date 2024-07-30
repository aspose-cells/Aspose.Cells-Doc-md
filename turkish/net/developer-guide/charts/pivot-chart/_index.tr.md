---
title: Aspose.Cells Kullanarak Bir PivotChart Nasıl Eklenir
linktitle: Pivot Grafik
type: docs
weight: 100
url: /tr/net/how-to-add-pivot-chart/
description: Aspose.Cells ı Kullanarak Bir PivotChart Nasıl Eklenir.
keywords: PivotChart
---
## PivotChart Nedir

Bir özet tabloyundaki verilerin görsel temsilidir. Özet tabloları, özet verileri özetleme, analiz etme, keşfetme ve sunma şekli sağlar. Pivot grafiklerinin bazı temel özellikleri ve yönleri şunlardır:

1. Dinamik Veri Temsili: Pivot grafikleri otomatik olarak özet tablosundaki değişiklikleri yansıtmak için güncellenir. Özet tablosunda alan ekler veya kaldırırsanız, pivot grafikleri buna göre güncellenir.

1. Etkileşimli: Pivot grafikleri etkileşimli olup, kullanıcıların veriyi filtrelemesine, sıralamasına ve derinlemesine incelemesine olanak tanır. Bu, veri kümesinin farklı yönlerini keşfetmeyi kolaylaştırır.

1. Esnek Düzen: Kullanıcılar, verilerin nasıl görüntülendiği konusunda esneklik sağlayan alanları sürükleyip bırakarak pivot grafiklerinin düzenini değiştirebilirler.

1. Çeşitli Grafik Türleri: Verinin doğası ve kazanmak istediğiniz içgörülere bağlı olarak bar grafikleri, çizgi grafikleri, pasta grafikleri ve daha fazlası gibi çeşitli grafik tipleri kullanılarak pivot grafikleri oluşturulabilir.

1. Özümseme: Pivot grafikleri büyük miktarda veriyi özetler ve toplamları, ortalamaları, sayıları veya diğer özet istatistikleri gösterebilir.

1. Filtreleme: Belirli kriterleri karşılayan verileri yalnızca görüntülemek için filtreleme yetenekleri sunarlar.

<br>
Pivot grafikleri, karmaşık veri kümelerinin net ve öz bir görsel özetini sağlamak için iş zekası ve veri analizi alanında yaygın olarak kullanılır. Veri odaklı kararlar almak için güçlü bir araçtır.

## Aspose.Cells kullanarak PivotChart ekleme

### **Pivot Tablo Ekleme**

Aspose.Cells kullanarak bir pivot tablosu oluşturmak için:

1. Bir Hücre nesnesi'nin PutValue/setValue yöntemini kullanarak bir çalışma sayfasındaki hücrelere bazı veriler ekleyin. Ayrıca zaten verilerle doldurulmuş bir şablon dosyası kullanabilirsiniz. Veriler, pivot tablosunun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun add yöntemini (Worksheet nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir pivot tablosu ekleyin.
1. Yeni PivotTable nesnesine PivotTables koleksiyonundan endeksini geçerek erişin. # PivotTable nesnesinde kapsanan herhangi bir pivot tablo nesnesini kullanarak tabloyu yönetin.

Kod örnekleri aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Pivot Grafik Ekleme**

Aspose.Cells kullanarak bir PivotChart oluşturmak için:

1. Bir grafik ekleyin.
1. Grafik PivotSource'unu elektronik tabloda zaten mevcut bir pivot çizelgesine atıf yapacak şekilde ayarlayın.
1. Diğer özellikleri ayarlayın.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

