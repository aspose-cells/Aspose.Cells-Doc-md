---
title: Rendera arbetsbladet och arbetsboken till bild med ImageOrPrintOptions
type: docs
weight: 220
url: /sv/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---
{{% alert color="primary" %}}

Detta dokument är utformat för att ge en detaljerad förståelse för hur man konverterar ett kalkylblad eller en arbetsbok till en bildfil och använder olika bild- och utskriftsalternativ för bilden, alternativ som upplösning, TIFF-komprimering, bildformat och sidkvalitet.

{{% /alert %}}

## **Översikt**

Ibland kan du behöva presentera dina kalkylblad som en bildrepresentation. Du måste presentera kalkylbladsbilderna i dina applikationer eller webbsidor. Du kan behöva infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem i något annat scenario. Du vill helt enkelt att ett kalkylblad ska renderas som en bild så att du kan använda det någon annanstans. Aspose.Cells stöder konvertering av kalkylblad i Excel-filer till bilder. Dessutom stöder Aspose.Cells inställning av olika alternativ som bildformat, upplösning (både vertikalt och horisontellt), bildkvalitet och andra bild- och utskriftsalternativ.

API tillhandahåller flera värdefulla klasser, t.ex.[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), etc.

 De[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) klass hanterar uppgiften att rendera bilder för kalkylbladet medan[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)gör samma sak för en arbetsbok. Båda ovannämnda klasser har flera överbelastade versioner av*att föreställa sig*metod som direkt kan konvertera ett kalkylblad eller en arbetsbok till bildfil(er) specificerade med önskade attribut eller alternativ. Du kan spara bildfilen på disken/strömmen. Det finns flera bildformat som stöds, t.ex. BMP, PNG, GIFF, JPEG, TIFF, EMF och så vidare.

### **Konvertera arbetsblad till bild**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Konverteringsalternativ**

Det är möjligt att spara specifika sidor till bild. Följande kod konverterar de första och andra kalkylbladen i en arbetsbok till JPG-bilder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Eller så kan du bläddra igenom arbetsboken och rendera varje kalkylblad i den till en separat bild:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Konvertera arbetsbok till bild:**

 För att återge hela arbetsboken till bildformat kan du antingen använda ovanstående tillvägagångssätt eller helt enkelt använda[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) klass som accepterar en instans av[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) samt föremålet för[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

{{% alert color="primary" %}}

 De[**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) klass kan bara spara arbetsboken i formatet TIFF.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## relaterade artiklar

- [Konvertera arbetsblad till olika bildformat](/cells/sv/java/converting-worksheet-to-different-image-formats/)
- [Exportera diagram till SVG med viewBox-attribut](/cells/sv/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exportera kalkylblad eller diagram till bild med önskad bredd och höjd](/cells/sv/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Konvertera kalkylblad till bild och kalkylblad till bild för sida](/cells/sv/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
