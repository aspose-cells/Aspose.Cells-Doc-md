---
title: Lettura e Scrittura Tabelle Query del Foglio di lavoro di Aspose.Cells
type: docs
weight: 40
url: /it/python-net/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET fornisce la collezione Worksheet.QueryTables che restituisce l'oggetto di tipo QueryTable tramite indice. Ha le seguenti due proprietà

- QueryTable.AdjustColumnWidth
- QueryTable.PreserveFormatting

Questi sono entrambi valori booleani. È possibile visualizzarli in Microsoft Excel tramite Dati > Connessioni > Proprietà.

{{% /alert %}}

## Lettura e Scrittura della Tabella di Query del Foglio di Lavoro

Il seguente esempio di codice legge la prima QueryTable del primo foglio di lavoro e quindi stampa entrambe le proprietà della QueryTable. Poi imposta il QueryTable.PreserveFormatting su true.

È possibile scaricare il file Excel di origine utilizzato in questo codice e il file Excel di output generato dal codice dai seguenti link.

- [File Excel di Origine](5115533.xlsx)
- [File Excel di Output](5115537.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAndWritingQueryTable.py" >}}

### Output della console

Ecco l'output console del codice di esempio sopra

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Recupero dell'intervallo di risultati della tabella di query

Aspose.Cells per Python via .NET fornisce l'opzione di leggere l'indirizzo, cioè l'intervallo di risultato delle celle, di una tabella di query. Il codice seguente dimostra questa funzione leggendo l'indirizzo dell'intervallo di risultato per una tabella di query. Il file di esempio può essere scaricato [qui](72417290.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-ReadingAddressOfResultRange.py" >}}

{{< app/cells/assistant language="python-net" >}}
