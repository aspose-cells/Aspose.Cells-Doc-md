---
title: Aspose.Cells Kullanarak Bir PivotChart Nasıl Eklenir
linktitle: Pivot Grafik
type: docs
weight: 100
url: /tr/java/how-to-add-pivot-chart/
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
### **Pivot Tablosu Oluşturma**

Aspose.Cells kullanarak bir pivot tablosu oluşturmak için:

1. Bir Hücre nesnesi'nin PutValue/setValue yöntemini kullanarak bir çalışma sayfasındaki hücrelere bazı veriler ekleyin. Ayrıca zaten verilerle doldurulmuş bir şablon dosyası kullanabilirsiniz. Veriler, pivot tablosunun veri kaynağı olarak kullanılacaktır.
1. PivotTables koleksiyonunun add yöntemini (Worksheet nesnesinde kapsüllenmiş) çağırarak çalışma sayfasına bir pivot tablosu ekleyin.
1. PivotTables koleksiyonundan yeni PivotTable nesnesine geçerek indeksini iletebilirsiniz.
1. Tabloyu yönetmek için PivotTable nesnesinde kapsüllenmiş herhangi bir pivot tablo nesnesini kullanın.

Aşağıda bileşen tarafından görevin tamamlanması için kullanılan kod örneği bulunmaktadır. Kodu çalıştırmak yeni bir dosya oluşturur: pivotTable_test.xls.

**Giriş verisi** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Çıktı pivot tablosu**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **Pivot Tablosuna Dayalı Pivot Çizelgesi Oluşturma**

Aspose.Cells kullanarak bir pivot çizelgesi oluşturmak için:

1. Bir grafik ekleyin.
1. Grafik PivotSource'unu elektronik tabloda zaten mevcut bir pivot çizelgesine atıf yapacak şekilde ayarlayın.
1. Diğer özellikleri ayarlayın.

Görevi gerçekleştirmek için bileşen tarafından kullanılan kod aşağıda verilmiştir. Kodu çalıştırmak yeni bir dosya oluşturur: pivotChart_test.xls.

**Pivot çizelgesi sayfası**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Bu makale Aspose.Cells kullanarak pivot tabloları ve pivot çizelgeleri oluşturmayı göstermektedir. Umarız kendi senaryolarınızda bu özellikleri kullanmanıza yardımcı olur.

Aspose.Cells yılların araştırması, tasarımı ve dikkatli ayarlamasından faydalanmıştır.

[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9) adresindeki sorularınızı, yorumlarınızı ve önerilerinizi bekliyoruz. Hızlı bir yanıt garantisi veriyoruz.

{{% /alert %}}
