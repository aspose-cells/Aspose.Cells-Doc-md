---
title: Generera villkorlig formatering DataBars-bilder
type: docs
weight: 170
url: /sv/java/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 Ibland måste du skapa bilder av datafält för villkorlig formatering. Du kan använda Aspose.Cells[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)) metod för att generera dessa bilder. Den här artikeln visar hur du genererar en DataBar-bild med Aspose.Cells.

{{% /alert %}}

## **Exempel**

 Följande exempelkod genererar DataBar-bilden av cell C1. Först kommer den åt cellens formatvillkorsobjekt, och sedan från det objektet kommer den åt DataBar-objektet och använder dess[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)) metod för att generera bilden av cellen. Slutligen sparar den bilden på disken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
