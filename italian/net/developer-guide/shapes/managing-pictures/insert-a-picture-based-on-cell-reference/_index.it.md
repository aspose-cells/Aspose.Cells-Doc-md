---
title: Inserisci un immagine basata sul riferimento della cella
type: docs
weight: 150
url: /it/net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

A volte hai un'immagine vuota e devi mostrare dati o contenuti nell'immagine impostando un riferimento nella Barra delle formule. Aspose.Cells supporta questa funzionalità (Microsoft Excel 2010).

{{% /alert %}}

## Inserimento di un'immagine basata sul riferimento della cella

Aspose.Cells supporta mostrare i contenuti di una cella del foglio di lavoro in una forma di immagine. Puoi collegare l'immagine alla cella che contiene i dati che desideri visualizzare. Poiché la cella o il range di celle è collegato all'oggetto grafico, le modifiche apportate ai dati in quella cella o in quel range di celle compariranno automaticamente nell'oggetto grafico. Aggiungi un'immagine al foglio di lavoro chiamando il metodo [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) della raccolta [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Specifica il range di celle utilizzando l'attributo [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) dell'oggetto [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

### Esempio di codice

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
