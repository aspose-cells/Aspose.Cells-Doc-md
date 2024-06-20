---
title: Infoga bilder och former från Excelfiler.
linktitle: Former
type: docs
weight: 140
url: /sv/net/insert-shapes/
description: Hantera bilder, oleobjekt, former i Excelfiler.
---

{{% alert color="primary" %}}

Ibland behöver du infoga vissa nödvändiga former i arbetsbladet. Du kan behöva infoga samma form på olika positioner på arbetsbladet. Eller så behöver du satsvis infoga former i arbetsbladet.

Var inte orolig! [Aspose.Cells](https://products.aspose.com/cells/) stöder alla dessa operationer.

{{% /alert %}}

Formerna i Excel är huvudsakligen uppdelade i följande typer:
- **Bilder**
- **OleObjekt**
- **Linjer**
- **Rektanglar**
- **Grundformer**
- **Blockpilar**
- **Ekvationformer**
- **Flödesscheman**
- **Stjärnor och banderoller**
- **Inrop**

Denna guide kommer att välja en eller två former från varje typ för att skapa exempel. Genom dessa exempel kommer du att lära dig hur du använder [Aspose.Cells](https://products.aspose.com/cells/) för att infoga den angivna formen i arbetsbladet.

## **Lägga till bilder i Excelkalkylblad i C#**

Att lägga till bilder i ett kalkylblad är mycket enkelt. Det tar bara några rader kod:
Ring helt enkelt [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)-metoden för [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-objektet). Metoden [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) tar följande parametrar:

- **Övre vänstra radindex**, indexet för den övre vänstra raden.
- **Övre vänstra kolumnindex**, indexet för den övre vänstra kolumnen.
- **Bildfilnamn**, namnet på bildfilen, komplett med sökväg.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **Infoga OLE-objekt i Excelkalkylblad i C#**

Aspose.Cells stöder att lägga till, extrahera och manipulera OLE-objekt i arbetsblad. Av den anledningen har Aspose.Cells klassen [**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection), som används för att lägga till ett nytt OLE-objekt i samlingens lista. En annan klass, [**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), representerar ett OLE-objekt. Den har några viktiga medlemmar:

- Egenskapen [**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata) anger bild (ikon) data av typen byte array. Bilden kommer att visas för att visa OLE-objektet i arbetsbladet.
- Egenskapen [**ObjectData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata) anger objektdata i form av en byte array. Denna data kommer att visas i sitt relaterade program när du dubbelklickar på OLE-objektikonen.

Följande exempel visar hur man lägger till en OLE-objekt/-objekt i ett arbetsblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **Infoga en linje i Excelkalkylblad i C#**

Linjens form tillhör kategorin **linjer**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga linjen
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan linjen från 'Nyligen använda former' eller 'Linjer'

![](line.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga en linje i kalkylarket.

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

Metoden returnerar ett [LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en linje i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](line2.png)



## **Infoga en linskära till Excel arbetsblad i C#**

Linjepilen tillhör kategorin **Linjer**. Det är ett specialfall av linje.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga linjepilen
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan linjepilen från 'Nyligen använda former' eller 'Linjer'

![](line_arrow1.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga en linjepil i kalkylarket.

{{% alert color="primary" %}}

[**public LineShape AddLine(int upperLeftRow, int top, int upperLeftColumn,	int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

Metoden returnerar ett [LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en linjepil i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](line_arrow2.png)



## **Infoga en rektangel till Excel arbetsblad i C#**

Rektangeln tillhör kategorin **Rektanglar**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga rektangeln
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan rektangeln från 'Nyligen använda former' eller 'Rektanglar'

![](rectangle.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga en rektangel i kalkylarket.

{{% alert color="primary" %}}

[**public RectangleShape AddRectangle(int upperLeftRow,	int top, int upperLeftColumn, int left,	int height,	int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

Metoden returnerar ett [RectangleShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en rektangel i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](rectangle2.png)



## **Infoga en kub i Excel-kalkylbladet i C#**

Kuben tillhör kategorin **Grundformer**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga kuben
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan kuben från **Grundläggande former**

![](cube.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga en kub i kalkylarket.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en kub i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](cube2.png)



## **Infoga en pratbubbla med pil till Excel-kalkylbladet i C#**

Formen av återuppringningpilar tillhör kategorin **Blockpilar**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga återuppringningspilar
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan återuppringningspilar från **Blockpilar**

![](callout_quad_arrow.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga återuppringningspilar i kalkylarket.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar återuppringningspilar i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](callout_quad_arrow2.png)



## **Infoga ett multiplikationstecken i Excel-kalkylbladet i C#**

Formen av multiplikationstecken tillhör kategorin **Ekvationformer**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga multiplikationstecknet
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan multiplikationstecknet från **Ekvationformer**

![](multiplication_sign.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga ett multiplikationstecken i kalkylarket.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar ett multiplikationstecken i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](multiplication_sign2.png)



## **Infoga en multidokument till Excel-kalkylbladet i C#**

Formen av multidokument tillhör kategorin **Flödesscheman**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga multi-dokument
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan multi-dokumentet från **Flödesscheman**

![](multidocument.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga ett multi-dokument i arbetsbladet.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar multi-dokument i ett arbetsblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](multidocument2.png)



## **Infoga en femuddig stjärna till Excel-kalkylbladet i C#**

Formen av Femuddig stjärna tillhör kategorin **Stjärnor och band**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga Femuddig stjärna
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan Femuddig stjärna från **Stjärnor och band**

![](star_5_points.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga en Femuddig stjärna i arbetsbladet.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top, int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar Femuddig stjärna i ett arbetsblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](star_5_points2.png)



## **Infoga en pratbubbla till Excel-kalkylbladet i C#**

Formen av pratbubblan tillhör kategorin **Pilfunktioner**.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga pratbubblan
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan pratbubblan från **Pilfunktioner**

![](thought_bubble_cloud.png)

***Använda Aspose.Cells***

Du kan använda följande metod för att infoga en pratbubbla i arbetsbladet.

{{% alert color="primary" %}}

[**public Shape AddAutoShape(AutoShapeType type, int upperLeftRow, int top,	int upperLeftColumn, int left, int height, int width)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

Metoden returnerar en [Shape](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape)-objekt.

{{% /alert %}}

Följande exempel visar hur man infogar pratbubblan i ett arbetsblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

Exekvera ovanstående kod, kommer du att få följande resultat:

![](thought_bubble_cloud2.png)

## **Fortsatta ämnen**
- [Ändra justeringsvärden för formen](/cells/sv/net/change-adjustment-values-of-the-shape/)
- [Kopiera former mellan kalkylblad](/cells/sv/net/copy-shapes-between-worksheets/)
- [Data i icke-primitiv form](/cells/sv/net/data-in-non-primitive-shape/)
- [Hitta absolut position av formen inuti kalkylbladet](/cells/sv/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Hämta anslutningspunkter från formen](/cells/sv/net/get-connection-points-from-shape/)
- [Hantera kontroller](/cells/sv/net/managing-controls/)
- [Lägg till ikoner i kalkylbladet](/cells/sv/net/insert-svg-to-excel/)
- [Hantera OLE-objekt](/cells/sv/net/managing-ole-objects/)
- [Hantera bilder](/cells/sv/net/managing-pictures/)
- [Hantera SmartArt](/cells/sv/net/managing-smartart/)
- [Hantera TextBox](/cells/sv/net/managing-textbox-of-excel/)
- [Lägg till WordArt-vattenstämpel på arbetsbladet](/cells/sv/net/add-wordart-watermark-to-worksheet/)
- [Uppdatera värdena i länkade former](/cells/sv/net/refresh-values-of-linked-shapes/)
- [Skicka form framåt eller bakåt inne i Arbetsbladet](/cells/sv/net/send-shape-front-or-back-inside-the-worksheet/)
- [Hantera formalternativ](/cells/sv/net/managing-shape-options/)
- [Hantera textalternativ för formen](/cells/sv/net/managing-shape-text-options/)
- [Webbutökningar - Office-tillägg](/cells/sv/net/web-extensions-office-add-ins/)

