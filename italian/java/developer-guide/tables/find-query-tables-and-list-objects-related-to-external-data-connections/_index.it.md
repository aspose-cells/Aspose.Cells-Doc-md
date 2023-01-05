---
title: Trova tabelle di query e oggetti elenco relativi a connessioni dati esterne
type: docs
weight: 20
url: /it/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---
## **Trova tabelle di query e oggetti elenco relativi a connessioni dati esterne**

A volte, è necessario scoprire le tabelle di query e gli oggetti elenco relativi ad alcune connessioni dati esterne. Le tabelle di query sono correlate all'oggetto connessione dati esterna con ID connessione, mentre gli oggetti elenco sono correlati a una tabella di query.

 Il seguente codice di esempio spiega come trovare le tabelle di query e gli oggetti elenco correlati alla connessione dati esterna. Il codice utilizza il[file excel di esempio](5472550.xlsm) che puoi scaricare dal link fornito. Puoi anche vedere l'output di questo codice di esempio in fondo a questo articolo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Uscita console**

 Ecco l'output della console del codice di esempio precedente che utilizza this[file excel di esempio](5472550.xlsm).

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
