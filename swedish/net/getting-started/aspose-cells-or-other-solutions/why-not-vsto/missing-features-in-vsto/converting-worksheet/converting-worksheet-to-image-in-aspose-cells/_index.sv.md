---
title: Konvertera arbetsblad till bild i Aspose.Cells
type: docs
weight: 20
url: /sv/net/converting-worksheet-to-image-in-aspose-cells/
---
Detta dokument är utformat för att ge utvecklarna en detaljerad förståelse för hur man konverterar ett kalkylblad till en bildfil & kalkylblad med flera sidor till en bildfil per sida.
 Ibland kan du behöva presentera kalkylblad som bilder, till exempel för att använda dem i applikationer eller webbsidor. Du kan behöva infoga bilderna i ett Word-dokument, en**PDF**fil, en PowerPoint-presentation eller använd dem i något annat scenario. Du vill helt enkelt rendera kalkylbladet som en bild. Aspose.Cells stöder konvertering av kalkylblad i Microsoft Excel-filer till bilder. Också,**Aspose.Cells** stöder konvertering av en arbetsbok till flera bildfiler, en per sida.

Du kanske använder Office Automation för att uppnå detta, men Office Automation har sina egna nackdelar. Det finns flera orsaker och problem inblandade: till exempel säkerhet, stabilitet, skalbarhet/hastighet, pris och funktioner. Kort sagt finns det många anledningar, men den främsta är att Microsoft själva starkt rekommenderar Office-automatisering.

 Den här artikeln visar hur du skapar en konsolapplikation i Visual Studio.Net, konverterar ett kalkylblad till en bild och ett kalkylblad till en bild för varje kalkylblad med några få och enklaste rader kod med Aspose.Cells API. Du måste importera Aspose.Cells.Rendering namnutrymme till ditt program/projekt. Den har flera värdefulla klasser, t.ex. SheetRender, ImageOrPrintOptions, WorkbookRender etc.Aspose.Cells.Rendering.SheetRender-klassen representerar ett kalkylblad för att rendera bilder för kalkylbladet, den har en överbelastad**Att föreställa sig** metod som direkt kan konvertera ett kalkylblad till bildfil(er) specificerade med dina önskade attribut eller alternativ. Den kan återvända**System.Drawing.Bitmap**objekt och du kan spara en bildfil på disken/strömmen. Det finns flera bildformat som stöds, t.ex. .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf etc.

{{< highlight "csharp" >}}

 //Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image format

imgOptions.ImageFormat = System.Drawing.Imaging.ImageFormat.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **Ladda ner exempelkod**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
