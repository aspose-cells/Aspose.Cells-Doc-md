---
title: Aggiorna i valori delle forme collegate
type: docs
weight: 3000
url: /it/java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

A volte, hai una forma collegata nel tuo file Excel che è collegata a una cella. In Microsoft Excel, cambiando il valore della cella collegata si cambia anche il valore della forma collegata. Questo funziona anche bene con Aspose.Cells se vuoi salvare il tuo foglio di lavoro in formato XLS o XLSX. Tuttavia, se vuoi salvare il tuo foglio di lavoro in formato PDF o HTML, allora dovrai chiamare il metodo [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) per aggiornare il valore della forma collegata.

{{% /alert %}}

## Esempio

La seguente schermata mostra il file Excel di origine utilizzato nel codice di esempio qui sotto. Ha una **Immagine 1** collegata alla cella A1. Cambieremo il valore della cella A1 con Aspose.Cells e poi chiameremo il metodo [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) per aggiornare il valore di **Immagine 1** e salvarlo in formato PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

Puoi scaricare il [file Excel di origine](5472956.xlsx) e il [PDF di output](5472955.pdf) dai link forniti.

### Codice Java per aggiornare i valori delle forme collegate

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
