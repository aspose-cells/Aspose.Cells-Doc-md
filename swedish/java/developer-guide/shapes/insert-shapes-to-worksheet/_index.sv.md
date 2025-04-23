---
title: Infoga former i arbetsbladet i Aspose.Cells
type: docs
weight: 5
url: /sv/java/insert-shapes-to-worksheet-in-aspose-cells/
---


{{% alert color="primary" %}}

Ibland behöver du infoga vissa nödvändiga former i arbetsbladet. Du kan behöva infoga samma form på olika positioner på arbetsbladet. Eller så behöver du satsvis infoga former i arbetsbladet.

Var inte orolig! [Aspose.Cells](https://products.aspose.com/cells/) stöder alla dessa operationer.

{{% /alert %}}

Formerna i Excel är huvudsakligen uppdelade i följande typer:
- **Linjer**
- **Rektanglar**
- **Grundformer**
- **Blockpilar**
- **Ekvationformer**
- **Flödesscheman**
- **Stjärnor och banderoller**
- **Inrop**

Denna guide kommer att välja en eller två former från varje typ för att skapa exempel. Genom dessa exempel kommer du att lära dig hur du använder [Aspose.Cells](https://products.aspose.com/cells/) för att infoga den angivna formen i arbetsbladet.



## **Infoga en Linje i Arbetsblad**

Linjens form tillhör kategorin **linjer**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga linjen
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan linjen från 'Nyligen använda former' eller 'Linjer'

![](line.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga en linje i kalkylarket.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en linje i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](line2.png)



## **Infoga en Linje Pil i Arbetsblad**

Linjepilen tillhör kategorin **Linjer**. Det är ett specialfall av linje.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga linjepilen
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan linjepilen från 'Nyligen använda former' eller 'Linjer'

![](line_arrow1.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga en linjepil i kalkylarket.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en linjepil i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](line_arrow2.png)



## **Infoga en Rektangel i Arbetsblad**

Rektangeln tillhör kategorin **Rektanglar**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga rektangeln
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan rektangeln från 'Nyligen använda former' eller 'Rektanglar'

![](rectangle.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga en rektangel i kalkylarket.

{{% alert color="primary" %}}

[**public Shape addShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape-int-int-int-int-int-int-int-)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en rektangel i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](rectangle2.png)



## **Infoga en Kub i Arbetsblad**

Kuben tillhör kategorin **Grundformer**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga kuben
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan kuben från **Grundläggande former**

![](cube.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga en kub i kalkylarket.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en kub i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](cube2.png)



## **Infoga en pratbubbepil i Arbetsblad**

Formen av återuppringningpilar tillhör kategorin **Blockpilar**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga återuppringningspilar
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan återuppringningspilar från **Blockpilar**

![](callout_quad_arrow.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga återuppringningspilar i kalkylarket.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar återuppringningspilar i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](callout_quad_arrow2.png)



## **Infoga en multiplikationsskylt i Arbetsblad**

Formen av multiplikationstecken tillhör kategorin **Ekvationformer**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga multiplikationstecknet
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan multiplikationstecknet från **Ekvationformer**

![](multiplication_sign.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga ett multiplikationstecken i kalkylarket.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar ett multiplikationstecken i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](multiplication_sign2.png)



## **Infoga en multidokument i Arbetsblad**

Formen av multidokument tillhör kategorin **Flödesscheman**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga multi-dokument
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan multi-dokumentet från **Flödesscheman**

![](multidocument.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga ett multi-dokument i arbetsbladet.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar multi-dokument i ett arbetsblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](multidocument2.png)



## **Infoga en femuddig stjärna i Arbetsblad**

Formen av Femuddig stjärna tillhör kategorin **Stjärnor och band**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga Femuddig stjärna
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan Femuddig stjärna från **Stjärnor och band**

![](star_5_points.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga en Femuddig stjärna i arbetsbladet.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar Femuddig stjärna i ett arbetsblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](star_5_points2.png)



## **Infoga en tankebubbla till arbetsbladet**

Formen av pratbubblan tillhör kategorin **Pilfunktioner**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga pratbubblan
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan pratbubblan från **Pilfunktioner**

![](thought_bubble_cloud.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga en pratbubbla i arbetsbladet.

{{% alert color="primary" %}}

[**public Shape addAutoShape(int type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape-int-int-int-int-int-int-int-)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/java/com.aspose.cells/Shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar pratbubblan i ett arbetsblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](thought_bubble_cloud2.png)
{{< app/cells/assistant language="java" >}}
