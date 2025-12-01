---
title: Alignment Settings with C++
linktitle: Alignment Settings
description: In the Aspose.Cells library, you can use cell alignment settings to adjust the layout and display of text. By adjusting settings such as horizontal alignment, vertical alignment, and text wrapping, you have more control over how text flows in cells. This document will provide you with detailed steps and sample code to help you quickly grasp how to use Aspose.Cells for cell alignment settings.
keywords: Aspose.Cells, cell alignment, horizontal alignment, vertical alignment, text wrapping
type: docs
weight: 20
url: /cpp/cells-alignment-settings/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Configuring Alignment Settings**

### **Alignment settings in Microsoft Excel**

Anyone who has used Microsoft Excel to format cells will be familiar with the alignment settings in Microsoft Excel.

As you can see from the above figure, there are different kinds of alignment options:

- Text alignment(horizontal & vertical)
- Indentation.
- Orientation.
- Text control.
- Text direction.

All of these alignment settings are fully supported by Aspose.Cells and are discussed in more detail below.

### **Alignment settings in Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection. Each item in the [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class.

Aspose.Cells provides [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) and [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) methods for the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class that are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) class provides useful properties for configuring alignment settings.

Select any text alignment type using the [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) enumeration. The pre-defined text alignment types in the [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) enumeration are:

|**Text Alignment Types**|**Description**|
| :- | :- |
|Bottom|Represents bottom text alignment|
|Center|Represents center text alignment|
|CenterAcross|Represents center across text alignment|
|Distributed|Represents distributed text alignment|
|Fill|Represents fill text alignment|
|General|Represents general text alignment|
|Justify|Represents justify text alignment|
|Left|Represents left text alignment|
|Right|Represents right text alignment|
|Top|Represents top text alignment|
|JustifiedLow|Aligns the text with an adjusted kashida length for Arabic text.|
|ThaiDistributed|Distributes Thai text especially, because each character is treated as a word.|

{{% alert color="primary" %}}

You can also apply the justify distributed setting using the [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/cpp/aspose.cells/style/isjustifydistributed/) property.

{{% /alert %}}

#### **Horizontal Alignment**

Use the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's [**GetHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gethorizontalalignment/) property to align the text horizontally.

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

    // Create workbook
    Workbook workbook;

    // Obtain the reference of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Set the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Vertical Alignment**

Similar to horizontal alignment, use the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's [**GetVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getverticalalignment/) property to align the text vertically.

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

    // Create workbook
    Workbook workbook;

    // Clearing all the worksheets
    workbook.GetWorksheets().Clear();

    // Adding a new worksheet to the Excel object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Setting the horizontal alignment of the text in the "A1" cell
    Style style = cell.GetStyle();

    // Setting the vertical alignment of the text in a cell
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Indentation**

It is possible to set the indentation level of the text in a cell with the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's [**GetIndentLevel()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getindentlevel/) property.

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the indentation level
    style.SetIndentLevel(2);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Orientation**

Set the orientation (rotation) of the text in a cell with the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's [**GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) property.

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set the rotation angle of the text to 25 degrees
    style.SetRotationAngle(25);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook in Excel 97-2003 format
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Text Control**

The following section discusses how to control text by setting text wrapping, shrink to fit and other formatting options.

##### **Wrapping Text**

Wrapping text in a cell makes it easier to read: the height of the cell adjusts to fit all the text, instead of cutting it off or spilling over into adjacent cells. Set text wrapping on or off with the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) property.

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

    // Create Workbook Object
    Workbook wb;

    // Open first Worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get Worksheet Cells Collection
    Cells cell = ws.GetCells();

    // Increase the width of First Column Width
    cell.SetColumnWidth(0, 35);

    // Increase the height of first row
    cell.SetRowHeight(0, 36);

    // Add Text to the First Cell
    cell.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make Cell's Text wrap
    Style style = cell.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cell.Get(0, 0).SetStyle(style);

    // Save Excel File
    wb.Save(outDir + u"WrappingText_out.xlsx");

    std::cout << "Text wrapping applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Shrinking to Fit**

An option to wrapping text in a field is to shrink the text size to fit a cell's dimensions. This is done by setting the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) property to **true**.

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Get the cell's style
    Style style = cell.GetStyle();

    // Set shrink to fit
    style.SetShrinkToFit(true);

    // Apply the style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Merging Cells**

Like Microsoft Excel, Aspose.Cells supports merging several cells into one. Aspose.Cells provides two approaches to this task. One way is to call the [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection's [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) method. The [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) method takes the following parameters to merge the cells:

- First row: the first row from where to start merging.
- First column: the first column from where to start merging.
- Number of rows: the number of rows to merge.
- Number of columns: the number of columns to merge.

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

    // Create a Workbook
    Workbook wbk;

    // Create a Worksheet and get the first sheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Create a Cells object to fetch all the cells
    Cells cells = worksheet.GetCells();

    // Merge some Cells (C6:E7) into a single C6 Cell
    cells.Merge(5, 2, 2, 3);

    // Input data into C6 Cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a Style object to fetch the Style of C6 Cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Create a Font object
    Font font = style.GetFont();

    // Set the name
    font.SetName(u"Times New Roman");

    // Set the font size
    font.SetSize(18);

    // Set the font color
    font.SetColor(Color::Blue());

    // Bold the text
    font.SetIsBold(true);

    // Make it italic
    font.SetIsItalic(true);

    // Set the background color of C6 Cell to Red
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the Style to C6 Cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the Workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

The other way is to first call the [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection's [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) method to create a range of the cells to be merged. The [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) method takes the same set of parameters as that of the [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) method discussed above and returns a [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) object. The [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) object also provides a [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) method that merges the range specified in the [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) object.

##### **Text Direction**

It is possible to set the reading order of text in cells. The reading order is the visual order in which characters, words, etc. are displayed. For example, English is a left to right language while Arabic is a right to left language.

The reading order is set with the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's [**GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gettextdirection/) property. Aspose.Cells provides pre-defined text direction types in the [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/) enumeration.

|**Text Direction Types**|**Description**|
| :- | :- |
|Context|The reading order consistent with the language of the first entered character|
|LeftToRight|Left to right reading order|
|RightToLeft|Right to left reading order|

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"I am using the latest version of Aspose.Cells to test this functionality.");

    // Get the style of cell A1
    Style style = cell.GetStyle();

    // Set text direction to left-to-right
    style.SetTextDirection(TextDirectionType::LeftToRight);

    // Apply the modified style to the cell
    cell.SetStyle(style);

    // Save the workbook
    workbook.Save(u"book1.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Advance topics**
- [Change Cells Alignment and Keep Existing Formatting](/cells/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Line Breaks and Text Wrapping](/cells/cpp/line-breaks-and-text-wrapping/)
{{< app/cells/assistant language="cpp" >}}
