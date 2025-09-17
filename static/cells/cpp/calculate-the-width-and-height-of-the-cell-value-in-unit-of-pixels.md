##Measure the Width and Height of the Cell Value in Unit of Pixels with C++
Learn how to Measure the Width and Height of the Cell Value in Unit of Pixels through the Aspose.Cells for C++ API.
Sometimes you need to calculate the width and height of cell value to fit the cell value inside the cell. Aspose.Cells provides [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) and [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) methods for this purpose. By using these methods you can calculate width and height of the cell value and then set the width of the column and height of the row of that cell respectively and this will then adjust or fit the cell value inside the cell.
Alternatively, you can also [autofit rows and columns of your cell or range of cells](https://docs.aspose.com/cells/cpp/autofit-rows-and-columns/) using Aspose.Cells APIs.
The following code explains the use of [**Cell.GetWidthOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getwidthofvalue/) and [**Cell.GetHeightOfValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getheightofvalue/) methods.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
// Create workbook object
Workbook workbook;
// Access first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Access cell B2 and add some value inside it
Cell cell = worksheet.GetCells().Get(u"B2");
cell.PutValue(u"Welcome to Aspose!");
// Enlarge its font to size 16
Style style = cell.GetStyle();
style.GetFont().SetSize(16);
cell.SetStyle(style);
// Calculate the width and height of the cell value in unit of pixels
int32_t widthOfValue = cell.GetWidthOfValue();
int32_t heightOfValue = cell.GetHeightOfValue();
// Print both values
std::wcout << u"Width of Cell Value: " << widthOfValue << std::endl;
std::wcout << u"Height of Cell Value: " << heightOfValue << std::endl;
// Set the row height and column width to adjust/fit the cell value inside cell
worksheet.GetCells().SetColumnWidthPixel(1, widthOfValue);
worksheet.GetCells().SetRowHeightPixel(1, heightOfValue);
// Save the output excel file
U16String outFilePath = u"output_out.xlsx";
workbook.Save(outFilePath);
Aspose::Cells::Cleanup();
}
```
## **Advance topics**
- [Get Text Width of Cell Value](https://docs.aspose.com/cells/cpp/get-text-width-of-cell-value/)
