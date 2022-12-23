---
title: Lettura e scrittura della tabella delle query del foglio di lavoro
type: docs
weight: 40
url: /it/net/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}}

Aspose.Cells fornisce la raccolta Worksheet.QueryTables che restituisce l'oggetto di tipo QueryTable per indice. Ha le seguenti due proprietà

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Questi sono entrambi valori booleani. Puoi visualizzarli in Microsoft Excel tramite Dati > Connessioni > Proprietà.

{{% /alert %}}

## Lettura e scrittura della tabella delle query del foglio di lavoro

Il seguente codice di esempio legge la prima QueryTable del primo foglio di lavoro e quindi stampa entrambe le proprietà QueryTable. Quindi imposta QueryTable.PreserveFormatting su true.

È possibile scaricare il file Excel di origine utilizzato in questo codice e il file Excel di output generato dal codice dai seguenti collegamenti.

- [File Excel di origine](5115533.xlsx)
- [File Excel di output](5115537.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.cs" >}}

### Uscita console

Ecco l'output della console del codice di esempio precedente

{{< highlight "java" >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Recupera l'intervallo dei risultati della tabella delle query

 Aspose.Cells fornisce l'opzione per leggere l'indirizzo, ovvero l'intervallo di celle dei risultati per una tabella di interrogazione. Il codice seguente illustra questa funzionalità leggendo l'indirizzo dell'intervallo di risultati per una tabella di query. Il file di esempio può essere scaricato[qui](72417290.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-ReadingAndWritingQueryTable-ReadingAddressOfResultRange.cs" >}}
