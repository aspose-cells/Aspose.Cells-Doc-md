---
title: Lettura e scrittura della tabella delle query del foglio di lavoro
type: docs
weight: 560
url: /it/java/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}} 

 Aspose.Cells fornisce[Foglio di lavoro.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) raccolta che restituisce il file[QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection) . Per ottenere uno specifico[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) , utilizzare il[QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\) ) e passare l'indice della QueryTable. Il[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) class ha le seguenti due proprietà per la regolazione della QueryTable.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Questi sono entrambi valori booleani. È possibile visualizzarli in Microsoft Excel tramite Dati > Connessioni > Proprietà.

{{% /alert %}} 
## **Lettura e scrittura della tabella delle query del foglio di lavoro**
 Il codice di esempio seguente legge il primo[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)del primo foglio di lavoro e quindi stampa entrambi i file[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) proprietà. Quindi imposta il[QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) a**VERO**.

Lo screenshot seguente mostra il[file excel di origine](5472578.xlsx) utilizzato nel codice e le sue proprietà che mostrano entrambi i[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)i valori.

![cose da fare:immagine_alt_testo](reading-and-writing-query-table-of-worksheet_1.png)

Lo screenshot seguente mostra il[file excel di output](5472574.xlsx) generato dal codice e dalle sue proprietà che mostrano entrambi i file[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)i valori. Come puoi vedere, la casella di controllo Formattazione conservata è selezionata ora.

![cose da fare:immagine_alt_testo](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Uscita console**
Ecco l'output della console del codice di esempio precedente

{{< highlight "java" >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}
## **Recupera l'intervallo dei risultati della tabella delle query**
Aspose.Cells offre la possibilità di leggere l'indirizzo, ovvero l'intervallo di risultati delle celle per una tabella di interrogazione. Il codice seguente illustra questa funzionalità leggendo l'indirizzo dell'intervallo di risultati per una tabella di query. Il file di esempio può essere scaricato[qui](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
