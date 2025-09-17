##Search and Replace Data in a Range with C++
This article shows how to search and replace data in a range in Excel using C++ code.
Sometimes you need to search for and replace specific data in a range, ignoring any cell values outside the desired range. Aspose.Cells allows you to limit a search to a specific range. This article explains how.
Aspose.Cells provides the [**FindOptions::SetRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/setrange/) method for specifying a range when searching data. The code sample below demonstrates how to search and replace data in a range.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Path of input excel file
U16String filePath = srcDir + u"input.xlsx";
// Create workbook
Workbook workbook(filePath);
// Get the first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Specify the range where you want to search
// Here the range is E9:H15
CellArea area = CellArea::CreateCellArea(u"E9", u"H15");
// Specify Find options
FindOptions opts;
opts.SetLookInType(LookInType::Values);
opts.SetLookAtType(LookAtType::EntireContent);
opts.SetRange(area);
Cell cell;
do
{
// Search the cell with value search within range
cell = worksheet.GetCells().Find(u"search", cell, opts);
// If no such cell found, then break the loop
if (!cell)
break;
// Replace the cell with value replace
cell.PutValue(u"replace");
} while (true);
// Save the workbook
U16String outputPath = srcDir + u"output.out.xlsx";
workbook.Save(outputPath);
std::cout << "Workbook saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
