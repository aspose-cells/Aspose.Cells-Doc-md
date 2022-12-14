---
title: Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve Liste Nesnelerini Bulun
type: docs
weight: 20
url: /tr/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---
{{% alert color="primary" %}} 

Bazen, bazı Dış Veri Bağlantılarıyla ilgili Sorgu Tablolarını ve Liste Nesnelerini bulmanız gerekir. Sorgu Tabloları, Bağlantı Kimliği olan Dış Veri Bağlantısı nesnesiyle, Liste Nesneleri ise Sorgu Tablosu ile ilişkilidir.

{{% /alert %}} 
## **Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve Liste Nesnelerini Bulun**
 Aşağıdaki örnek kodlar ile[örnek excel dosyası](5115493.xlsm) Dış Veri Bağlantısı ile ilgili Sorgu Tablolarının ve Liste Nesnelerinin nasıl bulunacağını açıklar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

 Aşağıdaki, yukarıdaki örnek kodları bununla çalıştırmanın konsol çıktısıdır.[örnek excel dosyası](5115493.xlsm).

{{< highlight "java" >}}

 connection: AAPL Connection

querytable hp?s=AAPL+Historical+Prices

refersto: =Sheet1!$Q$1:$W$69

connection: BOSL066360W7_SQLEXPRESS Test

querytable BOSL066360W7_SQLEXPRESS Test

Table Table_BOSL066360W7_SQLEXPRESS_Test

refersto: Sheet1!A1:B3

connection: BOSL066360W7_SQLEXPRESS Test1

querytable BOSL066360W7_SQLEXPRESS Test_1

Table Table_BOSL066360W7_SQLEXPRESS_Test_1

refersto: Sheet1!D1:E2

connection: UWTI Connection

querytable hp?s=UWTI+Historical+Prices

refersto: =Sheet1!$H$1:$N$69


{{< /highlight >}}
