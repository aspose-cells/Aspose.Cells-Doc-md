---
title: Forme nei grafici
type: docs
weight: 70
url: /it/net/controls-in-charts/
---
{{% alert color="primary" %}}

volte è necessario inserire oggetti di disegno come etichette, caselle di testo, immagini e così via in un grafico. Aspose.Cells può aggiungere i controlli a un grafico in fase di esecuzione.

{{% /alert %}}

## **Aggiunta del controllo etichetta al grafico**

Le etichette forniscono un mezzo per fornire informazioni agli utenti sul contenuto di un foglio di calcolo.
Aspose.Cells consente di aggiungere e manipolare etichette anche nei grafici.

Il[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**AddLabelInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart), utilizzato per aggiungere un controllo etichetta a un grafico. Di seguito è riportato un elenco dei parametri utilizzati per il metodo:

- **superiore** – l'offset verticale dell'etichetta dall'angolo superiore sinistro in unità di 1/4000 dell'area del grafico.
- **sinistra** – l'offset verticale dell'etichetta dall'angolo superiore sinistro in unità di 1/4000 dell'area del grafico.
- **altezza** – l'altezza dell'etichetta, in unità di 1/4000 dell'area del grafico.
- **larghezza** – la larghezza dell'etichetta, in unità di 1/4000 dell'area del grafico.

 Il metodo ritorna[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)oggetto. Il[**Etichetta**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) class rappresenta un'etichetta nel grafico. Ha alcuni membri importanti:

- [**Testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(proprietà) – specifica la stringa di didascalia di un'etichetta.
- [**Riempire**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (proprietà) – specifica gli attributi del colore di riempimento.

L'esempio seguente mostra come aggiungere un'etichetta al grafico. L'esempio utilizza un file di progettazione (**exp_piechart.xls**) che contiene un grafico. Utilizziamo questo file per inserire un'etichetta nel grafico. Di seguito è riportato il codice originale per l'aggiunta di un'etichetta al grafico. Il seguente output viene generato durante l'esecuzione del codice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

## **Aggiunta del controllo TextBox al grafico**

 Un modo per evidenziare informazioni importanti in un report consiste nell'utilizzare una casella di testo. Ad esempio, inserisci il testo per evidenziare il nome dell'azienda o per indicare l'area geografica con le vendite più elevate. Il[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**AddTextBoxInChart**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart)utilizzato per aggiungere un controllo casella di testo a un grafico. Di seguito è riportato l'elenco dei parametri utilizzati per il metodo:

- **superiore** – l'offset verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **sinistra** – l'offset verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **altezza**– l'altezza della casella di testo, in unità di 1/4000 dell'area del grafico.
- **larghezza** – la larghezza della casella di testo, in unità di 1/4000 dell'area del grafico.

 Il metodo ritorna[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) oggetto. Il[**Casella di testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)class rappresenta una casella di testo nel grafico.

L'esempio seguente mostra come aggiungere una casella di testo a un grafico. L'esempio utilizza il file di progettazione precedente (**exp_piechart.xls**) che contiene un grafico. Utilizziamo questo file per inserire una casella di testo nel grafico per mostrare il titolo del grafico. Di seguito è riportato il codice originale per l'aggiunta di una casella di testo al grafico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

## **Aggiunta di immagini al grafico**

Aspose.Cells consente di inserire immagini in un grafico. Ad esempio, aggiungi un'immagine per enfatizzare o dare più significato a un grafico o al suo contenuto, oppure inserisci un file di immagine del marchio.

 Il[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) class fornisce un metodo denominato[**Aggiungi immagine nel grafico**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart), utilizzato per aggiungere un oggetto immagine al grafico. Di seguito è riportato l'elenco dei parametri utilizzati per il metodo:

- **superiore**– l'offset verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **sinistra**– l'offset verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **flusso** – un oggetto stream che contiene i dati dell'immagine.
- **widthScale** – la scala della larghezza dell'immagine, un valore percentuale.
- **heightScala** – la scala dell'altezza dell'immagine, un valore percentuale.

 Il metodo restituisce un[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) oggetto. Il[**Immagine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)class rappresenta un oggetto immagine nel grafico.

L'esempio seguente mostra come aggiungere un'immagine al grafico. L'esempio utilizza il file di progettazione precedente (**exp_piechart.xls**) che contiene un grafico. Usiamo questo file per inserire un'immagine nel grafico. Di seguito è riportato il codice originale per l'aggiunta di immagini al grafico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

## **Aggiunta di una casella di controllo nel grafico**

 Aspose.Cells consente di inserire caselle di controllo in un foglio grafico utilizzando[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) enumerazione. L'esempio seguente mostra l'aggiunta di una casella di controllo a un foglio grafico.

L'immagine seguente mostra il foglio grafico con la casella di controllo nel file di output.

![cose da fare:immagine_alt_testo](controls-in-charts_1.jpg)

 Il[file di uscita](101089316.xlsx)generato dal seguente frammento di codice è allegato come riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

## **Argomenti avanzati**
- [Aggiungi filigrana WordArt al grafico](/cells/it/net/add-wordart-watermark-to-chart/)
