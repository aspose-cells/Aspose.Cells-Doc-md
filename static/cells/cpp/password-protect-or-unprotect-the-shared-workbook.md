##Password Protect or Unprotect the Shared Workbook with C++
Learn how to password protect or unprotect a shared workbook using Aspose.Cells for C++.
## **Possible Usage Scenarios**
You can protect or unprotect the shared workbook with Microsoft Excel as shown in the following screenshot. Aspose.Cells also supports this feature with the [**Workbook::ProtectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/protectsharedworkbook/) and [**Workbook::UnprotectSharedWorkbook()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/unprotectsharedworkbook/) methods.
![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)
## **Password Protect or Unprotect the Shared Workbook**
The following sample code creates a workbook and protects it while enabling sharing and saves it as [output Excel file](55541777.xlsx). The screenshot shows that when you try to unprotect it, Microsoft Excel prompts you to enter the password to unprotect it.
![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)
## **Sample Code**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create empty Excel file
Workbook wb;
// Protect the Shared Workbook with Password
wb.ProtectSharedWorkbook(u"1234");
// Uncomment this line to Unprotect the Shared Workbook
// wb.UnprotectSharedWorkbook(u"1234");
// Save the output Excel file
wb.Save(u"outputProtectSharedWorkbook.xlsx");
std::cout << "Shared workbook protection applied successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
