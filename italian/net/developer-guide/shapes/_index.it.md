---
title: Inserisci immagini e forme di file Excel.
linktitle: Forme
type: docs
weight: 140
url: /it/net/insert-shapes/
description: Gestisci immagini, oleoobject, forme in file Excel.
---
{{% alert color="primary" %}}

A volte è necessario inserire alcune forme necessarie nel foglio di lavoro. Potrebbe essere necessario inserire la stessa forma in diverse posizioni del foglio di lavoro. Oppure è necessario inserire in batch le forme nel foglio di lavoro.

 Non preoccuparti![Aspose.Cells](https://products.aspose.com/cells/) supporta tutte queste operazioni.

{{% /alert %}}

Le forme in excel si suddividono principalmente nelle seguenti tipologie:
- **Immagini**
- **OleObjects**
- **Linee**
- **Rettangoli**
- **Forme di base**
- **Frecce di blocco**
- **Forme di equazione**
- **Diagrammi di flusso**
- **Stelle e striscioni**
- **Didascalie**

Questo documento guida selezionerà una o due forme da ogni tipo per creare campioni. Attraverso questi esempi imparerai come usare[Aspose.Cells](https://products.aspose.com/cells/) per inserire la forma specificata nel foglio di lavoro.

## **Aggiunta di immagini nel foglio di lavoro di Excel in C#**

L'aggiunta di immagini a un foglio di calcolo è molto semplice. Bastano poche righe di codice:
 Basta chiamare il[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) metodo del[**Immagini**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) raccolta (incapsulata nel file[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) oggetto). Il[**Aggiungere**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)metodo accetta i seguenti parametri:

- **Indice della riga in alto a sinistra**, l'indice della riga in alto a sinistra.
- **Indice colonna in alto a sinistra**, l'indice della colonna in alto a sinistra.
- **Nome file immagine**, il nome del file immagine, completo di percorso.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **Inserimento di oggetti OLE nel foglio di lavoro di Excel in C#**

Aspose.Cells supporta l'aggiunta, l'estrazione e la manipolazione di oggetti OLE nei fogli di lavoro. Per questo Aspose.Cells ha il[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) class, utilizzata per aggiungere un nuovo oggetto OLE all'elenco di raccolte. Un'altra classe,[**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), rappresenta un oggetto OLE. Ha alcuni membri importanti:

-  Il[**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)La proprietà specifica i dati dell'immagine (icona) del tipo di array di byte. L'immagine verrà visualizzata per mostrare l'oggetto OLE nel foglio di lavoro.
-  Il[**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)La proprietà specifica i dati dell'oggetto sotto forma di un array di byte. Questi dati verranno visualizzati nel relativo programma quando si fa doppio clic sull'icona dell'oggetto OLE.

L'esempio seguente mostra come aggiungere uno o più oggetti OLE in un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **Inserimento di una riga nel foglio di lavoro Excel in C#**

 La forma della linea appartiene al**linee** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la riga
- Fare clic sul menu Inserisci e fare clic su Forme.
- Quindi, seleziona la linea da "Forme utilizzate di recente" o "Linee"

![](line.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire una riga nel foglio di lavoro.

{{% alert color="primary" %}}

[public LineShape AddLine(
 int upperLeftRow,
 in alto,
 int upperLeftColumn,
 int a sinistra,
 altezza intera,
 larghezza int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 Il metodo restituisce a[LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire una riga in un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](line2.png)



## **Inserimento di una freccia di linea nel foglio di lavoro Excel in C#**

 La forma della freccia della linea appartiene al**Linee**categoria. È un caso speciale di linea.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la freccia della linea
- Fare clic sul menu Inserisci e fare clic su Forme.
- Quindi, seleziona la freccia della linea da "Forme utilizzate di recente" o "Linee"

![](line_arrow1.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire una freccia di linea nel foglio di lavoro.

{{% alert color="primary" %}}

[public LineShape AddLine(
 int upperLeftRow,
 in alto,
 int upperLeftColumn,
 int a sinistra,
 altezza intera,
 larghezza int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 Il metodo restituisce a[LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire una freccia di linea in un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](line_arrow2.png)



## **Inserimento di un rettangolo in un foglio di lavoro Excel in C#**

 La forma del rettangolo appartiene al**Rettangoli** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire il rettangolo
- Fare clic sul menu Inserisci e fare clic su Forme.
- Quindi, seleziona il rettangolo da "Forme utilizzate di recente" o "Rettangoli"

![](rectangle.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire un rettangolo nel foglio di lavoro.

{{% alert color="primary" %}}

[public RectangleShape AddRectangle(
 int upperLeftRow,
 in alto,
 int upperLeftColumn,
 int a sinistra,
 altezza intera,
 larghezza int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

 Il metodo restituisce a[RettangoloForma](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire un rettangolo in un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](rectangle2.png)



## **Inserimento di un foglio di lavoro da cubo a Excel in C#**

 La forma del cubo appartiene al**Forme di base** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire il cubo
- Fare clic sul menu Inserisci e fare clic su Forme.
-  Quindi, seleziona il Cubo da**Forme di base**

![](cube.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire un cubo nel foglio di lavoro.

{{% alert color="primary" %}}

[forma pubblica AddAutoShape(
 tipo AutoShapeType,
 int upperLeftRow,
 in alto,
 int upperLeftColumn,
 int a sinistra,
 altezza intera,
 larghezza int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire un cubo in un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](cube2.png)



## **Inserimento di una freccia quadrupla callout nel foglio di lavoro Excel in C#**

 La forma della freccia quadrupla di callout appartiene al**Frecce di blocco** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la freccia quadrupla del callout
- Fare clic sul menu Inserisci e fare clic su Forme.
-  Quindi, seleziona la freccia quadrupla del callout da**Frecce di blocco**

![](callout_quad_arrow.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire una freccia quadrupla callout nel foglio di lavoro.

{{% alert color="primary" %}}

[forma pubblica AddAutoShape(
 tipo AutoShapeType,
 int upperLeftRow,
 in alto,
 int upperLeftColumn,
 int a sinistra,
 altezza intera,
 larghezza int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire una freccia quadrupla di callout in un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](callout_quad_arrow2.png)



## **Inserimento di un segno di moltiplicazione nel foglio di lavoro Excel in C#**

 La forma del segno di moltiplicazione appartiene al**Forme di equazione** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire il segno di moltiplicazione
- Fare clic sul menu Inserisci e fare clic su Forme.
-  Quindi, seleziona il segno di moltiplicazione da**Forme di equazione**

![](multiplication_sign.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire un segno di moltiplicazione nel foglio di lavoro.

{{% alert color="primary" %}}

[forma pubblica AddAutoShape(
 tipo AutoShapeType,
 int upperLeftRow,
 in alto,
 int upperLeftColumn,
 int a sinistra,
 altezza intera,
 larghezza int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire il segno di moltiplicazione in un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](multiplication_sign2.png)



## **Inserimento di un multidocumento nel foglio di lavoro Excel in C#**

La forma del multidocumento appartiene al**Diagrammi di flusso** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui vuoi inserire il multidocumento
- Fare clic sul menu Inserisci e fare clic su Forme.
-  Quindi, seleziona il multidocumento da**Diagrammi di flusso**

![](multidocument.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire un documento multiplo nel foglio di lavoro.

{{% alert color="primary" %}}

[forma pubblica AddAutoShape(
 tipo AutoShapeType,
 int upperLeftRow,
 in alto,
 int upperLeftColumn,
 int a sinistra,
 altezza intera,
 larghezza int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire più documenti in un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](multidocument2.png)



## **Inserimento di una stella a cinque punte nel foglio di lavoro Excel in C#**

 La forma della stella a cinque punte appartiene al**Stelle e striscioni** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la stella a cinque punte
- Fare clic sul menu Inserisci e fare clic su Forme.
-  Quindi, seleziona la stella a cinque punte da**Stelle e striscioni**

![](star_5_points.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il seguente metodo per inserire una stella a cinque punte nel foglio di lavoro.

{{% alert color="primary" %}}

[forma pubblica AddAutoShape(
 tipo AutoShapeType,
 int upperLeftRow,
 in alto,
 int upperLeftColumn,
 int a sinistra,
 altezza intera,
 larghezza int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire una stella a cinque punte in un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](star_5_points2.png)



## **Inserimento di una nuvola di bolle di pensiero nel foglio di lavoro di Excel in C#**

 La forma della nuvola di bolle di pensiero appartiene al**Didascalie** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la nuvola di bolle di pensiero
- Fare clic sul menu Inserisci e fare clic su Forme.
-  Quindi, seleziona la nuvola di bolle di pensiero da**Didascalie**

![](thought_bubble_cloud.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il seguente metodo per inserire una nuvola di bolle di pensiero nel foglio di lavoro.

{{% alert color="primary" %}}

[forma pubblica AddAutoShape(
 tipo AutoShapeType,
 int upperLeftRow,
 in alto,
 int upperLeftColumn,
 int a sinistra,
 altezza intera,
 larghezza int
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire una nuvola di bolle di pensiero in un foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](thought_bubble_cloud2.png)

## **Argomenti avanzati**
- [Modifica i valori di regolazione della forma](/cells/it/net/change-adjustment-values-of-the-shape/)
- [Copia forme tra fogli di lavoro](/cells/it/net/copy-shapes-between-worksheets/)
- [Dati in forma non primitiva](/cells/it/net/data-in-non-primitive-shape/)
- [Trovare la posizione assoluta della forma all'interno del foglio di lavoro](/cells/it/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Ottieni punti di connessione dalla forma](/cells/it/net/get-connection-points-from-shape/)
- [Gestione dei controlli](/cells/it/net/managing-controls/)
- [Aggiungi icone al foglio di lavoro](/cells/it/net/insert-svg-to-excel/)
- [Gestione degli oggetti OLE](/cells/it/net/managing-ole-objects/)
- [Gestione delle immagini](/cells/it/net/managing-pictures/)
- [Gestisci l'arte intelligente](/cells/it/net/managing-smartart/)
- [Gestione della casella di testo](/cells/it/net/managing-textbox-of-excel/)
- [Aggiungi filigrana WordArt al foglio di lavoro](/cells/it/net/add-wordart-watermark-to-worksheet/)
- [Aggiorna i valori delle forme collegate](/cells/it/net/refresh-values-of-linked-shapes/)
- [Invia la forma davanti o dietro all'interno del foglio di lavoro](/cells/it/net/send-shape-front-or-back-inside-the-worksheet/)
- [Gestisci opzioni forma](/cells/it/net/managing-shape-options/)
- [Gestisci opzioni testo forma](/cells/it/net/managing-shape-text-options/)
- [Estensioni Web - Componenti aggiuntivi per Office](/cells/it/net/web-extensions-office-add-ins/)

