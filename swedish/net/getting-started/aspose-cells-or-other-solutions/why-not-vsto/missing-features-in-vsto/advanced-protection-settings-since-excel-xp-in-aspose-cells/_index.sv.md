---
title: Avancerade skyddsinställningar sedan Excel XP i Aspose.Cells
type: docs
weight: 20
url: /sv/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---
{{% alert color="primary" %}}

- Ta bort rader eller kolumner.
- Redigera innehåll, objekt eller scenarier.
- Formatera celler, rader eller kolumner.
- Infoga rader, kolumner eller hyperlänkar.
- Välj låsta eller olåsta celler.
- Använd pivottabeller och mycket mer.

Aspose.Cells stöder alla avancerade skyddsinställningar som erbjuds av Excel XP eller senare versioner.

{{% /alert %}}

## **Avancerade skyddsinställningar med Excel XP och senare versioner**

Så här visar du skyddsinställningarna i Excel XP:

1.  Från**Verktyg** menyn, välj**Skydd** följd av**Skydda ark**.
 En dialogruta visas.

   **Dialog för att visa skyddsalternativ i Excel XP**

![todo:image_alt_text](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. Tillåt eller begränsa kalkylbladsfunktioner eller använd ett lösenord.

### **Avancerade skyddsinställningar med Aspose.Cells**

Aspose.Cells stöder alla avancerade skyddsinställningar.

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass.

 De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger[**Skydd**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)egenskap som används för att tillämpa dessa avancerade skyddsinställningar. De[**Skydd**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) egendom är i själva verket ett föremål för[**Skydd**](https://reference.aspose.com/cells/net/aspose.cells/protection) klass som kapslar in flera booleska egenskaper för att inaktivera eller aktivera begränsningar.

Nedan finns ett litet exempel på applikation. Den öppnar en Excel-fil och använder de flesta av de avancerade skyddsinställningarna som stöds av Excel XP och senare versioner.

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook excel = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = excel.Worksheets[0];

//Restricting users to delete columns of the worksheet

worksheet.Protection.AllowDeletingColumn = false;

//Restricting users to delete row of the worksheet

worksheet.Protection.AllowDeletingRow = false;

//Restricting users to edit contents of the worksheet

worksheet.Protection.AllowEditingContent = false;

//Restricting users to edit objects of the worksheet

worksheet.Protection.AllowEditingObject = false;

//Restricting users to edit scenarios of the worksheet

worksheet.Protection.AllowEditingScenario = false;

//Restricting users to filter

worksheet.Protection.AllowFiltering = false;

//Allowing users to format cells of the worksheet

worksheet.Protection.AllowFormattingCell = true;

//Allowing users to format rows of the worksheet

worksheet.Protection.AllowFormattingRow = true;

//Allowing users to insert columns in the worksheet

worksheet.Protection.AllowFormattingColumn = true;

//Allowing users to insert hyperlinks in the worksheet

worksheet.Protection.AllowInsertingHyperlink = true;

//Allowing users to insert rows in the worksheet

worksheet.Protection.AllowInsertingRow = true;

//Allowing users to select locked cells of the worksheet

worksheet.Protection.AllowSelectingLockedCell = true;

//Allowing users to select unlocked cells of the worksheet

worksheet.Protection.AllowSelectingUnlockedCell = true;

//Allowing users to sort

worksheet.Protection.AllowSorting = true;

//Allowing users to use pivot tables in the worksheet

worksheet.Protection.AllowUsingPivotTable = true;

//Saving the modified Excel file

excel.Save("output.xls", SaveFormat.Excel97To2003);

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
