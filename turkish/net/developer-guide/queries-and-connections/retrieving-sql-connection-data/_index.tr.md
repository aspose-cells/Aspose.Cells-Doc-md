---
title: SQL Bağlantı Verilerini Alma
type: docs
weight: 10
url: /tr/net/retrieving-sql-connection-data/
---
{{% alert color="primary" %}}

 Aspose.Cells, SQL bağlantı verilerini almanıza yardımcı olabilir. Bu, SQL sunucusuyla bağlantı kurmak için gereken tüm verileri içerir, örneğin,**sunucu URL'si**, **Kullanıcı adı**, **Tablo ismi**, **tam SQL sorgusu**, **Sorgu Türü**, **masanın yeri** , ve**adlandırılmış aralığın adı** ile ilişkili.

{{% /alert %}}

Microsoft Excel'de bir veritabanına şu şekilde bağlanın:

1.  tıklayarak**Veri** menü ve seçim**Diğer Kaynaklardan** bunu takiben**SQL Server'dan**.
1.  Ardından seçin**Veri** bunu takiben**Bağlantılar**.
1. Veritabanına bağlanmak ve bir veritabanı sorgusu oluşturmak için Bağlantılar sihirbazını kullanın.

Aspose.Cells, harici bağlantıları almak için Workbook.DataConnections özelliğini sağlar. Çalışma kitabındaki ExternalConnection nesnelerinin bir koleksiyonunu döndürür.

ExternalConnection nesnesi, SQL bağlantı verilerini içeriyorsa, bir DBConnection nesnesine tip-kast olabilir ve özellikleri veritabanı komutunu, komut tipini, bağlantı açıklamasını, bağlantı bilgilerini, kimlik bilgilerini vb. almak için kullanılabilir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}
