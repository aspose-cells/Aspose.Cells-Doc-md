---
title: Ta bort blanka utrymmen från data innan du renderar till bild
type: docs
weight: 270
url: /sv/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---

{{% alert color="primary" %}}

Ibland behöver du presentera kalkylbladsbilder i applikationer eller webbsidor. Till exempel kan du behöva infoga en bild i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller något annat dokument. I grund och botten vill du rendera ett kalkylblad som en bild så att det kan klistras in i andra applikationer. Aspose.Cells API:erna gör det möjligt att konvertera Microsoft Excel-kalkylblad till bilder.

{{% /alert %}}

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)-klassen kan konvertera ett kalkylblad till en bildfil med valfria egenskaper, till exempel bildformat, paginerade kalkylblad osv. Flera bildformat stöds, inklusive BMP, GIF, JPG, TIFF och EMF.

När du använder funktionen för att skapa bilder har utdata-bilden en vit/blank yta, det vill säga en ram, runt den som standard. Du kan ta bort detta. Ange över-, vänster-, under- och högermarginalerna för källdatakalkylbladet till 0 och specificera [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)-egenskaper därefter.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
{{< app/cells/assistant language="java" >}}
