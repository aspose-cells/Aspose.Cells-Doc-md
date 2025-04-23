---
title: Inserisci immagini e forme dei file di Excel.
linktitle: Forme
type: docs
weight: 140
url: /it/python-net/insert-shapes/
description: Gestisci immagini, oggetti OLE, forme nei file Excel.
---

{{% alert color="primary" %}}

A volte è necessario inserire alcune forme necessarie nel foglio di lavoro. Potresti aver bisogno di inserire la stessa forma in posizioni diverse del foglio di lavoro. O potresti aver bisogno di inserire batch di forme nel foglio di lavoro.

Non preoccuparti! [Aspose.Cells](https://products.aspose.com/cells/) supporta tutte queste operazioni.

{{% /alert %}}

Le forme in Excel sono principalmente divise nei seguenti tipi:
- **Immagini**
- **Oggetti OLE**
- **Linee**
- **Rettangoli**
- **Forme di base**
- **Frecce a blocco**
- **Forme di equazione**
- **Diagrammi di flusso**
- **Stelle e striscioni**
- **Callout**

Questo documento guida selezionerà uno o due forme da ciascun tipo per creare degli esempi. Attraverso questi esempi, imparerai come utilizzare [Aspose.Cells](https://products.aspose.com/cells/) per inserire la forma specificata nel foglio di lavoro.

## **Aggiunta di immagini nel foglio di lavoro di Excel in C#**

Aggiungere immagini a un foglio di calcolo è molto facile. Bastano poche righe di codice:
Basta chiamare il metodo [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) della collezione [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection) (incapsulata nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Il metodo [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) accetta i seguenti parametri:

- **upper_left_row**, l'indice della riga in alto a sinistra.
- **upper_left_column**, l'indice della colonna in alto a sinistra.
- **file_name**, il nome del file immagine, completo di percorso.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-Pictures-AddingPictures-1.py" >}}


## **Inserimento di oggetti OLE nel foglio di lavoro di Excel in C#**

Aspose.Cells per Python via .NET supporta l'aggiunta, l'estrazione e la manipolazione di oggetti OLE nei fogli di lavoro. Per questo motivo, Aspose.Cells per Python via .NET dispone della classe [**OleObjectCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobjectcollection), utilizzata per aggiungere un nuovo oggetto OLE alla lista della raccolta. Un'altra classe, [**OleObject**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject), rappresenta un oggetto OLE. Ha alcuni membri importanti:

- La proprietà [**image_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/image_data) specifica i dati dell'immagine (icona) di tipo array di byte. L'immagine verrà visualizzata per mostrare l'oggetto OLE nel foglio di lavoro.
- La proprietà [**object_data**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/object_data) specifica i dati dell'oggetto sotto forma di un array di byte. Questi dati verranno mostrati nel relativo programma quando si fa doppio clic sull'icona dell'oggetto OLE.

L'esempio seguente mostra come aggiungere un/i oggetto(i) OLE in un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-OLE-InsertingOLEObjects-1.py" >}}

## **Inserimento di una linea nel foglio di lavoro di Excel in C#**

La forma della linea appartiene alla categoria **linee**.

***In Microsoft Excel (ad esempio 2007):***

- Selezionare la cella dove si desidera inserire la linea
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi, selezionare la linea da 'Forme usate di recente' o 'Linee'

![](line.png)

***Utilizzo di Aspose.Cells per Python via .NET***

È possibile utilizzare il seguente metodo per inserire una linea nel foglio di lavoro.

{{% alert color="primary" %}}

[**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line)

Il metodo restituisce un oggetto [LineShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape).

{{% /alert %}}

L'esempio seguente mostra come inserire una linea in un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Line.py" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](line2.png)



## **Inserimento di una freccia di linea nel foglio di lavoro di Excel in C#**

La forma della freccia di linea appartiene alla categoria **Linee**. È un caso speciale di linea.

***In Microsoft Excel (ad esempio 2007):***

- Selezionare la cella dove si desidera inserire la freccia di linea
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi, selezionare la freccia della riga da 'Forme utilizzate di recente' o 'Linee'

![](line_arrow1.png)

***Utilizzo di Aspose.Cells per Python via .NET***

È possibile utilizzare il seguente metodo per inserire una freccia di linea nel foglio di lavoro.

{{% alert color="primary" %}}

[**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line)

Il metodo restituisce un oggetto [LineShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape).

{{% /alert %}}

L'esempio seguente mostra come inserire una freccia di linea in un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-LineArrow.py" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](line_arrow2.png)



## **Inserimento di un rettangolo nel foglio di lavoro di Excel in C#**

La forma del rettangolo appartiene alla categoria **Rettangoli**.

***In Microsoft Excel (ad esempio 2007):***

- Selezionare la cella in cui si desidera inserire il rettangolo
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi, selezionare il rettangolo da 'Forme utilizzate di recente' o 'Rettangoli'

![](rectangle.png)

***Utilizzo di Aspose.Cells per Python via .NET***

È possibile utilizzare il seguente metodo per inserire un rettangolo nel foglio di lavoro.

{{% alert color="primary" %}}

[**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle)

Il metodo restituisce un oggetto [RectangleShape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape).

{{% /alert %}}

L'esempio seguente mostra come inserire un rettangolo in un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Rectangle.py" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](rectangle2.png)



## **Inserimento di un cubo nel foglio di calcolo di Excel in C#**

La forma del cubo appartiene alla categoria **Forme di base**.

***In Microsoft Excel (ad esempio 2007):***

- Selezionare la cella in cui si desidera inserire il cubo
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi, selezionare il cubo da **Forme di base**

![](cube.png)

***Utilizzo di Aspose.Cells per Python via .NET***

È possibile utilizzare il seguente metodo per inserire un cubo nel foglio di lavoro.

{{% alert color="primary" %}}

[**public Shape add_auto_shape(type, upper_left_row, top, upper_left_column, left, height, width)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape).

{{% /alert %}}

L'esempio seguente mostra come inserire un cubo in un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Cube.py" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](cube2.png)



## **Inserimento di una freccia quadri callout in Excel Foglio di lavoro in C#**

La forma della freccia quadri callout appartiene alla categoria **Frecci quadrate**.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la freccia quadrupla di chiamata
- Fai clic sul menu Inserisci e seleziona Forme.
- Successivamente, seleziona la freccia quadrupla di chiamata da **Frecce a blocco**

![](callout_quad_arrow.png)

***Utilizzo di Aspose.Cells per Python via .NET***

Puoi utilizzare il seguente metodo per inserire una freccia quadrupla di chiamata nel foglio di lavoro.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape).

{{% /alert %}}

L'esempio seguente mostra come inserire una freccia quadrupla di chiamata in un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.py" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](callout_quad_arrow2.png)



## **Inserimento di un segno di moltiplicazione nel foglio di calcolo di Excel in C#**

La forma del segno di moltiplicazione appartiene alla categoria **Forme di equazione**.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire il segno di moltiplicazione
- Fai clic sul menu Inserisci e seleziona Forme.
- Successivamente, seleziona il segno di moltiplicazione da **Forme di equazione**

![](multiplication_sign.png)

***Utilizzo di Aspose.Cells per Python via .NET***

Puoi utilizzare il seguente metodo per inserire un segno di moltiplicazione nel foglio di lavoro.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape).

{{% /alert %}}

Nell'esempio seguente viene mostrato come inserire un segno di moltiplicazione in un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.py" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](multiplication_sign2.png)



## **Inserimento di un multidocumento in un foglio di lavoro di Excel in C#**

La forma del multidocumento appartiene alla categoria **FlowCharts**.

***In Microsoft Excel (ad esempio 2007):***

- Selezionare la cella in cui si desidera inserire il multidocumento
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi selezionare il multidocumento da **FlowCharts**

![](multidocument.png)

***Utilizzo di Aspose.Cells per Python via .NET***

Puoi utilizzare il seguente metodo per inserire un multidocumento nel foglio di lavoro.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape).

{{% /alert %}}

Nell'esempio seguente viene mostrato come inserire un multidocumento in un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-Multidocument.py" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](multidocument2.png)



## **Inserire una stella a cinque punte nel foglio di lavoro di Excel in C#**

La forma della stella a cinque punte appartiene alla categoria **Stelle e Bandiere**.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la stella a cinque punte
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi, seleziona la stella a cinque punte da **Stelle e Bandiere**

![](star_5_points.png)

***Utilizzo di Aspose.Cells per Python via .NET***

È possibile utilizzare il seguente metodo per inserire una stella a cinque punte nel foglio di lavoro.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape).

{{% /alert %}}

L'esempio seguente mostra come inserire una stella a cinque punte in un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-FivePointedStar.py" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](star_5_points2.png)



## **Inserimento di una nuvola a forma di fumetto nel foglio di lavoro di Excel in C#**

La forma della nuvola a forma di fumetto appartiene alla categoria **Callout**.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la nuvola a forma di fumetto
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi, seleziona la nuvola a forma di fumetto da **Callout**

![](thought_bubble_cloud.png)

***Utilizzo di Aspose.Cells per Python via .NET***

È possibile utilizzare il seguente metodo per inserire una nuvola di pensiero nel foglio di lavoro.

{{% alert color="primary" %}}

[**add_auto_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_auto_shape)

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape).

{{% /alert %}}

L'esempio seguente mostra come inserire una nuvola di pensiero in un foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Main-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.py" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](thought_bubble_cloud2.png)

## **Argomenti avanzati**
- [Modifica dei valori di regolazione della forma](/cells/it/python-net/change-adjustment-values-of-the-shape/)
- [Copia delle forme tra i fogli di lavoro](/cells/it/python-net/copy-shapes-between-worksheets/)
- [Dati in forma non primitiva](/cells/it/python-net/data-in-non-primitive-shape/)
- [Ricerca della posizione assoluta della forma all'interno del foglio di lavoro](/cells/it/python-net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Ottieni punti di connessione dalla forma](/cells/it/python-net/get-connection-points-from-shape/)
- [Gestione dei controlli](/cells/it/python-net/managing-controls/)
- [Aggiungi icone al foglio di lavoro](/cells/it/python-net/insert-svg-to-excel/)
- [Gestione di oggetti OLE](/cells/it/python-net/managing-ole-objects/)
- [Gestione delle immagini](/cells/it/python-net/managing-pictures/)
- [Gestisci Smart Art](/cells/it/python-net/managing-smartart/)
- [Gestione casella di testo](/cells/it/python-net/managing-textbox-of-excel/)
- [Aggiungere un'immagine WordArt al foglio di lavoro](/cells/it/python-net/add-wordart-watermark-to-worksheet/)
- [Aggiornamento dei valori delle forme collegate](/cells/it/python-net/refresh-values-of-linked-shapes/)
- [Invia la forma avanti o indietro all'interno del foglio di lavoro](/cells/it/python-net/send-shape-front-or-back-inside-the-worksheet/)
- [Gestire le opzioni di forma](/cells/it/python-net/managing-shape-options/)
- [Gestire le opzioni di testo di forma](/cells/it/python-net/managing-shape-text-options/)
- [Estensioni Web - Componenti aggiuntivi di Office](/cells/it/python-net/web-extensions-office-add-ins/)

