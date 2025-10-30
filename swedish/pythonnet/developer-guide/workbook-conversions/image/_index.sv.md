---
title: Bild
type: docs
weight: 300
url: /sv/python-net/convert-excel-to-image/
description: Konvertera diagram till bild genom att använda Aspose.Cells för Python via .NET API.
keywords: Python konverterar diagram till bild, Exportera diagram till bild i Python via NET, Python Spara diagram till bild.
---


{{% alert color="primary" %}}

Aspose.Cells för Python via .NET tillåter dig att exportera ett kalkylblad från arbetsboken och konvertera det till olika format. Den här artikeln förklarar hur man konverterar ett kalkylblad till olika format.

{{% /alert %}}

## Konvertering av arbetsbok till TIFF

En Excel-fil kan innehålla flera ark med flera sidor. [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) tillåter dig att konvertera Excel till TIFF med flera sidor. Dessutom kan du kontrollera flera alternativ för TIFF, som [Komprimering](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/tiff_compression/), Färgdjup([Horisontell upplösning](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/horizontal_resolution/), [Vertikal upplösning](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/vertical_resolution/)).

Följande kodsnutt visar hur man konverterar Excel till TIFF med flera sidor. Den [källa Excel-filen](workbook-to-tiff-with-mulitiple-pages.xlsx) och [genererade TIFF-bilden](workbook-to-tiff-with-mulitiple-pages.tiff) är bifogade för din referens.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.py" >}}

## **Konvertera Kalkylblad till Bild**

Kalkylblad innehåller data som du vill analysera. Till exempel kan ett kalkylblad innehålla parametrar, totaler, procenttal, undantag och beräkningar.

Som utvecklare kan det hända att du behöver presentera kalkylblad som bilder. Till exempel kan det hända att du behöver använda en bild av ett kalkylblad i en applikation eller webbsida. Du kan vilja infoga en bild i ett Microsoft Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan dokumenttyp. Med andra ord vill du att ett kalkylblad ska renderas som en bild så att du kan använda det någon annanstans.

Aspose.Cells för Python via .NET stöder konvertering av Excel-kalkylblad till bilder. För att använda den här funktionen måste du importera [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/) namespace till ditt program eller projekt. Det har flera värdefulla klasser för rendering och utskrift, till exempel [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender/), och andra.

[**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/)-klassen representerar ett kalkylblad som ska renderas som bilder. Den har en överbelastad metod, [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str), som kan konvertera ett kalkylblad till bildfil(er) med olika attribut eller alternativ. Den returnerar en System.Drawing.Bitmap-objekt och du kan spara en bildfil till disk eller ström. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Följande kodsnutt visar hur man konverterar ett kalkylblad i en Excel-fil till en bildfil.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToImageByPage-1.py" >}}

{{% alert color="primary" %}}

För närvarande stöder inte API:et för att konvertera kalkylblad till bilder 3D-bubble-diagram.

{{% /alert %}}

## **Konvertera Kalkylblad till SVG**

SVG står för Skalbara Vektorgrafik. SVG är en specifikation baserad på XML-standarder för tvådimensionell vektorgrafik. Det är en öppen standard som har varit under utveckling av World Wide Web Consortium (W3C) sedan 1999.

Aspose.Cells for Python via .NET har kunnat konvertera kalkylblad till SVG-bild sedan version 7.1.0. Följande kodsnutt visar hur man konverterar ett kalkylblad i en Excelfil till en SVG-bildfil.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheet-ConvertWorksheetToSVG-1.py" >}}

## **Fortsatta ämnen**
- [Konvertera ett Excel-diagram till bild](/cells/sv/python-net/convert-an-excel-chart-to-image/)
- [Konvertera diagram till bild i SVG-format](/cells/sv/python-net/converting-chart-to-image-in-svg-format/)
- [Exportera diagram till SVG med viewBox-attribut](/cells/sv/python-net/export-chart-to-svg-with-viewbox-attribute/)
{{< app/cells/assistant language="python-net" >}}
