##Get Max Column Index in Row and Max Row Index in Column with C++
Learn how to Get Max Column Index in Row and Max Row Index in Column through the Aspose.Cells for C++ API.
## **Possible Usage Scenarios**
When you only need to manipulate some data on the rows or columns, you need to know the data range of rows and columns. Aspose.Cells offers this feature. To obtain the maximum column index on a row, you can obtain the [Row.GetLastCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/) and [Row.GetLastDataCell()](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/) properties, and then use the [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) property to obtain the maximum column index and maximum data column index. But in order to obtain the maximum row index and maximum row data index on a column, you need to create a range on the column, then traverse the range to find the last cell, and finally obtain the [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) attribute on the cell.
Aspose.Cells provides the following properties and methods to help you achieve your goals.
- [**Row.GetLastCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastcell/)
- [**Row.GetLastDataCell()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/getlastdatacell/)
- [**Cell.GetColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/)
- [**Cell.GetRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/)
## **Get Max Column Index in Row and Max Row Index in Column using Aspose.Cells**
This example shows how to:
1. Load the [sample file](sample.xlsx).
1. Get the row that needs to get the maximum column index and maximum data column index.
1. Get [Cell.GetColumn()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcolumn/) attribute on the cell.
1. Create a range based on column.
1. Get iterator and traverse range.
1. Get [Cell.GetRow()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getrow/) attribute on the cell.
```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
U16String filePath = srcDir + u"sample.xlsx";
Workbook workbook(filePath);
Worksheet sheet = workbook.GetWorksheets().Get(0);
Cells cells = sheet.GetCells();
Row row = cells.CheckRow(1);
if (row)
{
std::cout << "Max column index in row: " << row.GetLastCell().GetColumn() << std::endl;
std::cout << "Max data column index in row: " << row.GetLastDataCell().GetColumn() << std::endl;
}
Range columnRange = cells.CreateRange(1, 1, true);
auto colIter = columnRange.GetEnumerator();
int maxRow = 0;
int maxDataRow = 0;
while (colIter.MoveNext())
{
Cell currCell = colIter.GetCurrent();
if (!currCell.GetStringValue().IsEmpty())
{
maxDataRow = currCell.GetRow();
}
if (!currCell.GetStringValue().IsEmpty() || currCell.GetHasCustomStyle())
{
maxRow = currCell.GetRow();
}
}
std::cout << "Max row index in Column: " << maxRow << std::endl;
std::cout << "Max data row index in Column: " << maxDataRow << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
