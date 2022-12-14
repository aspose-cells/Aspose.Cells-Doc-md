---
title: Konvertera arbetsblad till olika bildformat
type: docs
weight: 30
url: /sv/java/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}}

Aspose.Cells låter dig exportera ett kalkylblad från arbetsboken och konvertera det till olika format. Den här artikeln förklarar hur du konverterar ett kalkylblad till olika format.

{{% /alert %}}

## **Konvertera arbetsblad till bild**

Ibland är det användbart att spara en bild av ett kalkylblad. Bilder kan delas online, infogas i andra dokument (rapporter skrivna i Microsoft Word, till exempel, eller PowerPoint-presentationer).

Aspose.Cells tillhandahåller bildexport via**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)** klass. Den här klassen representerar kalkylbladet som kommer att renderas till en bild. De**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**klass ger**[toImage()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))**metod för att konvertera ett kalkylblad till en bildfil. BMP, PNG, JPEG, TIFF och EMF-format stöds.

{{% alert color="primary" %}}

Aspose.Cells för Java stöder även konvertering till TIFF-format. För att konvertera ett kalkylblad till en TIFF-bild, lägg till JAI-biblioteket i din klassväg.

{{% /alert %}} {{% alert color="primary" %}}

För närvarande stöder inte API:et för konvertering av kalkylblad till bild 3D-bubbeldiagram.

{{% /alert %}}

Koden nedan visar hur man konverterar ett kalkylblad i en Microsoft Excel-fil till en PNG-fil.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Konvertera arbetsblad till SVG**

 SVG står för**Skalbar vektorgrafik**. SVG är en specifikation baserad på XML-standarder för tvådimensionell vektorgrafik. Det är en öppen standard som har varit under utveckling av World Wide Web Consortium (W3C) sedan 1999.

Sedan versionen av v7.1.0,**Aspose.Cells för Java** kan konvertera kalkylblad till SVG-bilder.

För att använda den här funktionen måste du importera namnutrymmet com.aspose.cells till ditt program eller projekt. Den har flera värdefulla klasser för rendering och utskrift, till exempel,**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**, **[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)**, **[WorkbookRender](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender)**, och andra.

De**[com.aspose.cells.ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** class anger att kalkylbladet kommer att sparas i SVG-format.

De**[SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)**klass tar föremålet för**[ImageOrPrintOptions](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)** som en parameter som ställer in sparformatet till SVG-format.

Följande kodavsnitt visar hur man konverterar ett kalkylblad i en Excel-fil till en SVG-bildfil.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Gör aktivt kalkylblad i en arbetsbok**

Ett enkelt sätt att konvertera ett aktivt kalkylblad till en arbetsbok är att ställa in det aktiva arbetsbladets index och sedan spara arbetsboken som SVG. Det kommer att återge det aktiva arket till SVG. Följande exempelkod visar denna funktion:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## relaterade artiklar

- [Exportera diagram till SVG med viewBox-attribut](/cells/sv/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exportera kalkylblad eller diagram till bild med önskad bredd och höjd](/cells/sv/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Konvertera kalkylblad till bild och kalkylblad till bild för sida](/cells/sv/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
