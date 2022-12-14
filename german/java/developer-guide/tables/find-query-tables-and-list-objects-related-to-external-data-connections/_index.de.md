---
title: Suchen Sie Abfragetabellen und listen Sie Objekte auf, die sich auf externe Datenverbindungen beziehen
type: docs
weight: 20
url: /de/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---
## **Suchen Sie Abfragetabellen und listen Sie Objekte auf, die sich auf externe Datenverbindungen beziehen**

Manchmal müssen Sie Abfragetabellen herausfinden und Objekte auflisten, die sich auf eine externe Datenverbindung beziehen. Abfragetabellen beziehen sich auf ein externes Datenverbindungsobjekt mit Verbindungs-ID, während Listenobjekte auf eine Abfragetabelle bezogen sind.

 Der folgende Beispielcode erläutert, wie Sie Abfragetabellen und Listenobjekte im Zusammenhang mit externer Datenverbindung finden können. Der Code verwendet die[Excel-Beispieldatei](5472550.xlsm) die Sie über den angegebenen Link herunterladen können. Sie können die Ausgabe dieses Beispielcodes auch am Ende dieses Artikels sehen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Konsolenausgabe**

 Hier ist die Konsolenausgabe des obigen Beispielcodes, der this verwendet[Excel-Beispieldatei](5472550.xlsm).

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
