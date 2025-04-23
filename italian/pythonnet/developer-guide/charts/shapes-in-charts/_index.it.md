---
title: Forme nei grafici
description: Impara come usare Aspose.Cells per Python via .NET per aggiungere controlli e personalizzare grafici in Microsoft Excel. La nostra guida dimostrerà come manipolare gli elementi del grafico, regolare la formattazione e migliorare l aspetto e l usabilità complessiva dei tuoi grafici.
keywords: Aspose.Cells per Python via .NET, Controlli del grafico, Personalizzazione del grafico, Microsoft Excel, Elementi del grafico, Formattazione.
type: docs
weight: 70
url: /it/python-net/controls-in-charts/
---

{{% alert color="primary" %}}

A volte è necessario inserire oggetti di disegno come etichette, caselle di testo, immagini e così via in un grafico. Aspose.Cells per Python via .NET può aggiungere i controlli al grafico a runtime.

{{% /alert %}}

## **Aggiunta del Controllo Etichetta al Grafico**

Le etichette forniscono un modo per fornire informazioni agli utenti sul contenuto di un foglio di calcolo.
Aspose.Cells per Python via .NET consente di aggiungere e manipolare etichette anche nei grafici.

La classe [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_label_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label_in_chart), utilizzato per aggiungere un controllo etichetta a un grafico. Di seguito è riportato un elenco dei parametri utilizzati per il metodo:

- **top** – lo spostamento verticale dell'etichetta dall'angolo in alto a sinistra in unità dello 1/4000 dell'area del grafico.
- **sinistra** – lo spostamento verticale dell'etichetta dall'angolo in alto a sinistra in unità dello 1/4000 dell'area del grafico.
- **altezza** – l'altezza dell'etichetta, in unità dello 1/4000 dell'area del grafico.
- **larghezza** – la larghezza dell'etichetta, in unità dello 1/4000 dell'area del grafico.

Il metodo restituisce l'oggetto [**aspose.cells.drawing.Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label). La classe [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) rappresenta un'etichetta nel grafico. Ha alcuni membri importanti:

- [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) (proprietà) – specifica una stringa di sottotitolo dell'etichetta.
- [**fill**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill) (proprietà) – specifica gli attributi del colore di riempimento.

L'esempio seguente mostra come aggiungere un'etichetta al grafico. L'esempio utilizza un file di progettazione (**exp_piechart.xls**) che ha un grafico al suo interno. Usiamo questo file per inserire un'etichetta nel grafico. Di seguito è riportato il codice originale per aggiungere un'etichetta al grafico. L'output seguente viene generato durante l'esecuzione del codice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingLabelControl-1.py" >}}

## **Aggiunta del controllo TextBox al grafico**

Un modo per evidenziare informazioni importanti in un report è utilizzare una casella di testo. Ad esempio, inserire del testo per evidenziare il nome dell'azienda o per indicare la regione geografica con le vendite più alte. La classe [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_text_box_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_text_box_in_chart), che viene utilizzato per aggiungere un controllo casella di testo a un grafico. Di seguito è riportato l'elenco dei parametri utilizzati per il metodo:

- **top** – lo spostamento verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **left** – lo spostamento verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **height** – l'altezza della casella di testo, in unità di 1/4000 dell'area del grafico.
- **width** – la larghezza della casella di testo, in unità di 1/4000 dell'area del grafico.

Il metodo restituisce un oggetto [**aspose.cells.drawing.TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox). La classe [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox) rappresenta una casella di testo nel grafico.

L'esempio seguente mostra come aggiungere una casella di testo a un grafico. L'esempio utilizza il file di progettazione precedente (**exp_piechart.xls**) che contiene un grafico. Utilizziamo questo file per inserire una casella di testo nel grafico per mostrare il titolo del grafico. Di seguito è riportato il codice originale per aggiungere una casella di testo al grafico.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingTextBoxControl-1.py" >}}

## **Aggiunta di un'immagine al grafico**

Aspose.Cells per Python via .NET consente di inserire immagini in un grafico. Ad esempio, aggiungi un'immagine per sottolineare o dare più significato a un grafico o ai suoi contenuti, o inserisci un file immagine di marchio.

La classe [**aspose.cells.drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fornisce un metodo chiamato [**add_picture_in_chart**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture_in_chart), che viene utilizzato per aggiungere un oggetto immagine al grafico. Di seguito è riportato l'elenco dei parametri utilizzati per il metodo:

- **top** – lo spostamento verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **left** – lo spostamento verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **stream** – un oggetto stream che contiene i dati dell'immagine.
- **widthScale** – la scala della larghezza dell'immagine, un valore percentuale.
- **heightScale** – la scala dell'altezza dell'immagine, un valore percentuale.

Il metodo restituisce un oggetto [**aspose.cells.drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture). La classe [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) rappresenta un oggetto immagine nel grafico.

L'esempio seguente mostra come aggiungere un'immagine al grafico. L'esempio utilizza il file di progettazione precedente (**exp_piechart.xls**) che contiene un grafico. Utilizziamo questo file per inserire un'immagine nel grafico. Di seguito è riportato il codice originale per aggiungere un'immagine al grafico.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-AddingPictureToChart-1.py" >}}

## **Aggiunta di una casella di controllo nel grafico**

Aspose.Cells per Python via .NET consente di inserire caselle di controllo in un foglio di grafico usando l'enumerazione [**MsoDrawingType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msodrawingtype). L'esempio seguente dimostra come aggiungere una casella di controllo a un foglio di grafico.

L'immagine seguente mostra il foglio di lavoro del grafico con la casella di controllo nel file di output.

![todo:image_alt_text](controls-in-charts_1.jpg)

Il [file di output](101089316.xlsx) generato dal frammento di codice seguente è allegato per il tuo riferimento.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-InsertingControlsintoCharts-InsertCheckboxInChartSheet-1.py" >}}

## **Argomenti avanzati**
- [Aggiungi WordArt Watermark al grafico](/cells/it/python-net/add-wordart-watermark-to-chart/)
