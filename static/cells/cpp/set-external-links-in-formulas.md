##Set External Links in Formulas with C++
Learn how to include links to external files in formulas using Aspose.Cells with C++.
Sometimes, it is necessary to include links to external files in formulas, for example, to evaluate a cell or range value against them. Aspose.Cells provides this feature and this document explains how to use it.
The sample code below shows how to include external files in formulas.
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
// Instantiate a new Workbook
Workbook workbook;
// Get first Worksheet
Worksheet sheet = workbook.GetWorksheets().Get(0);
// Get Cells collection
Cells cells = sheet.GetCells();
// Set formula with external links
cells.Get(u"A1").SetFormula(U16String(u"=SUM('[") + srcDir + u"book1.xlsx]Sheet1'!A2, '[" + srcDir + u"book1.xlsx]Sheet1'!A4)");
// Set formula with external links
cells.Get(u"A2").SetFormula(U16String(u"='[") + srcDir + u"book1.xlsx]Sheet1'!A8");
// Save the workbook
workbook.Save(outDir + u"output_out.xlsx");
std::cout << "Workbook saved successfully with external links!" << std::endl;
Aspose::Cells::Cleanup();
}
```
