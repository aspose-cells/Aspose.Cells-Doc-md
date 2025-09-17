##Getting Headers or Footers with C++
This article explains how to programmatically get headers and footers from Excel or OpenOffice files using the C++ API or Library.
Headers and footers are displayed only in Page Layout view, Print Preview, and on printed pages.
You can also use the Page Setup dialog box if you want to view headers or footers for more than one worksheet at a time.
For other sheet types, such as chart sheets, or charts, you can insert headers and footers only by using the Page Setup dialog box.
## **Getting Headers and Footers in MS Excel**
1. Click the worksheet where you want to view or change headers or footers.
2. On the View tab, in the Workbook Views group, click Page Layout.
Excel displays the worksheet in Page Layout view.
3. To view or edit a header or footer, click the left, center, or right header or footer text box at the top or the bottom of the worksheet page (under Header, or above Footer).
## **Getting Headers and Footers using Aspose.Cells for C++**
With [**Worksheet.PageSetup.GetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheader/) and [**Worksheet.PageSetup.GetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfooter/) methods, C++ developers can simply get headers or footers from the file.
1. Construct Workbook to open the file.
2. Gets the worksheet where you want to get headers or footer.
3. Gets header or footer with specific section id.
```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
Workbook workbook(srcDir + u"HeaderFooter.xlsx");
Worksheet sheet = workbook.GetWorksheets().Get(0);
std::cout << sheet.GetPageSetup().GetHeader(0).ToUtf8() << std::endl;
std::cout << sheet.GetPageSetup().GetHeader(1).ToUtf8() << std::endl;
std::cout << sheet.GetPageSetup().GetHeader(2).ToUtf8() << std::endl;
std::cout << sheet.GetPageSetup().GetFooter(1).ToUtf8() << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
## **Parse Headers and Footers to Command List**
The header or footer text can contain special commands, for example a placeholder for the page number, current date or text formatting attributes.
Special commands are represented by a single letter with a leading ampersand ("&").
The header and footer strings are constructed using ABNF grammar. It's not easy to understand without a viewer.
Aspose.Cells for C++ provides [**Worksheet.PageSetup.GetCommands**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcommands/) method to parse headers and footers as command list.
The following code shows how to parse header or footer as command list and process commands:
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Instantiate a new Workbook
Workbook workbook(u"HeaderFooter.xlsx");
// Get the first worksheet
Worksheet sheet = workbook.GetWorksheets().Get(0);
// Get left section of header
U16String headerSection = sheet.GetPageSetup().GetHeader(0);
// Get commands from the header section
Vector<HeaderFooterCommand> commands = sheet.GetPageSetup().GetCommands(headerSection);
// Iterate through each command
for (int i = 0; i < commands.GetLength(); ++i)
{
HeaderFooterCommand c = commands[i];
switch (c.GetType())
{
case HeaderFooterCommandType::SheetName:
// Embedded the name of the sheet to header or footer
break;
default:
break;
}
}
Aspose::Cells::Cleanup();
return 0;
}
```
