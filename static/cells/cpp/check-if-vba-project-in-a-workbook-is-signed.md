##Check if VBA project in a Workbook is Signed with C++
Check if VBA project in a Workbook is Signed using Aspose.Cells with C++.
You can check if your VBA project is signed or not using Microsoft Excel via **Tools > Digital Signatures...** menu command. Similarly, you can check it programmatically using Aspose.Cells [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned).
## **Check if VBA project in a Workbook is Signed in C++**
The following code loads the workbook and checks if its VBA project is signed using [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned) property. The property will return **true** if the project is signed otherwise it will return **false**.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Path of input excel file
U16String sampleFilePath = srcDir + u"Sample1.xlsx";
// Create workbook
Workbook workbook(sampleFilePath);
// Check if the VBA project is signed
bool isSigned = workbook.GetVbaProject().IsSigned();
std::wcout << u"VBA Project is Signed: " << (isSigned ? u"true" : u"false") << std::endl;
Aspose::Cells::Cleanup();
}
```
