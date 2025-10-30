---
title: Konvertera Kalkylblad till Olika Bildformat
type: docs
weight: 90
url: /sv/go-cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells tillåter dig att exportera ett kalkylblad från en arbetsbok och konvertera det till olika bildformat. Den här artikeln förklarar hur man konverterar ett kalkylblad till olika bildformat.

{{% /alert %}}

## **Konvertera Kalkylblad till Bild**

Kalkylblad innehåller data som du vill analysera. Till exempel kan ett kalkylblad innehålla parametrar, totaler, procenttal, undantag och beräkningar.

 Som utvecklare kan du behöva visa kalkylblad som bilder. Till exempel, du kanske vill använda en bild av ett kalkylblad i en applikation eller webbsida. Du kan vilja infoga en bild i ett Microsoft Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan dokumentsort. Kort sagt, du vill att ett kalkylblad ska renderas som en bild så att du kan använda det någon annanstans.

Aspose.Cells stöder konvertering av Excel-kalkylblad till bilder. För att använda denna funktion måste du importera [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) namespace till ditt program eller projekt. Den har flera värdefulla klasser för rendering och utskrift, till exempel [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), och andra.

 `Aspose.Cells.Rendering.ISheetRender`-klassen representerar ett kalkylblad för att renderas som bilder. Den har en överskriden metod, [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), som kan konvertera ett kalkylblad till bildfil(er) med olika attribut eller alternativ. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, TIFF och EMF.

Följande kodsnutt visar hur man konverterar ett kalkylblad i en Excel-fil till en bildfil.

### **konvertera Excel/arbetsblad till PNG med GoLang**

Se följande exempelkod, dess [exempel Excel-fil](67338402.xlsx) and [utmatnings PNG-bilder](67338401.zip) för din referens.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Png.go" >}}

### **konvertera Excel/arbetsblad till TIFF med GoLang**

Se följande exempelkod, dess [exempel Excel-fil](67338402.xlsx) och [utmatnings TIFF-bild](67338419.zip) för din referens.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Tiff.go" >}}

## **konvertera Excel/arbetsblad till SVG med GoLang**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Svg.go" >}}

SVG står för Skalbara Vektorgrafik. SVG är en specifikation baserad på XML-standarder för tvådimensionell vektorgrafik. Det är en öppen standard som har varit under utveckling av World Wide Web Consortium (W3C) sedan 1999.

Aspose.Cells for Go via C++ har kunnat konvertera kalkylblad till SVG-bilder sedan version 24.12.0.

För att använda den här funktionen, importera `Aspose.Cells.Rendering` namespace till ditt program eller projekt. Det har flera värdefulla klasser för rendering och utskrifter, till exempel `ISheetRender`, `IImageOrPrintOptions` och andra.

Klassen `Aspose.Cells.Rendering.IImageOrPrintOptions` specificerar att kalkylbladet kommer att sparas i SVG-format. Följande kodsnutt visar hur man konverterar ett kalkylblad i en Excel-fil till en SVG-bildfil

Se följande exempelkod, dess [exempel Excel-fil](67338402.xlsx) and [utmatnings SVG-bilder](67338403.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_SVG.go" >}}
