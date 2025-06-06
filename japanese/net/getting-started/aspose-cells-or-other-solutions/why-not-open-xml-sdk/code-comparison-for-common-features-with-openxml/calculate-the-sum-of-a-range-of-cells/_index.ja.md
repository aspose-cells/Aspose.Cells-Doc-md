---
title: セル範囲の合計を計算する
type: docs
weight: 10
url: /ja/net/calculate-the-sum-of-a-range-of-cells/
---

## **OpenXML Excel**
以下はコードで使用する必要がある名前空間です：

{{< highlight csharp >}}

 using DocumentFormat.OpenXml;

using DocumentFormat.OpenXml.Packaging;

using DocumentFormat.OpenXml.Spreadsheet;

{{< /highlight >}}

以下がコードです：

{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Calculate the sum of a range of cells.xlsx";

string worksheetName = "Sheet1";

string firstCellName = "A1";

string lastCellName = "A3";

string resultCell = "A4";

CalculateSumOfCellRange(FileName, worksheetName, firstCellName, lastCellName, resultCell);

private static void CalculateSumOfCellRange(string docName, string worksheetName, string firstCellName, string lastCellName, string resultCell)

{

    // Open the document for editing.

    using (SpreadsheetDocument document = SpreadsheetDocument.Open(docName, true))

    {

        IEnumerable<Sheet> sheets = document.WorkbookPart.Workbook.Descendants<Sheet>().Where(s => s.Name == worksheetName);

        if (sheets.Count() == 0)

        {

            // The specified worksheet does not exist.

            return;

        }

        WorksheetPart worksheetPart = (WorksheetPart)document.WorkbookPart.GetPartById(sheets.First().Id);

        Worksheet worksheet = worksheetPart.Worksheet;

        // Get the row number and column name for the first and last cells in the range.

        uint firstRowNum = GetRowIndex(firstCellName);

        uint lastRowNum = GetRowIndex(lastCellName);

        string firstColumn = GetColumnName(firstCellName);

        string lastColumn = GetColumnName(lastCellName);

        double sum = 0;

        // Iterate through the cells within the range and add their values to the sum.

        foreach (Row row in worksheet.Descendants<Row>().Where(r => r.RowIndex.Value >= firstRowNum && r.RowIndex.Value <= lastRowNum))

        {

            foreach (Cell cell in row)

            {

                string columnName = GetColumnName(cell.CellReference.Value);

                if (CompareColumn(columnName, firstColumn) >= 0 && CompareColumn(columnName, lastColumn) <= 0)

                {

                    sum += double.Parse(cell.CellValue.Text);

                }

            }

        }

        // Get the SharedStringTablePart and add the result to it.

        // If the SharedStringPart does not exist, create a new one.

        SharedStringTablePart shareStringPart;

        if (document.WorkbookPart.GetPartsOfType<SharedStringTablePart>().Count() > 0)

        {

            shareStringPart = document.WorkbookPart.GetPartsOfType<SharedStringTablePart>().First();

        }

        else

        {

            shareStringPart = document.WorkbookPart.AddNewPart<SharedStringTablePart>();

        }

        // Insert the result into the SharedStringTablePart.

        int index = InsertSharedStringItem("Result: " + sum, shareStringPart);

        Cell result = InsertCellInWorksheet(GetColumnName(resultCell), GetRowIndex(resultCell), worksheetPart);

        // Set the value of the cell.

        result.CellValue = new CellValue(index.ToString());

        result.DataType = new EnumValue<CellValues>(CellValues.SharedString);

        worksheetPart.Worksheet.Save();

    }

}

// Given a cell name, parses the specified cell to get the row index.

private static uint GetRowIndex(string cellName)

{

    // Create a regular expression to match the row index portion the cell name.

    Regex regex = new Regex(@"\d+");

    Match match = regex.Match(cellName);

    return uint.Parse(match.Value);

}

// Given a cell name, parses the specified cell to get the column name.

private static string GetColumnName(string cellName)

{

    // Create a regular expression to match the column name portion of the cell name.

    Regex regex = new Regex("[A-Za-z]+");

    Match match = regex.Match(cellName);

    return match.Value;

}

// Given two columns, compares the columns.

private static int CompareColumn(string column1, string column2)

{

    if (column1.Length > column2.Length)

    {

        return 1;

    }

    else if (column1.Length < column2.Length)

    {

        return -1;

    }

    else

    {

        return string.Compare(column1, column2, true);

    }

}

// Given text and a SharedStringTablePart, creates a SharedStringItem with the specified text 

// and inserts it into the SharedStringTablePart. If the item already exists, returns its index.

private static int InsertSharedStringItem(string text, SharedStringTablePart shareStringPart)

{

    // If the part does not contain a SharedStringTable, create it.

    if (shareStringPart.SharedStringTable == null)

    {

        shareStringPart.SharedStringTable = new SharedStringTable();

    }

    int i = 0;

    foreach (SharedStringItem item in shareStringPart.SharedStringTable.Elements<SharedStringItem>())

    {

        if (item.InnerText == text)

        {

            // The text already exists in the part. Return its index.

            return i;

        }

        i++;

    }

    // The text does not exist in the part. Create the SharedStringItem.

    shareStringPart.SharedStringTable.AppendChild(new SharedStringItem(new DocumentFormat.OpenXml.Spreadsheet.Text(text)));

    shareStringPart.SharedStringTable.Save();

    return i;

}

// Given a column name, a row index, and a WorksheetPart, inserts a cell into the worksheet. 

// If the cell already exists, returns it. 

private static Cell InsertCellInWorksheet(string columnName, uint rowIndex, WorksheetPart worksheetPart)

{

    Worksheet worksheet = worksheetPart.Worksheet;

    SheetData sheetData = worksheet.GetFirstChild<SheetData>();

    string cellReference = columnName + rowIndex;

    // If the worksheet does not contain a row with the specified row index, insert one.

    Row row;

    if (sheetData.Elements<Row>().Where(r => r.RowIndex == rowIndex).Count() != 0)

    {

        row = sheetData.Elements<Row>().Where(r => r.RowIndex == rowIndex).First();

    }

    else

    {

        row = new Row() { RowIndex = rowIndex };

        sheetData.Append(row);

    }

    // If there is not a cell with the specified column name, insert one.  

    if (row.Elements<Cell>().Where(c => c.CellReference.Value == columnName + rowIndex).Count() > 0)

    {

        return row.Elements<Cell>().Where(c => c.CellReference.Value == cellReference).First();

    }

    else

    {

        // Cells must be in sequential order according to CellReference. Determine where to insert the new cell.

        Cell refCell = null;

        foreach (Cell cell in row.Elements<Cell>())

        {

            if (string.Compare(cell.CellReference.Value, cellReference, true) > 0)

            {

                refCell = cell;

                break;

            }

        }

        Cell newCell = new Cell() { CellReference = cellReference };

        row.InsertBefore(newCell, refCell);

        worksheet.Save();

        return newCell;

    }

}


{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Calculate the sum of a range of cells.xlsx";

string worksheetName = "Sheet1";

string firstCellName = "A1";

string lastCellName = "A3";

string resultCell = "A4";

CalculateSumOfCellRange(FileName, worksheetName, firstCellName, lastCellName, resultCell);

private static void CalculateSumOfCellRange(string docName, string worksheetName, string firstCellName, string lastCellName, string resultCell)

{

    //Instantiating a Workbook object

    Workbook workbook = new Workbook(docName);

    //Obtaining the reference of the worksheet by passing its Name

    Worksheet worksheet = workbook.Worksheets[worksheetName];

    //Adding a SUM formula to "A4" cell

    worksheet.Cells[resultCell].Formula = "=SUM(" + firstCellName + ":" + lastCellName + ")"; // =SUM(A1:A3)

    //Calculating the results of formulas

    workbook.CalculateFormula();

    //Get the calculated value of the cell

    string value = worksheet.Cells["A4"].Value.ToString();

    //Saving the Excel file

    workbook.Save(docName);

}

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)
- [Sourceforge](https://sourceforge.net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Calculate%20the%20sum%20of%20a%20range%20of%20cells%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Calculate%20the%20sum%20of%20a%20range%20of%20cells%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
