---
title: Offentliga API ändringar i Aspose.Cells 8.5.0
type: docs
weight: 160
url: /sv/net/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.4.2 till 8.5.0 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-5-0/), men också en beskrivning av eventuella ändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Ändrade ICustomFunction.CalculateCustomFunction-parametrar**
Om en parameter för den anpassade funktionen är en cellreferens användes i äldre versioner Aspose.Cells API för att konvertera cellreferensen till ett cellvärde eller en objektarray av alla cellvärden i det angivna området. Men för många funktioner och användare är inte cellvärdesarrayen för alla celler i det angivna området nödvändig, de behöver bara en enskild cell som motsvarar formelns position, eller bara behöver själva referensen istället för cellvärdet eller värdearrayen. För vissa situationer ökade det till och med risken för cirkulär referensfel.

För att stödja sådana krav har Aspose.Cells for .NET 8.5.0 ändrat parametervärdet till "paramsList" för hänvisade områden. Sedan v8.5.0 placerar API:et bara ReferredArea-objektet i "paramsList" när den motsvarande parametern är en hänvisning eller dess beräknade resultat är en hänvisning. Om du behöver hänvisningen själv kan du använda ReferredArea direkt. Om du behöver hämta en singelcellvärde från hänvisningen som motsvarar formelns position, kan du använda metoden ReferredArea.GetValue(rowOffset, int colOffset). Om du behöver cellvärden array för hela området, kan du använda metoden ReferredArea.GetValues.

Nu när Aspose.Cells for .NET 8.5.0 ger ReferredArea i "paramsList" kommer inte längre ReferredAreaCollection i "contextObjects" att behövas (i gamla versioner kunde den inte alltid ge en-till-en-mappning till parametrarna för den anpassade funktionen), så har detta släpp också tagit bort den från "contextObjects" nu.

Denna förändring kräver lite justeringar av kodimplementationen för ICustomFunction när du behöver värdet/värdena för referensparametern.

**Gammal implementation**

{{< highlight csharp >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}

**Ny implementation**

{{< highlight csharp >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}


### **Klassen CalculationOptions tillagd**
Aspose.Cells for .NET 8.5.0 har exponerat klassen CalculationOptions för att lägga till mer flexibilitet och utbyggnad för formelberäkningssmotorn. Den nytt tillagda klassen har följande egenskaper.

1. CalculationOptions.CalcStackSize: Specificerar stackstorleken för att beräkna celler rekursivt. -1 anger att beräkningen kommer att använda WorkbookSettings.CalcStackSize för motsvarande arbetsbok.
1. CalculationOptions.CustomFunction: Utökar formelberäkningsmotorn med anpassad formel.
1. CalculationOptions.IgnoreError: Booleskt värde som indikerar om fel ska döljas vid beräkning av formler, där felen kan bero på otillåten funktion, extern länk eller mer.
1. CalculationOptions.PrecisionStrategy: Värdet CalculationPrecisionStrategy som specifierar strategin för att hantera beräkningsprecisionen.
### **Enumeration CalculationPrecisionStrategy tillagd**
Aspose.Cells for .NET 8.5.0 har exponerat variationen CalculationPrecisionStrategy för att lägga till mer flexibilitet för formelberäkningssmotorn för att få önskade resultat. Denna variation strategieres precisionhantering. På grund av precisionens problem med IEEE 754 Floating-Point Arithmetic kan vissa till synes enkla formler inte beräknas för att ge de förväntade resultaten. Därför har den senaste API-versionen exponerat följande fält för att få önskade resultat enligt valet.

1. CalculationPrecisionStrategy.Decimal: Använder decimal som operand när det är möjligt, och är mest ineffektivt med avseende på prestandaöverväganden.
1. CalculationPrecisionStrategy.Round: Avrundar beräkningsresultaten enligt signifikant siffra.
1. CalculationPrecisionStrategy.None: Ingen strategi tillämpas därför används under beräkningen det ursprungliga dubbla värdet som operand och returnerar resultatet direkt. Detta alternativ är mest effektivt och är tillämpligt för de flesta fall.
### **Metoder tillagda för att använda CalculationOptions**
Med släppet av v8.5.0 har Aspose.Cells API lagt till överbelastningsversioner av metoden CalculateFormula som listas nedan.

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(CalculationOptions options, bool recursive)
- Cell.Calculate(CalculationOptions)
### **Fält PasteType.RowHeights tillagt**
Aspose.Cells API har tillhandahållit fältet PasteType.RowHeights variationsstrategi för att kopiera radhöjderna vid kopiering av områden. Genom att ange PasteOptions.PasteType-egenskapen till ((PasteType.RowHeights})) kommer höjderna för alla rader inne i källområdet att kopieras till destinationsområdet.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.Worksheets[0];

//Add destination worksheet

Worksheet dstSheet = workbook.Worksheets.Add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.Cells.SetRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.Cells.CreateRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.Cells.CreateRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.PasteType = PasteType.RowHeights;

//Copy source range to destination range with paste options

dstRange.Copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.Cells["D4"].PutValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.Save("output.xlsx", SaveFormat.Xlsx);

{{< /highlight >}}


### **Tillagd SheetRender.PageScale-egenskap**
När du ställer in sidlayoutskalning med hjälp av **Skala till n sidor i bredd och m i höjd** alternativet, beräknar Microsoft Excel skalningsfaktorn för sidlayouten. Samma kan uppnås med hjälp av egenskapen SheetRender.PageScale exponerad av Aspose.Cells for .NET 8.5.0. Denna egenskap returnerar ett dubbelvärde som kan omvandlas till procentvärde. Till exempel, om den returnerar 0.507968245 betyder det att skalningsfaktorn är 51%.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some data in these cells

worksheet.Cells["A4"].PutValue("Test");

worksheet.Cells["S4"].PutValue("Test");

//Set paper size

worksheet.PageSetup.PaperSize = PaperSizeType.PaperA4;

//Set fit to pages wide as 1

worksheet.PageSetup.FitToPagesWide = 1;

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Convert page scale double value to percentage

string strPageScale = sr.PageScale.ToString("0%");

//Write the page scale value

Console.WriteLine(strPageScale);

{{< /highlight >}}


### **Enum CellValueFormatStrategy tillagd**
Aspose.Cells for .NET 8.5.0 har lagt till en ny uppräkning CellValueFormatStrategy för att hantera situationer där cellvärden måste extraheras med eller utan tillämpad formatering. Uppräkningen CellValueFormatStrategy har följande fält.

1. CellValueFormatStrategy.CellStyle: Endast formaterad med cellens originalformat.
1. CellValueFormatStrategy.DisplayStyle: Formaterad med cellens visas stil.
1. CellValueFormatStrategy.None: Inte formaterad.
### **Tillagt Cell.GetStingValue-metod**
För att använda uppräkningen CellValueFormatStrategy, har v8.5.0 exponerat metoden Cell.GetStingValue som kan ta emot en parameter av typen CellValueFormatStrategy och returnerar värdet beroende på det angivna alternativet.

Följande kodsnutt visar hur man använder den nyligen exponerade metoden Cells.GetStingValue.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Get string value as Cell Style

string value = cell.GetStingValue(CellValueFormatStrategy.CellStyle);

Console.WriteLine(value);

//Get string value without any formatting

value = cell.GetStingValue(CellValueFormatStrategy.None);

Console.WriteLine(value);

{{< /highlight >}}


### **Tillagt Egenskapen ExportTableOptions.FormatStrategy**
Aspose.Cells for .NET 8.5.0 har exponerat egenskapen ExportTableOptions.FormatStrategy för användare som vill exportera data till DataTable med eller utan formatering. Denna egenskap använder uppräkningen CellValueFormatStrategy och exporterar datan enligt angivet alternativ.

Följande kod förklarar användningen av egenskapen ExportTableOptions.FormatStrategy.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell A1

Cell cell = worksheet.Cells["A1"];

//Put value inside the cell

cell.PutValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.GetStyle();

style.Number = 2;

cell.SetStyle(style);

//Print the cell values as it displays in excel

Console.WriteLine("Cell String Value: " + cell.StringValue);

//Print the cell value without any format

Console.WriteLine("Cell String Value without Format: " + cell.StringValueWithoutFormat);

//Export Data Table Options with FormatStrategy as CellStyle

ExportTableOptions opts = new ExportTableOptions();

opts.ExportAsString = true;

opts.FormatStrategy = CellValueFormatStrategy.CellStyle;

//Export Data Table

DataTable dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as Cell Style: " + dt.Rows[0][0].ToString());

//Export Data Table Options with FormatStrategy as None

opts.FormatStrategy = CellValueFormatStrategy.None;

dt = worksheet.Cells.ExportDataTable(0, 0, 1, 1, opts);

//Print the value of very first cell

Console.WriteLine("Export Data Table with Format Strategy as None: " + dt.Rows[0][0].ToString());

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
