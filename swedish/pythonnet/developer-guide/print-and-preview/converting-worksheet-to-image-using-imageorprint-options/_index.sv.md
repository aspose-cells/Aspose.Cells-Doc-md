---
title: Konvertera arbetsblad till bild med hjälp av alternativ för bild eller utskrift
type: docs
weight: 90
url: /sv/python-net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Detta dokument är utformat för att ge en detaljerad förståelse för hur man konverterar ett arbetsblad till en bildfil och tillämpar olika bild- och utskriftsalternativ för bilden, såsom upplösning, TIFF-komprimering, bildformat och sidkvalitet.

{{% /alert %}}

## **Spara arbetsblad till bilder - Olika tillvägagångssätt**

Ibland kan du behöva visa dina arbetsblad som en bild. Du vill infoga arbetsbladsbilder i dina program eller webbsidor. Du kan behöva infoga dessa bilder i ett Word-dokument, PDF-fil, PowerPoint-presentation eller använda dem i annat scenario. Enkelt sagt, du vill att ett arbetsblad ska renderas som en bild för att kunna använda det på andra platser. Aspose.Cells för Python via .NET stöder konvertering av arbetsblad i Excel-filer till bilder. Dessutom stöder Aspose.Cells för Python via .NET att ställa in olika alternativ som bildformat, upplösning (både vertikal och horisontell), bildkvalitet och andra bild- och utskriftsalternativ.

Du kan prova Office Automation, men Office Automation har sina egna nackdelar. Det finns flera skäl och problem involverade, till exempel säkerhet, stabilitet, skalbarhet och hastighet, pris och funktioner. Kort sagt, det finns många orsaker, där den främsta är att Microsoft själva starkt avråder från Office Automation för programvarulösningar.

Denna artikel visar hur man skapar ett konsolprogram i Visual Studio .NET, utför konvertering av ett arbetsblad till bild med olika bild- och utskriftsalternativ med några få enkla rader kod med Aspose.Cells för Python via .NET API.

Du behöver importera [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) namespace till ditt program/projekt. Det har flera värdefulla klasser, till exempel [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) osv.

Klassen [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) representerar ett arbetsblad för att rendera bilder för arbetsbladet, den har en överbelastad [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str)-metod som kan konvertera ett arbetsblad direkt till bildfil(er) som specificerats med önskade attribut eller alternativ. Den kan returnera System.Drawing.Bitmap-objekt och du kan spara en bildfil på disken/strömmen. Det finns flera bildformat som stöds, t.ex. BMP, PNG, GIFF, JPEG, TIFF, EMF med mera.

## **Använd Aspose.Cells för att konvertera arbetsblad till bild med hjälp av ImageOrPrint-alternativ**

### **Skapa en mallarbok i Microsoft Excel**

Jag skapade en ny arbetsbok i MS Excel och lade till lite data i det första arbetsbladet. Nu kommer jag att konvertera mallfilens arbetsblad “Sheet1” till en bildfil “SheetImage.tiff” och tillämpa olika bildalternativ som horisontell och vertikal upplösning, TiffCompression med mera.

### **Konvertera arbetsblad till en bildfil**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-WorksheetToAnImage-1.py" >}}


## **Bildkonvertering med användning av WorkbookRender**

En TIFF-bild kan innehålla fler än en ram. Du kan spara hela arbetsboken till en enda TIFF-bild med flera ramar eller sidor:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-UseWorkbookRenderForImageConversion-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
