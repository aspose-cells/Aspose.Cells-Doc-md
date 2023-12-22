---
title: Forme nei grafici
description: Scopri come utilizzare Aspose.Cells for .NET per aggiungere controlli e personalizzare i grafici in Microsoft Excel. La nostra guida mostrerà come manipolare gli elementi del grafico, regolare la formattazione e migliorare l'aspetto generale e l'usabilità dei grafici.
keywords: Aspose.Cells for .NET, Chart Controls, Chart Customization, Microsoft Excel, Chart Elements, Formatting.
type: docs
weight: 70
url: /it/net/controls-in-charts/
---
{{% alert color="primary" %}}

A volte è necessario inserire oggetti di disegno come etichette, caselle di testo, immagini e così via in un grafico. Aspose.Cells può aggiungere i controlli a un grafico in fase di esecuzione.

{{% /alert %}}

##  **Aggiunta del controllo etichetta al grafico**

Le etichette forniscono un mezzo per fornire informazioni agli utenti sul contenuto di un foglio di calcolo.
Aspose.Cells ti consente di aggiungere e manipolare etichette anche nei grafici.

IL[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) La classe fornisce un metodo denominato[**Aggiungi etichetta nel grafico**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabelinchart), utilizzato per aggiungere un controllo etichetta a un grafico. Di seguito l'elenco dei parametri utilizzati per il metodo:

- **superiore**– l'offset verticale dell'etichetta dall'angolo superiore sinistro in unità di 1/4000 dell'area della carta.
- **Sinistra**– l'offset verticale dell'etichetta dall'angolo superiore sinistro in unità di 1/4000 dell'area della carta.
- **altezza** – l'altezza dell'etichetta, in unità di 1/4000 dell'area grafica.
- **larghezza** – la larghezza dell'etichetta, in unità di 1/4000 dell'area della carta.

 Il metodo ritorna[**Aspose.Cells.Drawing.Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label)oggetto. IL[**Etichetta**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) la classe rappresenta un'etichetta nel grafico. Ha alcuni membri importanti:

- [**Testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)(proprietà) – specifica la stringa di didascalia di un'etichetta.
- [**Riempire**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fill) (proprietà) – specifica gli attributi del colore di riempimento.

L'esempio seguente mostra come aggiungere un'etichetta al grafico. L'esempio utilizza un file di progettazione (**exp_piechart.xls**) che contiene un grafico. Usiamo questo file per inserire un'etichetta nel grafico. Di seguito è riportato il codice originale per aggiungere un'etichetta al grafico. Il seguente output viene generato durante l'esecuzione del codice.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingLabelControl-1.cs" >}}

##  **Aggiunta del controllo TextBox al grafico**

Un modo per evidenziare informazioni importanti in un report consiste nell'utilizzare una casella di testo. Ad esempio, inserisci il testo per evidenziare il nome dell'azienda o per indicare la regione geografica con le vendite più elevate. IL[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) La classe fornisce un metodo denominato[**Aggiungi casella di testo nel grafico**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addtextboxinchart), che viene utilizzato per aggiungere un controllo casella di testo a un grafico. Di seguito è riportato l'elenco dei parametri utilizzati per il metodo:

- **superiore** – l'offset verticale della casella di testo dall'angolo superiore sinistro in unità di 1/4000 dell'area del grafico.
- **Sinistra** – l'offset verticale della casella di testo dall'angolo superiore sinistro in unità di 1/4000 dell'area del grafico.
- **altezza** – l'altezza della casella di testo, in unità di 1/4000 dell'area del grafico.
- **larghezza** – la larghezza della casella di testo, in unità di 1/4000 dell'area del grafico.

 Il metodo ritorna[**Aspose.Cells.Drawing.TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox) oggetto. IL[**Casella di testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)La classe rappresenta una casella di testo nel grafico.

L'esempio seguente mostra come aggiungere una casella di testo a un grafico. L'esempio utilizza il file di progettazione precedente (**exp_piechart.xls**) che contiene un grafico. Usiamo questo file per inserire una casella di testo nel grafico per mostrare il titolo del grafico. Di seguito è riportato il codice originale per aggiungere una casella di testo al grafico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.cs" >}}

##  **Aggiunta di un'immagine al grafico**

Aspose.Cells permette di inserire immagini in uno schema. Ad esempio, aggiungi un'immagine per enfatizzare o dare più significato a un grafico o ai suoi contenuti, oppure inserisci un file immagine del marchio.

 IL[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) La classe fornisce un metodo denominato[**Aggiungi immagine nel grafico**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpictureinchart), che viene utilizzato per aggiungere un oggetto immagine al grafico. Di seguito è riportato l'elenco dei parametri utilizzati per il metodo:

- **superiore** – l'offset verticale dell'immagine dall'angolo superiore sinistro in unità di 1/4000 dell'area della carta.
- **Sinistra** – l'offset verticale dell'immagine dall'angolo superiore sinistro in unità di 1/4000 dell'area della carta.
- **flusso** – un oggetto stream che contiene i dati dell'immagine.
- **larghezzaScala** – la scala della larghezza dell'immagine, un valore percentuale.
- **altezzaScala** – la scala dell'altezza dell'immagine, un valore percentuale.

 Il metodo restituisce un[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) oggetto. IL[**Immagine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)La classe rappresenta un oggetto immagine nel grafico.

L'esempio seguente mostra come aggiungere un'immagine al grafico. L'esempio utilizza il file di progettazione precedente (**exp_piechart.xls**) che contiene un grafico. Usiamo questo file per inserire un'immagine nel grafico. Di seguito è riportato il codice originale per aggiungere un'immagine al grafico.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-AddingPictureToChart-1.cs" >}}

##  **Aggiunta di una casella di controllo nel grafico**

 Aspose.Cells consente di inserire caselle di controllo in un foglio grafico utilizzando[**MsoDrawingType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msodrawingtype) enumerazione. L'esempio seguente mostra l'aggiunta di una casella di controllo a un foglio grafico.

L'immagine seguente mostra il foglio grafico con la casella di controllo nel file di output.

![cose da fare:immagine_alt_testo](controls-in-charts_1.jpg)

 IL[file di uscita](101089316.xlsx) generato dal seguente frammento di codice è allegato come riferimento.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.cs" >}}

##  **Argomenti avanzati**
- [Aggiungi filigrana WordArt al grafico](/cells/it/net/add-wordart-watermark-to-chart/)
