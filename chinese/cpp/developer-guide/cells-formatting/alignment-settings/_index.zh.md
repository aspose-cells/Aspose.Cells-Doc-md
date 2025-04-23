---
title: 用C++设置对齐方式
linktitle: 对齐设置
description: 在Aspose.Cells库中，您可以使用单元格对齐设置来调整文本的布局和显示。通过调整水平对齐、垂直对齐和文本换行等设置，您可以更好地控制文本在单元格中的流动。本文件将为您提供详细的步骤和样本代码，以帮助您快速掌握如何使用Aspose.Cells进行单元格对齐设置。
keywords: Aspose.Cells，单元格对齐，水平对齐，垂直对齐，文本换行
type: docs
weight: 20
url: /zh/cpp/cells-alignment-settings/
---

## **配置对齐设置**

### **Microsoft Excel中的对齐设置**

任何使用Microsoft Excel格式化单元格的人都会熟悉Microsoft Excel中的对齐设置。

从上面的图中可以看出，有不同种类的对齐选项：

- 文本对齐(水平和垂直)
- 缩进
- 方向
- 文本控制
- 文本方向

Aspose.Cells完全支持所有这些对齐设置，并在下面详细讨论。

### **Aspose.Cells中的对齐设置**

Aspose.Cells提供一个表示Excel文件的类[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)集合。[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)集合中的每个项表示[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类对象。

Aspose.Cells为[**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)和[**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)提供了[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的方法，用于获取和设置单元格的格式。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)类提供了有用的属性来配置对齐设置。

使用[**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/)枚举选择任何文本对齐类型。[**TextAlignmentType**](https://reference.aspose.com/cells/cpp/aspose.cells/textalignmenttype/)枚举中预定义的文本对齐类型包括：

|**文本对齐类型**|**描述**|
| :- | :- |
|Bottom|表示底部文本对齐
|Center|表示居中文本对齐
|CenterAcross|表示跨列居中文本对齐
|Distributed|表示分散文本对齐
|Fill|表示填充文本对齐
|General|表示常规文本对齐
|Justify|表示两端对齐文本对齐
|Left|表示左对齐文本对齐
|Right|表示右对齐文本对齐
|Top|表示顶部文本对齐|
|JustifiedLow|用于阿拉伯文本具有调整的卡什达长度。|
|ThaiDistributed|分布泰文，因为每个字符被视为一个单词。|

{{% alert color="primary" %}}

您还可以使用[**Style.IsJustifyDistributed**](https://reference.aspose.com/cells/cpp/aspose.cells/style/isjustifydistributed/)属性应用两端对齐分布设置。

{{% /alert %}}

#### **水平对齐**

使用[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)对象的[**GetHorizontalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gethorizontalalignment/)属性使文本水平对齐。

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

#### **垂直对齐**

与水平对齐类似，使用 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) 对象的 [**GetVerticalAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getverticalalignment/) 属性来垂直对齐文本。

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

#### **缩进**

可以使用 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) 对象的 [**GetIndentLevel()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getindentlevel/) 属性来设置单元格中文本的缩进级别。

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

#### **方向**

使用 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) 对象的 [**GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/) 属性来设置单元格中文本的方向（旋转）。

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

#### **文本控制**

以下部分讨论了如何通过设置文本换行、缩小以适应和其他格式设置选项来控制文本。

##### **自动换行文本**

在单元格中设置文本换行可使其更易读：单元格的高度会根据文本内容自动调整，而不会被截断或溢出到相邻单元格。可以使用 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) 对象的 [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) 属性来设置文本换行开或关闭。

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

##### **缩小以适应**

在单元格中设置文本字段换行的选项是缩小文本大小以适应单元格尺寸，可以通过将 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) 对象的 [**IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells/style/istextwrapped/) 属性设置为 **true** 来实现。

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

##### **合并单元格**

与 Microsoft Excel 一样，Aspose.Cells 支持将多个单元格合并为一个。Aspose.Cells 提供两种方法来完成此任务。一种方法是调用 [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) 集合的 [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) 方法。[**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) 方法接受以下参数来合并单元格：

- 第一行：开始合并的第一行。
- 第一列：开始合并的第一列。
- 行数：要合并的行数。
- 列数：要合并的列数。

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

另一种方法是首先调用 [**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/) 集合的 [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) 方法来创建要合并的单元格范围。[**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) 方法接受与上述 [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/merge/) 方法相同的参数集，并返回一个 [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) 对象。[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) 对象还提供一个 [**Merge**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) 方法，该方法合并 [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) 对象中指定的范围。

##### **文本方向**

可以设置单元格中文本的阅读顺序。阅读顺序是以字符、单词等显示的视觉顺序。例如，英语是从左到右的语言，而阿拉伯语是从右到左的语言。

阅读顺序是由 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) 对象的 [**GetTextDirection()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/gettextdirection/) 属性设置的。Aspose.Cells 在 [**TextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/textdirectiontype/) 枚举中提供了预定义的文本方向类型。

|**文本方向类型**|**描述**|
| :- | :- |
|Context|与第一个输入字符的语言一致的阅读顺序
|LeftToRight|从左到右的阅读顺序
|RightToLeft|从右到左的阅读顺序

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

## **高级主题**
- [更改单元格对齐方式并保留现有格式](/cells/zh/cpp/change-cells-alignment-and-keep-existing-formatting/)
- [换行和文本换行](/cells/zh/cpp/line-breaks-and-text-wrapping/)
