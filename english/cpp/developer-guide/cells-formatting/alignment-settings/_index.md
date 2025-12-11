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

- Text alignment (horizontal & vertical)
- Indentation.
- Orientation.
- Text control.
- Text direction.

All of these alignment settings are fully supported by Aspose.Cells and are discussed in more detail below.

### **Alignment settings in Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection. Each item in the [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class.

Aspose.Cells provides [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) and [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) methods for the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class that are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) class provides useful properties for configuring alignment settings.

Select any text alignment type using the [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) enumeration. The pre‑defined text alignment types in the [**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/) enumeration are:

| **Text Alignment Types** | **Description** |
| :- | :- |
| Bottom | Represents bottom text alignment |
| Center | Represents center text alignment |
| CenterAcross | Represents center‑across text alignment |
| Distributed | Represents distributed text alignment |
| Fill | Represents fill text alignment |
| General | Represents general text alignment |
| Justify | Represents justify text alignment |
| Left | Represents left text alignment |
| Right | Represents right text alignment |
| Top | Represents top text alignment |
| JustifiedLow | Aligns the text with an adjusted kashida length for Arabic text |
| ThaiDistributed | Distributes Thai text especially since each character is treated as a word |

{{% alert color="primary" %}}

You can also apply the justify distributed setting using the [**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/cpp/aspose.cells/style/isjustifydistributed/) property.

{{% /alert %}}

#### **Horizontal Alignment**

Use the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's **SetHorizontalAlignment()** method to align the text horizontally.

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

Similar to horizontal alignment, use the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's **SetVerticalAlignment()** method to align the text vertically.

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

    // Clear all the worksheets
    workbook.GetWorksheets().Clear();

    // Add a new worksheet to the workbook
    int i = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by its index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add some value to the "A1" cell
    cell.PutValue(u"Visit Aspose!");

    // Set the vertical alignment of the text in the "A1" cell
    Style style = cell.GetStyle();
    style.SetVerticalAlignment(TextAlignmentType::Center);
    cell.SetStyle(style);

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Indentation**

It is possible to set the indentation level of the text in a cell with the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's **SetIndentLevel()** method.

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

Set the orientation (rotation) of the text in a cell with the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's **SetRotationAngle()** method.

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

    // Save the workbook in Excel 97‑2003 format
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **Text Control**

The following section discusses how to control text by setting text wrapping, shrink‑to‑fit, and other formatting options.

##### **Wrapping Text**

Wrapping text in a cell makes it easier to read: the height of the cell adjusts to fit all the text, instead of cutting it off or spilling over into adjacent cells. Set text wrapping on or off with the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's **SetIsTextWrapped()** method.

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

    // Create Workbook object
    Workbook wb;

    // Open the first worksheet in the workbook
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Get worksheet cells collection
    Cells cells = ws.GetCells();

    // Increase the width of the first column
    cells.SetColumnWidth(0, 35);

    // Increase the height of the first row
    cells.SetRowHeight(0, 36);

    // Add text to the first cell
    cells.Get(0, 0).PutValue(u"I am using the latest version of Aspose.Cells to test this functionality");

    // Make the cell's text wrap
    Style style = cells.Get(0, 0).GetStyle();
    style.SetIsTextWrapped(true);
    cells.Get(0, 0).SetStyle(style);

    // Save Excel file
    wb.Save(outDir + u"WrappingText_out.xlsx");

    std::cout << "Text wrapping applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **Shrinking to Fit**

An alternative to wrapping text in a cell is to shrink the text size to fit the cell's dimensions. This is done by setting the **SetShrinkToFit()** property of the Style object to **true**.

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

Like Microsoft Excel, Aspose.Cells supports merging several cells into one. Aspose.Cells provides two approaches to this task.

**Approach 1 – Using `Cells.Merge`**

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

    // Create a workbook
    Workbook wbk;

    // Get the first worksheet
    Worksheet worksheet = wbk.GetWorksheets().Get(0);

    // Get the cells collection
    Cells cells = worksheet.GetCells();

    // Merge cells C6:E7 into a single cell (C6)
    cells.Merge(5, 2, 2, 3);

    // Input data into the merged cell
    worksheet.GetCells().Get(5, 2).PutValue(u"This is my value");

    // Create a style for the merged cell
    Style style = worksheet.GetCells().Get(5, 2).GetStyle();

    // Set font properties
    Font font = style.GetFont();
    font.SetName(u"Times New Roman");
    font.SetSize(18);
    font.SetColor(Color::Blue());
    font.SetIsBold(true);
    font.SetIsItalic(true);

    // Set background color
    style.SetForegroundColor(Color::Red());
    style.SetPattern(BackgroundType::Solid);

    // Apply the style to the merged cell
    worksheet.GetCells().Get(5, 2).SetStyle(style);

    // Save the workbook
    wbk.Save(outDir + u"mergingcells.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

**Approach 2 – Using `Cells.CreateRange`**

The other way is to first call the `Cells.CreateRange` method to create a range of the cells to be merged. The `CreateRange` method takes the same set of parameters as `Merge` and returns a `Range` object. The `Range` object also provides a `Merge` method that merges the specified range.

##### **Text Direction**

It is possible to set the reading order of text in cells. The reading order is the visual order in which characters, words, etc., are displayed. For example, English is a left‑to‑right language while Arabic is a right‑to‑left language.

The reading order is set with the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's **SetTextDirection()** method. Aspose.Cells provides pre‑defined text direction types in the [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/) enumeration.

| **Text Direction Types** | **Description** |
| :- | :- |
| Context | The reading order consistent with the language of the first entered character |
| LeftToRight | Left‑to‑right reading order |
| RightToLeft | Right‑to‑left reading order |

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

    // Set text direction to left‑to‑right
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

## **Advanced topics**
- [Change Cells Alignment and Keep Existing Formatting](/cells/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Line Breaks and Text Wrapping](/cells/cpp/line-breaks-and-text-wrapping/)
{{< app/cells/assistant language="cpp" >}}
