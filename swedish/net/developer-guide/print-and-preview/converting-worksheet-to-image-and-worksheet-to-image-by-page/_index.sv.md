---
title: Konvertera kalkylblad till bild och kalkylblad till bild för sida
type: docs
weight: 80
url: /sv/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Detta dokument är utformat för att ge utvecklarna en detaljerad förståelse för hur man konverterar ett kalkylblad till en bildfil & kalkylblad med flera sidor till en bildfil per sida.

Ibland kan du behöva presentera kalkylblad som bilder, till exempel för att använda dem i applikationer eller webbsidor. Du kan behöva infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem i något annat scenario. Du vill helt enkelt rendera kalkylbladet som en bild. Aspose.Cells stöder konvertering av kalkylblad i Microsoft Excel-filer till bilder. Dessutom stöder Aspose.Cells konvertering av en arbetsbok till flera bildfiler, en per sida.

Du kanske använder Office Automation för att uppnå detta, men Office Automation har sina egna nackdelar. Det finns flera orsaker och problem inblandade: till exempel säkerhet, stabilitet, skalbarhet/hastighet, pris och funktioner. Kort sagt finns det många anledningar, men den främsta är att Microsoft själva starkt rekommenderar Office-automatisering.

{{% /alert %}}

## **Använda Aspose.Cells för att konvertera kalkylblad till bildfil**

Den här artikeln visar hur du skapar en konsolapplikation i Visual Studio, konverterar ett kalkylblad till en bild och konverterar ett kalkylblad till en bild för varje kalkylblad med några få och enklaste rader kod med hjälp av Aspose.Cells API.

 Du måste importera[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) namnutrymme till ditt program/projekt. Den har flera värdefulla klasser, som t.ex[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), och så vidare. De[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) klass representerar ett kalkylblad för att rendera bilder för kalkylbladet och har en överbelastad[**Att föreställa sig**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)metod som kan konvertera ett kalkylblad till bildfiler direkt med vilka attribut eller alternativ som helst. Det kan returnera ett System.Drawing.Bitmap-objekt och du kan spara en bildfil på disken/strömmen. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF och andra.

Den här artikeln förklarar hur du:

- Konvertera ett kalkylblad till en bild
- Konvertera varje sida i ett kalkylblad till en bild

Den här uppgiften visar hur du använder Aspose.Cells för att konvertera ett kalkylblad från en mallarbetsbok till en bildfil.

### **Konfigurera projekt**

1.  Först,[ladda ner Aspose.Cells för .NET](https://downloads.aspose.com/cells/net).
1.  Installera det på din utvecklingsdator. Allt[Aspose](http://www.aspose.com/)komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar bara vattenstämplar i producerade dokument. Starta nu Visual Studio.Net och skapa en ny konsolapplikation. Det här exemplet använder en C#-konsolapplikation, men du kan också använda VB.NET. Lägg till referens till Aspose.Cells i skapat projekt.

### **Konvertera arbetsblad till bildfil**

 Jag skapade en ny arbetsbok i Microsoft Excel och la till några data i det första kalkylbladet:**Testbook.xlsx** (1 arbetsblad). Konvertera sedan mallfilens kalkylblad Sheet1 till en bildfil som heter SheetImage.jpg.

 Följande är koden som används av komponenten för att utföra uppgiften. Den konverterar Sheet1 in**Testbook.xlsx** till en bildfil för att förklara hur lätt denna konvertering är.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Använda Aspose.Cells för att konvertera kalkylblad till bildfil per sida**

Det här exemplet visar hur du använder Aspose.Cells för att konvertera ett kalkylblad från en mallarbetsbok som har flera sidor till en bildfil per sida.

### **Konvertera kalkylblad till bild per sida**

 Jag skapade en ny arbetsbok i Microsoft Excel och la till några data i det första kalkylbladet:**Testbook2.xlsx** (1 arbetsblad).

Konvertera nu mallfilens kalkylblad Sheet1 till bildfiler (en fil per sida). Eftersom jag redan skapat konsolapplikationen för att utföra kopieringsuppgiften, kommer jag att hoppa över dessa steg för att skapa konsolapplikationer och gå direkt till kalkylbladskonverteringsstegen.

Följande är koden som används av komponenten för att utföra uppgiften. Den konverterar Sheet1 i Testbook2.xls till bildfiler per sida.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

