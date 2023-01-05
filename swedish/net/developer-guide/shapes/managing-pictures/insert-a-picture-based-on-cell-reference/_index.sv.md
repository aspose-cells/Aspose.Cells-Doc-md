---
title: Infoga en bild baserat på Cell referens
type: docs
weight: 150
url: /sv/net/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

Ibland har du en tom bild och behöver visa data eller innehåll i bilden genom att ställa in en cellreferens i formelfältet. Aspose.Cells stöder den här funktionen (Microsoft Excel 2010).

{{% /alert %}}

## Infoga en bild baserat på Cell referens

Aspose.Cells stöder visning av innehållet i en kalkylbladscell i en bildform. Du kan länka bilden till cellen som innehåller data som du vill visa. Eftersom cellen eller cellområdet är länkat till grafikobjektet, visas ändringar som du gör i data i den cellen eller cellområdet automatiskt i grafikobjektet. Lägg till en bild i arbetsbladet genom att ringa[**Lägg till bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) metod för[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) samling (inkapslad i[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objekt). Ange cellintervallet med hjälp av[**Formel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) attribut av[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)objekt.

### Kodexempel

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
