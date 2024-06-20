---
title: Infoga en bild baserat på cellreferens
type: docs
weight: 150
url: /sv/net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Ibland har du en tom bild och behöver visa data eller innehåll i bilden genom att ange en cellreferens i formelfältet. Aspose.Cells stöder den här funktionen (Microsoft Excel 2010).

{{% /alert %}}

## Infoga en bild baserad på cellreferens

Aspose.Cells stöder att visa innehållet i en kalkylbladscell i en bildform. Du kan länka bilden till cellen som innehåller datan du vill visa. Eftersom cellen eller cellintervallet är länkad till den grafiska objektet visar ändringar som du gör i datan i den cellen eller cellintervallet automatiskt upp i det grafiska objektet. Lägg till en bild i kalkylbladet genom att använda [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) metoden i [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) objektet). Ange cellintervallet genom att använda [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) attributet i [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) objektet.

### Kodexempel

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
