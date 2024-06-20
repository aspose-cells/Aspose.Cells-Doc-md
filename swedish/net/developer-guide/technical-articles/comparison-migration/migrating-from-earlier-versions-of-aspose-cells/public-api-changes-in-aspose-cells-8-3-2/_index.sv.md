---
title: Offentliga API ändringar i Aspose.Cells 8.3.2
type: docs
weight: 120
url: /sv/net/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.3.1 till 8.3.2 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-3-2/) och [borttagna klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-3-2/), utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Mekanism för att ställa in absolut position för PivotItem**
För att tillhandahålla funktionen [PivotItem's Absolute Positioning](/cells/sv/net/specifying-the-absolute-position-of-the-pivot-item/), har Aspose.Cells for .NET 8.3.2 exponerat en serie egenskaper och hjälpmetoder som listas nedan.

- Egenskapen PivotItem.Position kan användas för att specificera positionen index i alla PivotItems oavsett förälder.
- Egenskapen PivotItem.PositionInSameParentNode kan användas för att specificera positionen index i PivotItems under samma föräldernod.
- Metoden PivotItem.Move(int count, bool isSameParent) kan användas för att flytta objektet upp eller ner baserat på värdet av count, där count är antalet positioner att flytta PivotItem upp eller ner. Om count-värdet är mindre än noll kommer objektet att flyttas upp, medan om count-värdet är större än noll kommer PivotItem att flyttas ner. Den Booleska typen isSameParent specificerar om flyttoperationen ska utföras i samma föräldernod eller inte.

{{% alert color="primary" %}} 

Observera att det är nödvändigt att anropa metoderna PivotTable.RefreshData och PivotTable.CalculateData innan du använder egenskaperna PivotItem.Position, PivotItem.PositionInSameParentNode och PivotItem.Move(int count, bool isSameParent).

{{% /alert %}} 
### **Klass SignatureLine tillagd**
Aspose.Cells for .NET 8.3.2 ger stöd för Signature Line för att härma MS Excel:s motsvarande funktion. Denna version av Aspose.Cells for .NET har exponerat klassen SignatureLine och egenskapen Picture.SignatureLine för detta ändamål.

Följande exempelkod lägger till en signaturlinje med hjälp av egenskapen Picture.SignatureLine till arbetsboken.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.Worksheets[0].Pictures.Add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.Worksheets[0].Pictures[index];

//Create signature line object

SignatureLine s = new SignatureLine();

s.Signer = "John Doe";

s.Title = "Development Lead";

s.Email = "john.doe@aspose.com";

//Assign the signature line object to Picture.SignatureLine property

pic.SignatureLine = s;

{{< /highlight >}}


### **Tillagd metod Chart.HasAxis**
Med utgåvan av v8.3.2 har Aspose.Cells API tillhandahållit metoden Chart.HasAxis(AxisType axisType, bool isPrimary) för att avgöra om diagrammet har en särskild axel eller inte.

Följande exempelkod visar användningen av metoden Chart.HasAxis för att avgöra om det angivna diagrammet har primär-, sekundär- och värdeaxel.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart

Chart chart = worksheet.Charts[0];

//Determine which axis exists in chart

bool ret = chart.HasAxis(AxisType.Category, true);

Console.WriteLine("Has Primary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Category, false);

Console.WriteLine("Has Secondary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, true);

Console.WriteLine("Has Primary Value Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, false);

Console.WriteLine("Has Secondary Value Axis: " + ret);

{{< /highlight >}}


### **Tillagd metod WorkbookSettings.CheckWriteProtectedPassword**
Metoden WorkbookSettings.CheckWriteProtectedPassword möjliggör för utvecklare att kontrollera om ett angivet lösenord för att ändra kalkylbladet är korrekt eller inte.

**C#**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **Överbelastningsmetoder WorkbookRender.ToPrinter och SheetRender.ToPrinter tillagda**
Aspose.Cells for .NET 8.3.2 har tillhandahållit metoderna WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) och SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) för att skriva ut sidområdet i arbetsbok och arbetsblad, respektive.

Följande exempelkod illustrerar användningen av ovanstående metoder för att skriva ut sidorna 2-5 i arbetsboken och arbetsbladet.

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.ToPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.ToPrinter(printerName, 1, 4);

{{< /highlight >}}


### **Tillagd metod Worksheet.RefreshPivotTables**
Den nytt tillagda metoden Worksheet.RefreshPivotTables gör det möjligt att uppdatera alla pivot-tabeller i en given kalkylblad med ett enda anrop.

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Tillagd metod Workbook.GetNamedStyle**
Aspose.Cells for .NET API har exponerat metoden Workbook.GetNamedStyle som accepterar en sträng som parameter och hämtar Style-objektet baserat på den passerade parametern.
### **Tillagd metod Cells.ImportTwoDimensionArray**
Aspose.Cells for .NET API har gjort det möjligt att importera tvådimensionella arrayer till kalkylbladsceller genom att exponera metoden Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions). Sagda metod importerar en tvådimensionell array av data till ett arbetsblad med mer flexibla alternativ som definierats i TxtLoadOptions.
### **Tillagd egenskaper OnePagePerSheet, PageIndex och PageCount**
Aspose.Cells for .NET 8.3.2 har exponerat egenskaperna OnePagePerSheet, PageIndex och PageCount för klassen XpsSaveOptions. Användaren kan anpassa allt innehåll i ett kalkylark på en enda sida av XPS med hjälp av egenskapen OnePagePerSheet och/eller hämta antalet sidor som ska skrivas ut med egenskapen PageCount. Egenskapen PageIndex får/inställer den nollbaserade index för den första sidan som ska sparas.
### **Tillagd egenskaper NumberDecimalSeparator och NumberGroupSeparator**
Aspose.Cells for .NET 8.3.2 har introducerat egenskaperna NumberDecimalSeparator och NumberGroupSeparator som kan få/inställa anpassade separatorer som används för formatering och tolkning av numeriska värden i kalkylblad.

Följande exempelkod illustrerar hur man specificerar anpassade separatorer med Aspose.Cells API. Följande kod specificerar anpassade decimal- och grup separatorer som punkt och mellanslag.

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Tillagd PdfSaveOptions.IsFontSubstitutionCharGranularity Egenskap**
Aspose.Cells for .NET 8.3.2 har exponerat PdfSaveOptions.IsFontSubstitutionCharGranularity egenskapen för att komma över problemet där vissa Unicode-tecken inte kan visas med en specifik teckensnittsfamilj. När PdfSaveOptions.IsFontSubstitutionCharGranularity egenskapen är satt till true kommer endast teckensnittet för ett specifikt tecken som inte kan visas att ändras till ett visbart teckensnitt och resten av ordet eller meningen ska förbli i det ursprungliga teckensnittet.

**C#**

{{< highlight csharp >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **Borttagen API:er**
### **Borttagna föråldrade metoder**
Följande metoder har tagits bort från den offentliga API:n.

- Workbook.Open & Workbook.Save metoder.
- Workbook.SetOleSize metod.
- Workbook.LoadData metod.
- WorkbookDesigner.Open & WorkbookDesigner.Save metoder.
- WorksheetCollection.DeleteName metod.
### **Borttagna föråldrade egenskaper**
Följande egenskaper har tagits bort från den offentliga API:n.

- Workbook.IsProtected egenskap.
- Workbook.Language egenskap.
- Workbook.Region egenskap.
- WorkbookSettings.ReCalcOnOpen egenskap.
- WorkbookSettings.Language egenskap.
- WorkbookSettings.Encoding egenskap.
- WorkbookSettings.ConvertNumericData egenskap.
- WorksheetCollection.HidePivotFieldList egenskap.
- WorksheetCollection.EnableHTTPCompression egenskap.
- WorksheetCollection.IsMinimized egenskap.
- WorksheetCollection.IsHidden egenskap.
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
### **Obsoletterad Workbook.SaveOptions-egenskap**
En instans av SaveOptions måste skickas till Workbook.Save-metoden efter att ha ställt in lämpliga SaveOptions-egenskaper.
### **Obsoletterad Workbook.Styles Property & Class StyleCollection**
Det rekommenderas att använda Workbook.CreateStyle-metoden för att skapa och manipulera stil för Workbook-instansen istället för att skapa en stil med StyleCollection.Add-metoden. Dessutom kan Workbook.GetNamedStyle(string)-metoden användas för att hämta namngiven stil istället för StyleCollection[string].
### **Obsoletterad PivotItem.Move(int count) Method**
Med utgivningen av Aspose.Cells 8.3.2 har API:n introducerat en annan överbelastning av PivotItem.Move-metoden som accepterar heltalsparametern för räkna och booleska parametern för att flytta en PivotItem inom föräldernoden.
