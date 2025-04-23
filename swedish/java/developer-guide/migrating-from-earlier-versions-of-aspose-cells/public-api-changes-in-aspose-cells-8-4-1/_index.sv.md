---
title: Offentliga API ändringar i Aspose.Cells 8.4.1
type: docs
weight: 150
url: /sv/java/public-api-changes-in-aspose-cells-8-4-1/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.4.0 till 8.4.1 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser etc.](/cells/sv/java/offentliga-api-ändringar-i-aspose-cells-8-4-1/) samt [borttagna klasser etc.](/cells/sv/java/offentliga-api-ändringar-i-aspose-cells-8-4-1/), men även en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Mekanism för att ändra databasanslutning**
Klassen com.aspose.cells.ExternalConnection innehöll redan metoden & egenskaperna som kunde användas för att inspektera databasanslutningsdetaljer som lagrats i en kalkylblad. De flesta egenskaper associerade med ExternalConnection-klassen var bara läsbara fram till utgivningen av Aspose.Cells for Java 8.4.1. Med denna utgåva har API:et gett stöd för att manipulera databasanslutningsinställningarna.

Följande kodsnutt visar hur man dynamiskt modifierar databasanslutningsinställningarna.

**Java**

{{< highlight csharp >}}

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

Här är några av de viktigaste egenskaper som exponeras av {ExternalConnection} -klassen.

|**Egenskapsnamn** |**Beskrivning** |
| :- | :- |
|BackgroundRefresh |Indikerar om anslutningen kan uppdateras i bakgrunden (asynkront). <br>true om föredragen användning av anslutningen är att uppdatera asynkront i bakgrunden; <br>false om föredragen användning av anslutningen är att uppdatera synkront i förgrunden. |
|ConnectionDescription |Specificerar användarbeskrivningen för denna anslutning |
|ConnectionId |Specificerar det unika identifieraren för denna anslutning. |
|Credentials |Specificerar autentiseringsmetoden som ska användas vid etablering (eller återetablering) av anslutningen. |
|IsDeleted |Indikerar om den associerade arbetsbokanslutningen har raderats. true om<br>anslutningen har raderats; annars false. |
|IsNew |True om anslutningen inte har uppdaterats första gången; annars false. Detta<br>läge kan inträffa när användaren sparar filen innan en förfrågan har avslutat returnerandet. |
|KeepAlive |True när kalkylbladsprogrammet ska anstränga sig för att hålla anslutningen<br>öppen. När false, ska programmet stänga anslutningen efter att informationen<br>har hämtats. |
|Name |Specificerar namnet på anslutningen. Varje anslutning måste ha ett unikt namn. |
|OdcFile |Specificerar den fullständiga sökvägen till extern anslutningsfil från vilken denna anslutning<br>skapades. Om en anslutning misslyckas under ett försök att uppdatera data, och reconnectionMethod=1,<br>ska kalkylbladsprogrammet försöka igen med information från den externa anslutningsfilen<br>istället för anslutningsobjektet inbäddat i arbetsboken. |
|OnlyUseConnectionFile |Indikerar om kalkylbladsprogrammet alltid och endast ska använda anslutningsinformationen i den externa anslutningsfilen som indikeras av odcFile-attributet<br>när anslutningen uppdateras. Om false, ska kalkylbladsprogrammet<br>följa proceduren som indikeras av reconnectionMethod-attributet |
|Parameters |Få ConnectionParameterCollection för en ODBC- eller webbfråga. |
|ReConnectionMethod |Specificera reconnectionMethod-typ |
|RefreshInternal|Specificerar antalet minuter mellan automatiska uppdateringar av anslutningen. |
|RefreshOnLoad |True om denna anslutning ska uppdateras när filen öppnas; annars false. |
|SaveData |True om de externa data hämtade via anslutningen för att fylla på en tabell ska sparas<br>med arbetsboken; annars false. |
|SavePassword |True om lösenordet ska sparas som en del av anslutningssträngen; annars False. |
|SourceFile |Används när datakällan är filbaserad. När en anslutning till en sådan datakälla misslyckas, försöker kalkylbladsprogrammet att ansluta direkt till denna fil. Kan anges i URI eller systemspecifik filsökväg. |
|SSOId|Identifierare för Single Sign On (SSO) används för autentisering mellan en mellanliggande<br>kalkylbladsserver och den externa datakällan. |
|Type |Specificerar datatyp för datakällan. |

### **Förmåga att formatera delsträng av datamärken. |**
Aspose.Cells for Java 8.4.1 har exponerat DataLabels.characters-metoden för att hämta en instans av FontSetting-klassen som motsvarar delsträngen av en ChartPoints.DataLabels. I sin tur kan instansen av FontSetting-klassen användas för att formatera delsträngen av DataLabels med olika typsnittsinställningar och färg.

Följande kodsnutt visar hur man använder DataLabels.characters-metoden.

**Java**

{{< highlight csharp >}}

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

### **Förmåga att ställa in önskade bildmått för kalkylblad & diagramexport.**
Aspose.Cells for Java 8.4.1 har exponerat ImageOrPrintOptions.setDesiredSize-metoden för att ställa in dimensionerna för den resulterande bilden vid export av kalkylblad & diagram till bilder. ImageOrPrintOptions.setDesiredSize-metoden accepterar två heltalsparametrar, där den första är önskad bredd och den andra är önskad höjd.

Följande kodsnutt visar hur man ställer in önskade dimensioner vid export av kalkylblad till PNG.

**Java**

{{< highlight csharp >}}

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

### **Rendera kommentarer till PDF**
Med utgåvan av v8.4.1 har Aspose.Cells API tillhandahållit egenskapen PageSetup.PrintComments och PrintCommentsType-uppräkningen för att underlätta renderingen av kommentarer vid konvertering av kalkylblad till PDF-format. PrintCommentsType-uppräkningen har följande konstanter. 

- PrintCommentsType.PRINT_NO_COMMENTS: Kommentarer ska inte renderas.
- PrintCommentsType.PRINT_IN_PLACE: Kommentarer ska renderas där de är placerade.
- PrintCommentsType.PRINT_SHEET_END: Kommentarer ska renderas i slutet av kalkylbladet.

Följande exempelkod demonstrerar användningen av PageSetup.PrintComments-egenskapen för att rendera kommentarer med alla möjliga värden för PrintCommentsType-uppräkningen.

**Java**

{{< highlight csharp >}}

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

### **Tillagd Workbook.isLicensed Egenskap**
Aspose.Cells for Java 8.4.1 har exponerat Workbook.isLicensed som kan vara till stor hjälp för att avgöra om licensen har laddats framgångsrikt eller inte. Om du får tillgång till denna egenskap innan du har ställt in licensen kommer den att returnera falskt och vice versa. Dock bör licensen vara giltig.

Följande exempelkod demonstrerar användningen av Workbook.isLicensed-egenskapen.

**Java**

{{< highlight csharp >}}

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

### **Tillagd ImageOrPrintOptions.SVGFitToViewPort-egenskap**
Aspose.Cells for Java 8.4.1 har exponerat SVGFitToViewPort-egenskapen för ImageOrPrintOptions-klassen som kan användas för att slå på viewBox-attributet för SVG-filformatet vid export av kalkylblad eller diagram till SVG-formatet. Standardvärdet för denna egenskap är falskt, därav kommer den genererade bas-XML för SVG-filen utan att ställa in nämnda egenskap inte inkludera viewBox-attributen.

Följande exempelkod demonstrerar användningen av ImageOrPrintOptions.SVGFitToViewPort-egenskapen.

**Java**

{{< highlight csharp >}}

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
## **Obsoletterade API:er**
### **Föråldrat Workbook.validateFormula-metod**
Använd Cell.Formula-egenskapen för att validera formeln.
{{< app/cells/assistant language="java" >}}
