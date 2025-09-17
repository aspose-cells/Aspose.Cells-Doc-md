##Get Max Range In A Worksheet with C++
This article describes how to get the max range, max data range, max display range of Excel files with Aspose.Cells for C++ library.
When reading data from the worksheet, we need to know the maximum area.
When copying all data from a worksheet, we need to know the maximum area.
When exporting a specified area to HTML and PDF, we need to know the maximum area.
Aspose.Cells for C++ contains different ways to find the max range in a worksheet.
## **Getting max range**
In Aspose.Cells, if the [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) and [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) objects are initialized, these rows and columns will be counted to the maximum area, even if there is no data in empty rows or columns.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create a workbook object and open the Excel file
Workbook workbook(u"Book1.xlsx");
// Get all the worksheets in the workbook
WorksheetCollection worksheets = workbook.GetWorksheets();
Worksheet sheet = worksheets.Get(0);
// Get the max data range
int maxRow = sheet.GetCells().GetMaxRow();
int maxColumn = sheet.GetCells().GetMaxColumn();
// Create a range from A1 to the max data range
Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);
// Set a null value in cell A10
sheet.GetCells().Get(u"A10").PutValue(nullptr);
// Update the max data range after modifying the sheet
maxRow = sheet.GetCells().GetMaxRow();
maxColumn = sheet.GetCells().GetMaxColumn();
// Update the range to include the new data
range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);
Aspose::Cells::Cleanup();
}
```
## **Getting max data range**
In most cases, we only need to obtain all the ranges containing all the data, even if the empty cells outside the range are formatted.
And the settings about shapes, tables, and pivot tables will be ignored.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Instantiate a new Workbook
Workbook workbook(u"Book1.xlsx");
// Get all the worksheets in the book
WorksheetCollection worksheets = workbook.GetWorksheets();
Worksheet sheet = worksheets.Get(0);
// Gets the max data range
int maxRow = sheet.GetCells().GetMaxDataRow();
int maxColumn = sheet.GetCells().GetMaxDataColumn();
// The range is A1:B3
Range range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);
// Put null value in cell A10
sheet.GetCells().Get(u"A10").PutValue(nullptr);
// Update max data range after modification
maxRow = sheet.GetCells().GetMaxDataRow();
maxColumn = sheet.GetCells().GetMaxDataColumn();
// The range is still A1:B3
range = sheet.GetCells().CreateRange(0, 0, maxRow + 1, maxColumn + 1);
Aspose::Cells::Cleanup();
}
```
## **Getting max display range**
When we export all data from the worksheet to HTML, PDF, or images, we need to obtain an area containing all visible objects, including data, styles, graphics, tables, and pivot tables.
The following codes show how to render the max display range to HTML:
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Path of input Excel file
U16String inputFilePath = srcDir + u"Book1.xlsx";
// Path of output HTML file
U16String outputFilePath = outDir + u"html.html";
// Instantiate a new Workbook
Workbook workbook(inputFilePath);
// Get all the worksheets in the book
WorksheetCollection worksheets = workbook.GetWorksheets();
// Get the max display range of the first worksheet
Range range = worksheets.Get(0).GetCells().GetMaxDisplayRange();
// Create HtmlSaveOptions to configure the export
HtmlSaveOptions saveOptions;
saveOptions.SetExportActiveWorksheetOnly(true);
// Set the export area to the range of the first worksheet
CellArea exportArea = CellArea::CreateCellArea(range.GetFirstRow(), range.GetFirstColumn(),
range.GetFirstRow() + range.GetRowCount() - 1,
range.GetFirstColumn() + range.GetColumnCount() - 1);
saveOptions.SetExportArea(exportArea);
// Save the range to HTML
workbook.Save(outputFilePath, saveOptions);
std::cout << "Range saved to HTML successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
Here is [source excel file](Book1.xlsx).
