---
title: Suchen Sie Abfragetabellen und listen Sie Objekte auf, die sich auf externe Datenverbindungen beziehen
type: docs
weight: 20
url: /de/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---
{{% alert color="primary" %}} 

Manchmal müssen Sie Abfragetabellen herausfinden und Objekte auflisten, die sich auf eine externe Datenverbindung beziehen. Abfragetabellen beziehen sich auf ein externes Datenverbindungsobjekt mit Verbindungs-ID, während Listenobjekte auf eine Abfragetabelle bezogen sind.

{{% /alert %}} 
## **Suchen Sie Abfragetabellen und listen Sie Objekte auf, die sich auf externe Datenverbindungen beziehen**
 Die folgenden Beispielcodes mit[Excel-Beispieldatei](5115493.xlsm) erklären, wie Abfragetabellen und Listenobjekte im Zusammenhang mit externen Datenverbindungen gefunden werden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

 Das Folgende ist die Konsolenausgabe der Ausführung der obigen Beispielcodes damit[Excel-Beispieldatei](5115493.xlsm).

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
