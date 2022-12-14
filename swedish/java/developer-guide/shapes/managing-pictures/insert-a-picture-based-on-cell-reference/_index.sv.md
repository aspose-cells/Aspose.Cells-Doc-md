---
title: Infoga en bild baserat på Cell Referens
type: docs
weight: 90
url: /sv/java/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

Ibland har du en tom bild och behöver visa data eller innehåll i bilden genom att ställa in en cellreferens i formelfältet. Aspose.Cells stöder den här funktionen (Microsoft Excel 2010).

{{% /alert %}}

## Infoga en bild baserat på Cell referens

Aspose.Cells stöder visning av innehållet i en kalkylbladscell i en bildform. Du kan länka bilden till cellen som innehåller data som du vill visa. Eftersom cellen eller cellområdet är länkat till det grafiska objektet, visas ändringar av data automatiskt i det grafiska objektet. Lägg till en bild i arbetsbladet genom att ringa[**addPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream) ) metod för[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) samling (inkapslad i[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) objekt). Ange cellintervallet med hjälp av[**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) metod för[**Bild**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)objekt.

Nedan är en skärmdump av filen som koden nedan genererar.

**Infoga en bild baserad på cellreferens**

![todo:image_alt_text](insert-a-picture-based-on-cell-reference_1.png)

## Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
