---
title: Konvertera kalkylblad till bild och kalkylblad till bild för sida
type: docs
weight: 210
url: /sv/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Detta dokument är utformat för att ge utvecklarna en detaljerad förståelse för hur man konverterar ett kalkylblad till en bildfil & kalkylblad med flera sidor till en bildfil per sida.

Ibland kan du behöva presentera kalkylblad som bilder, till exempel för att använda dem i applikationer eller webbsidor. Du kan behöva infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem i något annat scenario. Du vill helt enkelt rendera kalkylbladet som en bild. Aspose.Cells API:er stöder konvertering av kalkylblad i Microsoft Excel-filer till bilder. Dessutom stöder Aspose.Cells konvertering av en arbetsbok till flera bildfiler, en per sida.

{{% /alert %}}

## **Använda Aspose.Cells för att konvertera kalkylblad till bildfil**

Den här artikeln visar hur du använder Aspose.Cells för Java API för att konvertera ett kalkylblad till en bild. API:et tillhandahåller flera värdefulla klasser, som t.ex[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) , och så vidare. De[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) klass representerar ett kalkylblad för att rendera bilder för kalkylbladet och har en överbelastad[**att föreställa sig**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream)) metod som kan konvertera ett kalkylblad till bildfiler direkt med valfria attribut eller alternativ.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Resultat**

Efter exekvering av ovanstående kod konverteras kalkylbladet med namnet Sheet1 till en bildfil SheetImage.jpg.

**Utdata JPG**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Använda Aspose.Cells för att konvertera kalkylblad till bildfil per sida**

Det här exemplet visar hur du använder Aspose.Cells för att konvertera ett kalkylblad från en mallarbetsbok som har flera sidor till en bildfil per sida.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Resultat**

Efter exekvering av ovanstående kod konverteras kalkylbladet med namnet Sheet1 till två bildfiler (1 per sida) Sheet 1 Page 1.Tiff och Sheet 1 Page 2.Tiff.

**Genererad bildfil (ark 1 sida 1.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**Genererad bildfil (ark 1 sida 2.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Den här artikeln visar hur du konverterar ett kalkylblad till en bildfil och konverterar kalkylblad med flera sidor till flera bildfiler (en per sida) med Aspose.Cells. Aspose.Cells erbjuder mer flexibilitet än andra komponenter och ger enastående hastighet, effektivitet och tillförlitlighet. Resultaten visar att Aspose.Cells har dragit nytta av år av forskning, design och noggrann justering.

{{% /alert %}}

## relaterade artiklar

- [Konvertera arbetsblad till olika bildformat](/cells/sv/java/converting-worksheet-to-different-image-formats/)
- [Exportera kalkylblad eller diagram till bild med önskad bredd och höjd](/cells/sv/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
