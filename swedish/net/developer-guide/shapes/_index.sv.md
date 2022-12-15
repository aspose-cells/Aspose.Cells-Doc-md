---
title: Infoga bilder och former av Excel-filer.
linktitle: Former
type: docs
weight: 140
url: /sv/net/insert-shapes/
description: Hantera bilder, oleobject, former till Excel-filer.
---
{{% alert color="primary" %}}

Ibland behöver du infoga några nödvändiga former i kalkylbladet. Du kan behöva infoga samma form på olika positioner i kalkylbladet. Eller så måste du infoga former i kalkylbladet.

 Oroa dig inte![Aspose.Cells](https://products.aspose.com/cells/) stöder alla dessa operationer.

{{% /alert %}}

Formerna i excel är huvudsakligen indelade i följande typer:
- **Bilder**
- **OleObjects**
- **Rader**
- **Rektanglar**
- **Grundläggande former**
- **Block pilar**
- **Ekvationsformer**
- **Flödesdiagram**
- **Stjärnor och banderoller**
- **Bildtexter**

Detta guidedokument kommer att välja en eller två former från varje typ för att göra prover. Genom dessa exempel kommer du att lära dig hur du använder[Aspose.Cells](https://products.aspose.com/cells/) för att infoga den angivna formen i kalkylbladet.

## **Lägga till bilder i Excel-arbetsblad i C#**

Det är väldigt enkelt att lägga till bilder i ett kalkylblad. Det tar bara några rader kod:
 Ring helt enkelt[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) metod för[**Bilder**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) samling (inkapslad i[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objekt). De[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)metoden tar följande parametrar:

- **Övre vänstra radens index**, indexet för den övre vänstra raden.
- **Övre vänstra kolumnindex**, indexet för den övre vänstra kolumnen.
- **Bildfilens namn**, namnet på bildfilen, komplett med sökväg.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}


## **Infoga OLE-objekt i Excel-kalkylblad i C#**

Aspose.Cells stöder att lägga till, extrahera och manipulera OLE-objekt i kalkylblad. Av denna anledning har Aspose.Cells[**OleObjectCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobjectcollection) klass, används för att lägga till ett nytt OLE-objekt till samlingslistan. En annan klass,[**OleObject**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject), representerar ett OLE-objekt. Den har några viktiga medlemmar:

-  De[**ImageData**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/imagedata)egenskapen specificerar bilddata (ikon) av byte-arraytyp. Bilden kommer att visas för att visa OLE-objektet i kalkylbladet.
-  De[**Objektdata**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/objectdata)egenskapen specificerar objektdata i form av en byte-array. Dessa data kommer att visas i dess relaterade program när du dubbelklickar på OLE-objektikonen.

Följande exempel visar hur man lägger till ett eller flera OLE-objekt i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-InsertingOLEObjects-1.cs" >}}

## **Infoga en rad till Excel-kalkylblad i C#**

 Linjens form tillhör**rader** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga raden
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan raden från "Nyligen använda former" eller "Linjer"

![](line.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga en rad i kalkylbladet.

{{% alert color="primary" %}}

[public LineShape AddLine(
 int upperLeftRow,
 int topp,
 int övre vänstra kolumnen,
 int vänster,
 int höjd,
 int bredd
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 Metoden returnerar en[LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en rad i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Line.cs" >}}

Utför koden ovan, du får följande resultat:

![](line2.png)



## **Infoga en linjepil i Excel-kalkylblad i C#**

 Formen på linjepilen tillhör**Rader**kategori. Det är ett specialfall av linje.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga linjepilen
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan linjepilen från "Nyligen använda former" eller "Linjer"

![](line_arrow1.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga en linjepil i kalkylbladet.

{{% alert color="primary" %}}

[public LineShape AddLine(
 int upperLeftRow,
 int topp,
 int övre vänstra kolumnen,
 int vänster,
 int höjd,
 int bredd
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline)

 Metoden returnerar en[LineShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en linjepil i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-LineArrow.cs" >}}

Utför koden ovan, du får följande resultat:

![](line_arrow2.png)



## **Infoga en rektangel till Excel-kalkylblad i C#**

 Formen på rektangeln tillhör**Rektanglar** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga rektangeln
- Klicka på Infoga-menyn och klicka på Former.
- Välj sedan rektangeln från "Nyligen använda former" eller "Rektanglar"

![](rectangle.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga en rektangel i kalkylbladet.

{{% alert color="primary" %}}

[public RectangleShape AddRectangle(
 int upperLeftRow,
 int topp,
 int övre vänstra kolumnen,
 int vänster,
 int höjd,
 int bredd
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle)

 Metoden returnerar en[RectangleShape](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) objekt.

{{% /alert %}}

Följande exempel visar hur du infogar rektangel i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Rectangle.cs" >}}

Utför koden ovan, du får följande resultat:

![](rectangle2.png)



## **Infoga en kub till Excel-arbetsblad i C#**

 Formen på kuben tillhör**Grundläggande former** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga kuben
- Klicka på Infoga-menyn och klicka på Former.
-  Välj sedan kuben från**Grundläggande former**

![](cube.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga en kub i kalkylbladet.

{{% alert color="primary" %}}

[public Shape AddAutoShape(
 AutoShapeType typ,
 int upperLeftRow,
 int topp,
 int övre vänstra kolumnen,
 int vänster,
 int höjd,
 int bredd
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Metoden returnerar en[Form](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en kub i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Cube.cs" >}}

Utför koden ovan, du får följande resultat:

![](cube2.png)



## **Infoga en bildtext quad-pil i Excel-kalkylblad i C#**

 Formen på bildtexten quad pil tillhör**Block pilar** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga bildtexten quad-pilen
- Klicka på Infoga-menyn och klicka på Former.
-  Välj sedan bildtexten quad-pilen från**Block pilar**

![](callout_quad_arrow.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga en bildtext quad-pil i kalkylbladet.

{{% alert color="primary" %}}

[public Shape AddAutoShape(
 AutoShapeType typ,
 int upperLeftRow,
 int topp,
 int övre vänstra kolumnen,
 int vänster,
 int höjd,
 int bredd
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Metoden returnerar en[Form](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar bildtext quad-pil i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-CalloutQuadArrow.cs" >}}

Utför koden ovan, du får följande resultat:

![](callout_quad_arrow2.png)



## **Infoga ett multiplikationstecken i Excel-kalkylblad i C#**

 Formen på multiplikationstecknet tillhör**Ekvationsformer** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga multiplikationstecknet
- Klicka på Infoga-menyn och klicka på Former.
-  Välj sedan multiplikationstecknet från**Ekvationsformer**

![](multiplication_sign.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga ett multiplikationstecken i kalkylbladet.

{{% alert color="primary" %}}

[public Shape AddAutoShape(
 AutoShapeType typ,
 int upperLeftRow,
 int topp,
 int övre vänstra kolumnen,
 int vänster,
 int höjd,
 int bredd
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Metoden returnerar en[Form](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar multiplikationstecken i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-MultiplicationSign.cs" >}}

Utför koden ovan, du får följande resultat:

![](multiplication_sign2.png)



## **Infoga ett multidokument till Excel-kalkylblad i C#**

Formen på multidokument tillhör**Flödesdiagram** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga multidokumentet
- Klicka på Infoga-menyn och klicka på Former.
-  Välj sedan multidokumentet från**Flödesdiagram**

![](multidocument.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga ett multidokument i kalkylbladet.

{{% alert color="primary" %}}

[public Shape AddAutoShape(
 AutoShapeType typ,
 int upperLeftRow,
 int topp,
 int övre vänstra kolumnen,
 int vänster,
 int höjd,
 int bredd
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Metoden returnerar en[Form](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar flera dokument i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-Multidocument.cs" >}}

Utför koden ovan, du får följande resultat:

![](multidocument2.png)



## **Infoga en femuddig stjärna i Excel-arbetsbladet i C#**

 Formen på en femuddig stjärna tillhör**Stjärnor och banderoller** kategori.

***I Microsoft Excel (till exempel 2007):***

- Markera cellen där du vill infoga den femuddiga stjärnan
- Klicka på Infoga-menyn och klicka på Former.
-  Välj sedan den femuddiga stjärnan från**Stjärnor och banderoller**

![](star_5_points.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga en femuddig stjärna i kalkylbladet.

{{% alert color="primary" %}}

[public Shape AddAutoShape(
 AutoShapeType typ,
 int upperLeftRow,
 int topp,
 int övre vänstra kolumnen,
 int vänster,
 int höjd,
 int bredd
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Metoden returnerar en[Form](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar en femuddig stjärna i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-FivePointedStar.cs" >}}

Utför koden ovan, du får följande resultat:

![](star_5_points2.png)



## **Infogar ett tankebubbelmoln i Excel-arbetsblad i C#**

 Formen på tankebubbelmoln tillhör**Bildtexter** kategori.

***I Microsoft Excel (till exempel 2007):***

- Välj cellen där du vill infoga tankebubbelmolnet
- Klicka på Infoga-menyn och klicka på Former.
-  Välj sedan tankebubblans moln från**Bildtexter**

![](thought_bubble_cloud.png)

***Använder Aspose.Cells***

Du kan använda följande metod för att infoga ett tankebubbelmoln i kalkylbladet.

{{% alert color="primary" %}}

[public Shape AddAutoShape(
 AutoShapeType typ,
 int upperLeftRow,
 int topp,
 int övre vänstra kolumnen,
 int vänster,
 int höjd,
 int bredd
)](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addautoshape)

 Metoden returnerar en[Form](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) objekt.

{{% /alert %}}

Följande exempel visar hur man infogar tankebubblor i ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-InsertShapesToWorksheetInAsposeCells-ThoughtBubbleCloud.cs" >}}

Utför koden ovan, du får följande resultat:

![](thought_bubble_cloud2.png)

## **Förhandsämnen**
- [Ändra justeringsvärden för formen](/cells/sv/net/change-adjustment-values-of-the-shape/)
- [Kopiera former mellan kalkylblad](/cells/sv/net/copy-shapes-between-worksheets/)
- [Data i icke-primitiv form](/cells/sv/net/data-in-non-primitive-shape/)
- [Hitta den absoluta positionen av formen i arbetsbladet](/cells/sv/net/finding-absolute-position-of-shape-inside-the-worksheet/)
- [Få anslutningspunkter från form](/cells/sv/net/get-connection-points-from-shape/)
- [Hantera kontroller](/cells/sv/net/managing-controls/)
- [Lägg till ikoner i arbetsbladet](/cells/sv/net/insert-svg-to-excel/)
- [Hantera OLE-objekt](/cells/sv/net/managing-ole-objects/)
- [Hantera bilder](/cells/sv/net/managing-pictures/)
- [Hantera Smart Art](/cells/sv/net/managing-smartart/)
- [Hantera TextBox](/cells/sv/net/managing-textbox-of-excel/)
- [Lägg till WordArt vattenstämpel i arbetsbladet](/cells/sv/net/add-wordart-watermark-to-worksheet/)
- [Uppdatera värden för länkade former](/cells/sv/net/refresh-values-of-linked-shapes/)
- [Skicka form fram eller bak i arbetsbladet](/cells/sv/net/send-shape-front-or-back-inside-the-worksheet/)
- [Hantera formalternativ](/cells/sv/net/managing-shape-options/)
- [Hantera formtextalternativ](/cells/sv/net/managing-shape-text-options/)
- [Webbtillägg - Office-tillägg](/cells/sv/net/web-extensions-office-add-ins/)

