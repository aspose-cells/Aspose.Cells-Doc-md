##Create, Access, and Copy Named Ranges with C++
Learn how to create, access, and copy named ranges in Excel files using Aspose.Cells with C++.
## **Introduction**
Normally, column and row labels are used to refer to individual cells. It is possible to create descriptive names to represent cells, ranges of cells, formulas, or constant values. The word **name** may refer to a string of characters that represents a cell, range of cells, formula, or constant value. Assigning a name to a range means that that range of cells can be referred to by its name. Use easy-to-understand names, such as Products, to refer to hard-to-understand ranges, such as Sales!C20:C30. Labels can be used in formulas that refer to data on the same worksheet; if you want to represent a range on another worksheet, you may use a name. *Named ranges are among the most powerful features of Microsoft Excel, especially when used as the source range for list controls, pivot tables, charts, and so on.
## **Working with Named Range Using Microsoft Excel**
### **Create Named Ranges**
The following steps describe how to name a cell or range of cells using **MS Excel**. This method applies to **Microsoft Office Excel 2003**, **Microsoft Excel 97**, **2000**, and **2002**.
1. Select the cell or range of cells that you want to name.
1. Click the **Name Box** at the left end of the formula bar.
1. Type the name for the cells.
1. Press ENTER.
You cannot name a cell while you are changing the contents of the cell.
## **Working with Named Range Using Aspose.Cells**
Here, we use the Aspose.Cells API to do the task.
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection.
### **Create Named Range**
It is possible to create a named range by calling the overloaded [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) method of the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. A typical version of the [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) method takes the following parameters:
- Name of the upper left cell, the name of the top left cell in the range.
- Name of the lower right cell, the name of the bottom right cell in the range.
When the [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) method is called, it returns the newly created range as an instance of the [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) class. Use this [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) object to configure the named range. For example, set the name of the range using the [**GetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/getname/) property. The following example shows how to create a named range of cells that extends over B4:G14.
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
U16String inputFilePath = srcDir + u"book1.xls";
// Path of output Excel file
U16String outputFilePath = outDir + u"output.out.xls";
// Create workbook
Workbook workbook(inputFilePath);
// Accessing the first worksheet in the Excel file
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Creating a named range
Range range = worksheet.GetCells().CreateRange(u"B4", u"G14");
// Setting the name of the named range
range.SetName(u"TestRange");
// Saving the modified Excel file
workbook.Save(outputFilePath);
std::cout << "Named range created and file saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Input Data into the Cells in the Named Range**
You can insert data into the individual cells of a range following the pattern:
- **C++**: Range(row, column)
Say you have a named range of cells that spans A1:C4. The matrix makes 4 * 3 = 12 cells. The individual range cells are arranged sequentially: Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).
Use the following properties to identify the cells in the range:
- FirstRow returns the index of the first row in the named range.
- FirstColumn returns the index of the first column in the named range.
- RowCount returns the total number of rows in the named range.
- ColumnCount returns the total number of columns in the named range.
The following example shows how to input some values into the cells of a specified range.
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
// Instantiate a new Workbook
Workbook workbook;
// Get the first worksheet in the workbook
Worksheet worksheet1 = workbook.GetWorksheets().Get(0);
// Create a range of cells based on H1:J4
Range range = worksheet1.GetCells().CreateRange(u"H1", u"J4");
// Name the range
range.SetName(u"MyRange");
// Input some data into cells in the range
range.Get(0, 0).PutValue(u"USA");
range.Get(0, 1).PutValue(u"SA");
range.Get(0, 2).PutValue(u"Israel");
range.Get(1, 0).PutValue(u"UK");
range.Get(1, 1).PutValue(u"AUS");
range.Get(1, 2).PutValue(u"Canada");
range.Get(2, 0).PutValue(u"France");
range.Get(2, 1).PutValue(u"India");
range.Get(2, 2).PutValue(u"Egypt");
range.Get(3, 0).PutValue(u"China");
range.Get(3, 1).PutValue(u"Philipine");
range.Get(3, 2).PutValue(u"Brazil");
// Save the excel file
workbook.Save(outDir + u"rangecells.out.xls");
std::cout << "Range cells created and saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Identify Cells in the Named Range**
You can insert data into the individual cells of a range following the pattern:
- **C++**: Range(row, column)
If you have a named range that spans A1:C4. The matrix makes 4 * 3 = 12 cells. The individual range cells are arranged sequentially: Range(0, 0), Range(0, 1), Range(0, 2), Range(1, 0), Range(1, 1), Range(1, 2), Range(2, 0), Range(2, 1), Range(2, 2), Range(3, 0), Range(3, 1), Range(3, 2).
Use the following properties to identify the cells in the range:
- FirstRow returns the index of the first row in the named range.
- FirstColumn returns the index of the first column in the named range.
- RowCount returns the total number of rows in the named range.
- ColumnCount returns the total number of columns in the named range.
The following example shows how to input some values into the cells of a specified range.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Path of input excel file
U16String inputFilePath = srcDir + u"book1.xls";
// Create workbook
Workbook workbook(inputFilePath);
// Get the specified named range
Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");
// Identify range cells
std::cout << "First Row : " << range.GetFirstRow() << std::endl;
std::cout << "First Column : " << range.GetFirstColumn() << std::endl;
std::cout << "Row Count : " << range.GetRowCount() << std::endl;
std::cout << "Column Count : " << range.GetColumnCount() << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Access Named Ranges**
#### **Access a Specific Named Range**
Call the [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection's [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) method to get a range by the specified name. A typical [**GetRangeByName**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getrangebyname/) method takes the name of the named range and returns the specified named range as an instance of the [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) class. The following example shows how to access a specified range by its name.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Path of input excel file
U16String inputFilePath = srcDir + u"book1.xls";
// Create workbook
Workbook workbook(inputFilePath);
// Getting the specified named range
Range range = workbook.GetWorksheets().GetRangeByName(u"TestRange");
if (range)
{
std::cout << "Named Range : " << range.GetRefersTo().ToUtf8() << std::endl;
}
Aspose::Cells::Cleanup();
}
```
#### **Access All the Named Ranges in a Spreadsheet**
Call the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection's [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) method to get all named ranges in a spreadsheet. The [**GetNamedRanges**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnamedranges/) method returns an array of all named ranges in the [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection.
The following example shows how to access all the named ranges in a workbook.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
U16String inputFilePath = srcDir + u"book1.xls";
Workbook workbook(inputFilePath);
WorksheetCollection sheets = workbook.GetWorksheets();
Vector<Range> ranges = sheets.GetNamedRanges();
std::cout << "Total Number of Named Ranges: " << ranges.GetLength() << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Copy Named Ranges**
Aspose.Cells provides the [**Range.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/) method to copy a range of cells with formatting into another range.
The following example shows how to copy a source range of cells to another named range.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
Workbook workbook;
Worksheet worksheet = workbook.GetWorksheets().Get(0);
Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");
range1.SetName(u"MyRange");
Color borderColor = Color{ 0,0, 0, 128 };
range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, borderColor);
range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, borderColor);
range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, borderColor);
range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, borderColor);
range1.Get(0, 0).PutValue(u"Test");
range1.Get(0, 4).PutValue(u"123");
Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");
range2.SetName(u"testrange");
range2.Copy(range1);
workbook.Save(outDir + u"copyranges.out.xls");
std::cout << "Ranges copied successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
