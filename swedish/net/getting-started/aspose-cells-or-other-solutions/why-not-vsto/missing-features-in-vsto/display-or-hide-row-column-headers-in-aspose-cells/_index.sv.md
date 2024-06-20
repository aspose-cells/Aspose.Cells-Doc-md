---
title: Visa eller dölj rad och kolumnhuvuden i Aspose.Cells
type: docs
weight: 60
url: /sv/net/display-or-hide-row-column-headers-in-aspose-cells/
---

{{% alert color="primary" %}}

Alla arbetsblad i en Excel-fil består av celler som är placerade i rader och kolumner. Alla rader och kolumner har unika värden som används för att identifiera dem, och för att identifiera enskilda celler. Till exempel är rader numrerade - 1, 2, 3, 4 osv. - och kolumner är ordnade alfabetiskt - A, B, C, D osv. Rad- och kolumnvärden visas i rubrikerna. Genom att använda Aspose.Cells kan utvecklare styra synligheten av dessa rad- och kolumnrubriker.

{{% /alert %}}

## **Kontrollera synligheten av arbetsbladen**

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) -samling som möjliggör åtkomst till varje arbetsblad i en Excel-fil.

Ett arbetsblad representeras av klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Klassen [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för hantering av arbetsblad. För att kontrollera synligheten av rad- och kolumnhuvuden använder [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) egendom. [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) är en boolesk egendom, vilket innebär att den endast kan lagra ett **true** eller **false** värde.

Ett komplett exempel ges nedan som visar hur du använder [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassens [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) egendom för att dölja rad- och kolumnhuvuden på det första arbetsbladet i en fil.

Skärmdumpen visar Book1.xls, ingångsfilen. Den innehåller tre arbetsblad: Sheet1, Sheet2 och Sheet3. Varje arbetsblad visar rad- och kolumnhuvuden.

**Book1.xls: arbetsblad före modifiering**

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls öppnas genom att använda Workbook klassens Open-metod och rad- och kolumnhuvuden på det första arbetsbladet döljs. Den modifierade filen sparas som output.xls.

**Output.xls: kalkylblad efter ändring** 

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

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

## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
