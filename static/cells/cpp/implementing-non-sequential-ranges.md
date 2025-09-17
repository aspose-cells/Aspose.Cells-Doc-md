##Implementing Non-Sequential Ranges with C++
Learn how to create named ranges with non-adjacent cells using Aspose.Cells with C++.
Normally, named ranges are rectangular with cells continuous and adjacent to each other. But sometimes, you may need to use a non-sequential cell range in which cells are not adjacent. Aspose.Cells supports creating a named range with non-adjacent cells.
The code sample below shows how to create a named non-sequential range with Aspose.Cells for C++.
```c++
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
// Create a new workbook
Workbook workbook;
// Adding a Name for non sequenced range
int index = workbook.GetWorksheets().GetNames().Add(u"NonSequencedRange");
// Get the added name
Name name = workbook.GetWorksheets().GetNames().Get(index);
// Creating a non sequence range of cells
name.SetRefersTo(u"=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6");
// Save the workbook
workbook.Save(outDir + u"Output.out.xlsx");
std::cout << "Workbook saved successfully with non-sequenced range!" << std::endl;
Aspose::Cells::Cleanup();
}
```
