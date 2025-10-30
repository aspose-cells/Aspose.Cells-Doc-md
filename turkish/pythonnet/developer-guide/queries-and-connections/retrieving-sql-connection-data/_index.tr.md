---
title: SQL Bağlantı Verilerini Almak
type: docs
weight: 10
url: /tr/python-net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET, SQL bağlantı verilerini almanıza yardımcı olabilir. Bu, SQL sunucusuna bağlanmak için gereken tüm verileri içerir; örneğin, **sunucu URL'si**, **kullanıcı adı**, **tablo adı**, **tam SQL sorgusu**, **sorgu türü**, **tablonun konumu** ve **ile ilgili adlandırılmış alanın adı**.

{{% /alert %}}

Microsoft Excel'de, bir veritabanına bağlanmak için:

1. **Veri** menüsünü tıklayın ve **Diğer Kaynaklardan, SQL Server'dan** ardından **Veri Al**'ı seçin.
1. Ardından **Veri**'yi ve ardından **Bağlantılar**'ı seçin.
1. Bağlantı sihirbazını kullanarak veritabanına bağlanın ve bir veritabanı sorgusu oluşturun.

Aspose.Cells for Python via .NET, dış bağlantıları almak için Workbook.DataConnections özelliğini sağlar. Bu, çalışma kitabındaki ExternalConnection nesneleri koleksiyonunu döner.

ExternalConnection nesnesi SQL bağlantı verisi içeriyorsa, onu bir DBConnection nesnesine dönüştürmek ve veritabanı komutu, komut türü, bağlantı açıklaması, bağlantı bilgileri, kimlik bilgileri vb. özelliklerini almak için kullanılabilir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-RetrievingSQLConnectionData-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
