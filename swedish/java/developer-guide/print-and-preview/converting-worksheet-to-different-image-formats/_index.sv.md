---
title: Konvertera Kalkylblad till Olika Bildformat
type: docs
weight: 30
url: /sv/java/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells låter dig exportera ett kalkylblad från arbetsboken och konvertera det till olika format. Den här artikeln förklarar hur man konverterar ett kalkylblad till olika format.

{{% /alert %}}

## **Konvertera Kalkylblad till Bild**

Ibland är det användbart att spara en bild av ett kalkylblad. Bilder kan delas online, infogas i andra dokument (rapporter skrivna i Microsoft Word till exempel eller PowerPoint-presentationer).

Aspose.Cells tillhandahåller bildexport genom [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)-klassen. Denna klass representerar kalkylbladet som kommer att renderas till en bild. [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender)-klassen tillhandahåller [**toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage-int-java.io.OutputStream-)-metoden för att konvertera ett kalkylblad till en bildfil. BMP, PNG, JPEG, TIFF och EMF-format stöds.

{{% alert color="primary" %}}

Aspose.Cells for Java stöder också konvertering till TIFF-format. För att konvertera ett kalkylblad till en TIFF-bild, lägg till JAI-biblioteket till din klasssökväg.

{{% /alert %}} {{% alert color="primary" %}}

För närvarande stöder inte API:et för att konvertera kalkylblad till bild 3D-bubbel diagram.

{{% /alert %}}

Koden nedan visar hur du konverterar ett kalkylblad i en Excel-fil till en PNG-fil.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-WorksheetToImage-1.java" >}}

## **Konvertera Kalkylblad till SVG**

SVG står för **Skalbara Vektorgrafiker**. SVG är en specifikation baserad på XML-standarder för tvådimensionell vektorgrafik. Det är en öppen standard som har varit under utveckling av World Wide Web Consortium (W3C) sedan 1999.

Sedan utgåvan av v7.1.0, kan **Aspose.Cells for Java** konvertera kalkylblad till SVG-bilder.

För att använda den här funktionen måste du importera com.aspose.cells-namnrymden till ditt program eller projekt. Den har flera värdefulla klasser för rendering och utskrift, till exempel [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender), och andra.

[**com.aspose.cells.ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)-klassen specificerar att kalkylbladet kommer att sparas i SVG-format.

Klassen [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) tar objektet för [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) som en parameter som ställer in sparformatet till SVG-format.

Följande kodsnutt visar hur man konverterar en kalkylblad i en Excel-fil till en SVG-bildfil.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingWorksheetToSVG-ConvertingWorksheetToSVG.java" >}}

### **Rendera aktivt kalkylblad i en arbetsbok**

Ett enkelt sätt att konvertera aktivt kalkylblad i en arbetsbok är att ställa in det aktiva bladindexet och sedan spara arbetsboken som SVG. Det kommer att rendera det aktiva bladet till SVG. Följande exempelkod demonstrerar denna funktion:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertActiveWorksheetToSVG-1.java" >}}

## Relaterade artiklar

- [Exportera diagram till SVG med viewBox-attribut](/cells/sv/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exportera Arbetsblad eller Diagram till Bild med önskad Bredd och Höjd](/cells/sv/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Konvertera kalkylblad till bild och kalkylblad till bild per sida](/cells/sv/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
{{< app/cells/assistant language="java" >}}
