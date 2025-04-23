---
title: Konvertera kalkylblad till bild och Kalkylblad till bild per sida
type: docs
weight: 210
url: /sv/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Detta dokument är utformat för att ge utvecklarna en detaljerad förståelse för hur man konverterar ett kalkylblad till en bildfil och ett kalkylblad med flera sidor till en bildfil per sida.

Ibland kan du behöva presentera kalkylblad som bilder, till exempel för att använda dem i program eller webbsidor. Du kan behöva infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem i något annat scenario. Helt enkelt vill du rendera kalkylbladet som en bild. Aspose.Cells API: er stödjer att konvertera kalkylblad i Microsoft Excel-filer till bilder. Dessutom stöder Aspose.Cells att konvertera en arbetsbok till flera bildfiler, en per sida.

{{% /alert %}}

## **Använda Aspose.Cells för att konvertera kalkylblad till bildfil**

Denna artikel visar hur man använder Aspose.Cells for Java API för att konvertera ett kalkylblad till bild. API:en tillhandahåller flera värdefulla klasser, såsom [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender), och så vidare. Klassen [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) representerar ett kalkylblad för att rendera bilder för kalkylbladet och har en överlagrad [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage-int-java.io.OutputStream-)-metod som kan konvertera ett kalkylblad till bildfiler direkt med vilka attribut eller alternativ som helst.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Resultat**

Efter att ovanstående kod har utförts, konverteras kalkylbladet med namnet Sheet1 till en bildfil SheetImage.jpg.

**Den genererade JPG-bilden**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Använda Aspose.Cells för att konvertera arbetsblad till bildfil per sida**

Detta exempel visar hur man använder Aspose.Cells för att konvertera ett arbetsblad från en mallarbok som har flera sidor till en bildfil per sida.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Resultat**

Efter att ovanstående kod har utförts, konverteras kalkylbladet med namnet Sheet1 till två bildfiler (1 per sida) Sheet 1 Page 1.Tiff och Sheet 1 Page 2.Tiff.

**Genererad bildfil (Ark 1 Sida 1.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**Genererad bildfil (Sheet 1 Page 2.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Denna artikel visar hur man konverterar ett kalkylblad till en bildfil och konverterar kalkylblad med flera sidor till flera bildfiler (en per sida) med hjälp av Aspose.Cells. Aspose.Cells erbjuder mer flexibilitet än andra komponenter och ger enastående hastighet, effektivitet och tillförlitlighet.

{{% /alert %}}

## Relaterade artiklar

- [Konvertera Arbetsblad till olika bildformat](/cells/sv/java/converting-worksheet-to-different-image-formats/)
- [Exportera Arbetsblad eller Diagram till Bild med önskad Bredd och Höjd](/cells/sv/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
{{< app/cells/assistant language="java" >}}
