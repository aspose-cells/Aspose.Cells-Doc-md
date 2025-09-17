##Get HTML5 String from Cell with C++
Learn how to get HTML5 string from a cell using Aspose.Cells for C++ API.
## **Possible Usage Scenarios**
Aspose.Cells returns the HTML string of the cell using the [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) method which accepts a boolean parameter. If you pass **false** as a parameter, it will return Normal HTML but if you pass **true** as a parameter, it will return HTML5 string.
## **Get HTML5 String from Cell**
The following sample code creates a workbook object and adds some text in cell A1 of the first worksheet. It then gets the Normal HTML and HTML5 string from cell A1 using the [**GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) method and prints them on the console.
## **Sample Code**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create workbook
Workbook wb;
// Access first worksheet
Worksheet ws = wb.GetWorksheets().Get(0);
// Access cell A1 and put some text inside it
Cell cell = ws.GetCells().Get(u"A1");
cell.PutValue(u"This is some text.");
// Get the Normal and Html5 strings
U16String strNormal = cell.GetHtmlString(false);
U16String strHtml5 = cell.GetHtmlString(true);
// Print the Normal and Html5 strings on console
std::cout << "Normal:\r\n" << strNormal.ToUtf8() << std::endl;
std::cout << std::endl;
std::cout << "Html5:\r\n" << strHtml5.ToUtf8() << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Console Output**
Normal:
Html5:
