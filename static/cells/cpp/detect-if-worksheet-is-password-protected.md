##Detect if Worksheet is Password Protected with C++
Learn how to detect if a worksheet is password protected using Aspose.Cells for C++.
It is possible to protect the workbooks and worksheets separately. For instance, a spreadsheet may contain one or more worksheets that are password-protected, however, the spreadsheet itself may or may not be protected. Aspose.Cells APIs provide the means to detect if a given worksheet is password protected or not. This article demonstrates the usage of Aspose.Cells for C++ API to achieve the same.
Aspose.Cells for C++ has exposed the [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) property to detect if a worksheet is password protected or not. Boolean type [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/cpp/aspose.cells/protection/isprotectedwithpassword/) property returns **true** if [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) is password-protected and **false** if not.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Create an instance of Workbook and load a spreadsheet
Workbook book(srcDir + u"sample.xlsx");
// Access the protected Worksheet
Worksheet sheet = book.GetWorksheets().Get(0);
// Check if Worksheet is password protected
if (sheet.GetProtection().IsProtectedWithPassword())
{
std::cout << "Worksheet is password protected" << std::endl;
}
else
{
std::cout << "Worksheet is not password protected" << std::endl;
}
Aspose::Cells::Cleanup();
return 0;
}
```
