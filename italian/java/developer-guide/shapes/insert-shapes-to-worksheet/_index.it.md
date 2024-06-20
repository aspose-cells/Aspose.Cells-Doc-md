---
title: Inserisci forme nel foglio di lavoro in Aspose.Cells
type: docs
weight: 5
url: /it/java/insert-shapes-to-worksheet-in-aspose-cells/
---


{{% alert color="primary" %}}

A volte è necessario inserire alcune forme necessarie nel foglio di lavoro. Potresti aver bisogno di inserire la stessa forma in posizioni diverse del foglio di lavoro. O potresti aver bisogno di inserire batch di forme nel foglio di lavoro.

Non preoccuparti! [Aspose.Cells](https://products.aspose.com/cells/) supporta tutte queste operazioni.

{{% /alert %}}

Le forme in Excel sono principalmente divise nei seguenti tipi:
- **Linee**
- **Rettangoli**
- **Forme di base**
- **Frecce a blocco**
- **Forme di equazione**
- **Diagrammi di flusso**
- **Stelle e striscioni**
- **Callout**

Questo documento guida selezionerà uno o due forme da ciascun tipo per creare degli esempi. Attraverso questi esempi, imparerai come utilizzare [Aspose.Cells](https://products.aspose.com/cells/) per inserire la forma specificata nel foglio di lavoro.



## **Inserimento di una linea sul foglio di lavoro**

La forma della linea appartiene alla categoria **linee**.

***In Microsoft Excel (ad esempio 2007):***

- Selezionare la cella dove si desidera inserire la linea
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi, selezionare la linea da 'Forme usate di recente' o 'Linee'

![](line.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il seguente metodo per inserire una linea nel foglio di lavoro.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'esempio seguente mostra come inserire una linea in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](line2.png)



## **Inserimento di una freccia linea sul foglio di lavoro**

La forma della freccia di linea appartiene alla categoria **Linee**. È un caso speciale di linea.

***In Microsoft Excel (ad esempio 2007):***

- Selezionare la cella dove si desidera inserire la freccia di linea
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi, selezionare la freccia della riga da 'Forme utilizzate di recente' o 'Linee'

![](line_arrow1.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il seguente metodo per inserire una freccia di linea nel foglio di lavoro.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'esempio seguente mostra come inserire una freccia di linea in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](line_arrow2.png)



## **Inserimento di un rettangolo sul foglio di lavoro**

La forma del rettangolo appartiene alla categoria **Rettangoli**.

***In Microsoft Excel (ad esempio 2007):***

- Selezionare la cella in cui si desidera inserire il rettangolo
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi, selezionare il rettangolo da 'Forme utilizzate di recente' o 'Rettangoli'

![](rectangle.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il seguente metodo per inserire un rettangolo nel foglio di lavoro.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'esempio seguente mostra come inserire un rettangolo in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](rectangle2.png)



## **Inserimento di un cubo sul foglio di lavoro**

La forma del cubo appartiene alla categoria **Forme di base**.

***In Microsoft Excel (ad esempio 2007):***

- Selezionare la cella in cui si desidera inserire il cubo
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi, selezionare il cubo da **Forme di base**

![](cube.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il seguente metodo per inserire un cubo nel foglio di lavoro.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'esempio seguente mostra come inserire un cubo in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](cube2.png)



## **Inserimento di una freccia quadro di annotazione sul foglio di lavoro**

La forma della freccia quadri callout appartiene alla categoria **Frecci quadrate**.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la freccia quadrupla di chiamata
- Fai clic sul menu Inserisci e seleziona Forme.
- Successivamente, seleziona la freccia quadrupla di chiamata da **Frecce a blocco**

![](callout_quad_arrow.png)

***Utilizzando Aspose.Cells***

Puoi utilizzare il seguente metodo per inserire una freccia quadrupla di chiamata nel foglio di lavoro.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'esempio seguente mostra come inserire una freccia quadrupla di chiamata in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](callout_quad_arrow2.png)



## **Inserimento di un segno di moltiplicazione sul foglio di lavoro**

La forma del segno di moltiplicazione appartiene alla categoria **Forme di equazione**.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire il segno di moltiplicazione
- Fai clic sul menu Inserisci e seleziona Forme.
- Successivamente, seleziona il segno di moltiplicazione da **Forme di equazione**

![](multiplication_sign.png)

***Utilizzando Aspose.Cells***

Puoi utilizzare il seguente metodo per inserire un segno di moltiplicazione nel foglio di lavoro.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

Nell'esempio seguente viene mostrato come inserire un segno di moltiplicazione in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](multiplication_sign2.png)



## **Inserimento di un documento multidocumento sul foglio di lavoro**

La forma del multidocumento appartiene alla categoria **FlowCharts**.

***In Microsoft Excel (ad esempio 2007):***

- Selezionare la cella in cui si desidera inserire il multidocumento
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi selezionare il multidocumento da **FlowCharts**

![](multidocument.png)

***Utilizzando Aspose.Cells***

Puoi utilizzare il seguente metodo per inserire un multidocumento nel foglio di lavoro.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

Nell'esempio seguente viene mostrato come inserire un multidocumento in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](multidocument2.png)



## **Inserimento di una stella a cinque punte sul foglio di lavoro**

La forma della stella a cinque punte appartiene alla categoria **Stelle e Bandiere**.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la stella a cinque punte
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi, seleziona la stella a cinque punte da **Stelle e Bandiere**

![](star_5_points.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il seguente metodo per inserire una stella a cinque punte nel foglio di lavoro.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'esempio seguente mostra come inserire una stella a cinque punte in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](star_5_points2.png)



## **Inserimento di una nuvola di pensiero sul foglio di lavoro**

La forma della nuvola a forma di fumetto appartiene alla categoria **Callout**.

***In Microsoft Excel (ad esempio 2007):***

- Seleziona la cella in cui desideri inserire la nuvola a forma di fumetto
- Fai clic sul menu Inserisci e seleziona Forme.
- Quindi, seleziona la nuvola a forma di fumetto da **Callout**

![](thought_bubble_cloud.png)

***Utilizzando Aspose.Cells***

È possibile utilizzare il seguente metodo per inserire una nuvola di pensiero nel foglio di lavoro.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

Il metodo restituisce un oggetto [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape).

{{% /alert %}}

L'esempio seguente mostra come inserire una nuvola di pensiero in un foglio di lavoro.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

Eseguendo il codice precedente, otterrai i seguenti risultati:

![](thought_bubble_cloud2.png)
