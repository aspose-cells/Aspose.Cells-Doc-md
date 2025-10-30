---
title: Konvertera kalkylblad till bild och Kalkylblad till bild per sida
type: docs
weight: 80
url: /sv/python-net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Detta dokument är utformat för att ge utvecklarna en detaljerad förståelse för hur man konverterar ett kalkylblad till en bildfil och ett kalkylblad med flera sidor till en bildfil per sida.

Ibland kan du behöva visa arbetsblad som bilder, till exempel för att använda dem i appar eller webbsidor. Du kan behöva infoga bilderna i ett Word-dokument, PDF-fil, PowerPoint-presentation eller använda dem i andra scenarier. Enkel uttryckning, du vill rendera ett arbetsblad som en bild. Aspose.Cells för Python via .NET stöder konvertering av arbetsblad i Microsoft Excel-filer till bilder. Dessutom kan Aspose.Cells för Python via .NET konvertera en arbetsbok till flera bildfiler, en per sida.

Du kan använda Office Automation för att uppnå detta, men Office Automation har sina egna nackdelar. Det finns flera skäl och problem involverade: till exempel säkerhet, stabilitet, skalbarhet/hastighet, pris och funktioner. Kort sagt, det finns många skäl, men det främsta är att Microsoft själva starkt rekommenderar att inte använda Office Automation.

{{% /alert %}}

## **Använda Aspose.Cells för att konvertera kalkylblad till bildfil**

Denna artikel visar hur man skapar en konsolapplikation i Visual Studio, konverterar ett arbetsblad till en bild och konverterar ett arbetsblad till en bild för varje kalkylblad med några få enkla rader kod med Aspose.Cells för Python via .NET API.

Du behöver importera [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering)-namnrymden till ditt program/projekt. Den har flera värdefulla klasser, såsom [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender), och så vidare. Klassen [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) representerar ett kalkylblad för att rendera bilder för kalkylbladet och har en överlagrad [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)-metod som kan konvertera ett kalkylblad till bildfiler direkt med alla ställa in attribut eller alternativ. Den kan returnera ett System.Drawing.Bitmap-objekt och du kan spara en bildfil på disk/ström. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF, och andra.

Denna artikel förklarar hur man konverterar ett arbetsblad till en bild. Denna uppgift visar hur man använder Aspose.Cells för Python via .NET för att konvertera ett arbetsblad från ett mallarbetsbok till en bildfil.


### **Konvertera kalkylblad till bildfil**

Jag skapade en ny arbetsbok i Microsoft Excel och lade till lite data i det första kalkylbladet: **Testbook.xlsx** (1 kalkylblad). Nästa steg är att konvertera mallfilens kalkylblad Sheet1 till en bildfil som kallas SheetImage.jpg.

Följande är koden som används av komponenten för att utföra uppgiften. Den konverterar Sheet1 i **Testbook.xlsx** till en bildfil för att förklara hur enkel denna konvertering är.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheettoImageFile-1.py" >}}

## **Använda Aspose.Cells för att konvertera arbetsblad till bildfil per sida**

Detta exempel visar hur man använder Aspose.Cells för Python via .NET för att konvertera ett arbetsblad från ett mallarbetsbok som har flera sidor till en bildfil per sida.

### **Konvertera arbetsblad till bild per sida**

Jag skapade en ny arbetsbok i Microsoft Excel och lade till lite data i det första arbetsbladet: **Testbook2.xlsx** (1 arbetsblad).

Nu, konvertera mallfilens arbetsblad Sheet1 till bildfiler (en fil per sida). Eftersom jag redan skapat konsolapplikationen för att utföra kopieringsuppgiften, kommer jag att hoppa över de stegen för att skapa konsolapplikationen och gå direkt till arbetsbladskonverteringsstegen.

Följande är koden som används av komponenten för att utföra uppgiften. Den konverterar Sheet1 i Testbook2.xls till bildfiler per sida.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheetToImageByPage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
