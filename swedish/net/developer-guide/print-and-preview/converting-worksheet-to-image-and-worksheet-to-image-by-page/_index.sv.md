---
title: Konvertera kalkylblad till bild och Kalkylblad till bild per sida
type: docs
weight: 80
url: /sv/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Detta dokument är utformat för att ge utvecklarna en detaljerad förståelse för hur man konverterar ett kalkylblad till en bildfil och ett kalkylblad med flera sidor till en bildfil per sida.

Ibland kan du behöva presentera kalkylblad som bilder, till exempel för att använda dem i applikationer eller webbsidor. Du kanske behöver infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem i något annat scenario. Kort sagt, du vill rendera kalkylbladet som en bild. Aspose.Cells stöder konvertering av kalkylblad i Microsoft Excel-filer till bilder. Dessutom stöder Aspose.Cells konvertering av en arbetsbok till flera bildfiler, en per sida.

Du kan använda Office Automation för att uppnå detta, men Office Automation har sina egna nackdelar. Det finns flera skäl och problem involverade: till exempel säkerhet, stabilitet, skalbarhet/hastighet, pris och funktioner. Kort sagt, det finns många skäl, men det främsta är att Microsoft själva starkt rekommenderar att inte använda Office Automation.

{{% /alert %}}

## **Använda Aspose.Cells för att konvertera kalkylblad till bildfil**

Den här artikeln visar hur man skapar en konsolapplikation i Visual Studio, konverterar ett kalkylblad till en bild och konverterar ett kalkylblad till en bild för varje kalkylblad med några få och enkla rader kod med hjälp av Aspose.Cells API.

Du behöver importera [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)-namnrymden till ditt program/projekt. Den har flera värdefulla klasser, såsom [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), och så vidare. Klassen [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) representerar ett kalkylblad för att rendera bilder för kalkylbladet och har en överlagrad [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)-metod som kan konvertera ett kalkylblad till bildfiler direkt med alla ställa in attribut eller alternativ. Den kan returnera ett System.Drawing.Bitmap-objekt och du kan spara en bildfil på disk/ström. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, och andra.

Den här artikeln förklarar hur man:

- Konvertera ett kalkylblad till en bild
- Konvertera varje sida i ett kalkylblad till en bild

Det här exemplet visar hur man använder Aspose.Cells för att konvertera ett kalkylblad från en mallarbok till en bildfil.

### **Installationsprojekt**

1. Först, [ladda ned Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Installera den på din utvecklingsdator. Alla [Aspose](http://www.aspose.com/)-komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det lägger bara vattenstämplar på de producerade dokumenten. Starta nu Visual Studio.Net och skapa en ny konsolapplikation. Detta exempel använder en C#-konsolapplikation, men du kan också använda VB.NET. Lägg till referens till Aspose.Cells i det skapade projektet.

### **Konvertera kalkylblad till bildfil**

Jag skapade en ny arbetsbok i Microsoft Excel och lade till lite data i det första kalkylbladet: **Testbook.xlsx** (1 kalkylblad). Nästa steg är att konvertera mallfilens kalkylblad Sheet1 till en bildfil som kallas SheetImage.jpg.

Följande är koden som används av komponenten för att utföra uppgiften. Den konverterar Sheet1 i **Testbook.xlsx** till en bildfil för att förklara hur enkel denna konvertering är.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Använda Aspose.Cells för att konvertera arbetsblad till bildfil per sida**

Detta exempel visar hur man använder Aspose.Cells för att konvertera ett arbetsblad från en mallarbok som har flera sidor till en bildfil per sida.

### **Konvertera arbetsblad till bild per sida**

Jag skapade en ny arbetsbok i Microsoft Excel och lade till lite data i det första arbetsbladet: **Testbook2.xlsx** (1 arbetsblad).

Nu, konvertera mallfilens arbetsblad Sheet1 till bildfiler (en fil per sida). Eftersom jag redan skapat konsolapplikationen för att utföra kopieringsuppgiften, kommer jag att hoppa över de stegen för att skapa konsolapplikationen och gå direkt till arbetsbladskonverteringsstegen.

Följande är koden som används av komponenten för att utföra uppgiften. Den konverterar Sheet1 i Testbook2.xls till bildfiler per sida.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
