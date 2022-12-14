---
title: Inserisci un'immagine basata sul riferimento Cell
type: docs
weight: 90
url: /it/java/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

A volte hai un'immagine vuota e devi mostrare dati o contenuti nell'immagine impostando un riferimento di cella nella barra della formula. Aspose.Cells supporta questa funzione (Microsoft Excel 2010).

{{% /alert %}}

## Inserimento di un'immagine basata sul riferimento Cell

Aspose.Cells supporta la visualizzazione del contenuto di una cella del foglio di lavoro in una forma immagine. È possibile collegare l'immagine alla cella che contiene i dati che si desidera visualizzare. Poiché la cella o l'intervallo di celle è collegato all'oggetto grafico, le modifiche ai dati vengono visualizzate automaticamente nell'oggetto grafico. Aggiungi un'immagine al foglio di lavoro chiamando il metodo[**addPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream) ) metodo del[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) raccolta (incapsulata nel file[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) oggetto). Specificare l'intervallo di celle utilizzando il[**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) metodo del[**Immagine**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)oggetto.

Di seguito è riportato uno screenshot del file generato dal codice seguente.

**Inserimento di un'immagine basata sul riferimento di cella**

![cose da fare:immagine_alt_testo](insert-a-picture-based-on-cell-reference_1.png)

## Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
