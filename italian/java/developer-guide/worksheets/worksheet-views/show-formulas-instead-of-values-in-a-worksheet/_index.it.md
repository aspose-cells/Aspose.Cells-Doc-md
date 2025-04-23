---
title: Mostrare le Formule invece dei Valori in un Foglio di Lavoro
type: docs
weight: 100
url: /it/java/show-formulas-instead-of-values-in-a-worksheet/
---

{{% alert color="primary" %}}

È possibile mostrare le formule invece dei valori calcolati in Microsoft Excel utilizzando l'opzione *Mostra Formule* dalla barra **Formule**. Quando vengono mostrate le formule, Microsoft Excel visualizza le formule nel foglio di lavoro. È possibile ottenere lo stesso risultato utilizzando Aspose.Cells.

{{% /alert %}} 

Aspose.Cells fornisce una proprietà [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas). Impostarla su **true** per impostare Microsoft Excel per mostrare le formule.

L'immagine seguente mostra il foglio di lavoro che ha una formula nella cella A3: =Somma(A1:A2).

**Foglio di lavoro con formula nella cella A3**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

L'immagine seguente mostra la formula invece del valore calcolato, abilitato impostando la proprietà [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) su **true** con Aspose.Cells.

**Il foglio di lavoro ora mostra la formula invece del valore calcolato**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
{{< app/cells/assistant language="java" >}}
