---
title: Aggiorna i valori delle forme collegate
type: docs
weight: 3000
url: /it/java/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

 volte, hai una forma collegata nel tuo file Excel che è collegata a qualche cella. In Microsoft Excel, la modifica del valore della cella collegata modifica anche il valore della forma collegata. Funziona bene anche con Aspose.Cells se si desidera salvare la cartella di lavoro in formato XLS o XLSX. Tuttavia, se desideri salvare la tua cartella di lavoro in formato PDF o HTML, dovrai chiamare[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue()) per aggiornare il valore della forma collegata.

{{% /alert %}}

## Esempio

 Lo screenshot seguente mostra il file Excel di origine utilizzato nel codice di esempio riportato di seguito. Ha un collegamento**Immagine 1** collegato alla cella A1. Cambieremo il valore della cella A1 con Aspose.Cells e quindi chiameremo[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue() ) metodo per aggiornare il valore di**Immagine 1** e salvalo in formato PDF.

![cose da fare:immagine_alt_testo](refresh-values-of-linked-shapes_1.png)

Puoi scaricare il[file Excel di origine](5472956.xlsx) e il[uscita PDF](5472955.pdf) dai link indicati.

### Codice Java per aggiornare i valori delle forme collegate

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
