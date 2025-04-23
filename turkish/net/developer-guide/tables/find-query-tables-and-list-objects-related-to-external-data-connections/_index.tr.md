---
title: Dış Veri Bağlantılarıyla İlgili Sorgu Tabloları ve List Obje Bulma
type: docs
weight: 20
url: /tr/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---

{{% alert color="primary" %}} 

Bazı durumlarda, belirli bir Dış Veri Bağlantısı ile ilişkili Sorgu Tabloları ve List Objelerini bulmanız gerekebilir. Sorgu Tabloları, Bağlantı Kimliği ile ilişkili Dış Veri Bağlantısı nesnesi ile ilişkilidir, List Objeleri ise bir Sorgu Tablosu ile ilişkilidir.

{{% /alert %}} 
## **Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve List Obje Bulma**
Aşağıdaki örnek kodlar, [örnek excel dosyası](5115493.xlsm)'da Dış Veri Bağlantısı ile ilişkili Sorgu Tabloları ve List Obje nasıl bulacağınızı açıklar.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

Yukarıdaki örnek kodları bu [örnek excel dosyası](5115493.xlsm) ile çalıştırdığınızda konsol çıktısı aşağıdaki gibidir.

{{< highlight java >}}

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
{{< app/cells/assistant language="csharp" >}}
