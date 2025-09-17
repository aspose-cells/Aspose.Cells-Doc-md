##Remove duplicate rows in a Worksheet with C++
Learn how to remove duplicate rows in a worksheet using Aspose.Cells for C++.
Removing duplicate rows is one of Microsoft Excel's many useful features. It allows users to remove duplicate rows in a Worksheet, and you can pick which columns should be checked for duplicate information.
Aspose.Cells provides the `Cells::RemoveDuplicates()` method for this purpose. You can also set `startRow`, `startColumn`, `endRow`, and `endColumn` to pick up columns.
Following are the sample files which can be downloaded for testing this feature:
[removeduplicates.xlsx](removeduplicates.xlsx)
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create workbook
Workbook book(u"removeduplicates.xlsx");
// Remove duplicates from the first worksheet
book.GetWorksheets().Get(0).GetCells().RemoveDuplicates(0, 0, 5, 3);
// Save the result
book.Save(u"removeduplicates-result.xlsx");
std::cout << "Duplicates removed successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
