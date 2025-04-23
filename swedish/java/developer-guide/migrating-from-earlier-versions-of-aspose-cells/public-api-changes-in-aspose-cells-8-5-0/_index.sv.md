---
title: Offentliga API ändringar i Aspose.Cells 8.5.0
type: docs
weight: 170
url: /sv/java/public-api-changes-in-aspose-cells-8-5-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.4.2 till 8.5.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade allmänna metoder, [tillagda klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-5-0/), utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Ändrade ICustomFunction.CalculateCustomFunction-parametrar**
Om en parameter för den anpassade funktionen är en cellreferens användes i äldre versioner Aspose.Cells API för att konvertera cellreferensen till ett cellvärde eller en objektarray av alla cellvärden i det angivna området. Men för många funktioner och användare är inte cellvärdesarrayen för alla celler i det angivna området nödvändig, de behöver bara en enskild cell som motsvarar formelns position, eller bara behöver själva referensen istället för cellvärdet eller värdearrayen. För vissa situationer ökade det till och med risken för cirkulär referensfel.

För att stödja sådana krav har Aspose.Cells for Java 8.5.0 ändrat parametervärdet till "paramsList" för det angivna området. Sedan v8.5.0 sätter API:et bara ReferredArea-objektet i "paramsList" när den motsvarande parametern är en referens eller dess beräknade resultat är en referens. Om du behöver referensen själv kan du använda ReferredArea direkt. Om du behöver få ett enskilt cellvärde från referensen som motsvarar formelns position kan du använda ReferredArea.getValue(rowOffset, int colOffset)-metoden. Om du behöver cellvärdesarrayen för hela området kan du använda ReferredArea.getValues-metoden.

Nu när Aspose.Cells for Java 8.5.0 ger ReferredArea i "paramsList" behövs inte längre ReferredAreaCollection i "contextObjects" (i äldre versioner kunde den inte alltid ge en-ett-mappning till den anpassade funktionens parametrar), så denna version har också tagit bort den från "contextObjects" nu.

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
### **Klassen CalculationOptions tillagd**
Aspose.Cells for Java 8.5.0 har exponerat klassen CalculationOptions för att lägga till mer flexibilitet och utbyggnad för formelberäkningsmotorn. Den nyss tillagda klassen har följande egenskaper. 

1. CalculationOptions.CalcStackSize: Specificerar stackstorleken för att beräkna celler rekursivt. -1 anger att beräkningen kommer att använda WorkbookSettings.CalcStackSize för motsvarande arbetsbok.
1. CalculationOptions.CustomFunction: Utökar formelberäkningsmotorn med anpassad formel.
1. CalculationOptions.IgnoreError: Booleskt värde som indikerar om fel ska döljas vid beräkning av formler, där felen kan bero på otillåten funktion, extern länk eller mer.
1. CalculationOptions.PrecisionStrategy: Värdet CalculationPrecisionStrategy som specifierar strategin för att hantera beräkningsprecisionen.
### **Enumeration CalculationPrecisionStrategy tillagd**
Aspose.Cells for Java 8.5.0 har exponerat enumen CalculationPrecisionStrategy för att lägga till mer flexibilitet i formelberäkningsmotorn för att få önskade resultat. Denna enum strategisera beräkningsprecisionens hantering. På grund av precisionproblemet med IEEE 754 Floating-Point Arithmetic kan vissa tillsynes enkla formler inte beräknas för att ge förväntade resultat, därför har den senaste API-versionen exponerat följande fält för att få önskade resultat enligt valet.

1. CalculationPrecisionStrategy.DECIMAL: Använder decimal som operand när det är möjligt och är mest ineffektivt med avseende på prestanda.
1. CalculationPrecisionStrategy.ROUND: Avrundar beräkningsresultaten enligt signifikanta siffror.
1. CalculationPrecisionStrategy.NONE: Ingen strategi tillämpas därför under beräkningen använder motorn det ursprungliga dubbla värdet som operand och returnerar resultatet direkt. Detta alternativ är mest effektivt och är tillämpligt för de flesta fall.
### **Metoder tillagda för att använda CalculationOptions**
Med släppet av v8.5.0 har Aspose.Cells API lagt till överbelastningsversioner av calculateFormula-metoden som listas nedan.

- Workbook.calculateFormula(CalculationOptions)
- Worksheet.calculateFormula(CalculationOptions options, bool recursive)
- Cell.calculate(CalculationOptions)
### **Enum Field PasteType.ROW_HEIGHTS tillagd**
Aspose.Cells API har tillhandahållit fältet PasteType.ROW_HEIGHTS i enumen för att kopiera radhöjder vid kopiering av områden. Genom att ställa in PasteOptions.PasteType-egenskapen till ((PasteType.ROW_HEIGHTS}} kommer höjderna för alla rader i källområdet att kopieras till destinationsområdet.

**Java**

{{< highlight csharp >}}

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
### **Tillagd SheetRender.PageScale-egenskap**
När du ställer in siduppställningsskalningen med alternativet **Anpassa till n sidor bredvid m höga** beräknar Microsoft Excel skalfaktorn för siduppställning. Samma kan uppnås med hjälp av SheetRender.PageScale-egenskapen exponerad av Aspose.Cells for Java 8.5.0. Denna egenskap returnerar ett dubbelvärde som kan konverteras till procentvärde. Om det till exempel returnerar 0.507968245 betyder det att skalfaktorn är 51%.

**Java**

{{< highlight csharp >}}

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
### **Enum CellValueFormatStrategy tillagd**
Aspose.Cells for Java 8.5.0 har lagt till en ny enum CellValueFormatStrategy för att hantera situationer där cellvärden måste extraheras med eller utan tillämpad formatering. Enum CellValueFormatStrategy har följande fält. 

1. CellValueFormatStrategy.CELL_STYLE: Endast formaterad med cellens ursprungliga format.
1. CellValueFormatStrategy.DISPLAY_STYLE: Formaterad med cellens visade stil.
1. CellValueFormatStrategy.NONE: Ej formaterad.
### **Lade till Cell.getStringValue-metod**
För att använda CellValueFormatStrategy-uppräkningen, har v8.5.0 exponerat Cell.getStringValue-metoden som kan acceptera en parameter av typ CellValueFormatStrategy och returnera värdet beroende på det angivna alternativet.

Följande kodsnutt visar hur man använder den nyexponerade Cells.getStringValue-metoden.

**Java**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="java" >}}
