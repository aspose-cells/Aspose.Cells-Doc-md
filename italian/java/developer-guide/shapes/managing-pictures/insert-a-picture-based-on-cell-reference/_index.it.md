---
title: Inserire un immagine basata sul riferimento di una cella
type: docs
weight: 90
url: /it/java/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

A volte hai un'immagine vuota e devi mostrare dati o contenuti nell'immagine impostando un riferimento nella Barra delle formule. Aspose.Cells supporta questa funzionalità (Microsoft Excel 2010).

{{% /alert %}}

## Inserimento di un'immagine basata sul riferimento della cella

Aspose.Cells supporta la visualizzazione del contenuto di una cella del foglio di lavoro in una forma di immagine. È possibile collegare l'immagine alla cella che contiene i dati che si desidera visualizzare. Dato che la cella o il range di celle è collegato all'oggetto grafico, le modifiche ai dati compaiono automaticamente nell'oggetto grafico. Aggiungi un'immagine al foglio di lavoro chiamando il metodo [**addPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture-int-int-int-int-java.io.InputStream-) della collezione [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) (incapsulato nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). Specifica il range di celle utilizzando il metodo [**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) dell'oggetto [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

Di seguito è riportata una schermata del file generato dal codice sottostante.

**Inserimento di un'immagine basata sul riferimento di una cella**

![todo:image_alt_text](insert-a-picture-based-on-cell-reference_1.png)

## Codice di esempio

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
{{< app/cells/assistant language="java" >}}
