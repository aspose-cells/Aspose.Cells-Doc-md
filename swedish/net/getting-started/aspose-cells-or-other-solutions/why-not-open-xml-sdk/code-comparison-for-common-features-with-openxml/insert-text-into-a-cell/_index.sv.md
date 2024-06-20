---
title: Infoga text i en cell
type: docs
weight: 80
url: /sv/net/insert-text-into-a-cell/
---

## **OpenXML Excel**
{{< highlight csharp >}}

 string FilePath = @"..\..\..\..\Sample Files\";

string FileName = FilePath + "Insert text into a cell.xlsx";

InsertText(FileName, "Inserted Text");

// Given a document name and text, 

// inserts a new work sheet and writes the text to cell "A1" of the new worksheet.

public static void InsertText(string docName, string text)

{

    // Open the document for editing.

    using (SpreadsheetDocument spreadSheet = SpreadsheetDocument.Open(docName, true))

    {

        // Get the SharedStringTablePart. If it does not exist, create a new one.

        SharedStringTablePart shareStringPart;

        if (spreadSheet.WorkbookPart.GetPartsOfType<SharedStringTablePart>().Count() > 0)

        {

            shareStringPart = spreadSheet.WorkbookPart.GetPartsOfType<SharedStringTablePart>().First();

        }

        else

        {

            shareStringPart = spreadSheet.WorkbookPart.AddNewPart<SharedStringTablePart>();

        }

        // Insert the text into the SharedStringTablePart.

        int index = InsertSharedStringItem(text, shareStringPart);

        // Insert a new worksheet.

        WorksheetPart worksheetPart = InsertWorksheet(spreadSheet.WorkbookPart);

        // Insert cell A1 into the new worksheet.

        Cell cell = InsertCellInWorksheet("A", 1, worksheetPart);

        // Set the value of cell A1.

        cell.CellValue = new CellValue(index.ToString());

        cell.DataType = new EnumValue<CellValues>(CellValues.SharedString);

        // Save the new worksheet.

        worksheetPart.Worksheet.Save();

    }

}

// Given text and a SharedStringTablePart, creates a SharedStringItem with the specified text 

// and inserts it into the SharedStringTablePart. If the item already exists, returns its index.

private static int InsertSharedStringItem(string text, SharedStringTablePart shareStringPart)

{

    // If the part does not contain a SharedStringTable, create one.

    if (shareStringPart.SharedStringTable == null)

    {

        shareStringPart.SharedStringTable = new SharedStringTable();

    }

    int i = 0;

    // Iterate through all the items in the SharedStringTable. If the text already exists, return its index.

    foreach (SharedStringItem item in shareStringPart.SharedStringTable.Elements<SharedStringItem>())

    {

        if (item.InnerText == text)

        {

            return i;

        }

        i++;

    }

    // The text does not exist in the part. Create the SharedStringItem and return its index.

    shareStringPart.SharedStringTable.AppendChild(new SharedStringItem(new DocumentFormat.OpenXml.Spreadsheet.Text(text)));

    shareStringPart.SharedStringTable.Save();

    return i;

}

// Given a WorkbookPart, inserts a new worksheet.

private static WorksheetPart InsertWorksheet(WorkbookPart workbookPart)

{

    // Add a new worksheet part to the workbook.

    WorksheetPart newWorksheetPart = workbookPart.AddNewPart<WorksheetPart>();

    newWorksheetPart.Worksheet = new Worksheet(new SheetData());

    newWorksheetPart.Worksheet.Save();

    Sheets sheets = workbookPart.Workbook.GetFirstChild<Sheets>();

    string relationshipId = workbookPart.GetIdOfPart(newWorksheetPart);

    // Get a unique ID for the new sheet.

    uint sheetId = 1;

    if (sheets.Elements<Sheet>().Count() > 0)

    {

        sheetId = sheets.Elements<Sheet>().Select(s => s.SheetId.Value).Max() + 1;

    }

    string sheetName = "Sheet" + sheetId;

    // Append the new worksheet and associate it with the workbook.

    Sheet sheet = new Sheet() { Id = relationshipId, SheetId = sheetId, Name = sheetName };

    sheets.Append(sheet);

    workbookPart.Workbook.Save();

    return newWorksheetPart;

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

string FileName = FilePath + "Insert text into a cell.xlsx";

InsertText(FileName, "Inserted Text");

private static void InsertText(string docName, string text)

{

    //Instantiating a Workbook object

    Workbook workbook = new Workbook(docName);

    //Obtaining the reference of the Active worksheet

    Worksheet worksheet = workbook.Worksheets[workbook.Worksheets.ActiveSheetIndex];

    //insert value from cell

    worksheet.Cells["A1"].PutValue(text);

    //Saving the Excel file

    workbook.Save(docName);

}

{{< /highlight >}}
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/AsposeCellsVsOpenXMLv1.1)
- [Sourceforge](https://sourceforge.net/projects/asposeopenxml/files/Aspose.Cells%20Vs%20OpenXML/Insert%20text%20into%20a%20cell%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Insert%20text%20into%20a%20cell%20\(Aspose.Cells\).zip)
