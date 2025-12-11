---
title: Adding New Worksheets to Workbook and Activating a Sheet in VSTO and Aspose.Cells
type: docs
weight: 30
url: /net/adding-new-worksheets-to-workbook-and-activating-a-sheet-in-vsto-and-aspose-cells/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Migration tip:**
1. Add new worksheets to an existing Microsoft Excel file.
2. Fill data into the cells of each new worksheet.
3. Activate a sheet in the workbook.
4. Save as a Microsoft Excel file.

Below, are parallel code snippets for VSTO (C#) and Aspose.Cells for .NET (C#), that show how to achieve these tasks.

**VSTO**

{{< highlight csharp >}}

// Initiate application object
Excel.Application excelApp = Application;

// Specify the template Excel file path.
string myPath = "Book1.xls";

// Open the Excel file.
excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,
    Missing.Value, Missing.Value,
    Missing.Value, Missing.Value,
    Missing.Value, Missing.Value,
    Missing.Value, Missing.Value,
    Missing.Value, Missing.Value,
    Missing.Value, Missing.Value);

// Declare a Worksheet object.
Excel.Worksheet newWorksheet;

// Add 5 new worksheets to the workbook and fill some data
// into the cells.
for (int i = 1; i < 6; i++) {
    // Add a worksheet to the workbook.
    newWorksheet = (Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value,
        Missing.Value, Missing.Value);

    // Name the sheet.
    newWorksheet.Name = "New_Sheet" + i.ToString();

    // Get the Cells collection.
    Excel.Range cells = newWorksheet.Cells;

    // Input a string value to a cell of the sheet.
    cells.set_Item(i, i, "New_Sheet" + i.ToString());
}

// Activate the first worksheet by default.
((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

// Save the Excel file.
excelApp.ActiveWorkbook.SaveCopyAs("out_Book1.xls");

// Quit the application.
excelApp.Quit();

{{< /highlight >}}

**Aspose.Cells**

{{< highlight csharp >}}
// Instantiate an instance of License and set the license file
// through its path
Aspose.Cells.License license = new Aspose.Cells.License();
license.SetLicense("Aspose.Total.lic");

// Specify the template Excel file path.
string myPath = "Book1.xls";

// Instantiate a new Workbook and open the Excel file.
Workbook workbook = new Workbook(myPath);

// Declare a Worksheet object.
Worksheet newWorksheet;

// Add 5 new worksheets to the workbook and fill some data
// into the cells.
for (int i = 0; i < 5; i++) {
    // Add a worksheet to the workbook.
    newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

    // Name the sheet.
    newWorksheet.Name = "New_Sheet" + (i + 1).ToString();

    // Get the Cells collection.
    Cells cells = newWorksheet.Cells;

    // Input a string value to a cell of the sheet.
    cells[i, i].PutValue("New_Sheet" + (i + 1).ToString());
}

// Activate the first worksheet by default.
workbook.Worksheets.ActiveSheetIndex = 0;

// Save the Excel file.
workbook.Save("out_My_Book1.xls");

{{< /highlight >}}
## **Download Sample Code**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Adding.New.Worksheets.to.Workbook.and.Activating.a.Sheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
