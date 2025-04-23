---
title: Offentliga API ändringar i Aspose.Cells 8.3.2
type: docs
weight: 130
url: /sv/java/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.3.1 till 8.3.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser osv.](/cells/sv/java/offentliga-api-ändringar-i-aspose-cells-8-3-2/) och [borttagna klasser osv.](/cells/sv/java/offentliga-api-ändringar-i-aspose-cells-8-3-2/), utan även en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Mekanism för att ställa in absolut position för PivotItem**
För att tillhandahålla funktionen [PivotItem's absolut positionering](/cells/sv/java/ange-den-absoluta-positionen-för-pivot-item/), har Aspose.Cells for Java 8.3.2 exponerat en serie egenskaper och en metod enligt nedan.

- PivotItem.setPosition kan användas för att ställa in positionens index i alla PivotItems oavsett föräldernod.
- PivotItem.setPositionInSameParentNode kan användas för att ställa in positionens index i PivotItems under samma föräldernod.
- Metoden PivotItem.move(int count, bool isSameParent) kan användas för att flytta objektet uppåt eller nedåt baserat på count-värdet, där count är antalet positioner PivotItem ska flytta uppåt eller nedåt. Om count-värdet är mindre än noll flyttas objektet uppåt, medan om count-värdet är större än noll flyttas PivotItem nedåt. Booleskt typ isSameParent-parametern specificerar om flyttoperationen ska utföras i samma föräldernod eller inte.

{{% alert color="primary" %}} 

Observera att det är nödvändigt att anropa metoderna PivotTable.refreshData och PivotTable.calculateData innan du använder egenskaperna PivotItem.setPosition, PivotItem.setPositionInSameParentNode och metoden PivotItem.move(int count, bool isSameParent).

{{% /alert %}} 
### **Klass SignatureLine tillagd**
Aspose.Cells 8.3.2 ger stöd för Signature Line för att efterlikna MS Excels motsvarande funktion. Denna version har exponerat klassen SignatureLine och egenskapen Picture.SignatureLine för detta ändamål.

Följande exempelkod lägger till en signaturlinje med hjälp av egenskapen Picture.SignatureLine till arbetsboken.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.getWorksheets().get(0).getPictures().add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.getWorksheets().get(0).getPictures().get(index);

//Create signature line object

SignatureLine s = new SignatureLine();

s.setSigner("John Doe");

s.setTitle("Development Lead");

s.setEmail("john.doe@aspose.com");

//Assign the signature line object to Picture.SignatureLine property

pic.setSignatureLine(s);

{{< /highlight >}}
### **Tillagd Chart.hasAxis Metod**
Med utgivningen av v8.3.2 har Aspose.Cells API:er tillhandahållit metoden Chart.hasAxis(AxisType axisType, bool isPrimary) för att avgöra om diagrammet har en särskild axel eller inte.

Följande exempelkod visar användningen av metoden Chart.hasAxis för att avgöra om diagrammet har primär-, sekundär- och värdeaxlar.

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart

Chart chart = worksheet.getCharts().get(0);

//Determine which axis exists in chart

boolean ret = chart.hasAxis(AxisType.CATEGORY, true);

System.out.println("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.CATEGORY, false);

System.out.println("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, true);

System.out.println("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, false);

System.out.println("Has Seconary Value Axis: " + ret);

{{< /highlight >}}
### **Tillagd WorkbookSettings.checkWriteProtectedPassword Metod**
Metoden WorkbookSettings.checkWriteProtectedPassword gör det möjligt för utvecklare att kontrollera om ett angivet lösenord för att ändra kalkylarket är korrekt eller inte.

**Java**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Överlagringsmetoder WorkbookRender.toPrinter & SheetRender.toPrinter Tillagda**
Aspose.Cells 8.3.2 har tillhandahållit metoderna WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) och SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) för att skriva ut sidområdet för arbetsbok och kalkylblad.

Följande exempelkod illustrerar användningen av ovanstående metoder för att skriva ut sidorna 2-5 i arbetsboken och arbetsbladet.

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.toPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.toPrinter(printerName, 1, 4);

{{< /highlight >}}
### **Tillagd Worksheet.refreshPivotTables Metod**
Den nyligen tillagda metoden Worksheet.refreshPivotTables tillåter att uppdatera alla Pivot-tabeller i ett givet kalkylark med ett enda anrop.

**Java**

{{< highlight csharp >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Tillagd Workbook.getNamedStyle Metod**
Aspose.Cells 8.3.2 har exponerat metoden Workbook.getNamedStyle som accepterar en sträng som parameter och hämtar Style-objektet baserat på den angivna parametern.
### **Tillagd Cells.importTwoDimensionArray Metod**
Aspose.Cells API:er har gjort det möjligt att importera tvådimensionella matriser till kalkylarksceller genom att exponera metoden Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Sagda metod importerar en tvådimensionell matris av data till ett kalkylblad med mer flexibla alternativ definierade i TxtLoadOptions.
### **Tillagd egenskaper OnePagePerSheet, PageIndex och PageCount**
Aspose.Cells for Java 8.3.2 har exponerat egenskaperna OnePagePerSheet, PageIndex & PageCount för klassen XpsSaveOptions. Användaren kan få alla innehåll i en kalkylblad på en enda sida i XPS genom att använda egenskapen OnePagePerSheet och/eller hämta antalet sidor som ska skrivas ut med hjälp av egenskapen PageCount. Egenskapen PageIndex får/sätter indexet (baserat på 0) för den första sidan som ska sparas.
### **Tillagd egenskaper NumberDecimalSeparator och NumberGroupSeparator**
Aspose.Cells for Java 8.3.2 har introducerat egenskaperna NumberDecimalSeparator & NumberGroupSeparator som kan hämta/sätta anpassade separators som används för formatering & tolkning av numeriska värden i kalkylblad.

Följande exempelkod illustrerar hur man specificerar anpassade separatorer med Aspose.Cells API. Följande kod specificerar de anpassade decimal- och gruppseparatrarna som punkt och mellanslag, respektive.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Lade till egenskapen PdfSaveOptions.setFontSubstitutionCharGranularity**
Aspose.Cells for Java 8.3.2 har exponerat egenskapen PdfSaveOptions.setFontSubstitutionCharGranularity för att övervinna problemet där vissa Unicode-tecken inte kan visas med en specifik typsnittsfamilj. När egenskapen PdfSaveOptions.setFontSubstitutionCharGranularity är satt till sant kommer endast typsnittet för ett specifikt tecken som inte kan visas att ändras till ett visa typsnitt, resten av ordet eller meningen ska förbli i det ursprungliga typsnittet.

**Java**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **Borttagen API:er**
### **Borttagna föråldrade metoder**
Följande metoder har tagits bort från den offentliga API:n.

- Workbook.open & Workbook.save metoder.
- Workbook.setOleSize metod.
- Workbook.loadData metod.
- WorkbookDesigner.open & WorkbookDesigner.save metoder.
- WorksheetCollection.deleteName metod.
### **Borttagna föråldrade egenskaper**
Följande egenskaper har tagits bort från den offentliga API:n.

- Workbook.isProtected egenskap.
- Workbook.Language egenskap.
- Workbook.Region egenskap.
- WorkbookSettings.ReCalcOnOpen egenskap.
- WorkbookSettings.Language egenskap.
- WorkbookSettings.Encoding egenskap.
- WorkbookSettings.ConvertNumericData egenskap.
- WorksheetCollection.HidePivotFieldList egenskap.
- WorksheetCollection.EnableHTTPCompression egenskap.
- WorksheetCollection.isMinimized egenskap.
- WorksheetCollection.isHidden egenskap.
- WorksheetCollection.SheetTabBarWidth egenskap.
- WorksheetCollection.WindowLeft egenskap.
- WorksheetCollection.WindowLeftInch egenskap.
- WorksheetCollection.WindowLeftCM egenskap.
- WorksheetCollection.WindowTop egenskap.
- WorksheetCollection.WindowTopInch egenskap.
- WorksheetCollection.WindowTopCM egenskap.
- Egenskapen WorksheetCollection.WindowWidth.
- Egenskapen WorksheetCollection.WindowWidthInch.
- Egenskapen WorksheetCollection.WindowWidthCM.
- Egenskapen WorksheetCollection.WindowHeight.
- Egenskapen WorksheetCollection.WindowHeightInch.
- Egenskapen WorksheetCollection.WindowHeightCM.
- Egenskapen Worksheet.HPageBreaks.
- Egenskapen Worksheet.VPageBreaks.
- Egenskapen HtmlSaveOptions.DisplayHTMLCrossString.
- Egenskapen HtmlSaveOptions.ExportChartImageFormat.
- Egenskapen SaveOptions.ExpCellNameToXLSX.
- Egenskapen SaveOptions.DefaultFont.
- Egenskapen SaveOptions.Compliance.
- Egenskapen SaveOptions.PdfBookmark.
- Egenskapen SaveOptions.PdfImageCompression.
- Egenskapen TxtSaveOptions.AlwaysQuoted.
## **Obsoletterade API:er**
### **Föråldrad Workbook.saveOptions Egenskap**
En instans av SaveOptions måste skickas till Workbook.Save-metoden efter att ha ställt in lämpliga SaveOptions-egenskaper. 
### **Föråldrad Workbook.Styles & Klassen StyleCollection Egenskap**
Det rekommenderas att använda metoden Workbook.createStyle för att skapa och hantera stil för Workbook-instansen istället för att skapa en stil med metoden StyleCollection.add. Dessutom kan metoden Workbook.getNamedStyle(string) användas för att hämta namngiven stil istället för StyleCollection.get(string).
### **Föråldrad PivotItem.move(int count) Metod**
Med utgåvan av Aspose.Cells 8.3.2 har API:et introducerat en annan överbelastning av metoden PivotItem.move som accepterar det heltalsparametern för räkna och boolesk parameter för att flytta en PivotItem inom föräldernod. 
{{< app/cells/assistant language="java" >}}
