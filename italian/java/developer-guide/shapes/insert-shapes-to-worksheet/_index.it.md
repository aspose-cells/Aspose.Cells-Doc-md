---
title: Inserisci forme nel foglio di lavoro in Aspose.Cells
type: docs
weight: 5
url: /it/java/insert-shapes-to-worksheet-in-aspose-cells/
---
{{% alert color="primary" %}}

A volte è necessario inserire alcune forme necessarie nel foglio di lavoro. Potrebbe essere necessario inserire la stessa forma in diverse posizioni del foglio di lavoro. Oppure è necessario inserire in batch le forme nel foglio di lavoro.

 Non preoccuparti![Aspose.Cells](https://products.aspose.com/cells/) supporta tutte queste operazioni.

{{% /alert %}}

Le forme in excel si suddividono principalmente nelle seguenti tipologie:
- **Linee**
- **Rettangoli**
- **Forme di base**
- **Frecce di blocco**
- **Forme di equazione**
- **Diagrammi di flusso**
- **Stelle e striscioni**
- **Didascalie**

Questo documento guida selezionerà una o due forme da ogni tipo per creare campioni. Attraverso questi esempi imparerai come usare[Aspose.Cells](https://products.aspose.com/cells/) per inserire la forma specificata nel foglio di lavoro.



## **Inserimento di una riga nel foglio di lavoro**

 La forma della linea appartiene al**linee** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la riga
- Fare clic sul menu Inserisci e fare clic su Forme.
- Quindi, seleziona la linea da "Forme utilizzate di recente" o "Linee"

![](line.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire una riga nel foglio di lavoro.

{{% alert color="primary" %}}

[public Shape addShape(int tipo, int upperLeftRow, int top, int upperLeftColumn, int left, int altezza, int larghezza)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire una riga in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](line2.png)



## **Inserimento di una freccia di linea nel foglio di lavoro**

 La forma della freccia della linea appartiene al**Linee**categoria. È un caso speciale di linea.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la freccia della linea
- Fare clic sul menu Inserisci e fare clic su Forme.
- Quindi, seleziona la freccia della linea da "Forme utilizzate di recente" o "Linee"

![](line_arrow1.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire una freccia di linea nel foglio di lavoro.

{{% alert color="primary" %}}

[public Shape addShape(int tipo, int upperLeftRow, int top, int upperLeftColumn, int left, int altezza, int larghezza)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire una freccia di linea in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](line_arrow2.png)



## **Inserimento di un rettangolo nel foglio di lavoro**

 La forma del rettangolo appartiene al**Rettangoli** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire il rettangolo
- Fare clic sul menu Inserisci e fare clic su Forme.
- Quindi, seleziona il rettangolo da "Forme utilizzate di recente" o "Rettangoli"

![](rectangle.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire un rettangolo nel foglio di lavoro.

{{% alert color="primary" %}}

[public Shape addShape(int tipo, int upperLeftRow, int top, int upperLeftColumn, int left, int altezza, int larghezza)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire un rettangolo in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](rectangle2.png)



## **Inserimento di un cubo nel foglio di lavoro**

 La forma del cubo appartiene al**Forme di base** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire il cubo
- Fare clic sul menu Inserisci e fare clic su Forme.
-  Quindi, seleziona il Cubo da**Forme di base**

![](cube.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire un cubo nel foglio di lavoro.

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire un cubo in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](cube2.png)



## **Inserimento di una freccia quadrupla callout nel foglio di lavoro**

 La forma della freccia quadrupla di callout appartiene al**Frecce di blocco** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la freccia quadrupla del callout
- Fare clic sul menu Inserisci e fare clic su Forme.
-  Quindi, seleziona la freccia quadrupla del callout da**Frecce di blocco**

![](callout_quad_arrow.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire una freccia quadrupla callout nel foglio di lavoro.

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire una freccia quadrupla di callout in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](callout_quad_arrow2.png)



## **Inserimento di un segno di moltiplicazione nel foglio di lavoro**

 La forma del segno di moltiplicazione appartiene al**Forme di equazione** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire il segno di moltiplicazione
- Fare clic sul menu Inserisci e fare clic su Forme.
-  Quindi, seleziona il segno di moltiplicazione da**Forme di equazione**

![](multiplication_sign.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire un segno di moltiplicazione nel foglio di lavoro.

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire il segno di moltiplicazione in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](multiplication_sign2.png)



## **Inserimento di un documento multiplo nel foglio di lavoro**

La forma del multidocumento appartiene al**Diagrammi di flusso** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui vuoi inserire il multidocumento
- Fare clic sul menu Inserisci e fare clic su Forme.
-  Quindi, seleziona il multidocumento da**Diagrammi di flusso**

![](multidocument.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il metodo seguente per inserire un documento multiplo nel foglio di lavoro.

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire più documenti in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](multidocument2.png)



## **Inserimento di una stella a cinque punte nel foglio di lavoro**

 La forma della stella a cinque punte appartiene al**Stelle e striscioni** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la stella a cinque punte
- Fare clic sul menu Inserisci e fare clic su Forme.
-  Quindi, seleziona la stella a cinque punte da**Stelle e striscioni**

![](star_5_points.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il seguente metodo per inserire una stella a cinque punte nel foglio di lavoro.

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire una stella a cinque punte in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](star_5_points2.png)



## **Inserimento di una nuvola di bolle di pensiero nel foglio di lavoro**

 La forma della nuvola di bolle di pensiero appartiene al**Didascalie** categoria.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la nuvola di bolle di pensiero
- Fare clic sul menu Inserisci e fare clic su Forme.
-  Quindi, seleziona la nuvola di bolle di pensiero da**Didascalie**

![](thought_bubble_cloud.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il seguente metodo per inserire una nuvola di bolle di pensiero nel foglio di lavoro.

{{% alert color="primary" %}}

[public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Il metodo restituisce a[Forma](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) oggetto.

{{% /alert %}}

L'esempio seguente mostra come inserire una nuvola di bolle di pensiero in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

Esegui il codice sopra, otterrai i seguenti risultati:

![](thought_bubble_cloud2.png)
