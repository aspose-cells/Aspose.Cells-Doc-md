---
title: Trova Tabelle di Query e Oggetti Elenco relativi a Connessioni Dati Esterne
type: docs
weight: 20
url: /it/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---

## **Trova query tabelle e oggetti elenco relativi alle connessioni esterne dei dati**

A volte è necessario scoprire le Tabelle di Query e gli Oggetti Elenco relativi a alcune Connessioni Dati Esterne. Le Tabelle di Query sono correlate all'oggetto Connessione Dati Esterne con Id Connessione, mentre gli Oggetti Elenco sono correlati a una Tabella di Query.

Il codice di esempio seguente spiega come trovare le Tabelle di Query e gli Oggetti Elenco correlati a una Connessione Dati Esterna. Il codice utilizza il [file di lavoro di esempio](5472550.xlsm) che puoi scaricare dal link fornito. Puoi anche vedere l'output di questo codice di esempio in fondo a questo articolo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **Output della console**

Ecco l'output della console del codice di esempio sopra utilizzando questo [file di lavoro di esempio](5472550.xlsm).

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
