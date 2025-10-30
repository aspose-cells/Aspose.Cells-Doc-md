---
title: Aggiorna i valori delle forme collegate con Golang tramite C++
linktitle: Aggiorna i valori delle forme collegate
type: docs
weight: 3200
url: /it/go-cpp/refresh-values-of-linked-shapes/
description: Impara come aggiornare i valori delle forme collegate nei file Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte, hai una forma collegata nel tuo file Excel che è collegata a una cella. In Microsoft Excel, modificando il valore della cella collegata viene modificato anche il valore della forma collegata. Questo funziona anche bene con Aspose.Cells se vuoi salvare il tuo documento di lavoro in formato XLS o XLSX. Tuttavia, se desideri salvare il tuo documento di lavoro in formato PDF o HTML, allora dovrai chiamare il metodo [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/) per aggiornare il valore della forma collegata.

{{% /alert %}}

## Esempio

Lo screenshot seguente mostra il file Excel di origine utilizzato nel codice di esempio qui sotto. Ha un'immagine collegata collegata alle celle A1 a E4. Modificheremo il valore della cella B4 con Aspose.Cells e poi chiameremo il metodo [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/) per aggiornare il valore dell'immagine e salvarlo in formato PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Puoi scaricare il [file Excel di origine](95584291.xlsx) e il [PDF di output](95584292.pdf) dai link forniti.

### Codice C++ per aggiornare i valori delle forme collegate

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshValuesOfLinkedShapes.go" >}}
