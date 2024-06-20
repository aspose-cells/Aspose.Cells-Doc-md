---
title: Lettura e Scrittura Tabelle Query del Foglio di lavoro di Aspose.Cells
type: docs
weight: 560
url: /it/java/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}} 

Aspose.Cells fornisce la collezione Worksheet.getQueryTables() che restituisce la QueryTableCollection. Per ottenere un QueryTable specifico, utilizza la proprietà QueryTableCollection.get() e passa l'indice della QueryTable. La classe QueryTable ha le seguenti due proprietà per regolare la QueryTable.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Entrambi sono valori booleani. Puoi visualizzarli in Microsoft Excel tramite Dati > Connessioni > Proprietà.

{{% /alert %}} 
## **Lettura e Scrittura della Tabella Query del Foglio di Lavoro**
Il codice di esempio seguente legge la prima [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) della prima scheda e poi stampa entrambe le proprietà del [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable). Successivamente imposta [QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) su **true**.

Lo screenshot seguente mostra il file Excel di origine](5472578.xlsx) utilizzato nel codice e le relative proprietà mostrando entrambi i valori del [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable).

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_1.png)

Lo screenshot seguente mostra il file Excel di output](5472574.xlsx) generato dal codice e le relative proprietà che mostrano entrambi i valori del [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable). Come puoi vedere, ora la casella di controllo della formattazione conservata è selezionata.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Output della console**
Ecco l'output console del codice di esempio sopra

{{< highlight java >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}

## **Recupera l'intervallo di risultati della query table**
Aspose.Cells fornisce l'opzione per leggere l'indirizzo, cioè l'intervallo di risultati delle celle per una tabella di query. Il codice seguente dimostra questa funzionalità, leggendo l'indirizzo dell'intervallo di risultati per una tabella di query. Il file di esempio può essere scaricato [qui](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
