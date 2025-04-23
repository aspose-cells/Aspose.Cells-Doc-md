---
title: Hantera bilder
type: docs
weight: 10
url: /sv/net/managing-pictures/
---

Aspose.Cells tillåter utvecklare att lägga till bilder i kalkylbladet under körtiden. Dessutom kan placeringen av dessa bilder styras under körtiden, vilket diskuteras mer utförligt i de kommande avsnitten.

Den här artikeln förklarar hur man lägger till bilder och hur man infogar en bild som visar innehållet i vissa celler.

## **Lägga till bilder**

Att lägga till bilder i ett kalkylblad är mycket enkelt. Det tar bara några rader kod:
Ring helt enkelt [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)-metoden för [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-objektet). Metoden [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) tar följande parametrar:

- **Övre vänstra radindex**, indexet för den övre vänstra raden.
- **Övre vänstra kolumnindex**, indexet för den övre vänstra kolumnen.
- **Bildfilnamn**, namnet på bildfilen, komplett med sökväg.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Placering av bilder**

Det finns två möjliga sätt att kontrollera placeringen av bilder med hjälp av Aspose.Cells:

- Proportionell placering: definiera ett läge proportionellt med radhöjden och kolumnbredden.
- Absolut placering: definiera den exakta positionen på sidan där bilden kommer att infogas, till exempel 40 pixlar till vänster och 20 pixlar under kanten på cellen.

### **Proportionell placering**

Utvecklare kan placera bilderna proportionellt med radhöjden och kolumnbredden med hjälp av [**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) och [**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) egenskaperna hos [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)-objektet. Ett [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)-objekt kan erhållas från [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)-samlingen genom att skicka dess bildindex. Detta exempel placerar en bild i cellen F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Absolut positionering**

Utvecklare kan också placera bilderna absolut genom att använda [**Left**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) och [**Top**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) egenskaperna hos [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)-objektet. Detta exempel placerar en bild i cellen F6, 60 pixlar från vänster och 10 pixlar från toppen av cellen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Infoga en bild baserad på cellreferens**

Aspose.Cells låter dig visa innehållet i en arbetsbladscell i en bildform. Du kan länka bilden till cellen som innehåller de data du vill visa. Eftersom cellen eller cellintervallet är länkat till den grafiska objektet, visas ändringar som du gör i data i den cellen eller cellintervallet automatiskt i den grafiska objektet.

Lägg till en bild i arbetsbladet genom att ringa [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index)-metoden för [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-objektet). Ange cellintervallet genom att använda attributet [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) för [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)-objektet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Fortsatta ämnen**
- [Lägg till villkorliga ikoner inställda med celltexten](/cells/sv/net/add-conditional-icons-set-with-the-cell-text/)
- [Infoga en Länkbild från Webbadress](/cells/sv/net/insert-a-linked-picture-from-web-address/)
- [Infoga en Bild Baserat på Cellreferens](/cells/sv/net/insert-a-picture-based-on-cell-reference/)
- [Ladda en webbbild från en URL till ett Excel-arbetsblad](/cells/sv/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="csharp" >}}
