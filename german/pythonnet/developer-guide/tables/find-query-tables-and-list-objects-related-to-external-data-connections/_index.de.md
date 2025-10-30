---
title: Suchen Sie Abfrage Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen
type: docs
weight: 20
url: /de/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/
---

{{% alert color="primary" %}} 

Manchmal müssen Sie Abfrage-Tabellen und Listenobjekte im Zusammenhang mit einer externen Datenverbindung finden. Abfrage-Tabellen sind mit der Verbindungs-ID des externen Datenverbindungsobjekts verbunden, während Listenobjekte mit einer Abfrage-Tabelle verbunden sind.

{{% /alert %}} 
## **Abfrage-Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen finden**
Die folgenden Beispielcodes mit der [Beispiel-Excel-Datei](5115493.xlsm) erläutern, wie man Abfrage-Tabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen finden kann.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FindQueryTablesAndListObjectsOfExternalDataConnections.py" >}}


Folgendes ist die Konsolenausgabe beim Ausführen der oben genannten Beispielcodes mit dieser [Beispiel-Excel-Datei](5115493.xlsm).

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

{{< app/cells/assistant language="python-net" >}}
