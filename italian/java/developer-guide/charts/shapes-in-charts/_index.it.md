---
title: Controlli nei grafici
linktitle: Forme In Grafico
type: docs
weight: 60
url: /it/java/controls-in-charts/
---
{{% alert color="primary" %}}

volte è necessario inserire oggetti di disegno come etichette, caselle di testo, immagini e così via in un grafico. Aspose.Cells può aggiungere i controlli a un grafico in fase di esecuzione.

{{% /alert %}}

## **Aggiunta del controllo etichetta al grafico**

Le etichette forniscono un mezzo per fornire informazioni agli utenti sul contenuto di un foglio di calcolo. Aspose.Cells consente di aggiungere e manipolare etichette anche nei grafici.

 Il[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) class fornisce un metodo denominato[**addLabelInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLabelInChart(int,%20int,%20int,%20int)), utilizzato per aggiungere un controllo etichetta a un grafico. Di seguito è riportato un elenco dei parametri utilizzati per il metodo:

- **superiore** – l'offset verticale dell'etichetta dall'angolo superiore sinistro in unità di 1/4000 dell'area del grafico.
- **sinistra** – l'offset verticale dell'etichetta dall'angolo superiore sinistro in unità di 1/4000 dell'area del grafico.
- **altezza** – l'altezza dell'etichetta, in unità di 1/4000 dell'area del grafico.
- **larghezza** – la larghezza dell'etichetta, in unità di 1/4000 dell'area del grafico.

 Il metodo restituisce un oggetto di[**Etichetta**](https://reference.aspose.com/cells/java/com.aspose.cells/Label) classe, dove il[**Etichetta**](https://reference.aspose.com/cells/java/com.aspose.cells/Label)class rappresenta un'etichetta nel grafico. Ha alcuni membri importanti come descritto di seguito:

- [**Testo**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Text)La proprietà specifica la stringa di didascalia di un'etichetta.
- [**Riempire**](https://reference.aspose.com/cells/java/com.aspose.cells/label#Fill) La proprietà specifica gli attributi del colore di riempimento.

L'esempio seguente mostra come aggiungere un'etichetta al grafico. L'esempio utilizza un file di progettazione che contiene un grafico. Utilizziamo questo file per inserire un'etichetta nel grafico.

Di seguito è riportato uno screenshot del file di progettazione.

**Il grafico del progettista**

![cose da fare:immagine_alt_testo](controls-in-charts_1.png)

Di seguito è riportato il codice originale per l'aggiunta di un'etichetta al grafico. Il seguente output viene generato durante l'esecuzione del codice.

**Un'etichetta viene aggiunta al grafico**

![cose da fare:immagine_alt_testo](controls-in-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingLabelControl-AddingLabelControl.java" >}}

## **Aggiunta del controllo TextBox al grafico**

 Un modo per evidenziare informazioni importanti in un report consiste nell'utilizzare una casella di testo. Ad esempio, inserisci il testo per evidenziare il nome dell'azienda o per indicare l'area geografica con le vendite più elevate. Il[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) class fornisce un metodo denominato[**addTextBoxInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addTextBoxInChart(int,%20int,%20int,%20int)), utilizzato per aggiungere un controllo casella di testo a un grafico. Di seguito è riportato l'elenco dei parametri utilizzati per il metodo:

- **superiore** – l'offset verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **sinistra** – l'offset verticale della casella di testo dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **altezza**– l'altezza della casella di testo, in unità di 1/4000 dell'area del grafico.
- **larghezza** – la larghezza della casella di testo, in unità di 1/4000 dell'area del grafico.

 Il metodo restituisce un oggetto di[**Casella di testo**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox) classe dove il[**Casella di testo**](https://reference.aspose.com/cells/java/com.aspose.cells/TextBox)class rappresenta una casella di testo nel grafico.

L'esempio seguente mostra come aggiungere una casella di testo a un grafico. L'esempio utilizza il file di progettazione precedente che contiene un grafico. Utilizziamo questo file per inserire una casella di testo nel grafico per mostrare il titolo del grafico.

Di seguito è riportato il codice originale per l'aggiunta di una casella di testo al grafico. Il seguente output viene generato durante l'esecuzione del codice.

**Nel grafico viene aggiunta una casella di testo**

![cose da fare:immagine_alt_testo](controls-in-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingTextBoxControl-AddingTextBoxControl.java" >}}

## **Aggiunta di immagini al grafico**

Aspose.Cells consente di inserire immagini in un grafico. Ad esempio, aggiungi un'immagine per enfatizzare o dare più significato a un grafico o al suo contenuto, oppure inserisci un file di immagine del marchio.

 Il[**Collezione Shape**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) class fornisce un metodo denominato[**addPictureInChart**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPictureInChart(int,%20int,%20java.io.InputStream,%20int,%20int)), utilizzato per aggiungere un oggetto immagine al grafico. Di seguito è riportato l'elenco dei parametri utilizzati per il metodo:

- **superiore**– l'offset verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **sinistra**– l'offset verticale dell'immagine dall'angolo in alto a sinistra in unità di 1/4000 dell'area del grafico.
- **flusso** – un oggetto stream che contiene i dati dell'immagine.
- **widthScale** – la scala della larghezza dell'immagine, un valore percentuale.
- **heightScala** – la scala dell'altezza dell'immagine, un valore percentuale.

 Il metodo restituisce un oggetto di[**Immagine**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) classe dove il[**Immagine**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)class rappresenta un oggetto immagine nel grafico.

L'esempio seguente mostra come aggiungere un'immagine al grafico. L'esempio utilizza il file di progettazione precedente che contiene un grafico. Usiamo questo file per inserire un'immagine nel grafico.

Di seguito è riportato il codice originale per aggiungere un'immagine al grafico. Il seguente output viene generato durante l'esecuzione del codice

**Un'immagine viene inserita nel grafico**

![cose da fare:immagine_alt_testo](controls-in-charts_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-charts-AddingPictureToChart-AddingPictureToChart.java" >}}

## **Aggiunta di una casella di controllo nel grafico**

Aspose.Cells consente di inserire caselle di controllo in un foglio grafico utilizzando[**MsoDrawingType**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoDrawingType) enumerazione. L'esempio seguente mostra l'aggiunta di una casella di controllo a un foglio grafico.

L'immagine seguente mostra il foglio grafico con la casella di controllo nel file di output.

![cose da fare:immagine_alt_testo](controls-in-charts_5.jpg)

Il[file di uscita](InsertCheckboxInChartSheet_out.xlsx)generato dal seguente frammento di codice è allegato come riferimento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Charts-InsertCheckboxInChartSheet-1.java" >}}
