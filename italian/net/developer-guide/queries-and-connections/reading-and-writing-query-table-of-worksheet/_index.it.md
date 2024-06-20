---
title: Lettura e Scrittura Tabelle Query del Foglio di lavoro di Aspose.Cells
type: docs
weight: 40
url: /it/net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la collezione Worksheet.QueryTables che restituisce l'oggetto di tipo QueryTable per indice. Ha le seguenti due proprietà

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Questi sono entrambi valori booleani. È possibile visualizzarli in Microsoft Excel tramite Dati > Connessioni > Proprietà.

{{% /alert %}}

## Lettura e Scrittura della Tabella di Query del Foglio di Lavoro

Il seguente esempio di codice legge la prima QueryTable del primo foglio di lavoro e quindi stampa entrambe le proprietà della QueryTable. Poi imposta il QueryTable.PreserveFormatting su true.

È possibile scaricare il file Excel di origine utilizzato in questo codice e il file Excel di output generato dal codice dai seguenti link.

- [File Excel di Origine](5115533.xlsx)
- [File Excel di Output](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Output della console

Ecco l'output console del codice di esempio sopra

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Recupero dell'intervallo di risultati della tabella di query

Aspose.Cells fornisce l'opzione di leggere l'indirizzo ossia l'intervallo di risultati delle celle per una tabella di query. Il codice seguente dimostra questa funzionalità leggendo l'indirizzo dell'intervallo di risultati per una tabella di query. È possibile scaricare il file di esempio [qui](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
