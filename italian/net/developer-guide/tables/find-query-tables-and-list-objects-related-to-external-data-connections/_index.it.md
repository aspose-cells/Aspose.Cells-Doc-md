---
title: Trova tabelle di query e oggetti elenco relativi a connessioni dati esterne
type: docs
weight: 20
url: /it/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---
{{% alert color="primary" %}} 

A volte, è necessario scoprire le tabelle di query e gli oggetti elenco relativi ad alcune connessioni dati esterne. Le tabelle di query sono correlate all'oggetto connessione dati esterna con ID connessione, mentre gli oggetti elenco sono correlati a una tabella di query.

{{% /alert %}} 
## **Trova tabelle di query e oggetti elenco relativi a connessioni dati esterne**
 I seguenti codici di esempio con[file excel di esempio](5115493.xlsm) spiegare come trovare le tabelle di query e gli oggetti elenco relativi alla connessione dati esterna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

 Di seguito è riportato l'output della console dell'esecuzione dei codici di esempio precedenti con this[file excel di esempio](5115493.xlsm).

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
