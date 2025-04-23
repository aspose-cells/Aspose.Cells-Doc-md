---
title: Bild
type: docs
weight: 300
url: /sv/net/convert-excel-to-image/
---


{{% alert color="primary" %}}

Aspose.Cells låter dig exportera ett kalkylblad från arbetsboken och konvertera det till olika format. Den här artikeln förklarar hur man konverterar ett kalkylblad till olika format.

{{% /alert %}}

## Konvertering av arbetsbok till TIFF

En Excelfil kan innehålla flera ark med flera sidor. [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) tillåter dig att konvertera Excel till TIFF med flera sidor. Dessutom kan du styra flera alternativ för TIFF, som [Komprimering](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Färgdjup](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Upplösning ([Horisontell upplösning](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Vertikal upplösning](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

Följande kodsnutt visar hur man konverterar Excel till TIFF med flera sidor. Den [källa Excel-filen](workbook-to-tiff-with-mulitiple-pages.xlsx) och [genererade TIFF-bilden](workbook-to-tiff-with-mulitiple-pages.tiff) är bifogade för din referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Konvertera Kalkylblad till Bild**

Kalkylblad innehåller data som du vill analysera. Till exempel kan ett kalkylblad innehålla parametrar, totaler, procenttal, undantag och beräkningar.

Som utvecklare kan det hända att du behöver presentera kalkylblad som bilder. Till exempel kan det hända att du behöver använda en bild av ett kalkylblad i en applikation eller webbsida. Du kan vilja infoga en bild i ett Microsoft Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan dokumenttyp. Med andra ord vill du att ett kalkylblad ska renderas som en bild så att du kan använda det någon annanstans.

Aspose.Cells stöder konvertering av Excelkalkylblad till bilder. För att använda den här funktionen måste du importera [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)-namnrymden till ditt program eller projekt. Den har flera värdefulla klasser för rendering och utskrift, till exempel [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) och andra.

[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)-klassen representerar ett kalkylblad som ska renderas som bilder. Den har en överbelastad metod, [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index), som kan konvertera ett kalkylblad till bildfil(er) med olika attribut eller alternativ. Den returnerar en System.Drawing.Bitmap-objekt och du kan spara en bildfil till disk eller ström. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Följande kodsnutt visar hur man konverterar ett kalkylblad i en Excel-fil till en bildfil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

För närvarande stöder inte API:et för att konvertera kalkylblad till bilder 3D-bubble-diagram.

{{% /alert %}}

## **Konvertera Kalkylblad till SVG**

SVG står för Skalbara Vektorgrafik. SVG är en specifikation baserad på XML-standarder för tvådimensionell vektorgrafik. Det är en öppen standard som har varit under utveckling av World Wide Web Consortium (W3C) sedan 1999.

Aspose.Cells for .NET har kunnat konvertera kalkylblad till SVG-bild sedan version 7.1.0. Följande kodsnutt visar hur man konverterar ett kalkylblad i en Excelfil till en SVG-bildfil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Fortsatta ämnen**
- [Konvertera ett Excel-diagram till bild](/cells/sv/net/convert-an-excel-chart-to-image/)
- [Konvertera diagram till bild i SVG-format](/cells/sv/net/converting-chart-to-image-in-svg-format/)
- [Exportera diagram till SVG med viewBox-attribut](/cells/sv/net/export-chart-to-svg-with-viewbox-attribute/)
- [Spåra konverteringsframsteg för Excel till TIFF](/cells/sv/net/track-conversion-progress-of-excel-to-tiff/)
{{< app/cells/assistant language="csharp" >}}
