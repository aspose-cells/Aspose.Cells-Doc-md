##Password Protect the VBA Project of Excel Workbook with C++
Learn how to password protect the VBA Project of an Excel workbook using Aspose.Cells with C++.
## **Password Protect the VBA Project of Excel Workbook in C++**
You can password protect the VBA (Visual Basic for Applications) Project of a workbook with Aspose.Cells using the [**VbaProject.Protect()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/protect/) method.
## **Sample Code**
The following sample code loads the [sample Excel file](43352067.xlsm), accesses its VBA Project, and protects it with a password. Finally, it saves it as the [output Excel file](43352068.xlsm).
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Vba;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Path of input Excel file
U16String inputFilePath = srcDir + u"samplePasswordProtectVBAProject.xlsm";
// Path of output Excel file
U16String outputFilePath = outDir + u"outputPasswordProtectVBAProject.xlsm";
// Load the source Excel file
Workbook wb(inputFilePath);
// Access the VBA project of the workbook
VbaProject vbaProject = wb.GetVbaProject();
// Lock the VBA project for viewing with password
vbaProject.Protect(true, u"11");
// Save the output Excel file
wb.Save(outputFilePath);
std::cout << "VBA project password protected successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
