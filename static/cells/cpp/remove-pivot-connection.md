##Remove Pivot Connection with C++
Learn how to remove pivot connection with Aspose.Cells library using C++.
## **Possible Usage Scenarios**
If you want to disassociate slicer and pivot table in Excel, you need to right-click slicer and select "Report Connections..." item. In the option list, you can operate on the check box. Similarly, if you want to disassociate slicer and pivot table using Aspose.Cells API programmatically, please use the [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/removepivotconnection/) method. It will disassociate slicer and pivot table.
## **Disassociate slicer and pivot table**
The following sample code loads the [sample Excel file](remove-pivot-connection.xlsx) that contains an existing slicer. It accesses the slicers and then disassociates slicer and pivot table. Finally, it saves the workbook as [output Excel file](remove-pivot-connection-out.xlsx).
## **Sample Code**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Load sample Excel file containing slicer
U16String inputFilePath = u"remove-pivot-connection.xlsx";
Workbook wb(inputFilePath);
// Access first worksheet
Worksheet ws = wb.GetWorksheets().Get(0);
// Access the first PivotTable inside the PivotTable collection
PivotTable pivottable = ws.GetPivotTables().Get(0);
// Access the first slicer inside the slicer collection
Slicer slicer = ws.GetSlicers().Get(0);
// Remove PivotTable connection
slicer.RemovePivotConnection(pivottable);
// Save the workbook in output XLSX format
U16String outputFilePath = u"remove-pivot-connection-out.xlsx";
wb.Save(outputFilePath);
std::cout << "Pivot connection removed successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
