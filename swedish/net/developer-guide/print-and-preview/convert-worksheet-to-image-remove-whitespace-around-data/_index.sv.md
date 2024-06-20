---
title: Konvertera kalkylblad till bild  Ta bort mellanrum runt data
type: docs
weight: 40
url: /sv/net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

Ibland måste du presentera kalkylbladsbilder i applikationer eller webbsidor. Till exempel kan du behöva infoga bilder i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller något annat dokument. I huvudsak vill du rendera ett kalkylblad som en bild så att det kan klistras in i andra applikationer. Aspose.Cells gör det möjligt att konvertera Microsoft Excel-kalkylblad till bilder.

{{% /alert %}}

## **Ta bort mellanrum runt data**

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)-API:en konverterar ett kalkylblad till en bildfil med vilka attribut som helst, till exempel bildformat, sidade kalkylblad, osv. Flera bildformat stöds, inklusive BMP, GIF, JPG, TIFF och EMF.

När du använder funktionen ark-till-bild har den resulterande bilden ett mellanrum, det vill säga en ram, runt den som standard. Du kan ta bort detta genom att ställa in de översta, understa, vänstra och högra sidmarginalerna för källkalkylbladet till 0 och ange [**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)-attribut därefter.

Följande kodsippa tar bort mellanrummet runt datan i den resulterande bilden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

