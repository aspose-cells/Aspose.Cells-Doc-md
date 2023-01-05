---
title: Offentlig API Ändringar i Aspose.Cells 8.5.0
type: docs
weight: 170
url: /sv/java/public-api-changes-in-aspose-cells-8-5-0/
---
{{% alert color="primary" %}} 

 Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.4.2 till 8.5.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-5-0/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Ändrade parametrar för ICustomFunction.CalculateCustomFunction**
Om en parameter för den anpassade funktionen är cellreferens, används i den gamla versionen Aspose.Cells API:er för att konvertera cellreferensen till ett cellvärde eller en objektmatris med alla cellvärden i det refererade området. För många funktioner och användare krävs dock inte cellvärdesmatrisen för alla celler i det refererade området, de behöver bara en enda cell som motsvarar formelns position, eller behöver bara referensen i sig istället för cellvärdet eller värdematrisen . För vissa situationer ökade hämtning av alla cellvärden till och med risken för cirkulära referensfel.

För att stödja en sådan typ av krav har Aspose.Cells for Java 8.5.0 ändrat parametervärdet till "paramsList" för refererat område. Sedan v8.5.0 lägger API bara in ReferredArea-objektet i "paramsList" när motsvarande parameter är en referens eller dess beräknade resultat är referens. Om du behöver själva referensen kan du använda ReferredArea direkt. Om du behöver få ett enskilt cellvärde från referensen som motsvarar formelns position, kan du använda metoden ReferredArea.getValue(rowOffset, int colOffset). Om du behöver en cellvärdesarray för hela området kan du använda metoden ReferredArea.getValues.

Nu när Aspose.Cells for Java 8.5.0 ger ReferredArea i "paramsList", kommer ReferredAreaCollection i "contextObjects" inte att behövas längre (i gamla versioner kunde den inte alltid ge en-till-en-karta till parametrarna för den anpassade funktionen), så den här versionen har också tagit bort den från "contextObjects" nu.

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

            o = ra.getValues();

        }

        else

        {

            o = ra.getValue(0, 0);

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
 Aspose.Cells for Java 8.5.0 har exponerat klassen CalculationOptions för att lägga till mer flexibilitet och utökningsbarhet för formelberäkningsmotorn. Den nyligen tillagda klassen har följande egenskaper.

1. CalculationOptions.CalcStackSize: Angav stackstorleken för att beräkna celler rekursivt. -1 anger att beräkningen kommer att använda WorkbookSettings.CalcStackSize för motsvarande arbetsbok.
1. CalculationOptions.CustomFunction: Utökar formelberäkningsmotorn med anpassad formel.
1. CalculationOptions.IgnoreError: Boolesk typvärde indikerar om fel ska döljas vid beräkning av formlerna, där felen kan bero på funktionen som inte stöds, extern länk eller mer.
1. CalculationOptions.PrecisionStrategy: CalculationPrecisionStrategy-typvärde som anger strategin för bearbetningsprecision i beräkningen.
### **Uppräkning BeräkningPrecisionStrategy tillagd**
Aspose.Cells for Java 8.5.0 har exponerat uppräkningen CalculationPrecisionStrategy för att lägga till mer flexibilitet till formelberäkningsmotorn för att få önskade resultat. Denna uppräkning strategier hanteringen av beräkningsprecisionen. På grund av precisionsproblemet med IEEE 754 Floating-Point Arithmetic, kanske vissa till synes enkla formler inte beräknas för att ge förväntade resultat, därför har den senaste API-byggnaden exponerat följande fält för att få önskade resultat enligt urvalet.

1. CalculationPrecisionStrategy.DECIMAL: Använder decimal som operand där det är möjligt, och är mest ineffektivt utifrån prestandaöverväganden.
1. CalculationPrecisionStrategy.ROUND: Avrundar beräkningsresultaten enligt signifikant siffra.
1. CalculationPrecisionStrategy.NONE: Ingen strategi tillämpas därför under beräkningen använder motorn det ursprungliga dubbelvärdet som operand och returnerar resultatet direkt. Det här alternativet är mest effektivt och kan användas i de flesta fall.
### **Metoder tillagda för att använda beräkningsalternativ**
Med lanseringen av v8.5.0 har Aspose.Cells API lagt till överbelastningsversioner av calculateFormula-metoden enligt listan nedan.

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(CalculationOptions-alternativ, bool rekursiv)
- Cell.calculate(CalculationOptions)
### **Uppräkningsfält PasteType.ROW_HEIGHTS har lagts till**
Aspose.Cells API:er har tillhandahållit PasteType.ROW_HEIGHTS uppräkningsfält för att kopiera radhöjderna samtidigt som intervallen kopieras. När du ställer in egenskapen PasteOptions.PasteType till ((PasteType.ROW_HEIGHTS}} höjderna på alla rader inom källområdet kommer att kopieras till destinationsområdet.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Source worksheet

Worksheet srcSheet = workbook.getWorksheets().get(0);

//Add destination worksheet

Worksheet dstSheet = workbook.getWorksheets().add("Destination Sheet");

//Set the row height of the 4th row

//This row height will be copied to destination range

srcSheet.getCells().setRowHeight(3, 50);

//Create source range to be copied

Range srcRange = srcSheet.getCells().createRange("A1:D10");

//Create destination range in destination worksheet

Range dstRange = dstSheet.getCells().createRange("A1:D10");

//PasteOptions, we want to copy row heights of source range to destination range

PasteOptions opts = new PasteOptions();

opts.setPasteType(PasteType.ROW_HEIGHTS);

//Copy source range to destination range with paste options

dstRange.copy(srcRange, opts);

//Write informative message in cell D4 of destination worksheet

dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

//Save the workbook in xlsx format

workbook.save("output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Property SheetRender.PageScale tillagd**
När du ställer in Skalning av sidinställningar med**Passar till n sida/sidor bred och m hög** option, Microsoft Excel beräknar skalfaktorn för sidinställningar. Samma kan uppnås med egenskapen SheetRender.PageScale exponerad av Aspose.Cells for Java 8.5.0. Den här egenskapen returnerar ett dubbelt värde som kan konverteras till procentuellt värde. Till exempel, om den returnerar 0,507968245 betyder det att skalfaktorn är 51 %.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some data in these cells

worksheet.getCells().get("A4").putValue("Test");

worksheet.getCells().get("S4").putValue("Test");

//Set paper size

worksheet.getPageSetup().setPaperSize(PaperSizeType.PAPER_A_4);

//Set fit to pages wide as 1

worksheet.getPageSetup().setFitToPagesWide(1);

//Calculate page scale via sheet render

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

//Write the page scale value

System.out.println(sr.getPageScale());

{{< /highlight >}}
### **Uppräkning CellValueFormatStrategy tillagd**
 Aspose.Cells for Java 8.5.0 har lagt till en ny uppräkning CellValueFormatStrategy för att hantera situationer där cellvärden måste extraheras med eller utan formatering. Enumeration CellValueFormatStrategy har följande fält.

1. CellValueFormatStrategy.CELL_STYLE: Endast formaterad med cellens ursprungliga format.
1. CellValueFormatStrategy.DISPLAY_STYLE: Formaterad med cellens visade stil.
1. CellValueFormatStrategy.NONE: Ej formaterad.
### **Metod Cell.getStringValue Added**
För att kunna använda uppräkningen CellValueFormatStrategy har v8.5.0 avslöjat metoden Cell.getStringValue som kan acceptera en parameter av typen CellValueFormatStrategy och returnerar värdet beror på det angivna alternativet.

Följande kodavsnitt visar hur man använder den nyligen exponerade metoden Cells.getStringValue.

**Java**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell A1

Cell cell = worksheet.getCells().get("A1");

//Put value inside the cell

cell.putValue(0.012345);

//Format the cell that it should display 0.01 instead of 0.012345

Style style = cell.getStyle();

style.setNumber(2);

cell.setStyle(style);

//Get string value as Cell Style

String value = cell.getStringValue(CellValueFormatStrategy.CELL_STYLE);

System.out.println(value);

//Get string value without any formatting

value = cell.getStringValue(CellValueFormatStrategy.NONE);

System.out.println(value);

{{< /highlight >}}
