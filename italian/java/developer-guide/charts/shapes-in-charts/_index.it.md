---
title: Controlli nei grafici
linktitle: Forme nel grafico
type: docs
weight: 60
url: /it/java/controls-in-charts/
---

{{% alert color="primary" %}}

A volte è necessario inserire oggetti disegno come etichette, caselle di testo, immagini e così via in un grafico. Aspose.Cells può aggiungere i controlli a un grafico durante l'esecuzione.

{{% /alert %}}

## **Aggiunta del Controllo Etichetta al Grafico**

Le etichette forniscono un modo per fornire informazioni agli utenti sul contenuto di un foglio di calcolo. Aspose.Cells consente di aggiungere e manipolare le etichette anche nei grafici.

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) fornisce un metodo chiamato [**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)), usato per aggiungere un controllo etichetta a un grafico. Di seguito è riportato un elenco dei parametri utilizzati per il metodo:

- **top** – lo spostamento verticale dell'etichetta dall'angolo in alto a sinistra in unità dello 1/4000 dell'area del grafico.
- **sinistra** – lo spostamento verticale dell'etichetta dall'angolo in alto a sinistra in unità dello 1/4000 dell'area del grafico.
- **altezza** – l'altezza dell'etichetta, in unità dello 1/4000 dell'area del grafico.
- **width** – la larghezza dell'etichetta, in unità pari a 1/4000 dell'area del grafico.

Il metodo restituisce un oggetto della classe [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label), in cui la classe [**Label**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) rappresenta un'etichetta nel grafico. Ha alcuni membri importanti come dettagliato di seguito:

- La proprietà [**Text**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text) specifica una stringa di didascalia dell'etichetta.
- La proprietà [**Fill**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) specifica gli attributi del colore di riempimento.

L'esempio seguente mostra come aggiungere un'etichetta al grafico. L'esempio utilizza un file del designer che contiene un grafico. Utilizziamo questo file per inserire un'etichetta nel grafico.

Di seguito è riportata un'istantanea del file del designer.

**Il grafico del designer**

![todo:image_alt_text](controls-in-charts_1.png)

Di seguito è riportato il codice originale per aggiungere un'etichetta al grafico. L'output seguente viene generato durante l'esecuzione del codice.

**È stata aggiunta un'etichetta nel grafico**

![todo:image_alt_text](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **Aggiunta del controllo TextBox al grafico**

Un modo per evidenziare informazioni importanti in un report è utilizzare una casella di testo. Ad esempio, inserire del testo per evidenziare il nome dell'azienda o per indicare la regione geografica con le vendite più alte. La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) fornisce un metodo chiamato [**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)), che viene utilizzato per aggiungere un controllo casella di testo a un grafico. Di seguito è riportato l'elenco dei parametri utilizzati per il metodo:

- **top** – lo spostamento verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **left** – lo spostamento verticale della casella di testo dall'angolo superiore sinistro in unità pari a 1/4000 dell'area del grafico.
- **height** – l'altezza della casella di testo, in unità di 1/4000 dell'area del grafico.
- **width** – la larghezza della casella di testo, in unità di 1/4000 dell'area del grafico.

Il metodo restituisce un oggetto della classe [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) dove la classe [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) rappresenta una casella di testo nel grafico.

Nell'esempio seguente viene mostrato come aggiungere una casella di testo a un grafico. L'esempio utilizza il file del designer precedente che contiene un grafico. Utilizziamo questo file per inserire una casella di testo nel grafico in modo da mostrare il titolo del grafico.

Di seguito è riportato il codice originale per aggiungere una casella di testo al grafico. Il seguente output viene generato durante l'esecuzione del codice.

**È stata aggiunta una casella di testo nel grafico**

![todo:image_alt_text](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Aggiunta di un'immagine al grafico**

Aspose.Cells consente di inserire immagini in un grafico. Ad esempio, aggiungi un'immagine per enfatizzare o dare più significato a un grafico o ai suoi contenuti, o inserisci un file immagine del marchio.

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) fornisce un metodo chiamato [**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)), che viene utilizzato per aggiungere un oggetto immagine al grafico. Di seguito è riportato l'elenco dei parametri utilizzati per il metodo:

- **top** – lo spostamento verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **left** – lo spostamento verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **stream** – un oggetto stream che contiene i dati dell'immagine.
- **widthScale** – la scala della larghezza dell'immagine, un valore percentuale.
- **heightScale** – la scala dell'altezza dell'immagine, un valore percentuale.

Il metodo restituisce un oggetto della classe [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) dove la classe [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) rappresenta un oggetto immagine nel grafico.

Nell'esempio seguente viene mostrato come aggiungere un'immagine al grafico. L'esempio utilizza il file del designer precedente che contiene un grafico. Utilizziamo questo file per inserire un'immagine nel grafico.

Di seguito è riportato il codice originale per aggiungere un'immagine al grafico. Il seguente output viene generato durante l'esecuzione del codice

**È stata inserita un'immagine nel grafico**

![todo:image_alt_text](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Aggiunta di una casella di controllo nel grafico**

Aspose.Cells consente di inserire caselle di controllo in un foglio di grafico utilizzando l'enumerazione [**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType). L'esempio seguente dimostra come aggiungere una casella di controllo a un foglio di grafico.

L'immagine seguente mostra il foglio di lavoro del grafico con la casella di controllo nel file di output.

![todo:image_alt_text](controls-in-charts_5.jpg)

Il [file di output](InsertCheckboxInChartSheet_out.xlsx) generato dal seguente frammento di codice è allegato per il tuo riferimento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
