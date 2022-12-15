---
title: Offentlig API Ändringar i Aspose.Cells 8.5.0
type: docs
weight: 160
url: /sv/net/public-api-changes-in-aspose-cells-8-5-0/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.4.2 till 8.5.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-5-0/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Ändrade parametrar för ICustomFunction.CalculateCustomFunction**
Om en parameter för den anpassade funktionen är cellreferens, används i den gamla versionen Aspose.Cells API:er för att konvertera cellreferensen till ett cellvärde eller en objektmatris med alla cellvärden i det refererade området. För många funktioner och användare krävs dock inte cellvärdesmatrisen för alla celler i det refererade området, de behöver bara en enda cell som motsvarar formelns position, eller behöver bara referensen i sig istället för cellvärdet eller värdematrisen . För vissa situationer ökade hämtning av alla cellvärden till och med risken för cirkulära referensfel.

För att stödja en sådan typ av krav har Aspose.Cells for .NET 8.5.0 ändrat parametervärdet till "paramsList" för refererat område. Sedan v8.5.0 lägger API bara in ReferredArea-objektet i "paramsList" när motsvarande parameter är en referens eller dess beräknade resultat är referens. Om du behöver själva referensen kan du använda ReferredArea direkt. Om du behöver få ett enskilt cellvärde från referensen som motsvarar formelns position, kan du använda metoden ReferredArea.GetValue(rowOffset, int colOffset). Om du behöver en cellvärdesarray för hela området kan du använda metoden ReferredArea.GetValues.

Nu när Aspose.Cells for .NET 8.5.0 ger ReferredArea i "paramsList", kommer ReferredAreaCollection i "contextObjects" inte att behövas längre (i gamla versioner kunde den inte alltid ge en-till-en-karta till parametrarna för den anpassade funktionen), så den här versionen har också tagit bort den från "contextObjects" nu.

Denna ändring kräver ändringar av koden för implementeringen för ICustomFunction lite när du behöver värdet/värdena för referensparametern.

**Gammal implementering**

{{< highlight "csharp" >}}

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

**Ny implementering**

{{< highlight "csharp" >}}

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


### **Klassberäkningsalternativ har lagts till**
Aspose.Cells for .NET 8.5.0 har exponerat klassen CalculationOptions för att lägga till mer flexibilitet och utökningsbarhet för formelberäkningsmotorn. Den nyligen tillagda klassen har följande egenskaper.

1. CalculationOptions.CalcStackSize: Angav stackstorleken för att beräkna celler rekursivt. -1 anger att beräkningen kommer att använda WorkbookSettings.CalcStackSize för motsvarande arbetsbok.
1. CalculationOptions.CustomFunction: Utökar formelberäkningsmotorn med anpassad formel.
1. CalculationOptions.IgnoreError: Boolesk typvärde indikerar om fel ska döljas vid beräkning av formlerna, där felen kan bero på funktionen som inte stöds, extern länk eller mer.
1. CalculationOptions.PrecisionStrategy: CalculationPrecisionStrategy-typvärde som anger strategin för bearbetningsprecision i beräkningen.
### **Uppräkning BeräkningPrecisionStrategy tillagd**
Aspose.Cells for .NET 8.5.0 har exponerat uppräkningen CalculationPrecisionStrategy för att lägga till mer flexibilitet till formelberäkningsmotorn för att få önskade resultat. Denna uppräkning strategier hanteringen av beräkningsprecisionen. På grund av precisionsproblemet med IEEE 754 Floating-Point Arithmetic, kanske vissa till synes enkla formler inte beräknas för att ge förväntade resultat, därför har den senaste API-byggnaden exponerat följande fält för att få önskade resultat enligt urvalet.

1. CalculationPrecisionStrategy.Decimal: Använder decimal som operand där det är möjligt, och är mest ineffektivt utifrån prestanda.
1. CalculationPrecisionStrategy.Round: Avrundar beräkningsresultaten enligt signifikant siffra.
1. CalculationPrecisionStrategy.None: Ingen strategi används därför under beräkningen använder motorn det ursprungliga dubbelvärdet som operand och returnerar resultatet direkt. Det här alternativet är mest effektivt och kan användas i de flesta fall.
### **Metoder tillagda för att använda beräkningsalternativ**
Med lanseringen av v8.5.0 har Aspose.Cells API lagt till överbelastningsversioner av CalculateFormula-metoden enligt listan nedan.

- Workbook.CalculateFormula(CalculationOptions)
- Worksheet.CalculateFormula(Alternativ för beräkningsalternativ, bool rekursiv)
- Cell. Beräkna (Beräkningsalternativ)
### **Uppräkningsfältet PasteType.RowHeights har lagts till**
Aspose.Cells API:er har tillhandahållit uppräkningsfältet PasteType.RowHeights i syfte att kopiera radhöjderna medan intervallen kopieras. När egenskapen PasteOptions.PasteType ställs in på ((PasteType.RowHeights}} kommer höjderna på alla rader inom källområdet att kopieras till destinationsområdet.

**C#**

{{< highlight "csharp" >}}

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


### **Property SheetRender.PageScale tillagd**
När du ställer in Skalning av sidinställningar med**Passar till n sida/sidor bred och m hög** option, Microsoft Excel beräknar skalfaktorn för sidinställningar. Samma kan uppnås med egenskapen SheetRender.PageScale exponerad av Aspose.Cells for .NET 8.5.0. Den här egenskapen returnerar ett dubbelt värde som kan konverteras till procentuellt värde. Till exempel, om den returnerar 0,507968245 betyder det att skalfaktorn är 51 %.

**C#**

{{< highlight "csharp" >}}

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


### **Uppräkning CellValueFormatStrategy tillagd**
Aspose.Cells for .NET 8.5.0 har lagt till en ny uppräkning CellValueFormatStrategy för att hantera situationer där cellvärden måste extraheras med eller utan formatering. Enumeration CellValueFormatStrategy har följande fält.

1. CellValueFormatStrategy.CellStyle: Endast formaterad med cellens ursprungliga format.
1. CellValueFormatStrategy.DisplayStyle: Formaterad med cellens visade stil.
1. CellValueFormatStrategy.None: Ej formaterad.
### **Metod Cell.GetStingValue Added**
För att kunna använda uppräkningen CellValueFormatStrategy har v8.5.0 avslöjat metoden Cell.GetStingValue som kan acceptera en parameter av typen CellValueFormatStrategy och returnerar värdet beror på det angivna alternativet.

Följande kodavsnitt visar hur man använder den nyligen exponerade metoden Cells.GetStingValue.

**C#**

{{< highlight "csharp" >}}

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


### **Egenskap ExportTableOptions.FormatStrategy tillagd**
Aspose.Cells for .NET 8.5.0 har exponerat egenskapen ExportTableOptions.FormatStrategy för de användare som vill exportera data till DataTable med eller utan formatering. Den här egenskapen använder CellValueFormatStrategy-uppräkningen och exporterar data enligt angivet alternativ.

Följande kod förklarar användningen av egenskapen ExportTableOptions.FormatStrategy.

**C#**

{{< highlight "csharp" >}}

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
