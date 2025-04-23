---
title: Infoga en bild baserat på cellreferens
type: docs
weight: 150
url: /sv/python-net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Ibland har du en tom bild och behöver visa data eller innehåll i bilden genom att ställa in en cellreferens i formelfältet. Aspose.Cells för Python via .NET stöder denna funktion (Microsoft Excel 2010).

{{% /alert %}}

## Infoga en bild baserad på cellreferens

Aspose.Cells för Python via .NET stöder att visa innehållet i en arbetsbladscell i en bildfigur. Du kan länka bilden till cellen som innehåller den data du vill visa. Eftersom cellen eller cellområdet är kopplat till den grafiska objektet, visas automatiskt ändringar i datan i den cellen eller cellområdet i den grafiska figur. Lägg till en bild i arbetsbladet genom att anropa [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture)-metoden av [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-objektet). Ange cellområdet med hjälp av [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula)-attributet hos [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-objektet.

### Kodexempel

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertPictureCellReference-1.py" >}}
