---
title: Konvertera kalkylblad till bild  Ta bort mellanrum runt data
type: docs
weight: 40
url: /sv/python-net/convert-worksheet-to-image-remove-whitespace-around-data/
---

{{% alert color="primary" %}}

Ibland behöver du visa arbetsbladbilder i appar eller webbsidor. Till exempel kan du behöva infoga bilder i ett Word-dokument, PDF-fil, PowerPoint-presentation eller annat dokument. Grundläggande vill du rendera ett arbetsblad som en bild för att klistra in den i andra program. Aspose.Cells för Python via .NET tillåter dig att konvertera Microsoft Excel-arbetsblad till bilder.

{{% /alert %}}

## **Ta bort mellanrum runt data**

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender)-API:en konverterar ett kalkylblad till en bildfil med vilka attribut som helst, till exempel bildformat, sidade kalkylblad, osv. Flera bildformat stöds, inklusive BMP, GIF, JPG, TIFF och EMF.

När du använder funktionen ark-till-bild har den resulterande bilden ett mellanrum, det vill säga en ram, runt den som standard. Du kan ta bort detta genom att ställa in de översta, understa, vänstra och högra sidmarginalerna för källkalkylbladet till 0 och ange [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)-attribut därefter.

Följande kodsippa tar bort mellanrummet runt datan i den resulterande bilden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-RemoveWhitespaceAroundData-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
