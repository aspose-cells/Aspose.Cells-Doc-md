---
title: Få en kolumnrubrik
type: docs
weight: 40
url: /sv/net/get-a-column-heading/
---
## **OpenXML Excel**
{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Get a column heading.xlsx";

string worksheetName = "Sheet1";

string cellName = "B3";

string s1 = GetColumnHeading(FileName, worksheetName, cellName);

// Given a document name, a worksheet name, and a cell name, gets the column of the cell and returns

// the content of the first cell in that column.

public static string GetColumnHeading(string docName, string worksheetName, string cellName)

{

// Open the document as read-only.

using (SpreadsheetDocument document = SpreadsheetDocument.Open(docName, false))

{

    IEnumerable<Sheet> sheets = document.WorkbookPart.Workbook.Descendants<Sheet>().Where(s => s.Name == worksheetName);

    if (sheets.Count() == 0)

    {

        // The specified worksheet does not exist.

        return null;

    }

    WorksheetPart worksheetPart = (WorksheetPart)document.WorkbookPart.GetPartById(sheets.First().Id);

    // Get the column name for the specified cell.

    string columnName = GetColumnName(cellName);

    // Get the cells in the specified column and order them by row.

    IEnumerable<Cell> cells = worksheetPart.Worksheet.Descendants<Cell>().Where(c => string.Compare(GetColumnName(c.CellReference.Value), columnName, true) == 0)

        .OrderBy(r => GetRowIndex(r.CellReference));

    if (cells.Count() == 0)

    {

        // The specified column does not exist.

        return null;

    }

    // Get the first cell in the column.

    Cell headCell = cells.First();

    // If the content of the first cell is stored as a shared string, get the text of the first cell

    // from the SharedStringTablePart and return it. Otherwise, return the string value of the cell.

    if (headCell.DataType != null && headCell.DataType.Value == CellValues.SharedString)

    {

        SharedStringTablePart shareStringPart = document.WorkbookPart.GetPartsOfType<SharedStringTablePart>().First();

        SharedStringItem[] items = shareStringPart.SharedStringTable.Elements<SharedStringItem>().ToArray();

        return items[int.Parse(headCell.CellValue.Text)].InnerText;

    }

    else

    {

        return headCell.CellValue.Text;

    }

}

}

// Given a cell name, parses the specified cell to get the column name.

private static string GetColumnName(string cellName)

{

// Create a regular expression to match the column name portion of the cell name.

Regex regex = new Regex("[A-Za-z]+");

Match match = regex.Match(cellName);

return match.Value;

}

// Given a cell name, parses the specified cell to get the row index.

private static uint GetRowIndex(string cellName)

{

// Create a regular expression to match the row index portion the cell name.

Regex regex = new Regex(@"\d+");

Match match = regex.Match(cellName);

return uint.Parse(match.Value);

}

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Get a column heading.xlsx";

string worksheetName = "Sheet1";

string cellName = "B3";

string s1 = GetColumnHeading(FileName, worksheetName, cellName);

private static string GetColumnHeading(string docName, string worksheetName, string cellName)

{

    //Instantiating a Workbook object

    Workbook workbook = new Workbook(docName);

    //Obtaining the reference of the worksheet by passing its Name

    Worksheet worksheet = workbook.Worksheets[worksheetName];

    //Removing value from cell

    Cell Cell = worksheet.Cells[cellName];

    //Get First row of the column

    string ColumnHeadingName = CellsHelper.CellIndexToName(0, Cell.Column);

    //return value of heading cell

    return worksheet.Cells[ColumnHeadingName].Value.ToString();

}

{{< /highlight >}}
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)
- [Sourceforge](https://sourceforge.net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Get%20a%20column%20heading%20\(Aspose.Cells\).zip/download)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Get%20a%20column%20heading%20\(Aspose.Cells\).blixtlås)
