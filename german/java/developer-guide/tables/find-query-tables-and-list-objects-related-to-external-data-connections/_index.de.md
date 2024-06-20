---
title: Suchen Sie Abfrage Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen
type: docs
weight: 20
url: /de/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---

## **Abfrage-Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen finden**

Manchmal müssen Sie Abfrage-Tabellen und Listenobjekte im Zusammenhang mit einer externen Datenverbindung finden. Abfrage-Tabellen sind mit der Verbindungs-ID des externen Datenverbindungsobjekts verbunden, während Listenobjekte mit einer Abfrage-Tabelle verbunden sind.

Der folgende Beispielcode erklärt, wie Sie Abfrage-Tabellen und Listenobjekte im Zusammenhang mit einer externen Datenverbindung finden können. Der Code verwendet die [Beispiel-Excel-Datei](5472550.xlsm), die Sie über den bereitgestellten Link herunterladen können. Sie können auch die Ausgabe dieses Beispielcodes am Ende dieses Artikels sehen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes unter Verwendung dieser [Beispiel-Excel-Datei](5472550.xlsm).

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
