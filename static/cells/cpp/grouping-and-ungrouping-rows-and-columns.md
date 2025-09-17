##Grouping and Ungrouping Rows and Columns with C++
Learn how to group and ungroup rows and columns in Excel files using Aspose.Cells with C++.
## **Introduction**
In a Microsoft Excel file, you can create an outline for the data to let you show and hide levels of detail with a single mouse click.
Click the **Outline Symbols**, 1,2,3, + and - to quickly display only the rows or columns that provide summaries or headings for sections in a worksheet, or you can use the symbols to see details under an individual summary or heading as shown below in the figure:
|**Grouping Rows and Columns.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|
## **Group Management of Rows and Columns**
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection that represents all cells in the worksheet.
The [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection provides several methods to manage rows or columns in a worksheet, few of these are discussed below in more detail.
### **Grouping Rows and Columns**
It is possible to group rows or columns by calling the [**GroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/grouprows/) and [**GroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/groupcolumns/) methods of the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Both methods take the following parameters:
- First row/column index, the first row or column in the group.
- Last row/column index, the last row or column in the group.
- Is hidden, a Boolean parameter that specifies whether to hide rows/columns after grouping or not.
```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Path of input Excel file
U16String inputFilePath = srcDir + u"book1.xls";
// Create workbook from file
Workbook workbook(inputFilePath);
// Access the first worksheet in the Excel file
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Group first six rows (from 0 to 5) and make them hidden
worksheet.GetCells().GroupRows(0, 5, true);
// Group first three columns (from 0 to 2) and make them hidden
worksheet.GetCells().GroupColumns(0, 2, true);
// Save the modified Excel file
U16String outputFilePath = srcDir + u"output.xls";
workbook.Save(outputFilePath);
std::cout << "Rows and columns grouped successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
#### **Group Settings**
Microsoft Excel allows you to configure group settings for displaying:
- Summary rows below detail.
- Summary columns to the right of detail.
Developers can configure these group settings using the [**GetOutline()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoutline/) property of the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class.
### **Summary Rows to Below of Detail**
It is possible to control whether summary rows are displayed below detail by setting the [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) class' [**GetSummaryRowBelow()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummaryrowbelow/) property to **true** or **false**.
```cpp
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
// Path of input Excel file
U16String inputFilePath = srcDir + u"sample.xlsx";
// Path of output Excel file
U16String outputFilePath = outDir + u"output.xls";
// Create workbook
Workbook workbook(inputFilePath);
// Get the first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Grouping first six rows and first three columns
worksheet.GetCells().GroupRows(0, 5, true);
worksheet.GetCells().GroupColumns(0, 2, true);
// Setting SummaryRowBelow property to false
worksheet.GetOutline().SetSummaryRowBelow(false);
// Save the modified Excel file
workbook.Save(outputFilePath);
std::cout << "Excel file modified and saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Summary Columns to Right of Detail**
Developers can also control displaying summary columns to the right of detail by setting the [**GetSummaryColumnRight()**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/getsummarycolumnright/) property of [**Outline**](https://reference.aspose.com/cells/cpp/aspose.cells/outline/) class to **true** or **false**.
```cpp
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
// Path of input Excel file
U16String inputFilePath = srcDir + u"sample.xlsx";
// Path of output Excel file
U16String outputFilePath = outDir + u"output.xls";
// Create workbook
Workbook workbook(inputFilePath);
// Get the first worksheet
WorksheetCollection sheets = workbook.GetWorksheets();
Worksheet worksheet = sheets.Get(0);
// Grouping first six rows and first three columns
worksheet.GetCells().GroupRows(0, 5, true);
worksheet.GetCells().GroupColumns(0, 2, true);
// Set summary column to the right
worksheet.GetOutline().SetSummaryColumnRight(true);
// Save the modified Excel file
workbook.Save(outputFilePath);
std::cout << "Excel file modified and saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Ungrouping Rows and Columns**
To ungroup any grouped rows or columns, call the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection's [**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) and [**UngroupColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungroupcolumns/) methods. Both methods take two parameters:
- First row or column index, the first row/column to be ungrouped.
- Last row or column index, the last row/column to be ungrouped.
[**UngroupRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/ungrouprows/) has an overload that takes a Boolean third parameter. Setting it to **true** removes all grouped information. Otherwise, only the outer group information is removed.
```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Path of input Excel file
U16String inputFilePath = srcDir + u"book1.xls";
// Create workbook from the input file
Workbook workbook(inputFilePath);
// Access the first worksheet in the Excel file
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Ungrouping first six rows (from 0 to 5)
worksheet.GetCells().UngroupRows(0, 5);
// Ungrouping first three columns (from 0 to 2)
worksheet.GetCells().UngroupColumns(0, 2);
// Save the modified Excel file
U16String outputFilePath = srcDir + u"output.xls";
workbook.Save(outputFilePath);
Aspose::Cells::Cleanup();
return 0;
}
```
