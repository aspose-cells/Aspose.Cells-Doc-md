---
title: Inserisci un immagine in base al riferimento della cella con Golang tramite C++
linktitle: Inserisci un immagine basata sul riferimento della cella
type: docs
weight: 150
url: /it/go-cpp/insert-a-picture-based-on-cell-reference/
description: Impara come inserire un immagine basata sul riferimento di cella usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A volte hai un'immagine vuota e devi mostrare dati o contenuti nell'immagine impostando un riferimento nella Barra delle formule. Aspose.Cells supporta questa funzionalità (Microsoft Excel 2010).

{{% /alert %}}

## Inserimento di un'immagine basata sul riferimento della cella

Aspose.Cells supporta mostrare i contenuti di una cella del foglio di lavoro in una forma di immagine. Puoi collegare l'immagine alla cella che contiene i dati che desideri visualizzare. Poiché la cella o il range di celle è collegato all'oggetto grafico, le modifiche apportate ai dati in quella cella o in quel range di celle compariranno automaticamente nell'oggetto grafico. Aggiungi un'immagine al foglio di lavoro chiamando il metodo [**AddPicture**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpicture_int_int_int_int_stream/) della raccolta [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)). Specifica il range di celle utilizzando l'attributo [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) dell'oggetto [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

### Esempio di codice

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertAPictureBasedOnCellReference.go" >}}
