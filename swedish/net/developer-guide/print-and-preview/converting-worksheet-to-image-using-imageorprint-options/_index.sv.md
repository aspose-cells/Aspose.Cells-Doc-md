---
title: Konvertera arbetsblad till bild med hjälp av alternativ för bild eller utskrift
type: docs
weight: 90
url: /sv/net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Detta dokument är utformat för att ge en detaljerad förståelse för hur man konverterar ett arbetsblad till en bildfil och tillämpar olika bild- och utskriftsalternativ för bilden, såsom upplösning, TIFF-komprimering, bildformat och sidkvalitet.

{{% /alert %}}

## **Spara arbetsblad till bilder - Olika tillvägagångssätt**

Ibland kan det hända att du behöver presentera dina arbetsblad som en bildlig representation. Du kan behöva infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem på annat sätt. Du vill helt enkelt ha ett arbetsblad renderat som en bild så att du kan använda det någon annanstans. Aspose.Cells stödjer konvertering av arbetsblad i Excel-filer till bilder. Dessutom stödjer Aspose.Cells inställning av olika alternativ som bildformat, upplösning (både vertikal och horisontell), bildkvalitet och andra bild- och utskriftsalternativ.

Du kan prova Office Automation, men Office Automation har sina egna nackdelar. Det finns flera skäl och problem involverade, till exempel säkerhet, stabilitet, skalbarhet och hastighet, pris och funktioner. Kort sagt, det finns många orsaker, där den främsta är att Microsoft själva starkt avråder från Office Automation för programvarulösningar.

Denna artikel visar hur man skapar en konsolapplikation i Visual Studio .NET, utför konvertering av ett arbetsblad till bild med olika bild- och utskriftsalternativ med några enkla kodrader med hjälp av Aspose.Cells API.

Du behöver importera [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) namespace till ditt program/projekt. Det har flera värdefulla klasser, till exempel [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) osv.

Klassen [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) representerar ett arbetsblad för att rendera bilder för arbetsbladet, den har en överbelastad [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)-metod som kan konvertera ett arbetsblad direkt till bildfil(er) som specificerats med önskade attribut eller alternativ. Den kan returnera System.Drawing.Bitmap-objekt och du kan spara en bildfil på disken/strömmen. Det finns flera bildformat som stöds, t.ex. BMP, PNG, GIFF, JPEG, TIFF, EMF med mera.

## **Använda Aspose.Cells för att konvertera arbetsblad till bild med hjälp av alternativ för bild eller utskrift**

### **Skapa en mallarbok i Microsoft Excel**

Jag skapade en ny arbetsbok i MS Excel och lade till lite data i det första arbetsbladet. Nu kommer jag att konvertera mallfilens arbetsblad “Sheet1” till en bildfil “SheetImage.tiff” och tillämpa olika bildalternativ som horisontell och vertikal upplösning, TiffCompression med mera.

### **Ladda ner och installera Aspose.Cells**

Först måste du [ladda ner](https://downloads.aspose.com/cells/net) Aspose.Cells för .Net. Installera det på din utvecklingsdator. Alla [Aspose](http://www.aspose.com/)-komponenter, när de väl är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det lägger bara in vattenstämplar i producerade dokument.

### **Skapa ett projekt**

Starta Visual Studio. Net och skapa en ny konsolapplikation. Detta exempel kommer att visa en C#-konsolapplikation, men du kan också använda VB.NET.

### **Lägg till referenser**

Detta projekt kommer att använda Aspose.Cells. Så du måste lägga till en referens till Aspose.Cells-komponenten i ditt projekt. Till exempel, lägg till en referens till ….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll

### **Konvertera arbetsblad till en bildfil**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **Konverteringsalternativ**

Det är möjligt att spara specifika sidor som bild. Följande kod konverterar arbetsböckerets första och andra kalkylblad till JPG-bilder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **Bildkonvertering med användning av WorkbookRender**

En TIFF-bild kan innehålla fler än en ram. Du kan spara hela arbetsboken till en enda TIFF-bild med flera ramar eller sidor:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
