---
title: Özet Tablo ve Kaynak Veriler
type: docs
weight: 110
url: /tr/java/pivot-table-and-source-data/
---
## **Pivot Tablonun Kaynak Verileri**
Tasarım zamanında bilinmeyen farklı veri kaynaklarından (veritabanı gibi) veri alan pivot tablolarla Microsoft Excel raporları oluşturmak istediğiniz zamanlar olabilir. Bu makale, bir pivot tablonun veri kaynağını dinamik olarak değiştirmek için bir yaklaşım sunar.
## **Pivot Tablonun Kaynak Verilerini Değiştirme**
1. Yeni bir tasarımcı şablonu oluşturma.
1. Aşağıdaki ekran görüntüsündeki gibi yeni bir tasarımcı şablon dosyası oluşturun.
 1. Ardından adlandırılmış bir aralık tanımlayın,**Veri kaynağı** , bu hücre aralığını ifade eder.

      **Bir tasarımcı şablonu oluşturma ve adlandırılmış bir aralık tanımlama, DataSource** 

![yapılacaklar:resim_alternatif_Metin](pivot-table-and-source-data_1.png)

1. Bu adlandırılmış aralığa göre Pivot Tablo Oluşturma.
 1. Microsoft Excel'de seçin**Veri** , sonra**Pivot tablo** ve**Özet Grafik Raporu**.
 1. İlk adımda oluşturulan adlandırılmış aralığa dayalı olarak bir pivot tablo oluşturun.

      **DataSource adlı aralığa dayalı bir pivot tablo oluşturma** 

![yapılacaklar:resim_alternatif_Metin](pivot-table-and-source-data_2.png)

1.  Tablo satırını ve sütununu özetlemek için ilgili alanı sürükleyin, ardından aşağıdaki ekran görüntüsündeki gibi elde edilen pivot tabloyu oluşturun.

   **Karşılık gelen bir alana dayalı bir pivot tablo oluşturma** 

![yapılacaklar:resim_alternatif_Metin](pivot-table-and-source-data_3.png)

1.  Pivot tabloya sağ tıklayın ve seçin**Tablo Seçenekleri**.
 1. Kontrol**Açıkken yenile** içinde**veri seçenekleri** ayarlar.

      **Pivot tablo seçeneklerini ayarlama** 

![yapılacaklar:resim_alternatif_Metin](pivot-table-and-source-data_4.png)



Artık bu dosyayı tasarımcı şablon dosyanız olarak kaydedebilirsiniz.

1. Yeni verileri doldurma ve bir pivot tablonun kaynak verilerini değiştirme.
1. Tasarımcı şablonu oluşturulduktan sonra, pivot tablonun kaynak verilerini değiştirmek için aşağıdaki kodu kullanın.

Aşağıdaki örnek kodu çalıştırmak, pivot tablonun kaynak verilerini değiştirir ve pivot tablo aşağıdaki gibi görünür.

**Dinamik olarak değiştirilen pivot tablo** 

![yapılacaklar:resim_alternatif_Metin](pivot-table-and-source-data_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ChangeSourceData-ChangeSourceData.java" >}}
