---
title: Offentlig API Ändringar i Aspose.Cells 8.3.2
type: docs
weight: 120
url: /sv/net/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.3.1 till 8.3.2 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-3-2/) och[borttagna klasser osv.](/cells/sv/net/public-api-changes-in-aspose-cells-8-3-2/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Mekanism för att ställa in absolut position för PivotItem**
 För att tillhandahålla funktionen[PivotItems absoluta positionering](/cells/sv/net/specifying-the-absolute-position-of-the-pivot-item/)Aspose.Cells for .NET 8.3.2 har avslöjat en rad egenskaper och hjälpmetoder enligt listan nedan.

- Egenskapen PivotItem.Position kan användas för att ange positionsindex i alla PivotItems oavsett överordnad nod.
- PivotItem.PositionInSameParentNode-egenskapen kan användas för att ange positionsindex i PivotItems under samma överordnade nod.
- PivotItem.Move(int count, bool isSameParent)-metoden kan användas för att flytta objektet uppåt eller nedåt baserat på count-värdet, där count är antalet positioner för att flytta PivotItem uppåt eller nedåt. Om räknevärdet är mindre än noll, kommer objektet att flyttas uppåt, där som om räknevärdet är större än noll, kommer PivotItem att flyttas nedåt, boolesk typ isSameParent parametern anger om flyttoperationen måste utföras i samma överordnade nod eller inte.

{{% alert color="primary" %}} 

Observera att det är nödvändigt att anropa metoderna PivotTable.RefreshData och PivotTable.CalculateData innan du använder metoderna PivotItem.Position, PivotItem.PositionInSameParentNode och PivotItem.Move(int count, bool isSameParent).

{{% /alert %}} 
### **Class SignatureLine tillagd**
Aspose.Cells for .NET 8.3.2 ger stöd för signaturlinjen för att efterlikna MS Excels motsvarande funktion. Den här versionen av Aspose.Cells for .NET har exponerat klassen SignatureLine och egenskapen Picture.SignatureLine för detta ändamål.

Följande exempelkod lägger till en signaturrad med egenskapen Picture.SignatureLine till arbetsboken.

**C#**

{{< highlight "csharp" >}}

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


### **Metoddiagram.HasAxis tillagd**
Med lanseringen av v8.3.2 har Aspose.Cells API tillhandahållit metoden Chart.HasAxis(AxisType axisType, bool isPrimary) för att avgöra om diagrammet har en viss axel eller inte.

Följande exempelkod visar användningen av metoden Chart.HasAxis för att avgöra om exempeldiagrammet har primär-, sekundär- och värdeaxel.

**C#**

{{< highlight "csharp" >}}

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


### **Method WorkbookSettings.CheckWriteProtectedPassword har lagts till**
Metod WorkbookSettings.CheckWriteProtectedPassword gör det möjligt för utvecklarna att kontrollera om ett givet lösenord för att ändra kalkylarket är korrekt eller inte.

**C#**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **Överbelastningsmetoder WorkbookRender.ToPrinter & SheetRender.ToPrinter har lagts till**
Aspose.Cells for .NET 8.3.2 har tillhandahållit arbetsboken WorkbookRender.ToPrinter(sträng PrinterName, int PrintPageIndex, int PrintPageCount) och SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageIndex, int PrintPageCount) arbetsblad för att skriva ut arbetsboken respektive.

Följande exempelkod illustrerar användningen av ovannämnda metoder för att skriva ut sidorna 2-5 i arbetsboken och arbetsbladet.

**C#**

{{< highlight "csharp" >}}

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


### **Metod Worksheet.RefreshPivotTables tillagda**
Den nya metoden Worksheet.RefreshPivotTables gör det möjligt att uppdatera alla pivottabeller i ett visst kalkylblad i ett enda anrop.

**C#**

{{< highlight "csharp" >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Metod Workbook.GetNamedStyle tillagd**
Aspose.Cells for .NET API har avslöjat metoden Workbook.GetNamedStyle som accepterar strängen som parameter och hämtar Style-objektet baserat på parametern som skickas.
### **Metod Cells.ImportTwoDimensionArray har lagts till**
Aspose.Cells for .NET API har gjort det möjligt att importera tvådimensionella arrayer till kalkylbladsceller genom att exponera metoden Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions)-metoden Den nämnda metoden importerar en tvådimensionell array av data till ett kalkylblad med mer flexibla alternativ definierade i TxtLoadOptions.
### **Egenskaper OnePagePerSheet, PageIndex & PageCount har lagts till**
Aspose.Cells for .NET 8.3.2 har exponerat egenskaperna OnePagePerSheet, PageIndex och PageCount för klassen XpsSaveOptions. Användaren kan anpassa allt innehåll i ett kalkylblad på en enda sida i XPS med hjälp av egenskapen OnePagePerSheet och/eller hämta antalet sidor som ska skrivas ut med egenskapen PageCount. Egenskapen PageIndex hämtar/ställer in det 0-baserade indexet för den första sidan som ska sparas.
### **Egenskaper NumberDecimalSeparator & NumberGroupSeparator tillagd**
Aspose.Cells for .NET 8.3.2 har introducerat NumberDecimalSeparator & NumberGroupSeparator-egenskaper som kan hämta/ställa in de anpassade separatorer som används för att formatera och analysera de numeriska värdena i kalkylblad.

Följande exempelkod illustrerar hur du anger anpassade avgränsare med Aspose.Cells API. Följande kod anger anpassade decimal- och gruppavgränsare som punkt respektive mellanslag.

**C#**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **Egenskapen PdfSaveOptions.IsFontSubstitutionCharGranularity har lagts till**
Aspose.Cells for .NET 8.3.2 har avslöjat egenskapen PdfSaveOptions.IsFontSubstitutionCharGranularity för att lösa problemet där vissa Unicode-tecken inte kan visas med en specifik teckensnittsfamilj. När egenskapen PdfSaveOptions.IsFontSubstitutionCharGranularity är inställd på true ändras endast teckensnittet med ett specifikt tecken som inte är visningsbart till visningsbart teckensnitt och resten av ordet eller meningen ska förbli i det ursprungliga teckensnittet.

**C#**

{{< highlight "csharp" >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **Borttagna API:er**
### **Tog bort föråldrade metoder**
Följande metoder har tagits bort från allmänheten API.

- Arbetsbok.Öppna & Arbetsbok.Spara metoder.
- Workbook.SetOleSize-metoden.
- Arbetsbok.LoadData-metod.
- WorkbookDesigner.Open & WorkbookDesigner.Spara metoder.
- Metoden WorksheetCollection.DeleteName.
### **Borttagen föråldrade egenskaper**
Följande fastigheter har tagits bort från allmänheten API.

- Workbook.IsProtected-egenskap.
- Arbetsbok.Språkegenskap.
- Arbetsbok.Regionsegendom.
- Egenskapen WorkbookSettings.ReCalcOnOpen.
- WorkbookSettings.Language-egenskap.
- WorkbookSettings.Encoding-egenskap.
- Egenskapen WorkbookSettings.ConvertNumericData.
- Egenskapen WorksheetCollection.HidePivotFieldList.
- Egenskapen WorksheetCollection.EnableHTTPCompression.
- WorksheetCollection.IsMinimized property.
- Egenskapen WorksheetCollection.IsHidden.
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
### **Egendomsarbetsbok.SaveOptions föråldrat**
Ett objekt med SaveOptions måste skickas till Workbook.Save-metoden efter att ha ställt in korrekta SaveOptions-egenskaper.
### **Fastighetsarbetsbok. Stilar & Klassstilsamling Föråldrad**
Det rekommenderas att använda metoden Workbook.CreateStyle för att skapa och manipulera stil för Workbook-instanser istället för att skapa en Style med metoden StyleCollection.Add. Dessutom kan metoden Workbook.GetNamedStyle(sträng) användas för att få namngiven stil istället för StyleCollection[sträng].
### **Metod PivotItem.Move(int count) Föråldrad**
Med lanseringen av Aspose.Cells 8.3.2 har API introducerat ytterligare en överbelastning av metoden PivotItem.Move som accepterar heltalsparametern för count och boolean parameter för att flytta en PivotItem inom den överordnade noden.
