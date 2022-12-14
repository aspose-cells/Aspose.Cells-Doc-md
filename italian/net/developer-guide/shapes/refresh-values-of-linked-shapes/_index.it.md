---
title: Aggiorna i valori delle forme collegate
type: docs
weight: 3200
url: /it/net/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

 volte, hai una forma collegata nel tuo file Excel che è collegata a qualche cella. In Microsoft Excel, la modifica del valore della cella collegata modifica anche il valore della forma collegata. Funziona bene anche con Aspose.Cells se si desidera salvare la cartella di lavoro in formato XLS o XLSX. Tuttavia, se desideri salvare la tua cartella di lavoro in formato PDF o HTML, dovrai chiamare[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) metodo per aggiornare il valore della forma collegata.

{{% /alert %}}

## Esempio

 Lo screenshot seguente mostra il file Excel di origine utilizzato nel codice di esempio riportato di seguito. Ha un'immagine collegata collegata alle celle da A1 a E4. Cambieremo il valore della cella B4 con Aspose.Cells e quindi chiameremo[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)metodo per aggiornare il valore dell'immagine e salvarla in formato PDF.

![cose da fare:immagine_alt_testo](refresh-values-of-linked-shapes_1.jpg)

Puoi scaricare il[file Excel di origine](95584291.xlsx) e il[uscita PDF](95584292.pdf) dai link indicati.

### C# codice per aggiornare i valori delle forme collegate

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
