##Add Cells to Microsoft Excel Formula Watch Window with C++
Learn how to use Aspose.Cells for C++ to add cells to the formula watch window in Excel. Load or create an Excel file, manipulate cells, set formulas, and save the modified file.
## **Possible Usage Scenarios**
Microsoft Excel Watch Window is a useful tool to conveniently monitor cell values and their formulas in a window. You can open the *Watch Window* in Microsoft Excel by clicking *Formulas > Watch Window*. It has the *Add Watch* button that can be used to add cells for inspection. Similarly, you can use the [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellwatchcollection/add/) method to add cells to the *Watch Window* using Aspose.Cells API.
## **Add Cells to Microsoft Excel Formula Watch Window**
The following sample code sets the formula of cells C1 and E1 and adds both of them to the Watch Window. It then saves the workbook as an [output Excel file](67338481.xlsx). If you open the output Excel file and view the *Watch Window*, you will see both cells as shown in this screenshot.
![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)
## **Sample Code**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
Aspose::Cells::Startup();
// Create empty workbook
Workbook wb;
// Access first worksheet
Worksheet ws = wb.GetWorksheets().Get(0);
// Put some integer values in cell A1 and A2
ws.GetCells().Get(u"A1").PutValue(10);
ws.GetCells().Get(u"A2").PutValue(30);
// Access cell C1 and set its formula
Cell c1 = ws.GetCells().Get(u"C1");
c1.SetFormula(u"=Sum(A1,A2)");
// Add cell C1 into cell watches by name
ws.GetCellWatches().Add(c1.GetName());
// Access cell E1 and set its formula
Cell e1 = ws.GetCells().Get(u"E1");
e1.SetFormula(u"=A2*A1");
// Add cell E1 into cell watches by its row and column indices
ws.GetCellWatches().Add(e1.GetRow(), e1.GetColumn());
// Save workbook to output XLSX format
wb.Save(u"outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat::Xlsx);
std::cout << "Workbook saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
