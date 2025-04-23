---
title: Inserisci un immagine basata sul riferimento della cella
type: docs
weight: 150
url: /it/python-net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

A volte si ha un'immagine vuota e bisogna mostrare dati o contenuti nell'immagine impostando un riferimento di cella nella Barra della Formula. Aspose.Cells for Python via .NET supporta questa funzione (Microsoft Excel 2010).

{{% /alert %}}

## Inserimento di un'immagine basata sul riferimento della cella

Aspose.Cells for Python via .NET supporta la visualizzazione del contenuto di una cella del foglio di lavoro in una forma immagine. È possibile collegare l'immagine alla cella che contiene i dati che si vogliono visualizzare. Poiché la cella o l'intervallo di celle è collegato all'oggetto grafico, le modifiche apportate ai dati in quella cella o intervallo di celle appaiono automaticamente nell'oggetto grafico. Aggiungi un'immagine al foglio di lavoro chiamando il metodo [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) della collezione [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Specifica l'intervallo di celle usando l'attributo [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) dell'oggetto [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

### Esempio di codice

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertPictureCellReference-1.py" >}}
