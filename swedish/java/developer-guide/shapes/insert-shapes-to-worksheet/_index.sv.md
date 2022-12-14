---
title: Infoga former till arbetsblad i Aspose.Cells
type: docs
weight: 5
url: /sv/java/insert-shapes-to-worksheet-in-aspose-cells/
---
{{% alert color="primary" %}}

Ibland behöver du infoga några nödvändiga former i kalkylbladet. Du kan behöva infoga samma form på olika positioner i kalkylbladet. Eller så måste du infoga former i kalkylbladet.

 Oroa dig inte![Aspose.Cells](https://products.aspose.com/cells/) stöder alla dessa operationer.

{{% /alert %}}

Formerna i excel är huvudsakligen indelade i följande typer:
- **Rader**
- **Rektanglar**
- **Grundläggande former**
- **Block pilar**
- **Ekvationsformer**
- **Flödesdiagram**
- **Stjärnor och banderoller**
- **Bildtexter**

Detta guidedokument kommer att välja en eller två former från varje typ för att göra prover. Genom dessa exempel kommer du att lära dig hur du använder[Aspose.Cells](https://products.aspose.com/cells/) för att infoga den angivna formen i kalkylbladet.



## **Infoga en rad i arbetsbladet**

 Linjens form tillhör**rader** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga raden
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan raden från "Nyligen använda former" eller "Linjer"

![](line.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga en rad i kalkylbladet.

{{% alert color="primary" %}}

[public Shape addShape(int typ, int upperLeftRow, int top, int upperLeftColumn, int left, int höjd, int bredd)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Metoden returnerar en[Form](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en rad i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Line.java" >}}

Utför koden ovan, du får följande resultat:

![](line2.png)



## **Infoga en linjepil i arbetsblad**

 Formen på linjepilen tillhör**Rader**kategori. Det är ett specialfall av linje.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga linjepilen
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan linjepilen från "Nyligen använda former" eller "Linjer"

![](line_arrow1.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga en linjepil i kalkylbladet.

{{% alert color="primary" %}}

[public Shape addShape(int typ, int upperLeftRow, int top, int upperLeftColumn, int left, int höjd, int bredd)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Metoden returnerar en[Form](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en linjepil i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-LineArrow.java" >}}

Utför koden ovan, du får följande resultat:

![](line_arrow2.png)



## **Infoga en rektangel i arbetsbladet**

 Formen på rektangeln tillhör**Rektanglar** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga rektangeln
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan rektangeln från "Nyligen använda former" eller "Rektanglar"

![](rectangle.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga en rektangel i kalkylbladet.

{{% alert color="primary" %}}

[public Shape addShape(int typ, int upperLeftRow, int top, int upperLeftColumn, int left, int höjd, int bredd)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Metoden returnerar en[Form](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objekt.

{{% /alert %}}

Följande exempel visar hur du infogar rektangel i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Rectangle.java" >}}

Utför koden ovan, du får följande resultat:

![](rectangle2.png)



## **Infoga en kub i arbetsbladet**

 Formen på kuben tillhör**Grundläggande former** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga kuben
- Klicka på Infoga-menyn och klicka på Former.
-  Välj sedan kuben från**Grundläggande former**

![](cube.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga en kub i kalkylbladet.

{{% alert color="primary" %}}

[public Shape addAutoShape(int typ, int upperLeftRow, int top, int upperLeftColumn, int left, int höjd, int bredd)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Metoden returnerar en[Form](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en kub i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Cube.java" >}}

Utför koden ovan, du får följande resultat:

![](cube2.png)



## **Infogar en bildtext quad-pil i kalkylblad**

 Formen på bildtexten quad pil tillhör**Block pilar** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga bildtexten quad-pilen
- Klicka på Infoga-menyn och klicka på Former.
-  Välj sedan bildtexten quad-pilen från**Block pilar**

![](callout_quad_arrow.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga en bildtext quad-pil i kalkylbladet.

{{% alert color="primary" %}}

[public Shape addAutoShape(int typ, int upperLeftRow, int top, int upperLeftColumn, int left, int höjd, int bredd)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Metoden returnerar en[Form](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar bildtext quad-pil i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.java" >}}

Utför koden ovan, du får följande resultat:

![](callout_quad_arrow2.png)



## **Infoga ett multiplikationstecken i arbetsbladet**

 Formen på multiplikationstecknet tillhör**Ekvationsformer** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga multiplikationstecknet
- Klicka på Infoga-menyn och klicka på Former.
-  Välj sedan multiplikationstecknet från**Ekvationsformer**

![](multiplication_sign.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga ett multiplikationstecken i kalkylbladet.

{{% alert color="primary" %}}

[public Shape addAutoShape(int typ, int upperLeftRow, int top, int upperLeftColumn, int left, int höjd, int bredd)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Metoden returnerar en[Form](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar multiplikationstecken i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.java" >}}

Utför koden ovan, du får följande resultat:

![](multiplication_sign2.png)



## **Infoga ett multidokument i kalkylblad**

Formen på multidokument tillhör**Flödesdiagram** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga multidokumentet
- Klicka på Infoga-menyn och klicka på Former.
-  Välj sedan multidokumentet från**Flödesdiagram**

![](multidocument.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga ett multidokument i kalkylbladet.

{{% alert color="primary" %}}

[public Shape addAutoShape(int typ, int upperLeftRow, int top, int upperLeftColumn, int left, int höjd, int bredd)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Metoden returnerar en[Form](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar flera dokument i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-Multidocument.java" >}}

Utför koden ovan, du får följande resultat:

![](multidocument2.png)



## **Infoga en femuddig stjärna i arbetsbladet**

 Formen på en femuddig stjärna tillhör**Stjärnor och banderoller** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga den femuddiga stjärnan
- Klicka på Infoga-menyn och klicka på Former.
-  Välj sedan den femuddiga stjärnan från**Stjärnor och banderoller**

![](star_5_points.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga en femuddig stjärna i kalkylbladet.

{{% alert color="primary" %}}

[public Shape addAutoShape(int typ, int upperLeftRow, int top, int upperLeftColumn, int left, int höjd, int bredd)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Metoden returnerar en[Form](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en femuddig stjärna i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-FivePointedStar.java" >}}

Utför koden ovan, du får följande resultat:

![](star_5_points2.png)



## **Infoga ett tankebubbelmoln i arbetsblad**

 Formen på tankebubbelmoln tillhör**Bildtexter** kategori.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga tankebubbelmolnet
- Klicka på Infoga-menyn och klicka på Former.
-  Välj sedan tankebubblans moln från**Bildtexter**

![](thought_bubble_cloud.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga ett tankebubbelmoln i kalkylbladet.

{{% alert color="primary" %}}

[public Shape addAutoShape(int typ, int upperLeftRow, int top, int upperLeftColumn, int left, int höjd, int bredd)](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addAutoShape(int,%20int,%20int,%20int,%20int,%20int,%20int))

 Metoden returnerar en[Form](https://reference.aspose.com/cells/java/com.aspose.cells/Shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar tankebubblor i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-Java-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.java" >}}

Utför koden ovan, du får följande resultat:

![](thought_bubble_cloud2.png)
