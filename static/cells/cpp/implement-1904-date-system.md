##Implement 1904 Date System with C++
Aspose.Cells is a C++ library for working with spreadsheet files. It supports the implementation of the 1904 date system, allowing users to calculate and format based on the January 1, 1904 date system. This article describes how to implement the 1904 date system using the Aspose.Cells library.
Microsoft Excel supports two date systems: 1900 date system (the default date system implemented in Excel for Windows) and 1904 date system. The 1904 date system is normally used to provide compatibility with Macintosh Excel files and is the default system if you are using Excel for Macintosh. You can set the 1904 date system for Excel files using Aspose.Cells.
To implement 1904 date system in Microsoft Excel (for example Microsoft Excel 2003):
1. From the **Tools** menu, select **Options**, and select the **Calculation** tab.
1. Select the **1904 date system** option.
1. Click **OK**.
|**Selecting 1904 date system in Microsoft Excel**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|
See the following sample code on how to achieve this using Aspose.Cells APIs.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Path of input excel file
U16String inputFilePath = srcDir + u"book1.xlsx";
// Path of output excel file
U16String outputFilePath = outDir + u"Mybook.out.xlsx";
// Create workbook
Workbook workbook(inputFilePath);
// Implement 1904 date system
WorkbookSettings settings = workbook.GetSettings();
settings.SetDate1904(true);
// Save the excel file
workbook.Save(outputFilePath);
std::cout << "Excel file saved successfully with 1904 date system!" << std::endl;
Aspose::Cells::Cleanup();
}
```
