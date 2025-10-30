---
title: Forme nei Grafici con Golang tramite C++
linktitle: Forme nei grafici
description: Impara come usare Aspose.Cells for C++ per aggiungere controlli e personalizzare i grafici in Microsoft Excel. La nostra guida dimostrerà come manipolare gli elementi del grafico, regolare il formato e migliorare l aspetto e l usabilità generale dei tuoi grafici.
keywords: Aspose.Cells for C++, Controlli grafico, Personalizzazione grafico, Microsoft Excel, Elementi del grafico, Formattazione.
type: docs
weight: 70
url: /it/go-cpp/controls-in-charts/
---

{{% alert color="primary" %}}

A volte è necessario inserire oggetti disegno come etichette, caselle di testo, immagini e così via in un grafico. Aspose.Cells può aggiungere i controlli a un grafico durante l'esecuzione.

{{% /alert %}}

## **Aggiunta del Controllo Etichetta al Grafico**

Le etichette forniscono un modo per fornire informazioni agli utenti sul contenuto di un foglio di calcolo.
Aspose.Cells consente di aggiungere e manipolare le etichette anche nei grafici.

La classe [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) fornisce un metodo chiamato [**AddLabelInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlabelinchart/), usato per aggiungere un controllo etichetta a un grafico. Di seguito è riportato un elenco dei parametri usati per il metodo:

- **top** – lo spostamento verticale dell'etichetta dall'angolo in alto a sinistra in unità dello 1/4000 dell'area del grafico.
- **sinistra** – lo spostamento verticale dell'etichetta dall'angolo in alto a sinistra in unità dello 1/4000 dell'area del grafico.
- **altezza** – l'altezza dell'etichetta, in unità dello 1/4000 dell'area del grafico.
- **larghezza** – la larghezza dell'etichetta, in unità dello 1/4000 dell'area del grafico.

Il metodo restituisce un oggetto [**Aspose::Cells::Drawing::Label**](https://reference.aspose.com/cells/go-cpp/label/). La classe [**Label**](https://reference.aspose.com/cells/go-cpp/label/) rappresenta un'etichetta nel grafico. Ha alcuni membri importanti:

- [**Text**](https://reference.aspose.com/cells/go-cpp/shape/gettext/) (proprietà) – specifica la stringa di didascalia di un'etichetta.
- [**Fill**](https://reference.aspose.com/cells/go-cpp/shape/getfill/) (proprietà) – specifica gli attributi del colore di riempimento.

L'esempio seguente mostra come aggiungere un'etichetta al grafico. L'esempio utilizza un file di progettazione (**exp_piechart.xls**) che ha un grafico al suo interno. Usiamo questo file per inserire un'etichetta nel grafico. Di seguito è riportato il codice originale per aggiungere un'etichetta al grafico. L'output seguente viene generato durante l'esecuzione del codice.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts.go" >}}
## **Aggiunta del controllo TextBox al grafico**

Un modo per evidenziare informazioni importanti in un report è utilizzare una casella di testo. Ad esempio, inserisci del testo per evidenziare il nome dell'azienda o per indicare la regione geografica con le vendite più alte. La classe [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) fornisce un metodo chiamato [**AddTextBoxInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addtextboxinchart/), usato per aggiungere un controllo casella di testo a un grafico. Di seguito l'elenco dei parametri usati per il metodo:

- **top** – lo spostamento verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **left** – lo spostamento verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **height** – l'altezza della casella di testo, in unità di 1/4000 dell'area del grafico.
- **width** – la larghezza della casella di testo, in unità di 1/4000 dell'area del grafico.

Il metodo restituisce un oggetto [**Aspose::Cells::Drawing::TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/). La classe [**TextBox**](https://reference.aspose.com/cells/go-cpp/textbox/) rappresenta una casella di testo nel grafico.

L'esempio seguente mostra come aggiungere una casella di testo a un grafico. L'esempio utilizza il file di progettazione precedente (**exp_piechart.xls**) che contiene un grafico. Utilizziamo questo file per inserire una casella di testo nel grafico per mostrare il titolo del grafico. Di seguito è riportato il codice originale per aggiungere una casella di testo al grafico.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-1.go" >}}
## **Aggiunta di un'immagine al grafico**

Aspose.Cells consente di inserire immagini in un grafico. Ad esempio, aggiungi un'immagine per enfatizzare o dare più significato a un grafico o ai suoi contenuti, o inserisci un file immagine del marchio.

La classe [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/go-cpp/shapecollection/) fornisce un metodo chiamato [**AddPictureInChart**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpictureinchart/), usato per aggiungere un oggetto immagine al grafico. Di seguito l'elenco dei parametri usati per il metodo:

- **top** – lo spostamento verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **left** – lo spostamento verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **stream** – un oggetto stream che contiene i dati dell'immagine.
- **widthScale** – la scala della larghezza dell'immagine, un valore percentuale.
- **heightScale** – la scala dell'altezza dell'immagine, un valore percentuale.

Il metodo restituisce un oggetto [**Aspose::Cells::Drawing::Picture**](https://reference.aspose.com/cells/go-cpp/picture/). La classe [**Picture**](https://reference.aspose.com/cells/go-cpp/picture/) rappresenta un oggetto immagine nel grafico.

L'esempio seguente mostra come aggiungere un'immagine al grafico. L'esempio utilizza il file di progettazione precedente (**exp_piechart.xls**) che contiene un grafico. Utilizziamo questo file per inserire un'immagine nel grafico. Di seguito è riportato il codice originale per aggiungere un'immagine al grafico.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-2.go" >}}
## **Aggiunta di una casella di controllo nel grafico**

Aspose.Cells consente di inserire caselle di controllo in un foglio grafico utilizzando l'enumerazione [**MsoDrawingType**](https://reference.aspose.com/cells/go-cpp/msodrawingtype/). L'esempio seguente illustra come aggiungere una casella di controllo a un foglio grafico.

L'immagine seguente mostra il foglio di lavoro del grafico con la casella di controllo nel file di output.

![todo:image_alt_text](controls-in-charts_1.jpg)

Il [file di output](101089316.xlsx) generato dal frammento di codice seguente è allegato per il tuo riferimento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShapesInCharts-3.go" >}}
## **Argomenti avanzati**
- [Aggiungi WordArt Watermark al grafico](/cells/it/cpp/add-wordart-watermark-to-chart/)
