---
title: Konvertera arbetsblad till olika bildformat
type: docs
weight: 90
url: /sv/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells låter dig exportera ett kalkylblad från en arbetsbok och konvertera det till olika bildformat. Den här artikeln förklarar hur du konverterar ett kalkylblad till olika bildformat.

{{% /alert %}} 
##  **Konvertera arbetsblad till bild**
Arbetsblad innehåller data som du vill analysera. Ett kalkylblad kan till exempel innehålla parametrar, summor, procentsatser, undantag och beräkningar.

Som utvecklare kan du behöva presentera kalkylblad som bilder. Till exempel kan du behöva använda en bild av ett kalkylblad i ett program eller en webbsida. Du kanske vill infoga en bild i ett Microsoft Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan dokumenttyp. Enkelt uttryckt vill du att ett kalkylblad ska renderas som en bild så att du kan använda det någon annanstans.

Aspose.Cells stöder konvertering av Excel-kalkylblad till bilder. För att använda den här funktionen måste du importera[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)namnutrymme till ditt program eller projekt. Den har flera värdefulla klasser för rendering och utskrift, till exempel,[SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)och andra.

Klassen `Aspose.Cells.Rendering.ISheetRender` representerar ett kalkylblad att rendera som bilder. Den har en överbelastad metod,[Att föreställa sig](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), som kan konvertera ett kalkylblad till bildfil(er) med olika attribut eller alternativ. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, EMF.

Följande kodavsnitt visar hur man konverterar ett kalkylblad i en Excel-fil till en bildfil.
###  **PNG Format**
 Se följande exempelkod, dess[exempel på Excel-fil](67338402.xlsx) , och den[utgång PNG Bilder](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}
<!--
### **TIFF Format**
Please see the following sample code, its [sample Excel file](67338402.xlsx), and the [output TIFF Image](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}
-->
##  **Konvertera arbetsblad till SVG**
SVG står för Scalable Vector Graphics. SVG är en specifikation baserad på XML-standarder för tvådimensionell vektorgrafik. Det är en öppen standard som har varit under utveckling av World Wide Web Consortium (W3C) sedan 1999.

Aspose.Cells for C++ har kunnat konvertera kalkylblad till SVG bild sedan version 18.5.0.

För att använda den här funktionen, importera namnområdet `Aspose.Cells.Rendering` till ditt program eller projekt. Den har flera värdefulla klasser för rendering och utskrift, till exempel `ISheetRender`, `IImageOrPrintOptions` och andra.

Klassen `Aspose.Cells.Rendering.IImageOrPrintOptions` anger att kalkylbladet kommer att sparas i formatet SVG. Följande kodsnutt visar hur man konverterar ett kalkylblad i en Excel-fil till en SVG-bildfil

 Se följande exempelkod, dess[exempel på Excel-fil](67338402.xlsx) , och den[utgång SVG Bilder](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
