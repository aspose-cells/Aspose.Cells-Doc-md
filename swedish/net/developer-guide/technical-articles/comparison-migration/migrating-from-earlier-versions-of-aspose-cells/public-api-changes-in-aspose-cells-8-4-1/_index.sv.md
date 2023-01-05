---
title: Offentlig API Ändringar i Aspose.Cells 8.4.1
type: docs
weight: 140
url: /sv/net/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.4.0 till 8.4.1 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-4-1/) och[borttagna klasser osv.](/cells/sv/net/public-api-changes-in-aspose-cells-8-4-1/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Mekanism för att ändra databasanslutningen**
Klassen Aspose.Cells.ExternalConnections.ExternalConnection innehöll redan metoden och egenskaperna som kunde användas för att inspektera databasanslutningsdetaljerna lagrade i ett kalkylblad. De flesta egenskaper som är associerade med klassen Aspose.Cells.ExternalConnections.ExternalConnection var skrivskyddade fram till utgivningen av Aspose.Cells for .NET 8.4.1. Med den här utgåvan har API gett stöd för att manipulera databasanslutningsinställningarna också.

Följande kodavsnitt visar hur du dynamiskt ändrar databasanslutningsinställningar.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first data connection

Aspose.Cells.ExternalConnections.ExternalConnection conn = workbook.DataConnections[0];

//Change a few properties

conn.Name = "MyConnectionName";

conn.OdcFile = "MyDefaulConnection.odc";

conn.ConnectionDescription = "Test Connection";

conn.Credentials = Aspose.Cells.ExternalConnections.CredentialsMethodType.Prompt;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}



Här är några av de viktigaste egenskaperna som exponeras av klassen {Aspose.Cells.ExternalConnections.ExternalConnection}}.

|**Egendomsnamn**|**Beskrivning**|
|:- |:- |
|BackgroundRefresh|Indikerar om anslutningen kan uppdateras i bakgrunden (asynkront).<br> sant om föredragen användning av anslutningen är att uppdatera asynkront i bakgrunden;<br>false om föredragen användning av anslutningen är att uppdatera synkront i förgrunden.|
|Anslutningsbeskrivning|Anger användarbeskrivningen för denna anslutning|
|Anslutnings-ID|Anger den unika identifieraren för denna anslutning.|
|Referenser|Anger den autentiseringsmetod som ska användas när anslutningen upprättas (eller återupprättas).|
|Är Raderad|Indikerar om den associerade arbetsboksanslutningen har tagits bort. sant om<br>anslutningen har tagits bort; annars falskt.|
|Är ny| Sant om anslutningen inte har uppdaterats för första gången; annars falskt. Detta<br>tillstånd kan inträffa när användaren sparar filen innan en fråga har slutat återkomma.|
|Håll vid liv|Sant när kalkylprogrammet ska anstränga sig för att behålla anslutningen<br> öppen. När det är falskt bör applikationen stänga anslutningen efter att ha hämtat<br>information.|
|namn|Anger namnet på anslutningen. Varje anslutning måste ha ett unikt namn.|
|OdcFile| Anger den fullständiga sökvägen till den externa anslutningsfilen från vilken anslutningen kom<br> skapas. Om en anslutning misslyckas under ett försök att uppdatera data, och reconnectionMethod=1,<br> då försöker kalkylarket igen med information från den externa anslutningsfilen<br>istället för det anslutningsobjekt som är inbäddat i arbetsboken.|
|OnlyUseConnectionFile| Anger om kalkylbladsapplikationen alltid och bara ska använda<br> anslutningsinformation i den externa anslutningsfilen som anges av odcFile-attributet<br> när anslutningen uppdateras. Om falskt, då kalkylarksapplikationen<br>bör följa proceduren som anges av attributet reconnectionMethod|
|Parametrar|Hämtar ConnectionParameterCollection för en ODBC- eller webbfråga.|
|Återanslutningsmetod|Ange reconnectionMethod-typ|
|Uppdatera Internt|Anger antalet minuter mellan automatiska uppdateringar av anslutningen.|
|RefreshOnLoad|Sant om den här anslutningen ska uppdateras när filen öppnas; annars falskt.|
|Spara data|Sant om den externa data som hämtas via anslutningen för att fylla i en tabell ska sparas<br>med arbetsboken; annars falskt.|
|Spara lösenord|True om lösenordet ska sparas som en del av anslutningssträngen; annars, Falskt.|
|Källfilen| Används när den externa datakällan är filbaserad. När en anslutning till en sådan data<br> källan misslyckas försöker kalkylarksprogrammet ansluta direkt till den här filen. Kanske<br>uttryckt i URI eller systemspecifik filsökvägsnotation.|
|SSOId|Identifierare för enkel inloggning (SSO) som används för autentisering mellan en intermediär<br>kalkylarkML-server och den externa datakällan.|
|Typ|Anger datakällans typ.|

### **Möjlighet att formatera understräng av DataLabels text**
Aspose.Cells for .NET 8.4.1 har exponerat metoden DataLabels.Characters för att hämta en instans av FontSetting-klassen som motsvarar understrängen i en ChartPoints.DataLabels. I sin tur kan instansen av FontSetting-klassen användas för att formatera understrängen för DataLabels med olika teckensnittsinställningar och färg.

Följande kodavsnitt visar hur du använder metoden DataLabels.Characters.

**C#**

{{< highlight "csharp" >}}

 //Create a workbook from source Excel file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Access the first chart inside the sheet

Aspose.Cells.Charts.Chart chart = worksheet.Charts[0];

//Access the data label of first series first point

Aspose.Cells.Charts.DataLabels labels = chart.NSeries[0].Points[0].DataLabels;

//Set data label text

labels.Text = "Rich Text Label";

//Set the font setting of the first 10 characters

Aspose.Cells.FontSetting settings = labels.Characters(0, 10);

settings.Font.Color = System.Drawing.Color.Red;

settings.Font.IsBold = true;

//Save the workbook

workbook.Save(output);

{{< /highlight >}}


### **Möjlighet att ställa in önskade bildmått för kalkylblad och diagramexport**
Aspose.Cells for .NET 8.4.1 har exponerat metoden ImageOrPrintOptions.SetDesiredSize för att ställa in dimensionerna för den resulterande bilden samtidigt som kalkylblad och diagram exporteras till bilder. Metoden ImageOrPrintOptions.SetDesiredSize accepterar två parametrar av heltalstyp, där den första är den önskade bredden och den andra är den önskade höjden.

Följande kodavsnitt visar hur du ställer in önskade dimensioner när du exporterar kalkylblad till PNG.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set resultant image format

options.ImageFormat = System.Drawing.Imaging.ImageFormat.Png;

//Set desired dimensions as 400x400

options.SetDesiredSize(400, 400);

//Render sheet to image

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.png"); 

{{< /highlight >}}

{{% alert color="primary" %}} 

Samma egenskap kan också användas för att konvertera diagram till bilder.

{{% /alert %}} 


### **Återge kommentarer till PDF**
Med lanseringen av v8.4.1 har Aspose.Cells API tillhandahållit egenskapen PageSetup.PrintComments & PrintCommentsType för att underlätta återgivningen av kommentarer samtidigt som kalkylblad konverteras till formatet PDF. PrintCommentsType-uppräkningen har följande konstanter.

- PrintCommentsType.PrintNoComments: Kommentarer ska inte återges.
- PrintCommentsType.PrintInPlace: Kommentarer ska återges där de är placerade.
- PrintCommentsType.PrintSheetEnd: Kommentarer ska återges i slutet av kalkylbladet.

Följande exempelkod visar användningen av egenskapen PageSetup.PrintComments för att återge kommentarerna med alla möjliga PrintCommentsType-uppräkningsvärden.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of workbook

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Print no comments

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintNoComments;

//Save workbook in PDF format without comments

workbook.Save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintInPlace;

//Save workbook in PDF format while rendering comments in place

workbook.Save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.PageSetup.PrintComments = Aspose.Cells.PrintCommentsType.PrintSheetEnd;

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.Save("printsheetend.pdf");

{{< /highlight >}}


### **Flytta arbetsblad till Aspose.Cells.GridDesktop**
Aspose.Cells.GridDesktop tillhandahåller metoden WorksheetCollection.MoveTo, som kan användas för att flytta ett kalkylblad till det angivna indexet. Ovannämnda metod tar indexen (nollbaserade) för källarbetsbladet och målarbetsbladet som parametrar.

Följande exempelkod visar användningen av WorksheetCollection.MoveTo-egenskapen.

**C#**

{{< highlight "csharp" >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Lade till Workbook.IsLicensed Property**
Aspose.Cells for .NET 8.4.1 har avslöjat Workbook.IsLicensed vilket kan vara till stor hjälp för att avgöra om licensen har laddats eller inte. Om du kommer åt den här egenskapen innan du ställer in licensen kommer den att returnera falskt och vice versa, dock bör licensen vara giltig.

Följande exempelkod visar användningen av Workbook.IsLicensed-egenskapen.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object before setting a license

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook();

//Check if the license is loaded or not

if (!workbook.IsLicensed)

{

    //Set license

    Aspose.Cells.License license = new Aspose.Cells.License();

    lic.SetLicense(licPath);

}

else

{

    //do process

}

{{< /highlight >}}


### **Lagt till egenskapen ImageOrPrintOptions.SVGFitToViewPort**
Aspose.Cells for .NET 8.4.1 har exponerat egenskapen SVGFitToViewPort för klassen ImageOrPrintOptions som kan användas för att aktivera viewBox-attributet för filformatet SVG medan kalkylblad eller diagram exporteras till formatet SVG. Standardvärdet för den här egenskapen är falskt, därför kommer bas-XML-filen för SVG som genereras utan att ange ovannämnda egenskap inte att inkludera viewBox-attributet.

Följande exempelkod visar användningen av egenskapen ImageOrPrintOptions.SVGFitToViewPort.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Aspose.Cells.Workbook workbook = new Aspose.Cells.Workbook(input);

//Access first worksheet

Aspose.Cells.Worksheet worksheet = workbook.Worksheets[0];

//Create an instance of ImageOrPrintOptions

Aspose.Cells.Rendering.ImageOrPrintOptions options = new Aspose.Cells.Rendering.ImageOrPrintOptions();

//Set image format to SVG

options.SaveFormat = Aspose.Cells.SaveFormat.SVG;

//Set the SVGFitToViewPort to true

options.SVGFitToViewPort = true;

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

Aspose.Cells.Rendering.SheetRender renderer = new Aspose.Cells.Rendering.SheetRender(worksheet, options);

renderer.ToImage(0, "output.svg");

{{< /highlight >}}
## **Föråldrade API:er**
### **Metod Workbook.ValidateFormula Obsoleted**
Använd metoden Cell.Formula för att validera formeln.
