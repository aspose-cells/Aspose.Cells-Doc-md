---
title: Infoga en bild baserad på cellreferens
type: docs
weight: 90
url: /sv/java/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Ibland har du en tom bild och behöver visa data eller innehåll i bilden genom att ange en cellreferens i formelfältet. Aspose.Cells stöder den här funktionen (Microsoft Excel 2010).

{{% /alert %}}

## Infoga en bild baserad på cellreferens

Aspose.Cells stöder visning av innehållet i en kalkylblads cell i en bildform. Du kan länka bilden till cellen som innehåller data som du vill visa. Eftersom cellen eller cellintervallet är länkat till den grafiska objektet, visas ändringar av datat automatiskt i grafikobjektet. Lägg till en bild till kalkylbladet genom att använda [**addPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture-int-int-int-int-java.io.InputStream-)-metoden av [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)-samlingen (inkapslad i [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-objektet). Ange cellintervallet genom att använda [**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula)-metoden av [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)-objektet.

Nedan finns en skärmbild på filen som koden nedan genererar.

**Infogar en bild baserat på cellreferens**

![todo:image_alt_text](insert-a-picture-based-on-cell-reference_1.png)

## Exempelkod

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
{{< app/cells/assistant language="java" >}}
