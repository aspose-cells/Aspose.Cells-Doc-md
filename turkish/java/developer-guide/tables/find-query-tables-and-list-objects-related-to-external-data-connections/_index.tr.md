---
title: Dış Veri Bağlantılarıyla İlgili Sorgu Tabloları ve List Obje Bulma
type: docs
weight: 20
url: /tr/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---

## **Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve List Obje Bulma**

Bazı durumlarda, belirli bir Dış Veri Bağlantısı ile ilişkili Sorgu Tabloları ve List Objelerini bulmanız gerekebilir. Sorgu Tabloları, Bağlantı Kimliği ile ilişkili Dış Veri Bağlantısı nesnesi ile ilişkilidir, List Objeleri ise bir Sorgu Tablosu ile ilişkilidir.

Aşağıdaki örnek kod, Dış Veri Bağlantısıyla ilişkili Sorgu Tablolarını ve Liste Nesnelerini nasıl bulabileceğinizi açıklar. Kod, [örnek excel dosyası](5472550.xlsm) kullanır. Bu örnek kodun çıktısını bu makalenin alt kısmında görebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Konsol Çıktısı**

Yukarıdaki örnek kodun konsol çıktısı bu [örnek excel dosyası](5472550.xlsm) kullanılarak elde edilir.

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
{{< app/cells/assistant language="java" >}}
