---
title: Rendera kalkylbladet och arbetsboken till bild med ImageOrPrintOptions
type: docs
weight: 220
url: /sv/java/render-the-worksheet-and-workbook-to-image-using-imageorprintoptions/
---

{{% alert color="primary" %}}

Detta dokument är utformat för att ge en detaljerad förståelse för hur man konverterar ett kalkylblad eller en arbetsbok till en bildfil och tillämpar olika bild- och utskriftsalternativ för bilden, alternativ som upplösning, TIFF-komprimering, bildformat och sidkvalitet.

{{% /alert %}}

## **Översikt**

Ibland kan det hända att du behöver presentera dina arbetsblad som en bildlig representation. Du kan behöva infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem på annat sätt. Du vill helt enkelt ha ett arbetsblad renderat som en bild så att du kan använda det någon annanstans. Aspose.Cells stödjer konvertering av arbetsblad i Excel-filer till bilder. Dessutom stödjer Aspose.Cells inställning av olika alternativ som bildformat, upplösning (både vertikal och horisontell), bildkvalitet och andra bild- och utskriftsalternativ.

API:et tillhandahåller flera värdefulla klasser, till exempel [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), etc.

[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)-klassen hanterar uppgiften att rendera bilder för kalkylbladet medan [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender)-klassen gör samma sak för en arbetsbok. Båda ovanstående klasser har flera överlagrade versioner av *tillBild*-metoden som direkt kan konvertera ett kalkylblad eller en arbetsbok till bildfil(er) med de alternativ eller egenskaper du önskar. Du kan spara bildfilen till disk/ström. Flera bildformat stöds, t.ex. BMP, PNG, GIFF, JPEG, TIFF, EMF och så vidare.

### **Konvertera kalkylblad till bild**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImage-1.java" >}}

## **Konverteringsalternativ**

Det är möjligt att spara specifika sidor som bild. Följande kod konverterar arbetsböckerets första och andra kalkylblad till JPG-bilder.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConversionOptions-1.java" >}}

Eller så kan du gå igenom arbetsboken och rendera varje kalkylblad till en separat bild:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-WorksheetToSeparateImage-1.java" >}}

## **Konvertera arbetsbok till bild:**

För att rendera hela arbetsboken till bildformat kan du antingen använda ovanstående metod eller helt enkelt använda klassen [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) som accepterar en instans av [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) samt objektet av [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions).

Du kan spara hela arbetsboken till en enda TIFF-bild med flera ramar eller sidor:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorkbooktoImage-1.java" >}}

## Relaterade artiklar

- [Konvertera Arbetsblad till olika bildformat](/cells/sv/java/converting-worksheet-to-different-image-formats/)
- [Exportera diagram till SVG med viewBox-attribut](/cells/sv/java/export-chart-to-svg-with-viewbox-attribute/)
- [Exportera Arbetsblad eller Diagram till Bild med önskad Bredd och Höjd](/cells/sv/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Konvertera kalkylblad till bild och kalkylblad till bild per sida](/cells/sv/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
