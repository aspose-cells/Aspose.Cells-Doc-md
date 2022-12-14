---
title: Konvertera kalkylblad till bild - Ta bort blanksteg runt data
type: docs
weight: 40
url: /sv/net/convert-worksheet-to-image-remove-whitespace-around-data/
---
{{% alert color="primary" %}}

Ibland måste du presentera kalkylbladsbilder i applikationer eller webbsidor. Till exempel kan du behöva infoga bilder i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller något annat dokument. I grund och botten vill du rendera ett kalkylblad som en bild så att det kan klistras in i andra applikationer. Aspose.Cells låter dig konvertera Microsoft Excel-kalkylblad till bilder.

{{% /alert %}}

## **Ta bort blanksteg runt Data**

 De[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)API konverterar ett kalkylblad till en bildfil med alla specificerade attribut, till exempel bildformat, sidnumrerade ark, etc. Flera bildformat stöds, inklusive BMP, GIF, JPG, TIFF och EMF.

 När du använder ark-till-bild-funktionen har den utgående bilden blanksteg, det vill säga en ram, runt sig som standard. Du kan ta bort detta genom att ställa in de övre, nedre, vänstra och högra sidinställningarna för källarbetsbladet till 0 och ange[**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)attribut i enlighet därmed.

Följande kodavsnitt tar bort blanktecken runt data i utdatabilden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

