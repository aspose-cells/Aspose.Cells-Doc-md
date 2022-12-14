---
title: Skriv ut kalkylblad
type: docs
weight: 20
url: /sv/net/print-spreadsheets/
---
Inställningar för sidinställningar ger också flera utskriftsalternativ (även kallade arkalternativ) som låter användare styra sina utskrivna sidor med kalkylblad. Dessa utskriftsalternativ tillåter användare att:

- Välj ett specifikt utskriftsområde i kalkylbladet
- Skriv ut titlar
- Skriv ut rutnät
- Skriv ut rad-/kolumnrubriker
- Uppnå utkastkvalitet
- Skriv ut kommentarer
- Skriv ut Cell Fel
- Definiera sidordning
  **Ställa in utskrifts-/arkalternativ**

Aspose.Cells stöder alla dessa utskriftsalternativ och utvecklare kan enkelt konfigurera dessa alternativ för sina önskade kalkylblad med hjälp av de olika egenskaperna som erbjuds av klassen PageSetup. Användningen av dessa egenskaper för klassen PageSetup diskuteras mer i detalj nedan.
## **Ställ in utskriftsområde**
Som standard väljs endast det utskriftsområdet som innehåller hela området av kalkylbladet, som innehåller data, men utvecklare kan också skapa ett specifikt utskriftsområde för kalkylbladet enligt deras önskemål.

 För att välja ett specifikt utskriftsområde kan utvecklare använda set**PrintArea** metod för**Utskriftsformat** klass. Du kan ange cellområdet för utskriftsområdet till denna metod som argument.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Ställ in utskriftsrubriker**
 Aspose.Cells låter dig ange rad- och kolumnrubriker som du vill ska upprepas på alla sidor i ditt utskrivna kalkylblad. För att göra det kan utvecklare använda set**PrintTitleColumns** och**setPrintTitleRows** metoder för**Utskriftsformat** klass.

Raderna eller kolumnerna (som ska upprepas på alla sidor i det utskrivna kalkylbladet) definieras genom att skicka deras rad- eller kolumnnummer. Till exempel är rader definierade som \ $1: \ $2 och kolumner definieras som \ $A: \ $B.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Ställ in andra utskriftsalternativ**
**Utskriftsformat** class tillhandahåller även flera andra metoder för att ställa in allmänna utskriftsalternativ enligt följande:

- **setPrintGridlines metod** , skickas en boolesk parameter till denna metod som definierar om rutnät ska skrivas ut eller inte
- **setPrintHeadings-metoden** skickas en boolesk parameter till denna metod som definierar om rad- och kolumnrubriker ska skrivas ut eller inte
- **setBlackAndWhite-metoden** , skickas en boolesk parameter till denna metod som definierar om kalkylblad ska skrivas ut i svartvitt läge eller inte
- **setPrintComments-metoden** , definierar om utskriftskommentarerna ska visas på kalkylbladet eller i slutet av kalkylbladet
- **setPrintDraft-metoden** , skickas en boolesk parameter till denna metod som definierar om kalkylblad ska skrivas ut i utkastkvalitet eller inte
- **setPrintErrors-metoden** , definierar om cellfel ska skrivas ut som visas, tomt, streck eller ej

 Att använda set**Skriv ut Kommentarer** och ställ in**PrintErrors** metoder, Aspose.Cells tillhandahåller också två uppräkningar, PrintCommentsType och PrintErrorsType som innehåller fördefinierade värden som ska passeras en parameter för att ställa in PrintComments respektive set PrintErrors metoder.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Allowing to print gridlines

pageSetup.PrintGridlines = true;

//Allowing to print row/column headings

pageSetup.PrintHeadings = true;

//Allowing to print worksheet in black & white mode

pageSetup.BlackAndWhite = true;

//Allowing to print comments as displayed on worksheet

pageSetup.PrintComments = PrintCommentsType.PrintInPlace;

//Allowing to print worksheet with draft quality

pageSetup.PrintDraft = true;

//Allowing to print cell errors as N/A

pageSetup.PrintErrors = PrintErrorsType.PrintErrorsNA;

{{< /highlight >}}
## **Ställ in sidordning**
**Utskriftsformat**klass tillhandahåller set Order-metod som används för att beställa flera sidor i ditt kalkylblad som ska skrivas ut. Det finns två möjligheter att beställa sidorna enligt följande:

Ner och sedan över så kommer den att skriva ut alla sidor ner innan den skriver ut sidorna till höger
Över och nedåt så kommer den att skriva ut sidor från vänster till höger innan du skriver ut sidorna nedan
Aspose.Cells tillhandahåller en uppräkning, PrintOrderType som innehåller alla fördefinierade ordertyper som ska tilldelas till setPage Order-metoden.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Ladda ner exempelkod**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
