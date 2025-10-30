---
title: Aggiorna i valori delle forme collegate
type: docs
weight: 3200
url: /it/python-java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

A volte, hai una forma collegata nel tuo file Excel che è collegata a una cella. In Microsoft Excel, modificando il valore della cella collegata viene modificato anche il valore della forma collegata. Questo funziona anche bene con Aspose.Cells se vuoi salvare il tuo documento di lavoro in formato XLS o XLSX. Tuttavia, se desideri salvare il tuo documento di lavoro in formato PDF o HTML, allora dovrai chiamare il metodo [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue()) per aggiornare il valore della forma collegata.

{{% /alert %}}

## Esempio

La schermata seguente mostra il file Excel di origine utilizzato nel codice di esempio qui sotto. Ha un'immagine collegata collegata alle celle da A1 a E4. Cambieremo il valore della cella B4 con Aspose.Cells e poi chiameremo il metodo [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/python-java/asposecells.api/shapecollection#updateSelectedValue()) per aggiornare il valore dell'immagine e salvarlo in formato PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Puoi scaricare il [file Excel di origine](sampleRefreshValueOfLinkedShapes.xlsx) e il [PDF di output](95584292.pdf) dai link forniti.

### Codice C# per aggiornare i valori delle forme collegate

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-RefreshValueOfLinkedShapes-1.py" >}}
{{< app/cells/assistant language="csharp" >}}
