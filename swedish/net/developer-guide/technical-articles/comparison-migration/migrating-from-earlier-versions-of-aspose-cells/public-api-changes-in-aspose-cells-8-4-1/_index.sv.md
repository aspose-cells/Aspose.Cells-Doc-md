---
title: Offentliga API ändringar i Aspose.Cells 8.4.1
type: docs
weight: 140
url: /sv/net/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.4.0 till 8.4.1 som kan vara intressanta för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-4-1/) och [borttagna klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-4-1/), utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Mekanism för att ändra databasanslutning**
Klassen Aspose.Cells.ExternalConnections.ExternalConnection innehöll redan metoden & egenskaper som kunde användas för att inspektera databaskopplingsdetaljer som lagrats i ett kalkylblad. De flesta av egenskaperna associerade med klassen Aspose.Cells.ExternalConnections.ExternalConnection var skrivskyddade fram till utgåvan av Aspose.Cells for .NET 8.4.1. Med denna utgåva har API:et tillhandahållit stödet för att manipulera inställningarna för databaskopplingen.

Följande kodsnutt visar hur man dynamiskt modifierar databasanslutningsinställningarna.

**C#**

{{< highlight csharp >}}

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



Här är några av de viktigaste egenskaperna som exponeras av {Aspose.Cells.ExternalConnections.ExternalConnection}}-klassen.

|**Egenskapsnamn**|**Beskrivning**|
| :- | :- |
|BackgroundRefresh|Indikerar om anslutningen kan uppdateras i bakgrunden (asynkront).<br>true om föredragen användning av anslutningen är att uppdateras asynkront i bakgrunden; <br>false om föredragen användning av anslutningen är att uppdateras synkront i förgrunden.|
|ConnectionDescription|Specificerar användarbeskrivningen för denna anslutning|
|ConnectionId|Specificerar det unika identifieraren för denna anslutning.|
|Credentials|Anger autentiseringsmetoden som ska användas vid etablering (eller om-etablering) av anslutningen.|
|IsDeleted|Indikerar om den associerade arbetsbokanslutningen har tagits bort. true om <br>anslutningen har tagits bort; annars false.|
|IsNew|True om anslutningen inte har uppdaterats första gången; annars false. Det <br>här tillståndet kan inträffa när användaren sparar filen innan en förfrågan har avslutats.|
|KeepAlive|True när kalkylbladsprogrammet ska göra ansträngningar för att hålla anslutningen <br>öppen. När false ska programmet stänga anslutningen efter hämtning av <br>informationen.|
|Name|Anger namnet på anslutningen. Varje anslutning måste ha ett unikt namn.|
|OdcFile|Specificerar fullständig sökväg till extern anslutningsfil från vilken denna anslutning skapades.<br>Om en anslutning misslyckas vid ett försök att uppdatera data och reconnectionMethod=1,<br>kommer kalkylbladsprogrammet att försöka igen med information från den externa anslutningsfilen<br>istället för anslutningsobjektet inbäddat i arbetsboken.|
|OnlyUseConnectionFile|Indikerar om kalkylbladsprogrammet alltid och enbart ska använda <br>anslutningsinformationen i den externa anslutningsfilen som anges av odcFile-attributet <br>när anslutningen uppdateras. Om false ska kalkylbladsprogrammet följa <br>förfarandet som anges av reconnectionMethod-attributet|
|Parameters|Får ConnectionParameterCollection för en ODBC- eller webbförfrågan.|
|ReConnectionMethod|Ange reconnectionMethod-typ|
|RefreshInternal|Specificerar antalet minuter mellan automatiska uppdateringar av anslutningen.|
|RefreshOnLoad|True om denna anslutning ska uppdateras vid öppnande av filen; annars false.|
|SaveData|True om den externa datan som hämtats via anslutningen för att fylla på en tabell ska sparas<br>med arbetsboken; annars false.|
|SavePassword|True om lösenordet ska sparas som en del av anslutningssträngen; annars False.|
|SourceFile|Används när den externa datakällan är filbaserad. När en anslutning till en sådan data<br>källa misslyckas, försöker kalkylbladsprogrammet att ansluta direkt till denna fil. Kan vara <br>uttryckt i URI eller systemspecifik filsökvägsnotation.|
|SSOId|Identifierare för Single Sign On (SSO) som används för autentisering mellan en intermediär <br>spreadsheetML-server och den externa datakällan.|
|Type|Anger datakälltypen.|

### **Förmåga att formatera delsträng av datamärken. |**
Aspose.Cells for .NET 8.4.1 har exponerat metoden DataLabels.Characters för att hämta en instans av FontSetting-klassen som motsvarar delsträngen av ett ChartPoints.DataLabels. I sin tur kan instansen av FontSetting-klassen användas för att formatera delsträngen av DataLabels med olika fonterinställningar och färger.

Den följande kodsnutten visar hur man använder metoden DataLabels.Characters.

**C#**

{{< highlight csharp >}}

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


### **Förmåga att ställa in önskade bildmått för kalkylblad & diagramexport.**
Aspose.Cells for .NET 8.4.1 har exponerat metoden ImageOrPrintOptions.SetDesiredSize för att ange dimensionerna för den resulterande bilden vid export av kalkylblad & diagram till bilder. Metoden ImageOrPrintOptions.SetDesiredSize accepterar två parametrar av typen heltal, där den första är önskad bredd och den andra är önskad höjd.

Följande kodsnutt visar hur man ställer in önskade dimensioner vid export av kalkylblad till PNG.

**C#**

{{< highlight csharp >}}

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


### **Rendera kommentarer till PDF**
Med utgåvan av v8.4.1 har Aspose.Cells API tillhandahållit egenskapen PageSetup.PrintComments och PrintCommentsType-uppräkningen för att underlätta renderingen av kommentarer vid konvertering av kalkylblad till PDF-format. PrintCommentsType-uppräkningen har följande konstanter.

- PrintCommentsType.PrintNoComments: Kommentarer ska inte renderas.
- PrintCommentsType.PrintInPlace: Kommentarer ska renderas där de är placerade.
- PrintCommentsType.PrintSheetEnd: Kommentarer ska renderas i slutet av kalkylbladet.

Följande exempelkod demonstrerar användningen av PageSetup.PrintComments-egenskapen för att rendera kommentarer med alla möjliga värden för PrintCommentsType-uppräkningen.

**C#**

{{< highlight csharp >}}

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


### **Flytta arbetsblad i Aspose.Cells.GridDesktop**
Aspose.Cells.GridDesktop tillhandahåller WorksheetCollection.MoveTo-metoden, som kan användas för att flytta ett arbetsblad till det angivna indexet. Ovanstående metod tar index (nollbaserat) för källarbetsbladet och destinationsarbetsbladet som parametrar.

Följande kodexempel visar användningen av WorksheetCollection.MoveTo-egenskapen.

**C#**

{{< highlight csharp >}}

 //Move the second worksheet to 4th position.

GridDesktop1.Worksheets.MoveTo(1, 3);

{{< /highlight >}}


### **Tillagd Workbook.IsLicensed-egenskap**
Aspose.Cells for .NET 8.4.1 har exponerat Workbook.IsLicensed vilket kan vara till stor hjälp för att avgöra om licensen har laddats in framgångsrikt eller inte. Om du får åtkomst till denna egenskap innan licensen har angetts kommer den returnera falskt och vice versa, men licensen ska vara giltig.

Följande kodexempel visar användningen av Workbook.IsLicensed-egenskapen.

**C#**

{{< highlight csharp >}}

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


### **Tillagd ImageOrPrintOptions.SVGFitToViewPort-egenskap**
Aspose.Cells for .NET 8.4.1 har exponerat SVGFitToViewPort-egenskapen för ImageOrPrintOptions-klassen som kan användas för att aktivera viewBox-attributet för SVG-filformatet vid export av kalkylblad eller diagram till SVG-format. Standardvärdet för denna egenskap är falskt, varför den grundläggande XML för SVG-filen som skapats utan att ange den ovanstående egenskapen inte kommer att inkludera viewBox-attributet.

Följande exempelkod demonstrerar användningen av ImageOrPrintOptions.SVGFitToViewPort-egenskapen.

**C#**

{{< highlight csharp >}}

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
## **Obsoletterade API:er**
### **Föråldrad Workbook.ValidateFormula-metod**
Använd Cell.Formula-metoden för att validera formeln.
{{< app/cells/assistant language="csharp" >}}
