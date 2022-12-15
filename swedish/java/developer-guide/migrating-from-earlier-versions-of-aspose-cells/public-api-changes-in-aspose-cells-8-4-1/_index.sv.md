---
title: Offentlig API Ändringar i Aspose.Cells 8.4.1
type: docs
weight: 150
url: /sv/java/public-api-changes-in-aspose-cells-8-4-1/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.4.0 till 8.4.1 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-4-1/) och[borttagna klasser osv.](/cells/sv/java/public-api-changes-in-aspose-cells-8-4-1/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Mekanism för att ändra databasanslutningen**
Klassen com.aspose.cells.ExternalConnection innehöll redan metoden och egenskaperna som kunde användas för att inspektera databasanslutningsdetaljer lagrade i ett kalkylblad. De flesta egenskaper som är associerade med klassen ExternalConnection var läsbara tills Aspose.Cells for Java släpptes 8.4.1. Med den här utgåvan har API gett stöd för att manipulera databasanslutningsinställningarna också.

Följande kodavsnitt visar hur du dynamiskt ändrar databasanslutningsinställningar.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first data connection

com.aspose.cells.ExternalConnection conn = workbook.getDataConnections().get(0);

//Change a few properties

conn.setName("MyConnectionName");

conn.setOdcFile("MyDefaulConnection.odc");

conn.setConnectionDescription("Test Connection");

conn.setCredentials(com.aspose.cells.CredentialsMethodType.PROMPT);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

Här är några av de viktigaste egenskaperna som exponeras av klassen {ExternalConnection}}.

|**Egendomsnamn** |**Beskrivning** |
|:- |:- |
| BackgroundRefresh|Indikerar om anslutningen kan uppdateras i bakgrunden (asynkront).<br> sant om föredragen användning av anslutningen är att uppdatera asynkront i bakgrunden;<br> false om föredragen användning av anslutningen är att uppdatera synkront i förgrunden.|
| Anslutningsbeskrivning| Anger användarbeskrivningen för denna anslutning|
| Anslutnings-ID| Anger den unika identifieraren för denna anslutning.|
| Referenser| Anger den autentiseringsmetod som ska användas när anslutningen upprättas (eller återupprättas).|
| Är Raderad|Indikerar om den associerade arbetsboksanslutningen har tagits bort. sant om<br> anslutningen har tagits bort; annars falskt.|
| Är ny| Sant om anslutningen inte har uppdaterats för första gången; annars falskt. Detta<br> tillstånd kan inträffa när användaren sparar filen innan en fråga har slutat återkomma.|
| Håll vid liv|Sant när kalkylprogrammet ska anstränga sig för att behålla anslutningen<br> öppna. När det är falskt bör applikationen stänga anslutningen efter att ha hämtat<br> information.|
| namn| Anger namnet på anslutningen. Varje anslutning måste ha ett unikt namn.|
| OdcFile| Anger den fullständiga sökvägen till den externa anslutningsfilen från vilken anslutningen kom<br> skapas. Om en anslutning misslyckas under ett försök att uppdatera data, och reconnectionMethod=1,<br> då försöker kalkylarket igen med information från den externa anslutningsfilen<br> istället för det anslutningsobjekt som är inbäddat i arbetsboken.|
| OnlyUseConnectionFile| Anger om kalkylbladsapplikationen alltid och bara ska använda<br> anslutningsinformation i den externa anslutningsfilen som anges av odcFile-attributet<br> när anslutningen uppdateras. Om falskt, då kalkylarksapplikationen<br>bör följa proceduren som anges av attributet reconnectionMethod|
| Parametrar| Hämtar ConnectionParameterCollection för en ODBC- eller webbfråga.|
| Återanslutningsmetod| Ange reconnectionMethod-typ|
|Uppdatera Internt| Anger antalet minuter mellan automatiska uppdateringar av anslutningen.|
| RefreshOnLoad| Sant om den här anslutningen ska uppdateras när filen öppnas; annars falskt.|
| Spara data|Sant om den externa data som hämtas via anslutningen för att fylla i en tabell ska sparas<br> med arbetsboken; annars falskt.|
| Spara lösenord| True om lösenordet ska sparas som en del av anslutningssträngen; annars, Falskt.|
| Källfilen| Används när den externa datakällan är filbaserad. När en anslutning till en sådan data<br> källan misslyckas försöker kalkylarksprogrammet ansluta direkt till den här filen. Kanske<br> uttryckt i URI eller systemspecifik filsökvägsnotation.|
|SSOId|Identifierare för enkel inloggning (SSO) som används för autentisering mellan en intermediär<br> kalkylarkML-server och den externa datakällan.|
| Typ| Anger datakällans typ.|

### **Möjlighet att formatera understräng av DataLabels text**
Aspose.Cells for Java 8.4.1 har exponerat metoden DataLabels.characters för att hämta en instans av FontSetting-klassen som motsvarar understrängen i en ChartPoints.DataLabels. I sin tur kan instansen av FontSetting-klassen användas för att formatera understrängen för DataLabels med olika teckensnittsinställningar och färg.

Följande kodavsnitt visar hur du använder metoden DataLabels.characters.

**Java**

{{< highlight "csharp" >}}

 //Create a workbook from source Excel file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first chart inside the sheet

com.aspose.cells.Chart chart = worksheet.getCharts().get(0);

//Access the data label of first series first point

com.aspose.cells.DataLabels labels = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

//Set data label text

labels.setText("Rich Text Label");

//Set the font setting of the first 10 characters

com.aspose.cells.FontSetting settings = labels.characters(0, 10);

settings.getFont().setColor(com.aspose.cells.Color.getRed());

settings.getFont().setBold(true);

//Save the workbook

workbook.save(output);

{{< /highlight >}}

### **Möjlighet att ställa in önskade bildmått för kalkylblad och diagramexport**
Aspose.Cells for Java 8.4.1 har exponerat metoden ImageOrPrintOptions.setDesiredSize för att ställa in dimensionerna för den resulterande bilden samtidigt som kalkylblad och diagram exporteras till bilder. Metoden ImageOrPrintOptions.setDesiredSize accepterar två parametrar av heltalstyp, där den första är den önskade bredden och den andra är den önskade höjden.

Följande kodavsnitt visar hur du ställer in önskade dimensioner när du exporterar kalkylblad till PNG.

**Java**

{{< highlight "csharp" >}}

 com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set resultant image format

options.setImageFormat(com.aspose.cells.ImageFormat.getPng());

//Set desired dimensions as 400x400

options.setDesiredSize(400, 400);

//Render sheet to image

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.png");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Samma metod kan också användas för att konvertera diagram till bilder.

{{% /alert %}} 

### **Återge kommentarer till PDF**
 Med lanseringen av v8.4.1 har Aspose.Cells API tillhandahållit egenskapen PageSetup.PrintComments & PrintCommentsType för att underlätta renderingen av kommentarer samtidigt som kalkylblad konverteras till PDF-format. PrintCommentsType-uppräkningen har följande konstanter.

- PrintCommentsType.PRINT_NEJ_KOMMENTARER: Kommentarer får inte återges.
- PrintCommentsType.PRINT_I_PLATS: Kommentarer ska återges där de placeras.
- PrintCommentsType.PRINT_ARK_SLUT: Kommentarer ska återges i slutet av arbetsbladet.

Följande exempelkod visar användningen av egenskapen PageSetup.PrintComments för att återge kommentarerna med alla möjliga PrintCommentsType-uppräkningsvärden.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of workbook

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Print no comments

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_NO_COMMENTS);

//Save workbook in PDF format without comments

workbook.save("nocomments.pdf");

//Print the comments as displayed on sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_IN_PLACE);

//Save workbook in PDF format while rendering comments in place

workbook.save("printinplace.pdf");

//Print the comments at the end of sheet

worksheet.getPageSetup().setPrintComments(com.aspose.cells.PrintCommentsType.PRINT_SHEET_END);

//Save workbook in PDF format while rendering comments at the end of worksheet

workbook.save("printsheetend.pdf");

{{< /highlight >}}

### **Lade till Workbook.isLicensed Property**
Aspose.Cells for Java 8.4.1 har avslöjat Workbook.isLicensed som kan vara till stor hjälp för att avgöra om licensen har laddats eller inte. Om du kommer åt den här egenskapen innan du ställer in licensen kommer den att returnera falskt och vice versa, dock bör licensen vara giltig.

Följande exempelkod visar användningen av egendomen Workbook.isLicensed.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object before setting a license

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook();

//Check if the license is loaded or not

if (!workbook.isLicensed())

{

	//Set license

	com.aspose.cells.License license = new com.aspose.cells.License();

	lic.SetLicense(licPath);

}

else

{

  //do process

}

{{< /highlight >}}

### **Lagt till egenskapen ImageOrPrintOptions.SVGFitToViewPort**
Aspose.Cells for Java 8.4.1 har exponerat egenskapen SVGFitToViewPort för klassen ImageOrPrintOptions som kan användas för att aktivera viewBox-attributet för SVG-filformatet medan kalkylblad eller diagram exporteras till SVG-format. Standardvärdet för den här egenskapen är falskt, därför kommer bas-XML för SVG-filen som genereras utan att ställa in ovannämnda egenskap inte att inkludera viewBox-attributet.

Följande exempelkod visar användningen av egenskapen ImageOrPrintOptions.SVGFitToViewPort.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object from source file

com.aspose.cells.Workbook workbook = new com.aspose.cells.Workbook(input);

//Access first worksheet

com.aspose.cells.Worksheet worksheet = workbook.getWorksheets().get(0);

//Create an instance of ImageOrPrintOptions

com.aspose.cells.ImageOrPrintOptions options = new com.aspose.cells.ImageOrPrintOptions();

//Set image format to SVG

options.setSaveFormat(com.aspose.cells.SaveFormat.SVG);

//Set the SVGFitToViewPort to true

options.setSVGFitToViewPort(true);

//Create an instance of SheetRender and initialize it with worksheet instance as well as object of ImageOrPrintOptions

com.aspose.cells.SheetRender renderer = new com.aspose.cells.SheetRender(worksheet, options);

renderer.toImage(0, "output.svg");

{{< /highlight >}}
## **Föråldrade API:er**
### **Method Workbook.validateFormula Obsoleted**
Använd egenskapen Cell.Formula för att validera formeln.
