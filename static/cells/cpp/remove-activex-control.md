##Remove ActiveX Control with C++
Learn how to remove ActiveX Control from workbooks using Aspose.Cells for C++.
## **Remove ActiveX Control**
Aspose.Cells provides the ability to remove ActiveX Control from workbooks. For this, the API provides the [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/) method. The following code snippet demonstrates the use of the [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/) method to remove ActiveX Control.
## **Sample Code**
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
// Create a workbook
Workbook wb(srcDir + u"sampleUpdateActiveXComboBoxControl.xlsx");
// Access first shape from first worksheet
Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);
// Remove Shape ActiveX Control
shape.RemoveActiveXControl();
// Save the workbook
wb.Save(outDir + u"RemoveActiveXControl_out.xlsx");
std::cout << "ActiveX Control removed successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
