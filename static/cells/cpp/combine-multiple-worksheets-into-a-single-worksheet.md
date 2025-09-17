##Combine Multiple Worksheets into a Single Worksheet with C++
Learn how to combine multiple worksheets into a single worksheet using Aspose.Cells with C++.
Sometimes, you need to combine multiple worksheets into a single worksheet. This can easily be achieved using Aspose.Cells API. This article will show you a code example that reads a source workbook and combines the data of all source worksheets into a single worksheet inside a destination workbook.
The following code snippet shows you how to combine multiple worksheets into a single worksheet.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
//For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
//Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
//Path of input excel file
U16String filePath = srcDir + u"SampleInput.xlsx";
//Create workbook from the input file
Workbook workbook(filePath);
//Create a destination workbook
Workbook destWorkbook;
//Get the first worksheet of the destination workbook
Worksheet destSheet = destWorkbook.GetWorksheets().Get(0);
//Variable to maintain total row count during copy
int32_t totalRowCount = 0;
//Iterate through each worksheet in the source workbook
for (int32_t i = 0; i < workbook.GetWorksheets().GetCount(); i++)
{
Worksheet sourceSheet = workbook.GetWorksheets().Get(i);
//Get the display range of the source sheet
Range sourceRange = sourceSheet.GetCells().GetMaxDisplayRange();
//Create a range in the destination sheet according to the source range
Range destRange = destSheet.GetCells().CreateRange(sourceRange.GetFirstRow() + totalRowCount,
sourceRange.GetFirstColumn(), sourceRange.GetRowCount(), sourceRange.GetColumnCount());
//Copy data from source range to destination range
destRange.Copy(sourceRange);
//Update the total row count for the next iteration
totalRowCount += sourceRange.GetRowCount();
}
//Save the destination workbook to the output path
U16String outputFilePath = srcDir + u"Output.out.xlsx";
destWorkbook.Save(outputFilePath);
std::cout << "Workbook processed and saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
