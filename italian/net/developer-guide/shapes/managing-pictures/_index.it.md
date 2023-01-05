---
title: Gestione delle immagini
type: docs
weight: 10
url: /it/net/managing-pictures/
---
Aspose.Cells consente agli sviluppatori di aggiungere immagini ai fogli di calcolo in fase di esecuzione. Inoltre, il posizionamento di queste immagini può essere controllato in fase di esecuzione, come discusso più dettagliatamente nelle prossime sezioni.

Questo articolo spiega come aggiungere immagini e come inserire un'immagine che mostri il contenuto di determinate celle.

## **Aggiunta di immagini**

L'aggiunta di immagini a un foglio di calcolo è molto semplice. Bastano poche righe di codice:
 Basta chiamare il[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) metodo del[**Immagini**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) raccolta (incapsulata nel file[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) oggetto). Il[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)metodo accetta i seguenti parametri:

- **Indice della riga in alto a sinistra**, l'indice della riga in alto a sinistra.
- **Indice colonna in alto a sinistra**, l'indice della colonna in alto a sinistra.
- **Nome file immagine**, il nome del file immagine, completo di percorso.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Immagini di posizionamento**

Esistono due modi possibili per controllare il posizionamento delle immagini utilizzando Aspose.Cells:

- Posizionamento proporzionale: definire una posizione proporzionale all'altezza e alla larghezza della riga.
- Posizionamento assoluto: definire la posizione esatta sulla pagina in cui verrà inserita l'immagine, ad esempio 40 pixel a sinistra e 20 pixel sotto il bordo della cella.

### **Posizionamento proporzionale**

 Gli sviluppatori possono posizionare le immagini proporzionalmente all'altezza della riga e alla larghezza della colonna utilizzando il formato[**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) e[**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) proprietà del[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) oggetto. UN[**Immagine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) oggetto può essere ottenuto dal[**Immagini**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)raccolta passando il relativo indice delle immagini. Questo esempio inserisce un'immagine nella cella F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Posizionamento assoluto**

 Gli sviluppatori possono anche posizionare le immagini in modo assoluto utilizzando il file[**Sinistra**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) e[**Superiore**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) proprietà del[**Immagine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)oggetto. Questo esempio posiziona un'immagine nella cella F6, 60 pixel da sinistra e 10 pixel dalla parte superiore della cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Inserimento di un'immagine basata sul riferimento Cell**

Aspose.Cells consente di visualizzare il contenuto di una cella del foglio di lavoro in una forma immagine. È possibile collegare l'immagine alla cella che contiene i dati che si desidera visualizzare. Poiché la cella o l'intervallo di celle è collegato all'oggetto grafico, le modifiche apportate ai dati in tale cella o intervallo di celle vengono visualizzate automaticamente nell'oggetto grafico.

 Aggiungi un'immagine al foglio di lavoro chiamando il metodo[**Aggiungi immagine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) metodo del[**Collezione Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) raccolta (incapsulata nel file[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) oggetto). Specificare l'intervallo di celle utilizzando il[**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) attributo del[**Immagine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)oggetto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Argomenti avanzati**
- [Aggiungi set di icone condizionali con il testo Cell](/cells/it/net/add-conditional-icons-set-with-the-cell-text/)
- [Inserisci un'immagine collegata dall'indirizzo web](/cells/it/net/insert-a-linked-picture-from-web-address/)
- [Inserisci un'immagine basata sul riferimento Cell](/cells/it/net/insert-a-picture-based-on-cell-reference/)
- [Carica un'immagine Web da un URL in un foglio di lavoro Excel](/cells/it/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

