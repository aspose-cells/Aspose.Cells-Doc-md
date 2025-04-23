---
title: Hantera bilder
type: docs
weight: 10
url: /sv/python-net/managing-pictures/
---

Aspose.Cells för Python via .NET tillåter utvecklare att lägga till bilder till kalkylblad under körning. Dessutom kan positioneringen av dessa bilder kontrolleras vid körning, vilket diskuteras mer i detalj i kommande avsnitt.

Den här artikeln förklarar hur man lägger till bilder och hur man infogar en bild som visar innehållet i vissa celler.

## **Lägga till bilder**

Att lägga till bilder i ett kalkylblad är mycket enkelt. Det tar bara några rader kod:
Ring helt enkelt [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add)-metoden för [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-objektet). Metoden [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add) tar följande parametrar:

- **Övre vänstra radindex**, indexet för den övre vänstra raden.
- **Övre vänstra kolumnindex**, indexet för den övre vänstra kolumnen.
- **Bildfilnamn**, namnet på bildfilen, komplett med sökväg.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-AddingPictures-1.py" >}}

## **Placering av bilder**

Det finns två möjliga sätt att styra positioneringen av bilder med Aspose.Cells för Python via .NET:

- Proportionell placering: definiera ett läge proportionellt med radhöjden och kolumnbredden.
- Absolut placering: definiera den exakta positionen på sidan där bilden kommer att infogas, till exempel 40 pixlar till vänster och 20 pixlar under kanten på cellen.

### **Proportionell placering**

Utvecklare kan placera bilderna proportionellt med radhöjden och kolumnbredden med hjälp av [**upper_delta_x**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_x) och [**upper_delta_y**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_y) egenskaperna hos [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-objektet. Ett [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-objekt kan erhållas från [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection)-samlingen genom att skicka dess bildindex. Detta exempel placerar en bild i cellen F6.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.py" >}}

### **Absolut positionering**

Utvecklare kan också placera bilderna absolut genom att använda [**left**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/left) och [**top**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/top) egenskaperna hos [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-objektet. Detta exempel placerar en bild i cellen F6, 60 pixlar från vänster och 10 pixlar från toppen av cellen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.py" >}}

## **Infoga en bild baserad på cellreferens**

Aspose.Cells för Python via .NET låter dig visa innehållet i en cell i ett kalkylblad i en bildform. Du kan länka bilden till cellen som innehåller de data du vill visa. Eftersom cellen eller cellområdet är länkat till den grafiska objekten, visas ändringar du gör i data i den cellen eller cellområdet automatiskt i det grafiska objektet.

Lägg till en bild i arbetsbladet genom att ringa [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture)-metoden för [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-objektet). Ange cellintervallet genom att använda attributet [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) för [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-objektet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PictureCellReference-1.py" >}}

## **Fortsatta ämnen**
- [Lägg till villkorliga ikoner inställda med celltexten](/cells/sv/python-net/add-conditional-icons-set-with-the-cell-text/)
- [Infoga en Länkbild från Webbadress](/cells/sv/python-net/insert-a-linked-picture-from-web-address/)
- [Infoga en Bild Baserat på Cellreferens](/cells/sv/python-net/insert-a-picture-based-on-cell-reference/)
- [Ladda en webbbild från en URL till ett Excel-arbetsblad](/cells/sv/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

