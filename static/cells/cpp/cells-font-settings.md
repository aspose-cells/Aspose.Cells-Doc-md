##Font Settings with C++
Aspose.Cells is a C++ library for working with spreadsheet files. It supports setting the font settings of cells, allowing users to customize the font style and properties of cells. This article will introduce how to use the Aspose.Cells library to set cell font settings.
The look and feel of a text can be controlled by changing font settings. The font settings may include the name, style, size, color, and other effects of the fonts. Just like Microsoft Excel, Aspose.Cells also supports configuring the font settings of the cells.
## **Configuring Font Settings**
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection. Each item in the [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class.
Aspose.Cells provides the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class' [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) and [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) methods which are used to get and set a cell's formatting style. The [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) class provides properties for configuring font settings.
### **Setting Font Name**
Developers can apply any font to text inside a cell by using the [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) object's [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) property.
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
// Create a new workbook
Workbook workbook;
// Add a new worksheet to the workbook
int i = workbook.GetWorksheets().Add();
// Get the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.GetWorksheets().Get(i);
// Access the "A1" cell from the worksheet
Cell cell = worksheet.GetCells().Get(u"A1");
// Add some value to the "A1" cell
cell.PutValue(u"Hello Aspose!");
// Get the style of the cell
Style style = cell.GetStyle();
// Set the font name to "Times New Roman"
style.GetFont().SetName(u"Times New Roman");
// Apply the style to the cell
cell.SetStyle(style);
// Save the Excel file
workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);
std::cout << "Excel file saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Setting Font Style to Bold**
Developers can make text bold by setting the [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) object's [**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/) property to **true**.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
Aspose::Cells::Startup();
// Create a new workbook
Workbook workbook;
// Add a new worksheet to the workbook
int i = workbook.GetWorksheets().Add();
// Get the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.GetWorksheets().Get(i);
// Access the "A1" cell from the worksheet
Cell cell = worksheet.GetCells().Get(u"A1");
// Add some value to the "A1" cell
cell.PutValue(u"Hello Aspose!");
// Get the style of the cell
Style style = cell.GetStyle();
// Set the font weight to bold
style.GetFont().SetIsBold(true);
// Apply the style to the cell
cell.SetStyle(style);
// Save the Excel file
workbook.Save(u"out.xlsx");
std::cout << "Excel file saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
### **Setting Font Size**
Set the font size with the [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) object's [**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/) property.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
Aspose::Cells::Startup();
// Create a new workbook
Workbook workbook;
// Add a new worksheet to the workbook
int i = workbook.GetWorksheets().Add();
// Get the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.GetWorksheets().Get(i);
// Access the "A1" cell from the worksheet
Cell cell = worksheet.GetCells().Get(u"A1");
// Add some value to the "A1" cell
cell.PutValue(u"Hello Aspose!");
// Get the style of the cell
Style style = cell.GetStyle();
// Set the font size to 14
style.GetFont().SetSize(14);
// Apply the style to the cell
cell.SetStyle(style);
// Save the Excel file
workbook.Save(u"out.xlsx");
std::cout << "Excel file created successfully!" << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
### **Setting Font Color**
Use the [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) object's [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) property to set the font color. Select any color from the Color enumeration (part of the C++ framework) and assign it to the [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) property.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Create a new workbook
Workbook workbook;
// Add a new worksheet to the workbook
int i = workbook.GetWorksheets().Add();
// Get the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.GetWorksheets().Get(i);
// Access the "A1" cell from the worksheet
Cell cell = worksheet.GetCells().Get(u"A1");
// Add some value to the "A1" cell
cell.PutValue(u"Hello Aspose!");
// Get the style of the cell
Style style = cell.GetStyle();
// Set the font color to blue
style.GetFont().SetColor(Color::Blue());
// Apply the style to the cell
cell.SetStyle(style);
// Save the Excel file
workbook.Save(u"out.xlsx");
Aspose::Cells::Cleanup();
}
```
### **Setting Font Underline Type**
Use the [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) object's [**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/) property to underline text. Aspose.Cells offers various pre-defined font underline types in the [**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/) enumeration.
|**Font Underline Types**|**Description**|
| :- | :- |
|Accounting|A single accounting underline|
|Double|Double underline|
|DoubleAccounting|Double accounting underline|
|None|No underline|
|Single|A single underline|
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
// Create a new workbook
Workbook workbook;
// Add a new worksheet to the workbook
int i = workbook.GetWorksheets().Add();
// Get the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.GetWorksheets().Get(i);
// Access the "A1" cell from the worksheet
Cell cell = worksheet.GetCells().Get(u"A1");
// Add some value to the "A1" cell
cell.PutValue(u"Hello Aspose!");
// Get the style of the cell
Style style = cell.GetStyle();
// Set the font to be underlined
style.GetFont().SetUnderline(FontUnderlineType::Single);
// Apply the style to the cell
cell.SetStyle(style);
// Save the Excel file
workbook.Save(outDir + u"out.xlsx");
std::cout << "Excel file saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Setting Strikeout Effect**
Apply strikeout by setting the [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) object's [**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/) property to **true**.
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
int i = workbook.GetWorksheets().Add();
Worksheet worksheet = workbook.GetWorksheets().Get(i);
Cell cell = worksheet.GetCells().Get(u"A1");
cell.PutValue(u"Hello Aspose!");
Style style = cell.GetStyle();
style.GetFont().SetIsStrikeout(true);
cell.SetStyle(style);
workbook.Save(outDir + u"out.xlsx");
std::cout << "Excel file saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Setting Subscript Effect**
Apply subscript by setting the [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) object's [**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/) property to **true**.
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
// Create a new workbook
Workbook workbook;
// Add a new worksheet to the workbook
int i = workbook.GetWorksheets().Add();
// Obtain the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.GetWorksheets().Get(i);
// Access the "A1" cell from the worksheet
Cell cell = worksheet.GetCells().Get(u"A1");
// Add some value to the "A1" cell
cell.PutValue(u"Hello Aspose!");
// Obtain the style of the cell
Style style = cell.GetStyle();
// Set subscript effect
style.GetFont().SetIsSubscript(true);
// Apply the style to the cell
cell.SetStyle(style);
// Save the Excel file
workbook.Save(outDir + u"out.xlsx");
std::cout << "File saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Setting Superscript Effect on Font**
Developers can apply the superscript effect on the font by setting the [**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/) property of the [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) object to **true**.
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
// Create a new workbook
Workbook workbook;
// Add a new worksheet to the workbook
int i = workbook.GetWorksheets().Add();
// Obtain the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.GetWorksheets().Get(i);
// Access the "A1" cell from the worksheet
Cell cell = worksheet.GetCells().Get(u"A1");
// Add some value to the "A1" cell
cell.PutValue(u"Hello Aspose!");
// Obtain the style of the cell
Style style = cell.GetStyle();
// Set superscript effect
style.GetFont().SetIsSuperscript(true);
// Apply the style to the cell
cell.SetStyle(style);
// Save the Excel file
workbook.Save(outDir + u"out.xlsx");
std::cout << "Excel file saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Advance topics**
- [Apply Superscript and Subscript Effects on Fonts](https://docs.aspose.com/cells/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Get a List of Fonts used in a Spreadsheet or Workbook](https://docs.aspose.com/cells/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
