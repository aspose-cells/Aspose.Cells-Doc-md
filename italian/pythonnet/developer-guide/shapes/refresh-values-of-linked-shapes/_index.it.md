---
title: Aggiorna i valori delle forme collegate
type: docs
weight: 3200
url: /it/python-net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

A volte, nel tuo file Excel, hai una forma collegata a qualche cella. In Microsoft Excel, cambiare il valore della cella collegata cambia anche il valore della forma collegata. Questo funziona bene anche con Aspose.Cells per Python via .NET se vuoi salvare il tuo documento in formato XLS o XLSX. Tuttavia, se vuoi salvare il documento in formato PDF o HTML, allora dovrai chiamare il metodo [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) per aggiornare il valore della forma collegata.

{{% /alert %}}

## Esempio

Lo screenshot seguente mostra il file Excel di origine utilizzato nel codice di esempio sotto. Ha un'immagine collegata collegata alle celle A1 a E4. Cambieremo il valore della cella B4 con Aspose.Cells per Python via .NET e quindi chiameremo il metodo [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) per aggiornare il valore dell'immagine e salvarla in formato PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

È possibile scaricare il [file Excel di origine](95584291.xlsx) e il [PDF di output](95584292.pdf) dai link forniti.

### Codice C# per aggiornare i valori delle forme collegate

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-RefreshValueOfLinkedShapes-1.py" >}}
