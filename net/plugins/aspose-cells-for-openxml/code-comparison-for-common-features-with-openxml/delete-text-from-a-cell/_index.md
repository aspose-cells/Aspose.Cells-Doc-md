---
title: Delete text from a cell
type: docs
weight: 30
url: /net/delete-text-from-a-cell/
---

## **OpenXML Excel**
{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Delete text from a cell.xlsx";

string sheetName = "Sheet1";

string colName = "B";

uint rowIndex = 2;

DeleteTextFromCell(FileName, sheetName, colName, rowIndex);

// Given a document, a worksheet name, a column name, and a one-based row index,

// deletes the text from the cell at the specified column and row on the specified worksheet.

public static void DeleteTextFromCell(string docName, string sheetName, string colName, uint rowIndex)

{

    // Open the document for editing.

    using (SpreadsheetDocument document = SpreadsheetDocument.Open(docName, true))

    {

        IEnumerable<Sheet> sheets = document.WorkbookPart.Workbook.GetFirstChild<Sheets>().Elements<Sheet>().Where(s => s.Name == sheetName);

        if (sheets.Count() == 0)

        {

            // The specified worksheet does not exist.

            return;

        }

        string relationshipId = sheets.First().Id.Value;

        WorksheetPart worksheetPart = (WorksheetPart)document.WorkbookPart.GetPartById(relationshipId);

        // Get the cell at the specified column and row.

        Cell cell = GetSpreadsheetCell(worksheetPart.Worksheet, colName, rowIndex);

        if (cell == null)

        {

            // The specified cell does not exist.

            return;

        }

        cell.Remove();

        worksheetPart.Worksheet.Save();

    }

}

// Given a worksheet, a column name, and a row index, gets the cell at the specified column and row.

private static Cell GetSpreadsheetCell(Worksheet worksheet, string columnName, uint rowIndex)

{

    IEnumerable<Row> rows = worksheet.GetFirstChild<SheetData>().Elements<Row>().Where(r => r.RowIndex == rowIndex);

    if (rows.Count() == 0)

    {

        // A cell does not exist at the specified row.

        return null;

    }

    IEnumerable<Cell> cells = rows.First().Elements<Cell>().Where(c => string.Compare(c.CellReference.Value, columnName + rowIndex, true) == 0);

    if (cells.Count() == 0)

    {

        // A cell does not exist at the specified column, in the specified row.

        return null;

    }

    return cells.First();

}

// Given a shared string ID and a SpreadsheetDocument, verifies that other cells in the document no longer 

// reference the specified SharedStringItem and removes the item.

private static void RemoveSharedStringItem(int shareStringId, SpreadsheetDocument document)

{

    bool remove = true;

    foreach (var part in document.WorkbookPart.GetPartsOfType<WorksheetPart>())

    {

        Worksheet worksheet = part.Worksheet;

        foreach (var cell in worksheet.GetFirstChild<SheetData>().Descendants<Cell>())

        {

            // Verify if other cells in the document reference the item.

            if (cell.DataType != null &&

                cell.DataType.Value == CellValues.SharedString &&

                cell.CellValue.Text == shareStringId.ToString())

            {

                // Other cells in the document still reference the item. Do not remove the item.

                remove = false;

                break;

            }

        }

        if (!remove)

        {

            break;

        }

    }

    // Other cells in the document do not reference the item. Remove the item.

    if (remove)

    {

        SharedStringTablePart shareStringTablePart = document.WorkbookPart.SharedStringTablePart;

        if (shareStringTablePart == null)

        {

            return;

        }

        SharedStringItem item = shareStringTablePart.SharedStringTable.Elements<SharedStringItem>().ElementAt(shareStringId);

        if (item != null)

        {

            item.Remove();

            // Refresh all the shared string references.

            foreach (var part in document.WorkbookPart.GetPartsOfType<WorksheetPart>())

            {

                Worksheet worksheet = part.Worksheet;

                foreach (var cell in worksheet.GetFirstChild<SheetData>().Descendants<Cell>())

                {

                    if (cell.DataType != null &&

                        cell.DataType.Value == CellValues.SharedString)

                    {

                        int itemIndex = int.Parse(cell.CellValue.Text);

                        if (itemIndex > shareStringId)

                        {

                            cell.CellValue.Text = (itemIndex - 1).ToString();

                        }

                    }

                }

                worksheet.Save();

            }

            document.WorkbookPart.SharedStringTablePart.SharedStringTable.Save();

        }

    }

}

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Delete text from a cell.xlsx";

string sheetName = "Sheet1";

string colName = "B";

uint rowIndex = 2;

DeleteTextFromCell(FileName, sheetName, colName, rowIndex);

private static void DeleteTextFromCell(string docName, string sheetName, string colName, uint rowIndex)

    {

        //Instantiating a Workbook object

        Workbook workbook = new Workbook(docName);

        //Obtaining the reference of the worksheet by passing its Name

        Worksheet worksheet = workbook.Worksheets[sheetName];

        //Removing value from cell

        worksheet.Cells[colName + rowIndex].PutValue("");

        //Saving the Excel file

        workbook.Save(docName);

    }

{{< /highlight >}}
## **Download Sample Code**
- [CodePlex](https://asposeopenxml.codeplex.com/releases/view/616479)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)
- [Sourceforge](https://sourceforge.net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Delete%20text%20from%20a%20cell%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Delete%20text%20from%20a%20cell%20\(Aspose.Cells\).zip)
