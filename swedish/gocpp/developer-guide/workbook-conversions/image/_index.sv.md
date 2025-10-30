---
title: Konvertera Excel till bild med Golang via C++
linktitle: Konvertera Excel till bild
type: docs
weight: 300
url: /sv/go-cpp/convert-excel-to-image/
description: Lär dig hur man konverterar Excel ark till bilder, inklusive TIFF och SVG format, med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells låter dig exportera ett kalkylblad från arbetsboken och konvertera det till olika format. Den här artikeln förklarar hur man konverterar ett kalkylblad till olika format.

{{% /alert %}}

## Konvertering av arbetsbok till TIFF

En Excel-fil kan innehålla flera blad med flera sidor. [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/) låter dig konvertera Excel till TIFF med flera sidor. Du kan också styra flera alternativ för TIFF, som [komprimering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), upplösning ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

Följande kodsnutt visar hur man konverterar Excel till TIFF med flera sidor. Den [källa Excel-filen](workbook-to-tiff-with-mulitiple-pages.xlsx) och [genererade TIFF-bilden](workbook-to-tiff-with-mulitiple-pages.tiff) är bifogade för din referens.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image.go" >}}
## **Konvertera Kalkylblad till Bild**

Kalkylblad innehåller data som du vill analysera. Till exempel kan ett kalkylblad innehålla parametrar, totaler, procenttal, undantag och beräkningar.

Som utvecklare kan det hända att du behöver presentera kalkylblad som bilder. Till exempel kan det hända att du behöver använda en bild av ett kalkylblad i en applikation eller webbsida. Du kan vilja infoga en bild i ett Microsoft Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan dokumenttyp. Med andra ord vill du att ett kalkylblad ska renderas som en bild så att du kan använda det någon annanstans.

Aspose.Cells stödjer konvertering av Excel-ark till bilder. För att använda denna funktion behöver du importera [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/go-cpp/)-namnutrymmet till ditt program eller projekt. Det har flera värdefulla klasser för rendering och utskrift, till exempel [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/) och andra.

Klassen [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/) representerar ett arbetsblad för rendering som bilder. Den har en överlagrad metod, [**ToImage**](https://reference.aspose.com/cells/go-cpp/sheetrender/toimage/), som kan konvertera ett arbetsblad till bildfiler med olika attribut eller alternativ. Den returnerar ett objekt av typen `System.Drawing.Bitmap` och du kan spara en bildfil till disk eller ström. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Följande kodsnutt visar hur man konverterar ett kalkylblad i en Excel-fil till en bildfil.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-1.go" >}}
{{% alert color="primary" %}}

För närvarande stöder inte API:et för att konvertera kalkylblad till bilder 3D-bubble-diagram.

{{% /alert %}}

## **Konvertera Kalkylblad till SVG**

SVG står för Skalbara Vektorgrafik. SVG är en specifikation baserad på XML-standarder för tvådimensionell vektorgrafik. Det är en öppen standard som har varit under utveckling av World Wide Web Consortium (W3C) sedan 1999.

Aspose.Cells for C++ har kunnat konvertera arbetsblad till SVG-bild sedan version 7.1.0. Följande kodsnutt visar hur man konverterar ett arbetsblad i en Excel-fil till en SVG-bildfil.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-2.go" >}}
## **Fortsatta ämnen**
- [Konvertera ett Excel-diagram till bild](/cells/sv/cpp/convert-an-excel-chart-to-image/)
- [Konvertera diagram till bild i SVG-format](/cells/sv/cpp/converting-chart-to-image-in-svg-format/)
- [Exportera diagram till SVG med viewBox-attribut](/cells/sv/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Spåra konverteringsframsteg för Excel till TIFF](/cells/sv/cpp/track-conversion-progress-of-excel-to-tiff/)
