---
title: Mostra formule invece di valori in un foglio di lavoro
type: docs
weight: 100
url: /it/java/show-formulas-instead-of-values-in-a-worksheet/
---
{{% alert color="primary" %}}

È possibile mostrare formule invece di valori calcolati in Microsoft Excel utilizzando t*Mostra formule* opzione dal**Formule**nastro. Quando vengono visualizzate le formule, Microsoft Excel visualizza le formule nel foglio di lavoro. Puoi ottenere la stessa cosa usando Aspose.Cells.

{{% /alert %}} 

Aspose.Cells fornisce a[**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) proprietà. Imposta questo su**VERO**per impostare Microsoft Excel per visualizzare le formule.

L'immagine seguente mostra il foglio di lavoro che ha una formula nella cella A3: =Sum(A1:A2).

**Foglio di lavoro con formula nella cella A3**

![cose da fare:immagine_alt_testo](show-formulas-instead-of-values-in-a-worksheet_1.png)

 L'immagine seguente mostra la formula invece del valore calcolato, abilitata impostando il[**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) proprietà a**VERO** con Aspose.Cells.

**Il foglio di lavoro ora mostra la formula invece del valore calcolato**

![cose da fare:immagine_alt_testo](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
