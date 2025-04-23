---
title: Hitta frågetabeller och lista objekt relaterade till externa dataanslutningar
type: docs
weight: 20
url: /sv/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---

## **Hitta frågetabeller och lista objekt relaterade till externa dataanslutningar**

Ibland behöver du ta reda på frågetabeller och lista objekt relaterade till någon extern dataanslutning. Frågetabeller är relaterade till objekt för extern dataanslutning med anslutnings-ID, medan lista objekt är relaterade till en frågetabell.

Följande exempelkod förklarar hur du kan hitta frågetabeller och listobjekt relaterade till extern dataanslutning. Koden använder [prov excelfil](5472550.xlsm) som du kan ladda ner från den angivna länken. Du kan också se resultatet av denna exempelkod längst ner i den här artikeln.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Konsoloutput**

Här är konsolresultatet av ovanstående exempelkod med hjälp av denna [prov excelfil](5472550.xlsm).

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
