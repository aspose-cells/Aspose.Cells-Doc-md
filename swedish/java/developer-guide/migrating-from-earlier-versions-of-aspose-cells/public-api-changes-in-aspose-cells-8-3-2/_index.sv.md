---
title: Offentliga API-ändringar i Aspose.Cells 8.3.2
type: docs
weight: 130
url: /sv/java/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.3.1 till 8.3.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-3-2/) och[borttagna klasser osv.](/cells/sv/java/public-api-changes-in-aspose-cells-8-3-2/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Mekanism för att ställa in absolut position för PivotItem**
 För att tillhandahålla funktionen[PivotItems absoluta positionering](/cells/sv/java/specifying-the-absolute-position-of-the-pivot-item/), Aspose.Cells för Java 8.3.2 har avslöjat en serie egenskaper och en metod enligt listan nedan.

- PivotItem.setPosition kan användas för att ställa in positionsindex i alla PivotItems oavsett föräldernod.
- PivotItem.setPositionInSameParentNode kan användas för att ställa in positionsindex i PivotItems under samma överordnade nod.
- Metoden PivotItem.move(int count, bool isSameParent) kan användas för att flytta objektet uppåt eller nedåt baserat på count-värdet, där count är antalet positioner för att flytta PivotItem uppåt eller nedåt. Om räknevärdet är mindre än noll, kommer objektet att flyttas uppåt, där som om räknevärdet är större än noll, kommer PivotItem att flyttas nedåt, boolesk typ isSameParent parametern anger om flyttoperationen måste utföras i samma överordnade nod eller inte.

{{% alert color="primary" %}} 

Observera att det är nödvändigt att anropa metoderna PivotTable.refreshData och PivotTable.calculateData innan du använder metoderna PivotItem.setPosition, PivotItem.setPositionInSameParentNode och PivotItem.move(int count, bool isSameParent).

{{% /alert %}} 
### **Class SignatureLine tillagd**
Aspose.Cells 8.3.2 ger stöd för signaturlinjen för att efterlikna MS Excels motsvarande funktion. Den här versionen har exponerat klassen SignatureLine och egenskapen Picture.SignatureLine för detta ändamål.

Följande exempelkod lägger till en signaturrad med egenskapen Picture.SignatureLine till arbetsboken.

**Java**

{{< highlight "csharp" >}}

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
### **Metoddiagram.hasAxis tillagd**
Med lanseringen av v8.3.2 har API:et Aspose.Cells tillhandahållit metoden Chart.hasAxis(AxisType axisType, bool isPrimary) för att avgöra om diagrammet har en viss axel eller inte.

Följande exempelkod visar användningen av metoden Chart.hasAxis för att avgöra om exempeldiagrammet har primär-, sekundär- och värdeaxel.

**Java**

{{< highlight "csharp" >}}

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
### **Metod WorkbookSettings.checkWriteProtectedPassword har lagts till**
Metod WorkbookSettings.checkWriteProtectedPassword gör det möjligt för utvecklarna att kontrollera om ett givet lösenord för att ändra kalkylarket är korrekt eller inte.

**Java**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Överbelastningsmetoder WorkbookRender.toPrinter & SheetRender.toPrinter har lagts till**
Aspose.Cells 8.3.2 har tillhandahållit metoderna WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) och SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) för att skriva ut sidorna i arbetsboken respektive kalkylbladet.

Följande exempelkod illustrerar användningen av ovannämnda metoder för att skriva ut sidorna 2-5 i arbetsboken och arbetsbladet.

**Java**

{{< highlight "csharp" >}}

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
### **Metod Worksheet.refreshPivotTables tillagd**
Den nya metoden Worksheet.refreshPivotTables gör det möjligt att uppdatera alla pivottabeller i ett visst kalkylblad i ett enda anrop.

**Java**

{{< highlight "csharp" >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Metod Workbook.getNamedStyle tillagd**
Aspose.Cells 8.3.2 har exponerat metoden Workbook.getNamedStyle som accepterar strängen som parameter och hämtar Style-objektet baserat på parametern som skickas.
### **Metod Cells.importTwoDimensionArray har lagts till**
Aspose.Cells API har gjort det möjligt att importera tvådimensionella arrayer till kalkylbladsceller genom att exponera metoden Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Den nämnda metoden importerar en tvådimensionell array av data till ett kalkylblad med mer flexibla alternativ definierade i TxtLoadOptions.
### **Egenskaper OnePagePerSheet, PageIndex & PageCount har lagts till**
Aspose.Cells för Java 8.3.2 har exponerat egenskaperna OnePagePerSheet, PageIndex och PageCount för klassen XpsSaveOptions. Användaren kan anpassa allt innehåll i ett kalkylblad på en enda sida i XPS med hjälp av egenskapen OnePagePerSheet och/eller hämta antalet sidor som ska skrivas ut med egenskapen PageCount. Egenskapen PageIndex hämtar/ställer in det 0-baserade indexet för den första sidan som ska sparas.
### **Egenskaper NumberDecimalSeparator & NumberGroupSeparator tillagd**
Aspose.Cells för Java 8.3.2 har introducerat NumberDecimalSeparator & NumberGroupSeparator-egenskaper som kan hämta/ställa in anpassade separatorer som används för att formatera och analysera de numeriska värdena i kalkylblad.

Följande exempelkod illustrerar hur du anger anpassade separatorer med Aspose.Cells API. Följande kod specificerar de anpassade decimal- och gruppseparatorerna som punkt respektive mellanslag.

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **Egenskapen PdfSaveOptions.setFontSubstitutionCharGranularity har lagts till**
Aspose.Cells för Java 8.3.2 har avslöjat egenskapen PdfSaveOptions.setFontSubstitutionCharGranularity för att lösa problemet där vissa Unicode-tecken inte kan visas med en specifik teckensnittsfamilj. När egenskapen PdfSaveOptions.setFontSubstitutionCharGranularity är inställd på true ändras endast teckensnittet med ett specifikt tecken som inte är visningsbart till visningsbart teckensnitt och resten av ordet eller meningen ska förbli i det ursprungliga teckensnittet.

**Java**

{{< highlight "csharp" >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **Borttagna API:er**
### **Tog bort föråldrade metoder**
Följande metoder har tagits bort från Public API.

- Workbook.open & Workbook.save metoder.
- Workbook.setOleSize-metoden.
- Workbook.loadData-metoden.
- WorkbookDesigner.open & WorkbookDesigner.save metoder.
- Metoden WorksheetCollection.deleteName.
### **Borttagen föråldrade egenskaper**
Följande egenskaper har tagits bort från Public API.

- Workbook.isProtected egenskap.
- Arbetsbok.Språkegenskap.
- Arbetsbok.Regionsegendom.
- Egenskapen WorkbookSettings.ReCalcOnOpen.
- WorkbookSettings.Language-egenskap.
- WorkbookSettings.Encoding-egenskap.
- Egenskapen WorkbookSettings.ConvertNumericData.
- Egenskapen WorksheetCollection.HidePivotFieldList.
- Egenskapen WorksheetCollection.EnableHTTPCompression.
- WorksheetCollection.isMinimerad egenskap.
- WorksheetCollection.isDold egenskap.
- Egenskapen WorksheetCollection.SheetTabBarWidth.
- Egenskapen WorksheetCollection.WindowLeft.
- Egenskapen WorksheetCollection.WindowLeftInch.
- Egenskapen WorksheetCollection.WindowLeftCM.
- Egenskapen WorksheetCollection.WindowTop.
- Egenskapen WorksheetCollection.WindowTopInch.
- Egenskapen WorksheetCollection.WindowTopCM.
- Egenskapen WorksheetCollection.WindowWidth.
- Egenskapen WorksheetCollection.WindowWidthInch.
- Egenskapen WorksheetCollection.WindowWidthCM.
- Egenskapen WorksheetCollection.WindowHeight.
- Egenskapen WorksheetCollection.WindowHeightInch.
- Egenskapen WorksheetCollection.WindowHeightCM.
- Egenskapen Worksheet.HPageBreaks.
- Egenskapen Worksheet.VPageBreaks.
- HtmlSaveOptions.DisplayHTMLCrossString-egenskap.
- HtmlSaveOptions.ExportChartImageFormat-egenskapen.
- Egenskapen SaveOptions.ExpCellNameToXLSX.
- Egenskapen SaveOptions.DefaultFont.
- Egenskapen SaveOptions.Compliance.
- SaveOptions.PdfBookmark-egenskap.
- Egenskapen SaveOptions.PdfImageCompression.
- TxtSaveOptions.AlwaysQuoted egenskap.
## **Föråldrade API:er**
### **Egenskapsarbetsbok.sparaalternativ Föråldrad**
 Ett objekt med SaveOptions måste skickas till Workbook.Save-metoden efter att ha ställt in korrekta SaveOptions-egenskaper.
### **Fastighetsarbetsbok. Stilar & Klassstilsamling Föråldrad**
Det rekommenderas att använda metoden Workbook.createStyle för att skapa och manipulera stil för Workbook-instansen istället för att skapa en Style med metoden StyleCollection.add. Dessutom kan Workbook.getNamedStyle(string)-metoden användas för att få namngiven stil istället för StyleCollection.get(string).
### **Metod PivotItem.move(int count) Föråldrad**
 Med lanseringen av Aspose.Cells 8.3.2 har API:et infört ytterligare en överbelastning av metoden PivotItem.move som accepterar heltalsparametern för count och boolesk parameter för att flytta en PivotItem inom den överordnade noden.
