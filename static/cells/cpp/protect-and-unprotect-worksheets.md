##Protect and Unprotect Worksheet with C++
Protect and unprotect worksheet of Excel files with Aspose.Cells for C++.
To prevent other users from accidentally or deliberately changing, moving, or deleting data in a worksheet, you can lock the cells on your Excel worksheet and then protect the sheet with a password.
## **Protect and Unprotect Worksheet in MS Excel**
1. Click **Review > Protect Worksheet**.
1. Enter a password in **the Password box**.
1. Select **allow** options.
1. Select **OK**, re-enter the password to confirm it, and then select **OK** again.
## **Protect Worksheet Using Aspose.Cells for C++**
Only need the following simple lines of code to implement protecting workbook structure of Excel files.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create a new workbook
Workbook workbook;
// Get the first worksheet
Worksheet sheet = workbook.GetWorksheets().Get(0);
// Protect contents of the worksheet
sheet.Protect(ProtectionType::Contents);
// Protect worksheet with password
sheet.GetProtection().SetPassword(u"test");
// Save as Excel file
workbook.Save(u"Book1.xlsx");
std::cout << "Workbook created and protected successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Unprotect Worksheet Using Aspose.Cells for C++**
Unprotecting worksheet is easy with Aspose.Cells API. If worksheet is password-protected, a correct password is required.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create a new workbook
Workbook workbook(u"Book1.xlsx");
// Get the first worksheet
Worksheet sheet = workbook.GetWorksheets().Get(0);
// Unprotect the worksheet with password
sheet.Unprotect(u"password");
// Save the workbook
workbook.Save(u"Book1.xlsx");
std::cout << "Worksheet unprotected successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Advance topics**
- [Advanced Protection Settings since Excel XP](https://docs.aspose.com/cells/cpp/advanced-protection-settings-since-excel-xp/)
- [Detect if Worksheet is Password Protected](https://docs.aspose.com/cells/cpp/detect-if-worksheet-is-password-protected/)
- [Protecting Worksheets](https://docs.aspose.com/cells/cpp/protecting-worksheets/)
- [Unprotect a Worksheet](https://docs.aspose.com/cells/cpp/unprotect-a-worksheet/)
- [Verify Password Used to Protect the Worksheet](https://docs.aspose.com/cells/cpp/verify-password-used-to-protect-the-worksheet/)
