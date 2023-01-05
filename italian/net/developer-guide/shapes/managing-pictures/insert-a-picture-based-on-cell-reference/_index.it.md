---
title: Inserisci un'immagine basata sul riferimento Cell
type: docs
weight: 150
url: /it/net/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

volte hai un'immagine vuota e devi mostrare dati o contenuti nell'immagine impostando un riferimento di cella nella barra della formula. Aspose.Cells supporta questa funzione (Microsoft Excel 2010).

{{% /alert %}}

## Inserimento di un'immagine basata sul riferimento Cell

Aspose.Cells supporta la visualizzazione del contenuto di una cella del foglio di lavoro in una forma immagine. È possibile collegare l'immagine alla cella che contiene i dati che si desidera visualizzare. Poiché la cella o l'intervallo di celle è collegato all'oggetto grafico, le modifiche apportate ai dati in tale cella o intervallo di celle vengono visualizzate automaticamente nell'oggetto grafico. Aggiungi un'immagine al foglio di lavoro chiamando il metodo[**Aggiungi immagine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) metodo del[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) raccolta (incapsulata nel file[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) oggetto). Specificare l'intervallo di celle utilizzando il[**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) attributo del[**Immagine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)oggetto.

### Esempio di codice

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
