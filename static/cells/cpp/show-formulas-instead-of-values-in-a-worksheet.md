##Show Formulas Instead of Values in a Worksheet with C++
This article provides sample code for using the C++ API to programmatically display formulas rather than values in an Excel worksheet or spreadsheet.
It is possible to show formulas instead of calculated values in Microsoft Excel using the **Show Formulas** option from the **Formulas** ribbon. When formulas are shown, Microsoft Excel displays formulas in the worksheet. You can achieve the same thing using Aspose.Cells.
Aspose.Cells provides a [**Worksheet.GetShowFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getshowformulas/) property. Set this to **true** to set Microsoft Excel to display formulas.
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
// Path of input excel file
U16String filePath = srcDir + u"source.xlsx";
// Load the source workbook
Workbook workbook(filePath);
// Access the first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Show formulas of the worksheet
worksheet.SetShowFormulas(true);
// Save the workbook
workbook.Save(outDir + u"out.xlsx");
std::cout << "Formulas shown successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
