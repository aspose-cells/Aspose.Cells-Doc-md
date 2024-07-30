---
title: Rilevare celle unite in un foglio di lavoro
type: docs
weight: 3000
url: /it/java/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

In Microsoft Excel, diverse celle possono essere unite in una. Questo viene spesso utilizzato per creare tabelle complesse o per creare una cella che contiene un'intestazione che si estende su diverse colonne.

Aspose.Cells ti consente di identificare aree di celle unite in un foglio di lavoro. Puoi anche dividerle. Questo articolo fornisce le linee di codice più semplici per eseguire il compito utilizzando Aspose.Cells.

Questo articolo fornisce istruzioni compatte su come individuare e poi separare le celle unite in un foglio di lavoro.

{{% /alert %}}

## **Dimostrazione**

Questo esempio utilizza un file modello di Microsoft Excel chiamato **MergeTrial**. Ha alcune aree di celle unite in un foglio chiamato Merge Trial.

**Il file di modello**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

Aspose.Cells fornisce il metodo [**Cells.getMergedCells()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells/#getMergedCells--) che viene utilizzato per ottenere tutte le celle unite.

Quando viene eseguito il codice seguente, cancella i contenuti del foglio e separa tutte le aree delle celle prima di salvare nuovamente il file.

**Il file di output**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **Esempio di codice**

Si prega di vedere il seguente codice di esempio per scoprire come identificare le aree di celle unite in un foglio di lavoro e separarle.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **Articoli Correlati**

- [Unione e separazione delle celle](/cells/it/java/unione-e-separazione-delle-celle/).
