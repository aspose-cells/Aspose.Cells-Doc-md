---
title: Aspose.Cells for Python via .NET kullanarak PivotGrafik ekleme
linktitle: Pivot Grafik
type: docs
weight: 100
url: /tr/python-net/how-to-add-pivot-chart/
description: Aspose.Cells for Python via .NET kullanarak PivotGrafik ekleme nasıl yapılır.
keywords: PivotChart
---
## PivotChart Nedir

Bir pivot grafiği, pivot tablodaki verilerin görsel temsilidir. Pivot grafikler, özet verileri özetleme, analiz etme, keşfetme ve sunma imkanı sağlar. İşte pivot grafiklerin bazı temel özellikleri ve yönleri:

1. Dinamik Veri Temsili: Pivot grafikleri, pivot tablodaki değişiklikleri otomatik olarak yansıtır. Pivot tablodaki alanları ekleyip çıkarırsanız, pivot grafik de buna göre güncellenir.

1. İnteraktif: Pivot grafikleri etkileşimlidir, kullanıcıların filtreleme, sıralama ve veri detayına inmesine izin verir. Bu, verilerin farklı yönlerini keşfetmeyi kolaylaştırır.

1. Esnek Düzen: Kullanıcılar alanları sürükleyip bırakarak pivot grafiğin düzenini değiştirebilir, bu da nasıl görselleştirileceğinde esneklik sağlar.

1. Çeşitli Grafik Türleri: Pivot grafikler çeşitli grafik türleri kullanılarak oluşturulabilir; çubuk grafikleri, çizgi grafikleri, pasta grafikleri ve daha fazlası, verinin doğasına ve elde etmek istediğiniz içgörülere bağlı olarak.

1. Özetleme: Pivot grafikleri büyük miktarda veriyi özetler ve toplamlar, ortalamalar, sayımlar veya diğer özet istatistikleri gösterebilir.

1. Filtreleme: Filtreleme özellikleri sağlar, belirli kriterleri karşılayan verileri görüntülemenize olanak tanır.

<br>
Pivot grafikler, karmaşık veri setlerinin net ve öz bir görsel özetini sağlamak için iş zekası ve veri analizinde yaygın olarak kullanılır. Veri odaklı kararlar almak için güçlü bir araçtır.

## Aspose.Cells for Python Excel Kütüphanesi kullanarak PivotChart nasıl eklenir

### **Pivot Tablo Ekleme**

Aspose.Cells for Python via .NET kullanarak bir pivot tablosu oluşturmak için:

1. Bir Hücre nesnesi'nin PutValue/setValue yöntemini kullanarak bir çalışma sayfasındaki hücrelere bazı veriler ekleyin. Ayrıca zaten verilerle doldurulmuş bir şablon dosyası kullanabilirsiniz. Veriler, pivot tablosunun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun add yöntemini (Worksheet nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir pivot tablosu ekleyin.
1. Yeni PivotTable nesnesine PivotTables koleksiyonundan endeksini geçerek erişin. # PivotTable nesnesinde kapsanan herhangi bir pivot tablo nesnesini kullanarak tabloyu yönetin.

Kod örnekleri aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreatePivotTable-1.py" >}}

### **Pivot Grafik Ekleme**

Aspose.Cells for Python via .NET Kullanarak Bir PivotChart Oluşturmak için:

1. Bir grafik ekleyin.
1. Grafik PivotSource'unu elektronik tabloda zaten mevcut bir pivot çizelgesine atıf yapacak şekilde ayarlayın.
1. Diğer özellikleri ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreatePivotChart-1.py" >}}

