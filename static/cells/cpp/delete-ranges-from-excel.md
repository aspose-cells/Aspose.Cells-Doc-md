##Delete Ranges from Excel with C++
Learn how to delete ranges in Excel using Aspose.Cells with C++.
## **Introduction**
In Excel, you can select a range, then delete it and shift other data left or up.
## **Delete Ranges Using Aspose.Cells**
Aspose.Cells provides [Cells.DeleteRange](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterange/) method to delete a range.
## **Delete Ranges And Shift Cells Left**
Delete a range and shift cells left as the following codes with Aspose.Cells:
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Instantiate a new Workbook.
Workbook workbook;
// Get all the worksheets in the book.
WorksheetCollection worksheets = workbook.GetWorksheets();
// Get the first worksheet in the worksheets collection.
Worksheet worksheet = worksheets.Get(0);
// Gets cells.
Cells cells = worksheet.GetCells();
// Input some data with some formatting into a few cells in the range.
cells.Get(u"C2").PutValue(u"C2");
cells.Get(u"C3").PutValue(u"C3");
CellArea ca = CellArea::CreateCellArea(u"B2", u"B3");
// Delete the specified range of cells and shift cells to the left.
cells.DeleteRange(ca.StartRow, ca.StartColumn, ca.EndRow, ca.EndColumn, ShiftType::Left);
// Check if the value in B2 is equal to "C2".
std::cout << (worksheet.GetCells().Get(u"B2").GetStringValue() == u"C2" ? "True" : "False") << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Delete Ranges And Shift Cells Up**
Delete a range and shift cells up as the following codes with Aspose.Cells:
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Instantiate a new Workbook.
Workbook workbook;
// Get all the worksheets in the book.
WorksheetCollection worksheets = workbook.GetWorksheets();
// Get the first worksheet in the worksheets collection.
Worksheet worksheet = worksheets.Get(0);
// Gets cells.
Cells cells = worksheet.GetCells();
// Input some data with some formatting into a few cells in the range.
cells.Get(u"B4").PutValue(u"B4");
cells.Get(u"B5").PutValue(u"B5");
// Creates a CellArea for the range B2:B3.
CellArea ca = CellArea::CreateCellArea(u"B2", u"B3");
// Deletes the specified range and shifts cells up.
cells.DeleteRange(ca.StartRow, ca.StartColumn, ca.EndRow, ca.EndColumn, ShiftType::Up);
// Check the value in cell B2 to verify the operation.
std::cout << (worksheet.GetCells().Get(u"B2").GetStringValue() == u"B4" ? "Success" : "Failure") << std::endl;
Aspose::Cells::Cleanup();
}
```
