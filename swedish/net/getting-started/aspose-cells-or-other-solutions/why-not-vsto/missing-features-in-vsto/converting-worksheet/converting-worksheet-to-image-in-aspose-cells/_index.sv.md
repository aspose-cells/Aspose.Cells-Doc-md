---
title: Konvertera arbetsblad till bild i Aspose.Cells
type: docs
weight: 20
url: /sv/net/converting-worksheet-to-image-in-aspose-cells/
---

Detta dokument är utformat för att ge utvecklarna en detaljerad förståelse för hur man konverterar ett arbetsblad till en bildfil och ett arbetsblad med flera sidor till en bildfil per sida.
Ibland kan du behöva presentera arbetsblad som bilder, till exempel för att använda dem i program eller webbsidor. Du kan behöva infoga bilderna i ett Word-dokument, en **PDF**-fil, en PowerPoint-presentation eller använda dem i något annat scenario. Helt enkelt, du vill rendera arbetsbladet som en bild. Aspose.Cells stöder konvertering av arbetsblad i Microsoft Excel-filer till bilder. Dessutom stöder **Aspose.Cells** konvertering av en arbetsbok till flera bildfiler, en per sida.

Du kan använda Office Automation för att uppnå detta, men Office Automation har sina egna nackdelar. Det finns flera skäl och problem involverade: till exempel säkerhet, stabilitet, skalbarhet/hastighet, pris och funktioner. Kort sagt, det finns många skäl, men det främsta är att Microsoft själva starkt rekommenderar att inte använda Office Automation.

Den här artikeln visar hur du skapar en konsolapplikation i Visual Studio.Net, konverterar ett arbetsblad till en bild och ett arbetsblad till en bild för varje arbetsblad med några enkla rader kod med hjälp av Aspose.Cells API. Du måste importera Aspose.Cells.Rendering-namespace till ditt program/projekt. Det finns flera värdefulla klasser, t.ex. SheetRender, ImageOrPrintOptions, WorkbookRender etc. Aspose.Cells.Rendering.SheetRender-klassen representerar ett arbetsblad för att rendera bilder för arbetsbladet, den har en överbelastad **ToImage**-metod som kan direkt konvertera ett arbetsblad till bildfil(er) som specificerats med dina önskade attribut eller alternativ. Den kan returnera **System.Drawing.Bitmap**-objekt och du kan spara en bildfil på disk/stream. Det finns flera bildformat som stöds, t.ex. .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf etc.

{{< highlight csharp >}}

//Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image type

imgOptions.ImageType = ImageType.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **Ladda ned provkoden**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
