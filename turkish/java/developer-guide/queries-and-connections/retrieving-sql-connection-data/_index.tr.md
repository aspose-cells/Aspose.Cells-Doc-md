---
title: SQL Bağlantı Verilerini Almak
type: docs
weight: 20
url: /tr/java/retrieving-sql-connection-data/
---

{{% alert color="primary" %}} 

Aspose.Cells, SQL bağlantı verilerini almanıza yardımcı olabilir. Bu, SQL sunucusuna bağlanmak için gereken her türlü veriyi içerir, örneğin **sunucu URL'si**, **kullanıcı adı**, **tablo adı**, **tam SQL sorgusu**, **sorgu türü**, **tablonun konumu** ve onunla ilişkilendirilen adlandırılmış aralığın adı gibi.

{{% /alert %}} 

Microsoft Excel'de, bir veritabanına bağlanmak için:

1. **Veri** menüsünü tıklayın ve **Diğer Kaynaklardan, SQL Server'dan** ardından **Veri Al**'ı seçin.
1. Ardından **Veri**'yi ve ardından **Bağlantılar**'ı seçin.
1. Bağlantı sihirbazını kullanarak veritabanına bağlanın ve bir veritabanı sorgusu oluşturun.

**Microsoft Excel'de SQL bağlantı seçeneğini gösterme** 

![todo:image_alt_text](retrieving-sql-connection-data_1.png)

Aspose.Cells, Workbook.getDataConnections() yöntemini dış bağlantıları almak için sağlar. Bu, bir çalışma kitabındaki ExternalConnection nesnelerinin bir koleksiyonunu döndürür.

Eğer ExternalConnection nesnesi SQL bağlantı verisi içeriyorsa, bunun özellikleri DBConnection nesnesine tür dönüşümü yapılabilir ve veritabanı komutu, komut türü, bağlantı açıklaması, bağlantı bilgisi, kimlik bilgileri, ve benzeri kullanılabilir.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}






