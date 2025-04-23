---
title: Gestione delle immagini
type: docs
weight: 10
url: /it/python-net/managing-pictures/
---

Aspose.Cells per Python via .NET permette agli sviluppatori di aggiungere immagini ai fogli di calcolo in runtime. Inoltre, il posizionamento di queste immagini può essere controllato a runtime, come discusso nelle sezioni successive.

Questo articolo spiega come aggiungere immagini e come inserire un'immagine che mostra il contenuto di determinate celle.

## **Aggiunta di immagini**

Aggiungere immagini a un foglio di calcolo è molto facile. Bastano poche righe di codice:
Basta chiamare il metodo [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) della collezione [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) (incapsulata nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Il metodo [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) accetta i seguenti parametri:

- **Indice della riga in alto a sinistra**, l'indice della riga in alto a sinistra.
- **Indice della colonna in alto a sinistra**, l'indice della colonna in alto a sinistra.
- **Nome del file immagine**, il nome del file immagine, completo di percorso.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-AddingPictures-1.py" >}}

## **Posizionamento delle immagini**

Ci sono due modi possibili per controllare il posizionamento delle immagini usando Aspose.Cells per Python via .NET:

- Posizionamento proporzionale: definire una posizione proporzionale all'altezza e alla larghezza della riga.
- Posizionamento assoluto: definire l'esatta posizione sulla pagina in cui l'immagine sarà inserita, ad esempio, 40 pixel a sinistra e 20 pixel sotto il bordo della cella.

### **Posizionamento proporzionale**

Gli sviluppatori possono posizionare le immagini proporzionalmente all'altezza della riga e alla larghezza della colonna utilizzando le proprietà [**upper_delta_x**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_x) e [**upper_delta_y**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_y) dell'oggetto [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). Un oggetto [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) può essere ottenuto dalla raccolta [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) passando l'indice dell'immagine. Questo esempio posiziona un'immagine nella cella F6.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.py" >}}

### **Posizionamento Assoluto**

Gli sviluppatori possono anche posizionare le immagini in modo assoluto utilizzando le proprietà [**left**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/left) e [**top**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/top) dell'oggetto [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). Questo esempio posiziona un'immagine nella cella F6, 60 pixel a sinistra e 10 pixel dall'alto della cella.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.py" >}}

## **Inserimento di un'immagine in base al riferimento della cella**

Aspose.Cells per Python via .NET ti permette di visualizzare il contenuto di una cella del foglio di lavoro come forma immagine. Puoi collegare l'immagine alla cella che contiene i dati che desideri visualizzare. Dato che la cella, o l'intervallo di celle, è collegata all'oggetto grafico, le modifiche apportate ai dati in quella cella o intervallo di celle appaiono automaticamente nell'oggetto grafico.

Aggiungi un'immagine al foglio di lavoro chiamando il metodo [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) della raccolta [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) (incapsulata nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Specifica il range di celle utilizzando l'attributo [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) dell'oggetto [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PictureCellReference-1.py" >}}

## **Argomenti avanzati**
- [Aggiungi Impostazioni Icona Condizionale con il Testo della Cella](/cells/it/python-net/add-conditional-icons-set-with-the-cell-text/)
- [Inserisci un'immagine collegata dall'indirizzo web](/cells/it/python-net/insert-a-linked-picture-from-web-address/)
- [Inserisci un'immagine basata sul riferimento della cella](/cells/it/python-net/insert-a-picture-based-on-cell-reference/)
- [Caricare un'immagine Web da un URL in un foglio di lavoro Excel](/cells/it/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

