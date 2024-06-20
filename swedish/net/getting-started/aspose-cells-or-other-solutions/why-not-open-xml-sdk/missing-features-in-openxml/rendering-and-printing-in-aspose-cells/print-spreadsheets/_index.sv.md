---
title: Skriv ut kalkylblad
type: docs
weight: 20
url: /sv/net/print-spreadsheets/
---

Sidinställningar erbjuder också flera utskriftsalternativ (också kallade kalkylbladsoptioner) som låter användarna styra sina utskrivna kalkylbladssidor. Dessa utskriftsalternativ låter användarna:

- Välja ett specifikt utskriftsområde för kalkylbladet
- Skriv ut titlar
- Skriv ut rutnät
- Skriv ut rad/kolumnrubriker
- Uppnå utkastkvalitet
- Skriv ut kommentarer
- Skriv ut cellfel
- Definiera sidordning
  **Inställning av utskrift/kalkylbladsoptioner**

Aspose.Cells stöder alla dessa utskriftsalternativ och utvecklare kan enkelt konfigurera dessa alternativ för sina önskade kalkylblad med hjälp av de olika egenskaper som erbjuds av PageSetup-klassen. Användningen av dessa egenskaper i PageSetup-klassen diskuteras nedan mer i detalj.
## **Ange utskriftsområde**
Som standard är endast det utskriftsområde valt som omfattar hela området för kalkylbladet, som innehåller data men utvecklarna kan också skapa ett specifikt utskriftsområde för kalkylbladet enligt deras önskan.

För att välja ett specifikt utskriftsområde kan utvecklare använda **setPrintArea**-metoden i **PageSetup**-klassen. Du kan ange cellområdet för utskriftsområdet till den här metoden som argument.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Ställ in utskriftstitlar**
Aspose.Cells låter dig ange rad- och kolumnrubriker som du vill ha upprepade på alla sidor av ditt utskrivna kalkylblad. För att göra detta kan utvecklare använda **setPrintTitleColumns** och **setPrintTitleRows**-metoderna i **PageSetup**-klassen.

Raderna eller kolumnerna (som ska upprepas på alla sidor av det utskrivna kalkylarket) definieras genom att skicka deras rad- eller kolumnnummer. Till exempel definieras rader som \ $1: \ $2 och kolumner definieras som \ $A: \ $B.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **Ange andra utskriftsalternativ**
**PageSetup**-klassen tillhandahåller också flera andra metoder för att ställa in allmänna utskriftsalternativ enligt följande:

- **setPrintGridlines-metoden** , en boolesk parameter skickas till denna metod som definierar om rutnät ska skrivas ut eller inte
- **setPrintHeadings-metoden** , en boolesk parameter skickas till denna metod som definierar om rad- och kolumnrubriker ska skrivas ut eller inte
- **setBlackAndWhitemetoden** , en boolesk parameter skickas till denna metod som definierar om kalkylarket ska skrivas ut i svartvitt läge eller inte
- **setPrintComments method** , definierar om du vill visa utskriftskommentarer på arbetsbladet eller i slutet av arbetsbladet
- **setPrintDraft method** , en boolesk parameter skickas till denna metod som definierar om arbetsbladet ska skrivas ut i utkastkvalitet eller inte
- **setPrintErrors method** , definierar om cellfel ska skrivas ut som visas, tomma, streck eller N/A

För att använda metoderna set **PrintComments** och set **PrintErrors** tillhandahåller även Aspose.Cells två uppräkningar, PrintCommentsType & PrintErrorsType som innehåller fördefinierade värden att skickas som parametrar till set PrintComments och set PrintErrors-metoderna respektive.

{{< highlight csharp >}}

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
## **Ange sidordning**
**PageSetup** -klassen tillhandahåller en set Order-metod som används för att ordna flera sidor på ditt arbetsblad som ska skrivas ut. Det finns två möjligheter att ordna sidorna enligt följande:

Ner sedan över så att den skriver ut alla sidor ner innan den skriver ut sidor till höger
Över sedan ner så att den skriver ut sidor från vänster till höger innan den skriver ut sidor nedanför
Aspose.Cells tillhandahåller en uppräkning, PrintOrderType som innehåller alla fördefinierade ordningstyper som ska tilldelas setPage Order-metoden.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Ladda ned provkoden**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
