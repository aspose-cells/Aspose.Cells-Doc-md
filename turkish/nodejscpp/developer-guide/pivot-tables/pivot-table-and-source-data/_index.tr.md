---
title: Pivot Tablosu ve Kaynak Veri
type: docs
weight: 30
url: /tr/nodejs-cpp/pivot-table-and-source-data/
---

## **Pivot Tablosunun Kaynak Verisi**

Farklı veri kaynaklarından (örneğin bir veritabanı) alınan verileri alan ve tasarım zamanında bilinmeyen pivota tabloları olan Microsoft Excel raporları oluşturmak istediğinizde bazı durumlar olabilir. Bu makale, bir pivot tablosunun veri kaynağını dinamik olarak değiştirmenin bir yaklaşımını sunar.

### **Bir Pivot Tablosunun Veri Kaynağını Değiştirme**

1. Yeni bir tasarımcı şablonu oluşturma.
   1. Aşağıdaki ekran görüntüsünde olduğu gibi yeni bir tasarımcı şablonu dosyası oluşturun.
   1. Ardından bu hücre aralığına atıfta bulunan **DataSource** adlı bir adlandırılmış aralık tanımlayın.

      **Bir tasarımcı şablon oluşturma ve DataSource adlı adlandırılmış aralık tanımlama** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Bu adlandırılmış aralığa dayalı bir Özet Tablo Oluşturma.
   1. Microsoft Excel'de **Veri**'yi seçin, ardından **Özet Tablo** ve **Özet Tablo Grafik Raporu'nu** seçin.
   1. İlk adımda oluşturulan adlandırılmış aralığa dayalı bir özet tablo oluşturun.

      **DataSource** adlı adlandırılmış aralığa dayalı bir özet tablo oluşturma 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. İlgili alanı özet tablo satır ve sütununa sürükleyin, ardından aşağıdaki ekran görüntüsünde olduğu gibi sonuç özet tablosunu oluşturun.

   **İlgili alana dayalı bir özet tablo oluşturmak** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Özet tabloyu sağ tıklayın ve **Tablo Seçenekleri**'ni seçin.
   1. **Veri seçenekleri** ayarlarında **Açılışta yenile**'yi işaretleyin.

      **Özet tablo seçeneklerini ayarlama** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Şimdi bu dosyayı tasarımcı şablon dosyanız olarak kaydedebilirsiniz.

1. Yeni veri eklenmesi ve özet tablonun kaynak verisinin değiştirilmesi.
   1. Tasarımcı şablon oluşturulduktan sonra, özet tablonun kaynak verisini değiştirmek için aşağıdaki kodu kullanın.

Aşağıdaki örnek kodu çalıştırarak pivot tablosunun kaynak verisini değiştirin.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTable-ChangeSourceData-1.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
