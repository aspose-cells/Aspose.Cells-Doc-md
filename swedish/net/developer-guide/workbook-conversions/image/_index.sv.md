---
title: Bild
type: docs
weight: 300
url: /sv/net/convert-excel-to-image/
---
{{% alert color="primary" %}}

Aspose.Cells låter dig exportera ett kalkylblad från arbetsboken och konvertera det till olika format. Den här artikeln förklarar hur du konverterar ett kalkylblad till olika format.

{{% /alert %}}

## Konvertera arbetsbok till TIFF

 En Excel-fil kan innehålla flera ark med flera sidor.[WorkbookRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) låter dig konvertera Excel till TIFF med flera sidor. Du kan också styra flera alternativ för TIFF, som[Kompression](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcompression), [Färgdjup](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/tiffcolordepth), Upplösning([Horisontell upplösning](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/horizontalresolution), [Vertikal upplösning](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/verticalresolution)).

 Följande kodavsnitt visar hur du konverterar Excel till TIFF med flera sidor. De[käll Excel-fil](workbook-to-tiff-with-mulitiple-pages.xlsx) och[genererad TIFF-bild](workbook-to-tiff-with-mulitiple-pages.tiff) bifogas för din referens.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Convert-Workbook-To-Tiff-With-Mulitiple-Pages.cs" >}}

## **Konvertera arbetsblad till bild**

Arbetsblad innehåller data som du vill analysera. Ett kalkylblad kan till exempel innehålla parametrar, summor, procentsatser, undantag och beräkningar.

Som utvecklare kan du behöva presentera kalkylblad som bilder. Till exempel kan du behöva använda en bild av ett kalkylblad i ett program eller en webbsida. Du kanske vill infoga en bild i ett Microsoft Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan dokumenttyp. Enkelt uttryckt vill du att ett kalkylblad ska renderas som en bild så att du kan använda det någon annanstans.

Aspose.Cells stöder konvertering av Excel-kalkylblad till bilder. För att använda den här funktionen måste du importera**[Aspose.Cells.Rendering](https://reference.aspose.com/cells/net/aspose.cells.rendering)** namnutrymme till ditt program eller projekt. Den har flera värdefulla klasser för till exempel rendering och utskrift**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)**, **[WorkbookRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)**, och andra.

 De**[SheetRender](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)** klass representerar ett kalkylblad att rendera som bilder. Den har en överbelastad metod,**[ToImage](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)**, som kan konvertera ett kalkylblad till bildfil(er) med olika attribut eller alternativ. Det returnerar ett System.Drawing.Bitmap-objekt och du kan spara en bildfil på disk eller stream. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Följande kodavsnitt visar hur man konverterar ett kalkylblad i en Excel-fil till en bildfil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{% alert color="primary" %}}

För närvarande stöder API för konvertering av kalkylblad till bilder inte 3D-bubbeldiagram.

{{% /alert %}}

## **Konvertera arbetsblad till SVG**

SVG står för Scalable Vector Graphics. SVG är en specifikation baserad på XML-standarder för tvådimensionell vektorgrafik. Det är en öppen standard som har varit under utveckling av World Wide Web Consortium (W3C) sedan 1999.

Aspose.Cells for .NET har kunnat konvertera kalkylblad till SVG-bild sedan version 7.1.0. Följande kodavsnitt visar hur man konverterar ett kalkylblad i en Excel-fil till en SVG-bildfil.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToSVG-1.cs" >}}

## **Förhandsämnen**
- [Konvertera ett Excel-diagram till bild](/cells/sv/net/convert-an-excel-chart-to-image/)
- [Konvertera diagram till bild i SVG-format](/cells/sv/net/converting-chart-to-image-in-svg-format/)
- [Exportera diagram till SVG med viewBox-attribut](/cells/sv/net/export-chart-to-svg-with-viewbox-attribute/)
- [Spåra konverteringsförlopp för Excel till TIFF](/cells/sv/net/track-conversion-progress-of-excel-to-tiff/)
