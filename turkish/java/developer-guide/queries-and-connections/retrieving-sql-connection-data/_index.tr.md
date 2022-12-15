---
title: SQL Bağlantı Verilerini Alma
type: docs
weight: 20
url: /tr/java/retrieving-sql-connection-data/
---
{{% alert color="primary" %}} 

 Aspose.Cells, SQL bağlantı verilerini almanıza yardımcı olabilir. Bu, SQL sunucusuna bağlantı kurmak için gereken tüm verileri içerir, örneğin,**sunucu URL'si**, **Kullanıcı adı**, **Tablo ismi**, **tam SQL sorgusu**, **Sorgu Türü**, **masanın konumu** , ve**adlandırılmış aralığın adı** ile ilişkili.

{{% /alert %}} 

Microsoft Excel'de bir veritabanına şu şekilde bağlanın:

1.  tıklayarak**Veri** menü ve seçim**Diğer Kaynaklardan** bunu takiben**SQL Server'dan**.
1.  Ardından seçin**Veri** bunu takiben**Bağlantılar**.
1. Veritabanına bağlanmak ve bir veritabanı sorgusu oluşturmak için Bağlantılar sihirbazını kullanın.

**Microsoft Excel'de SQL bağlantı seçeneği gösteriliyor** 

![yapılacaklar:resim_alternatif_Metin](retrieving-sql-connection-data_1.png)

Aspose.Cells, harici bağlantıları almak için Workbook.getDataConnections() yöntemini sağlar. Çalışma kitabındaki ExternalConnection nesnelerinin bir koleksiyonunu döndürür.

ExternalConnection nesnesi SQL bağlantı verilerini içeriyorsa, veritabanı komutunu, komut türünü, bağlantı açıklamasını, bağlantı bilgilerini, kimlik bilgilerini vb. almak için kullanılan özelliklerini bir DBConnection nesnesine tür olarak aktarabilir.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}






