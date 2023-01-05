---
title: Visa eller dölj radkolumnrubriker i Aspose.Cells
type: docs
weight: 60
url: /sv/net/display-or-hide-row-column-headers-in-aspose-cells/
---
{{% alert color="primary" %}}

Alla kalkylblad i en Excel-fil är sammansatta av celler som är ordnade i rader och kolumner. Alla rader och kolumner har unika värden som används för att identifiera dem och för att identifiera enskilda celler. Till exempel är rader numrerade – 1, 2, 3, 4, etc. – och kolumner ordnas i alfabetisk ordning – A, B, C, D, etc. Rad- och kolumnvärdena visas i rubrikerna. Med hjälp av Aspose.Cells kan utvecklare kontrollera synligheten för dessa rad- och kolumnrubriker.

{{% /alert %}}

## **Styra arbetsbladens synlighet**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje kalkylblad i en Excel-fil.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad. För att kontrollera synligheten för rad- och kolumnrubriker använder du[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) fast egendom.[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) är en boolesk egenskap, vilket betyder att den bara kan lagra en**Sann** eller**falsk** värde.

 Ett komplett exempel ges nedan som visar hur man använder[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) egenskap för att dölja rad- och kolumnrubriker på det första kalkylbladet i en fil.

Skärmdumpen visar Book1.xls, indatafilen. Den innehåller tre arbetsblad: Blad1, Blad2 och Blad3. Varje kalkylblad visar rad- och kolumnrubriker.

**Book1.xls: kalkylblad före ändring**

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls öppnas genom att anropa Workbook-klassens Open-metod och rad- och kolumnrubrikerna på det första kalkylbladet är dolda. Den ändrade filen sparas som output.xls.

**Output.xls: kalkylblad efter modifiering** 

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the headers of rows and columns

worksheet.IsRowColumnHeadersVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
