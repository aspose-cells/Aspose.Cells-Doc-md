##Assign Macro to Form Control with C++
Learn how to assign a Macro Code to a Form Control like a Button using Aspose.Cells for C++.
Aspose.Cells allows you to assign a Macro Code to a Form Control like a Button. Please use the [**Shape.GetMacroName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getmacroname/) property to assign a new Macro Code to a Form Control inside the workbook.
The following sample code creates a new workbook, assigns a Macro Code to a Form Button, and saves the output in the XLSM format. Once you open the output XLSM file in Microsoft Excel, you will see the following macro code.
Sub ShowMessage()
MsgBox "Welcome to Aspose!"
End Sub
## **Assign Macro to Form Control in C++**
Here is the sample code to generate the output XLSM file with Macro Code.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Vba;
int main()
{
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
Workbook workbook;
Worksheet sheet = workbook.GetWorksheets().Get(0);
int moduleIdx = workbook.GetVbaProject().GetModules().Add(sheet);
VbaModule module = workbook.GetVbaProject().GetModules().Get(moduleIdx);
module.SetCodes(
u"Sub ShowMessage()\r\n"
u"    MsgBox \"Welcome to Aspose!\"\r\n"
u"End Sub"
);
Button button = sheet.GetShapes().AddButton(2, 0, 2, 0, 28, 80);
button.SetPlacement(PlacementType::FreeFloating);
button.GetFont().SetName(u"Tahoma");
button.GetFont().SetIsBold(true);
button.GetFont().SetColor(Color::Blue());
button.SetText(u"Aspose");
button.SetMacroName(sheet.GetName() + u".ShowMessage");
U16String outputPath = outDir + u"Output.out.xlsm";
workbook.Save(outputPath);
std::cout << "VBA button added successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
