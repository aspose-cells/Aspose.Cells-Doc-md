##Check if VBA Code is Signed with C++
Learn how to check if VBA code in Excel files is signed using Aspose.Cells with C++.
Aspose.Cells allows the user to check if the VBA code project is signed or not. Please use the [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) property to check if the VBA code project is signed or not.
The following code explains how to check if the VBA code is signed or not using the [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) property. You can use any of your Excel files to test this code. For testing purposes, you can use [this excel file used in the code](5115032.xlsm).
## **Check if VBA Code is Signed in C++**
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
// Path of input Excel file
U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";
// Create workbook
Workbook workbook(inputFilePath);
// Check if the VBA code project is signed
std::wcout << U"Is VBA Code Project Signed: " << workbook.GetVbaProject().IsSigned() << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
## Console Output
Below is the console output of the above code using the [sample excel file](5115032.xlsm) provided by the link.
Is VBA Code Project Signed: True
