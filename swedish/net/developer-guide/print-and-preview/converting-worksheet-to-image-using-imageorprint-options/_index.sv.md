---
title: Konvertera kalkylblad till bild med ImageOrPrint-alternativ
type: docs
weight: 90
url: /sv/net/converting-worksheet-to-image-using-imageorprint-options/
---
{{% alert color="primary" %}}

Detta dokument är utformat för att ge en detaljerad förståelse för hur man konverterar ett kalkylblad till en bildfil och använder olika bild- och utskriftsalternativ för bilden, alternativ som upplösning, TIFF-komprimering, bildformat och sidkvalitet.

{{% /alert %}}

##  **Spara kalkylblad till bilder – olika tillvägagångssätt**

Ibland kan du behöva presentera dina kalkylblad som en bildrepresentation. Du måste presentera kalkylbladsbilderna i dina applikationer eller webbsidor. Du kan behöva infoga bilderna i ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller använda dem i något annat scenario. Du vill helt enkelt att ett kalkylblad ska renderas som en bild så att du kan använda det någon annanstans. Aspose.Cells stöder konvertering av kalkylblad i Excel-filer till bilder. Dessutom stöder Aspose.Cells inställning av olika alternativ som bildformat, upplösning (både vertikalt och horisontellt), bildkvalitet och andra bild- och utskriftsalternativ.

Du kan prova Office Automation men Office Automation har sina egna nackdelar. Det finns flera orsaker och problem inblandade: till exempel säkerhet, stabilitet, skalbarhet och hastighet, pris och funktioner. Kort sagt, det finns många anledningar, med den främsta är att Microsoft själva starkt rekommenderar Office-automation från mjukvarulösningar.

Den här artikeln visar hur du skapar en konsolapplikation i Visual Studio .NET, utför konverteringen av ett kalkylblad till bild med olika bild- och utskriftsalternativ med några få och enklaste rader kod med Aspose.Cells API.

 Du måste importera[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)namnutrymme till ditt program/projekt. Den har flera värdefulla klasser, t.ex.[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)etc.

De[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) klass representerar ett kalkylblad för att rendera bilder för kalkylbladet, det har en överbelastad[**Att föreställa sig**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)metod som direkt kan konvertera ett kalkylblad till bildfil(er) specificerade med dina önskade attribut eller alternativ. Det kan returnera System.Drawing.Bitmap-objekt och du kan spara en bildfil på disken/strömmen. Det finns flera bildformat som stöds, t.ex. BMP, PNG, GIFF, JPEG, TIFF, EMF och så vidare.

##  **Använda Aspose.Cells för att konvertera kalkylblad till bild med ImageOrPrint-alternativ.**

###  **Skapa en mall arbetsbok i Microsoft Excel**

Jag skapade en ny arbetsbok i MS Excel och lade till lite data i det första kalkylbladet. Nu kommer jag att konvertera mallfilens kalkylblad "Sheet1" till en bildfil "SheetImage.tiff" och kommer att tillämpa olika bildalternativ som horisontella och vertikala upplösningar, TiffCompression etc.

###  **Ladda ner och installera Aspose.Cells**

 Först måste du[ladda ner](https://downloads.aspose.com/cells/net) Aspose.Cells för .Net. Installera det på din utvecklingsdator. Allt[Aspose](http://www.aspose.com/)komponenter, när de är installerade, fungerar i utvärderingsläge. Utvärderingsläget har ingen tidsbegränsning och det injicerar bara vattenstämplar i producerade dokument.

###  **Skapa ett projekt**

Starta Visual Studio. Nät och skapa en ny konsolapplikation. Det här exemplet visar en C# konsolapplikation, men du kan också använda VB.NET.

###  **Lägg till referenser**

Detta projekt kommer att använda Aspose.Cells. Så du måste lägga till referens till komponenten Aspose.Cells i ditt projekt. Lägg till exempel till en referens till ….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll

###  **Konvertera arbetsblad till en bildfil**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

##  **Konverteringsalternativ**

Det är möjligt att spara specifika sidor till bild. Följande kod konverterar de första och andra kalkylbladen i en arbetsbok till JPG-bilder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

##  **Bildkonvertering med WorkbookRender**

En TIFF-bild kan innehålla mer än en bildruta. Du kan spara hela arbetsboken till en enda TIFF-bild med flera ramar eller sidor:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

