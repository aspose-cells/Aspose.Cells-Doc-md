---
title: SQL Bağlantı Verilerini Almak
type: docs
weight: 10
url: /tr/net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells, SQL bağlantı verilerini almanıza yardımcı olabilir. Bu, SQL sunucusuna bağlantı kurmak için gereken tüm veriyi içerir; örneğin, **sunucu URL'si**, **kullanıcı adı**, **tablo adı**, **tam SQL sorgusu**, **sorgu türü**, **tablonun yeri** ve onunla ilişkilendirilmiş **adlandırılmış aralığın adı**.

{{% /alert %}}

Microsoft Excel'de, bir veritabanına bağlanmak için:

1. **Veri** menüsünü tıklayın ve **Diğer Kaynaklardan, SQL Server'dan** ardından **Veri Al**'ı seçin.
1. Ardından **Veri**'yi ve ardından **Bağlantılar**'ı seçin.
1. Bağlantı sihirbazını kullanarak veritabanına bağlanın ve bir veritabanı sorgusu oluşturun.

Aspose.Cells, Workbook.DataConnections özelliğini kullanarak dış bağlantıları almak için yardımcı olur. Çalışma kitabında ExternalConnection nesnelerinin bir koleksiyonunu döndürür.

ExternalConnection nesnesi SQL bağlantı verisi içeriyorsa, onu bir DBConnection nesnesine dönüştürmek ve veritabanı komutu, komut türü, bağlantı açıklaması, bağlantı bilgileri, kimlik bilgileri vb. özelliklerini almak için kullanılabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}
