---
title: Ta bort vita mellanslag från data innan du renderar till bild
type: docs
weight: 270
url: /sv/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---
{{% alert color="primary" %}}

Ibland måste du presentera kalkylbladsbilder i applikationer eller webbsidor. Till exempel kan du behöva infoga en bild i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller något annat dokument. I grund och botten vill du rendera ett kalkylblad som en bild så att det kan klistras in i andra applikationer. Aspose.Cells API:er låter dig konvertera Microsoft Excel-kalkylblad till bilder.

{{% /alert %}}

 De[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)klass kan konvertera ett kalkylblad till en bildfil med vilka attribut som helst, till exempel bildformat, sidnumrerade ark, etc. Flera bildformat stöds, inklusive BMP, GIF, JPG, TIFF och EMF.

När du använder ark-till-bild-funktionen har den utgående bilden vitt/tomt utrymme, det vill säga en ram, runt den som standard. Du kan ta bort detta. Ställ in de övre, vänstra, nedre och högra sidinställningarna för källarbetsbladet till 0 och ange[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)attribut i enlighet därmed.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
