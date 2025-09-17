##How to Control Sheet Tab Bar with C++
Learn how to Control Sheet Tab Bar through the Aspose.Cells for C++ API.
## **Possible Usage Scenarios**
When you need to adjust the display of the Excel sheet bar, you need to know how to control the sheet tab bar, such as hiding or showing the sheet tab bar, changing the sheet tab bar width, specifying the first visible tab, and so on. Aspose.Cells supports these features. Aspose.Cells provides the following properties and methods to help you achieve your goals.
- [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)
- [**WorkbookSettings.GetSheetTabBarWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getsheettabbarwidth/)
- [**WorkbookSettings.GetFirstVisibleTab()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getfirstvisibletab/)
## **How to Control Sheet Tab Bar using Aspose.Cells for C++**
This example shows how to:
1. Create a workbook.
1. Add data to cells in the first worksheet.
1. Display the sheet tab and set the width of the tab bar.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create a Workbook object
Workbook workbook;
// Obtain the reference to the newly added worksheet
Worksheet ws = workbook.GetWorksheets().Get(0);
Cells cells = ws.GetCells();
// Setting the value to the cells
Cell cell = cells.Get(u"A1");
cell.PutValue(u"Fruit");
cell = cells.Get(u"B1");
cell.PutValue(u"Count");
cell = cells.Get(u"C1");
cell.PutValue(u"Price");
cell = cells.Get(u"A2");
cell.PutValue(u"Apple");
cell = cells.Get(u"A3");
cell.PutValue(u"Mango");
cell = cells.Get(u"A4");
cell.PutValue(u"Blackberry");
cell = cells.Get(u"A5");
cell.PutValue(u"Cherry");
// Display the sheet tab and set the width of the tab bar
workbook.GetSettings().SetShowTabs(true);
workbook.GetSettings().SetSheetTabBarWidth(150);
// Save the workbook
workbook.Save(u"out.xlsx");
std::cout << "Workbook saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
Result file preview:
