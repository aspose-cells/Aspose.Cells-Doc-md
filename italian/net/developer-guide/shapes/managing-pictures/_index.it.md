---
title: Gestione delle immagini
type: docs
weight: 10
url: /it/net/managing-pictures/
---

Aspose.Cells consente ai programmatori di aggiungere immagini ai fogli di calcolo in fase di esecuzione. Inoltre, la posizione di queste immagini può essere controllata in fase di esecuzione, come discusso più in dettaglio nelle sezioni successive.

Questo articolo spiega come aggiungere immagini e come inserire un'immagine che mostra il contenuto di determinate celle.

## **Aggiunta di immagini**

Aggiungere immagini a un foglio di calcolo è molto facile. Bastano poche righe di codice:
Basta chiamare il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) della collezione [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) (incapsulata nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Il metodo [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) accetta i seguenti parametri:

- **Indice della riga in alto a sinistra**, l'indice della riga in alto a sinistra.
- **Indice della colonna in alto a sinistra**, l'indice della colonna in alto a sinistra.
- **Nome del file immagine**, il nome del file immagine, completo di percorso.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Posizionamento delle immagini**

Ci sono due possibili modi per controllare il posizionamento delle immagini utilizzando Aspose.Cells:

- Posizionamento proporzionale: definire una posizione proporzionale all'altezza e alla larghezza della riga.
- Posizionamento assoluto: definire l'esatta posizione sulla pagina in cui l'immagine sarà inserita, ad esempio, 40 pixel a sinistra e 20 pixel sotto il bordo della cella.

### **Posizionamento proporzionale**

Gli sviluppatori possono posizionare le immagini proporzionalmente all'altezza della riga e alla larghezza della colonna utilizzando le proprietà [**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) e [**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) dell'oggetto [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). Un oggetto [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) può essere ottenuto dalla raccolta [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) passando l'indice dell'immagine. Questo esempio posiziona un'immagine nella cella F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Posizionamento Assoluto**

Gli sviluppatori possono anche posizionare le immagini in modo assoluto utilizzando le proprietà [**Left**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) e [**Top**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) dell'oggetto [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture). Questo esempio posiziona un'immagine nella cella F6, 60 pixel a sinistra e 10 pixel dall'alto della cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Inserimento di un'immagine in base al riferimento della cella**

Aspose.Cells consente di visualizzare i contenuti di una cella del foglio di lavoro in una forma di immagine. È possibile collegare l'immagine alla cella che contiene i dati che si desidera visualizzare. Poiché la cella, o il range di celle, è collegata all'oggetto grafico, le modifiche apportate ai dati in quella cella o in quel range di celle appaiono automaticamente nell'oggetto grafico.

Aggiungi un'immagine al foglio di lavoro chiamando il metodo [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) della raccolta [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (incapsulata nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Specifica il range di celle utilizzando l'attributo [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) dell'oggetto [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Argomenti avanzati**
- [Aggiungi Impostazioni Icona Condizionale con il Testo della Cella](/cells/it/net/add-conditional-icons-set-with-the-cell-text/)
- [Inserisci un'immagine collegata dall'indirizzo web](/cells/it/net/insert-a-linked-picture-from-web-address/)
- [Inserisci un'immagine basata sul riferimento della cella](/cells/it/net/insert-a-picture-based-on-cell-reference/)
- [Caricare un'immagine Web da un URL in un foglio di lavoro Excel](/cells/it/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="csharp" >}}
