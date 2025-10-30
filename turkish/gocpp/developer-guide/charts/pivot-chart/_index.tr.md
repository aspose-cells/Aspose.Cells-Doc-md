---
title: Golang ile C++ kullanarak PivotChart nasıl eklenir
linktitle: Pivot Grafik
type: docs
weight: 100
url: /tr/go-cpp/how-to-add-pivot-chart/
description: Aspose.Cells ile Golang kullanarak C++ ile PivotChart ekleme
keywords: PivotChart
---

## PivotChart Nedir

Bir pivot grafiği, pivot tablodaki verilerin görsel temsilidir. Pivot grafikler, özet verileri özetleme, analiz etme, keşfetme ve sunma imkanı sağlar. İşte pivot grafiklerin bazı temel özellikleri ve yönleri:

1. **Dinamik Veri Temsili**: Pivot grafikleri, pivot tablodaki değişiklikleri otomatik olarak yansıtır. Pivot tablosuna alan ekleyip kaldırdığınızda, pivot grafiği de buna göre güncellenir.

1. **İnteraktif**: Pivot grafikleri etkileşimlidir, kullanıcıların filtreleme, sıralama ve detaylara inme yapmasına olanak tanır. Bu, veri setinin farklı yönlerini keşfetmeyi kolaylaştırır.

1. **Esnek Düzen**: Kullanıcılar, alanları sürükleyip bırakarak pivot grafiğin düzenini değiştirebilirler, bu da verilerin nasıl görselleştirileceği konusunda esneklik sağlar.

1. **Çeşitli Grafik Türleri**: Pivot grafikleri, çubuk grafikler, çizgi grafikler, pasta grafikler ve daha fazlası gibi farklı grafik türleri kullanılarak oluşturulabilir, bu da verilerin doğasına ve elde etmek istediğiniz içgörülere bağlıdır.

1. **Özetleme**: Pivot grafikleri büyük veri kümelerini özetler ve toplamları, ortalamaları, sayımları veya diğer özet istatistikleri gösterebilir.

1. **Filtreleme**: Belirli kriterleri karşılayan veriyi göstermenize olanak tanıyan filtreleme yetenekleri sağlar.

<br>
Pivot grafikler, karmaşık veri setlerinin net ve öz bir görsel özetini sağlamak için iş zekası ve veri analizinde yaygın olarak kullanılır. Veri odaklı kararlar almak için güçlü bir araçtır.

## Aspose.Cells kullanarak PivotChart ekleme

### **Pivot Tablo Ekleme**

Aspose.Cells kullanarak bir pivot tablosu oluşturmak için:

1. Bir çalışma sayfası hücrelerine `Cell` nesnesinin `PutValue` veya `SetValue` yöntemiyle bazı veriler ekleyin. Ayrıca, zaten veri doldurulmuş bir şablon dosyası kullanabilirsiniz. Veriler, pivot tablonun veri kaynağı olarak kullanılacaktır.
1. `PivotTables` koleksiyonunu `Add` yöntemiyle (`Worksheet` nesnesine kapsüllenmiş) kullanarak yeni bir pivot tablo ekleyin.
1. `PivotTables` koleksiyonundan yeni `PivotTable` nesnesine erişin ve onun indeksini kullanın. `PivotTable` nesnesine kapsüllenmiş herhangi bir pivot tablo nesnesini kullanarak tabloyu yönetin.

Kod örnekleri aşağıda verilmiştir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart.go" >}}
### **Pivot Grafik Ekleme**

Aspose.Cells kullanarak bir PivotChart oluşturmak için:

1. Bir grafik ekleyin.
1. Grafiğin `PivotSource` özelliğini, mevcut bir pivot tabloya referans olacak şekilde ayarlayın.
1. Diğer özellikleri ayarlayın.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart-1.go" >}}
