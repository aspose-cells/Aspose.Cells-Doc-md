---
title: Hantera bilder
type: docs
weight: 10
url: /sv/net/managing-pictures/
---
Aspose.Cells tillåter utvecklare att lägga till bilder i kalkylblad under körning. Dessutom kan placeringen av dessa bilder styras under körning, vilket diskuteras mer i detalj i de kommande avsnitten.

Den här artikeln förklarar hur man lägger till bilder och hur man infogar en bild som visar innehållet i vissa celler.

## **Lägga till bilder**

Det är väldigt enkelt att lägga till bilder i ett kalkylblad. Det tar bara några rader kod:
 Ring helt enkelt[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) metod för[**Bilder**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) samling (inkapslad i[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objekt). De[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)metoden tar följande parametrar:

- **Övre vänstra radens index**, indexet för den övre vänstra raden.
- **Övre vänstra kolumnindex**, indexet för den övre vänstra kolumnen.
- **Bildfilens namn**, namnet på bildfilen, komplett med sökväg.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Positionering av bilder**

Det finns två möjliga sätt att styra placeringen av bilder med Aspose.Cells:

- Proportionell positionering: definiera en position proportionell mot radens höjd och bredd.
- Absolut positionering: definiera den exakta positionen på sidan där bilden ska infogas, till exempel 40 pixlar till vänster och 20 pixlar under kanten av cellen.

### **Proportionell positionering**

 Utvecklare kan placera bilderna proportionellt mot radhöjd och kolumnbredd med hjälp av[**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) och[**ÖvreDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) egenskaper hos[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) objekt. A[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) objekt kan erhållas från[**Bilder**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)samling genom att skicka dess bildindex. Detta exempel placerar en bild i F6-cellen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Absolut positionering**

 Utvecklare kan också placera bilderna absolut genom att använda[**Vänster**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) och[**Topp**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) egenskaper hos[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)objekt. Det här exemplet placerar en bild i cell F6, 60 pixlar från vänster och 10 pixlar från toppen av cellen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Infoga en bild baserat på Cell referens**

Aspose.Cells låter dig visa innehållet i en kalkylbladscell i en bildform. Du kan länka bilden till cellen som innehåller data som du vill visa. Eftersom cellen, eller cellområdet, är länkat till grafikobjektet, visas ändringar som du gör i data i den cellen eller cellområdet automatiskt i grafikobjektet.

 Lägg till en bild i arbetsbladet genom att ringa[**Lägg till bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) metod för[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) samling (inkapslad i[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objekt). Ange cellintervallet med hjälp av[**Formel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) attribut av[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Förhandsämnen**
- [Lägg till villkorliga ikoner med texten Cell](/cells/sv/net/add-conditional-icons-set-with-the-cell-text/)
- [Infoga en länkad bild från webbadress](/cells/sv/net/insert-a-linked-picture-from-web-address/)
- [Infoga en bild baserat på Cell referens](/cells/sv/net/insert-a-picture-based-on-cell-reference/)
- [Ladda en webbbild från en URL till ett Excel-kalkylblad](/cells/sv/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

