---
title: Rileva Cells unito in un foglio di lavoro
type: docs
weight: 3000
url: /it/java/detect-merged-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

In Microsoft Excel, più celle possono essere unite in una sola. Questo è spesso usato per creare tabelle complesse o per creare una cella che contiene un'intestazione che si estende su più colonne.

Aspose.Cells consente di identificare le aree di celle unite in un foglio di lavoro. Puoi separarli anche tu. Questo articolo fornisce le righe di codice più semplici per eseguire l'attività utilizzando Aspose.Cells.

Questo articolo fornisce istruzioni compatte su come trovare e separare le celle unite in un foglio di lavoro.

{{% /alert %}}

## **Dimostrazione**

 Questo esempio usa un file Excel modello Microsoft chiamato**MergeTrial**. Ha alcune aree di celle unite in un foglio chiamato anche Merge Trial.

**Il file modello**

![cose da fare:immagine_alt_testo](detect-merged-cells-in-a-worksheet_1.png)

 Aspose.Cells fornisce il[**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells)metodo utilizzato per ottenere un ArrayList di aree di celle unite.

Quando viene eseguito il codice seguente, cancella il contenuto del foglio e separa tutte le aree delle celle prima di salvare nuovamente il file.

**Il file di output**

![cose da fare:immagine_alt_testo](detect-merged-cells-in-a-worksheet_2.png)

## **Esempio di codice**

Vedere il seguente codice di esempio per scoprire come identificare le aree di celle unite in un foglio di lavoro e separarle.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **articoli Correlati**

- [Unire e dividere le celle](/cells/it/java/merging-and-unmerging-cells/).
