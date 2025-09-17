##Check if VBA Project is Protected and Locked for Viewing with C++
Learn how to check if VBA Project is protected and locked for viewing in Excel files using Aspose.Cells for C++.
## Check if VBA Project is Protected and Locked for Viewing in C++
Aspose.Cells allows you to check if the VBA (Visual Basic for Applications) Project of an Excel file is protected and locked for viewing. For this, the API provides the [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/) property. If it is locked for viewing, then the [**VbaProject.GetIslockedForViewing()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getislockedforviewing/) property returns **true**.
## **Sample Code**
The following sample code loads the [sample Excel file](43352065.xlsm) and checks if the VBA (Visual Basic for Applications) Project of the Excel file is protected and locked for viewing. Please also see its Console Output for a reference.
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
// Path of input Excel file
U16String inputFilePath = srcDir + u"sampleCheckifVBAProjectisProtected.xlsm";
// Load your source Excel file
Workbook wb(inputFilePath);
// Access the VBA project of the workbook
VbaProject vbaProject = wb.GetVbaProject();
// Check if "Lock project for viewing" is true or not
std::cout << "Is VBA Project Locked for Viewing: " << vbaProject.GetIslockedForViewing() << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Console Output**
This is the console output of the above sample code when executed with the provided [sample Excel file](43352065.xlsm).
Is VBA Project Locked for Viewing: True
