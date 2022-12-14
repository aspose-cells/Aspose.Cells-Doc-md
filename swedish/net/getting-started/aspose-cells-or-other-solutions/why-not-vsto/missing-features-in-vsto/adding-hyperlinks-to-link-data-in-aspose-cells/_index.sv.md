---
title: Lägger till hyperlänkar till länkdata i Aspose.Cells
type: docs
weight: 10
url: /sv/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---
{{% alert color="primary" %}}

En hyperlänk används för att skapa en länk mellan två enheter. Alla är bekanta med användningen av hyperlänkar, särskilt på webbplatser.

Med hjälp av Aspose.Cells kan utvecklare skapa olika typer av hyperlänkar i Microsoft Excel-filer. Det här ämnet diskuterar vilka typer av hyperlänkar som stöds av Aspose.Cells och hur de kan användas i våra Excel-filer.

{{% /alert %}}

## **Lägga till hyperlänkar**

Tre typer av hyperlänkar kan läggas till i en cell med Aspose.Cells:

- [Lägger till länk till en URL](#adding-link-to-a-url).
- [Lägga till en länk till en annan cell i samma fil](#adding-a-link-to-a-cell-in-the-same-file).
- [Lägga till en länk till en extern fil](#adding-a-link-to-an-external-file).

Aspose.Cells tillåter utvecklare att lägga till hyperlänkar till Excel-filer antingen med hjälp av API eller[designerkalkylblad](/cells/sv/net/what-is-a-designer-spreadsheet/)(kalkylblad där hyperlänkar skapas manuellt och Aspose.Cells används för att importera dem till andra kalkylblad).

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsbladssamling**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class tillhandahåller olika metoder för att lägga till olika hyperlänkar till Excel-filer.

### **Lägger till länk till en URL**

 De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass innehåller en[**Hyperlänkar**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) samling. Varje objekt i hyperlänksamlingen representerar en hyperlänk. Lägg till hyperlänkar till URL:er genom att anropa Hyperlänksamlingens Add-metod. Add-metoden tar följande parametrar:

- Cell namn, namnet på cellen som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperlänksområde.
- Antal kolumner, antalet kolumner i detta hyperlänkintervall
- URL, URL-adressen.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding a hyperlink to a URL at "A1" cell

worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Lägga till en länk till en Cell i samma fil**

Det är möjligt att lägga till hyperlänkar till celler i samma Excel-fil genom att anropa Hyperlänksamlingens Add-metod. Add-metoden fungerar för både interna och externa hyperlänkar. En version av den överbelastade metoden tar följande parametrar:

- Cell namn, namnet på cellen som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperlänksområde.
- Antal kolumner, antalet kolumner i detta hyperlänkintervall.
- URL, adressen till målcellen.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the first (default) worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Lägga till en länk till en extern fil**

Det är möjligt att lägga till hyperlänkar till externa Excel-filer genom att anropa Hyperlänksamlingens Add-metod. Add-metoden tar följande parametrar:

- Cell namn, namnet på cellen som hyperlänken kommer att läggas till.
- Antal rader, antalet rader i detta hyperlänksområde.
- Antal kolumner, antalet kolumner i detta hyperlänkintervall.
- URL, adressen till målet, extern Excel-fil.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("A5", 1, 1, "C:\\book1.xls");

//Saving the Excel file

workbook.Save("C:\\book2.xls");

{{< /highlight >}}

## **Ladda ner Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **Ladda ner exempelkod**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
