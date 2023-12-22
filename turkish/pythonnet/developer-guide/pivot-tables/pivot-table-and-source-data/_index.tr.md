---
title: Pivot Tablo ve Kaynak Veriler
type: docs
weight: 30
url: /tr/python-net/pivot-table-and-source-data/
description: Bu makalede, pivot tablonun kaynak verilerinin Aspose.Cells for Python via .NET ile nasıl değiştirileceği gösterilmektedir.
keywords: Change Pivot Table's Source Data
---
##  **Pivot Tablonun Kaynak Verileri**

Tasarım zamanında bilinmeyen farklı veri kaynaklarından (veritabanı gibi) veri alan pivot tablolarla Microsoft Excel raporları oluşturmak istediğiniz zamanlar vardır. Bu makalede, pivot tablonun veri kaynağını dinamik olarak değiştirmeye yönelik bir yaklaşım sunulmaktadır.

###  **Pivot Tablonun Kaynak Verilerini Değiştirme**

1. Yeni bir tasarımcı şablonu oluşturma.
 1. Aşağıdaki ekran görüntüsündeki gibi yeni bir tasarımcı şablon dosyası oluşturun.
 1. Daha sonra bu hücre aralığını ifade eden *DataSource** adlı adlandırılmış bir aralık tanımlayın.

      **Tasarımcı şablonu oluşturma ve adlandırılmış bir aralığı tanımlama, DataSource** 

![yapılacak şey:image_alt_text](pivot-table-and-source-data_1.png)
   
1. Bu adlandırılmış aralığa dayalı bir Pivot Tablo Oluşturma.
1. Microsoft Excel'de şunu seçin:**Veri**, ardından **Özet Tablo** ve *Özet Grafik Raporu**.
 1. İlk adımda oluşturulan adlandırılmış aralığa göre bir pivot tablo oluşturun.

      **DataSource adlı adlandırılmış aralığa dayalı bir pivot tablo oluşturma** 

![yapılacak şey:image_alt_text](pivot-table-and-source-data_2.png)

   
 1. İlgili alanı pivot tablo satırına ve sütununa sürükleyin, ardından aşağıdaki ekran görüntüsündeki gibi elde edilen pivot tabloyu oluşturun.

   **İlgili alana dayalı bir pivot tablo oluşturma** 

![yapılacak şey:image_alt_text](pivot-table-and-source-data_3.png)

   
1. Pivot tabloya sağ tıklayın ve *Tablo Seçenekleri**'ni seçin.
 1. Kontrol edin**Açılışta yenile** içinde**Veri seçenekleri** ayarlar.

      **Pivot tablo seçeneklerini ayarlama** 

![yapılacak şey:image_alt_text](pivot-table-and-source-data_4.png)


Artık bu dosyayı tasarımcı şablon dosyanız olarak kaydedebilirsiniz.

1. Yeni verileri doldurma ve pivot tablonun kaynak verilerini değiştirme.
 1. Tasarımcı şablonu oluşturulduktan sonra pivot tablonun kaynak verilerini değiştirmek için aşağıdaki kodu kullanın.

Aşağıdaki örnek kodun yürütülmesi pivot tablonun kaynak verilerini değiştirir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-ChangeSourceData-1.py" >}}

