---
title: Trova Tabelle di Query e Oggetti Elenco relativi a Connessioni Dati Esterne
type: docs
weight: 20
url: /it/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/
---

{{% alert color="primary" %}} 

A volte è necessario scoprire le Tabelle di Query e gli Oggetti Elenco relativi a alcune Connessioni Dati Esterne. Le Tabelle di Query sono correlate all'oggetto Connessione Dati Esterne con Id Connessione, mentre gli Oggetti Elenco sono correlati a una Tabella di Query.

{{% /alert %}} 
## **Trova query tabelle e oggetti elenco relativi alle connessioni esterne dei dati**
I seguenti codici di esempio con [file Excel di esempio](5115493.xlsm) spiegano come trovare tabelle di query e oggetti elenco correlati a una connessione dati esterne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FindQueryTablesAndListObjectsOfExternalDataConnections.py" >}}


Il seguente è l'output della console dell'esecuzione dei codici di esempio precedenti con questo [file Excel di esempio](5115493.xlsm).

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
