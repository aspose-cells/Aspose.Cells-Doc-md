---
title: Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve Liste Nesnelerini Bulun
type: docs
weight: 20
url: /tr/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---
## **Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve Liste Nesnelerini Bulun**

Bazen, bazı Dış Veri Bağlantılarıyla ilgili Sorgu Tablolarını ve Liste Nesnelerini bulmanız gerekir. Sorgu Tabloları, Bağlantı Kimliği olan Dış Veri Bağlantısı nesnesiyle, Liste Nesneleri ise Sorgu Tablosu ile ilişkilidir.

 Aşağıdaki örnek kod, Dış Veri Bağlantısı ile ilgili Sorgu Tablolarını ve Liste Nesnelerini nasıl bulabileceğinizi açıklar. kod kullanır[örnek excel dosyası](5472550.xlsm) verilen bağlantıdan indirebilirsiniz. Bu örnek kodun çıktısını da bu makalenin altında görebilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Konsol Çıkışı**

 İşte bunu kullanan yukarıdaki örnek kodun konsol çıktısı[örnek excel dosyası](5472550.xlsm).

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
