##Update references in other worksheets while deleting blank columns and rows in a worksheet with C++
Learn how to update references in other worksheets while deleting blank columns and rows in a worksheet using Aspose.Cells for C++.
When you delete blank columns and rows in a worksheet, its references in other worksheets become invalid. If you want to avoid this behavior and ensure that references to the current worksheet in other worksheets are also updated, use the [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) property and set it to **true**.
## **Update references in other worksheets while deleting blank columns and rows in a worksheet**
Please see the following sample code and its console output. The cell E3 in the second worksheet has a formula `=Sheet1!C3`, which refers to cell C3 in the first worksheet. If you set the [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) property to **true**, this formula will be updated to `=Sheet1!A1` after deleting blank columns and rows in the first worksheet. However, if you set the [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) property to **false**, the formula in cell E3 of the second worksheet will remain `=Sheet1!C3` and become invalid.
### **Programming Sample**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create workbook
Workbook wb;
// Add second sheet with name Sheet2
wb.GetWorksheets().Add(u"Sheet2");
// Access first sheet and add some integer value in cell C1
// Also add some value in any cell to increase the number of blank rows and columns
Worksheet sht1 = wb.GetWorksheets().Get(0);
sht1.GetCells().Get(u"C1").PutValue(4);
sht1.GetCells().Get(u"K30").PutValue(4);
// Access second sheet and add formula in cell E3 which refers to cell C1 in first sheet
Worksheet sht2 = wb.GetWorksheets().Get(1);
sht2.GetCells().Get(u"E3").SetFormula(u"'Sheet1'!C1");
// Calculate formulas of workbook
wb.CalculateFormula();
// Print the formula and value of cell E3 in second sheet before deleting blank columns and rows in Sheet1.
std::cout << "Cell E3 before deleting blank columns and rows in Sheet1." << std::endl;
std::cout << "--------------------------------------------------------" << std::endl;
std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;
// If you comment DeleteOptions.UpdateReference property below, then the formula in cell E3 in second sheet will not be updated
DeleteOptions opts;
opts.SetUpdateReference(true);
// Delete all blank rows and columns with delete options
sht1.GetCells().DeleteBlankColumns(opts);
sht1.GetCells().DeleteBlankRows(opts);
// Calculate formulas of workbook
wb.CalculateFormula();
// Print the formula and value of cell E3 in second sheet after deleting blank columns and rows in Sheet1.
std::cout << std::endl;
std::cout << std::endl;
std::cout << "Cell E3 after deleting blank columns and rows in Sheet1." << std::endl;
std::cout << "--------------------------------------------------------" << std::endl;
std::cout << "Cell Formula: " << sht2.GetCells().Get(u"E3").GetFormula().ToUtf8() << std::endl;
std::cout << "Cell Value: " << sht2.GetCells().Get(u"E3").GetStringValue().ToUtf8() << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Console Output**
This is the console output of the above sample code when the [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) property is set to **true**.
Cell E3 before deleting blank columns and rows in Sheet1.
Cell Formula: =Sheet1!C1
Cell Value: 4
Cell E3 after deleting blank columns and rows in Sheet1.
Cell Formula: =Sheet1!A1
Cell Value: 4
This is the console output of the above sample code when the [**DeleteOptions.GetUpdateReference()**](https://reference.aspose.com/cells/cpp/aspose.cells/deleteoptions/getupdatereference/) property is set to **false**. As you can see, the formula in cell E3 of the second worksheet is not updated, and its cell value is now 0 instead of 4, which is invalid.
Cell E3 before deleting blank columns and rows in Sheet1.
Cell Formula: =Sheet1!C1
Cell Value: 4
Cell E3 after deleting blank columns and rows in Sheet1.
Cell Formula: =Sheet1!C1
Cell Value: 0
