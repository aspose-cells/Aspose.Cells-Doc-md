---
title: 用C++设置字体
linktitle: 字体设置
type: docs
weight: 30
url: /zh/cpp/cells-font-settings/
description: Aspose.Cells是一个用于处理电子表格文件的C++库。它支持设置单元格的字体，允许用户自定义单元格的字体样式和属性。本文将介绍如何使用Aspose.Cells库设置单元格字体。
keywords: Aspose.Cells, Cells, 字体设置, 样式, 属性
---

{{% alert color="primary" %}}

通过更改字体设置，可以控制文本的外观。字体设置包括字体名称、样式、大小、颜色及其他效果。就像微软Excel一样，Aspose.Cells也支持配置单元格的字体设置。

{{% /alert %}}

## **配置字体设置**

Aspose.Cells提供了一个类，[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)，它代表了一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)集合。[**GetCells()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getcells/)集合中的每个项代表了[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的对象。

Aspose.Cells提供了[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的[**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)和[**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)方法，用于获取和设置单元格的格式样式。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)类提供了用于配置字体设置的属性。

### **设置字体名称**

开发者可以通过使用 [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) 对象的 [GetName()](https://reference.aspose.com/cells/cpp/aspose.cells/font/getname/) 属性，为单元格内的文本应用任何字体。

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

### **将字体样式设置为粗体**

开发人员通过将[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)对象的[**IsBold**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isbold/)属性设置为**true**来使文本加粗。

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

### **设置字体大小**

使用[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)对象的[**GetSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getsize/)属性设置字体大小。

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

### **设置字体颜色**

使用 [**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) 对象的 [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) 属性设置字体颜色。从颜色枚举（C++框架的一部分）中选择任意颜色并赋值给 [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getcolor/) 属性。

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

### **设置字体下划线类型**

使用[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)对象的[**GetUnderline()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getunderline/)属性给文本添加下划线。Aspose.Cells在[**FontUnderlineType**](https://reference.aspose.com/cells/cpp/aspose.cells/fontunderlinetype/)枚举中提供了各种预定义的字体下划线类型。

|**字体下划线类型**|**描述**|
| :- | :- |
|Accounting| 单下划线|
|Double| 双下划线|
|DoubleAccounting| 双帐目下划线|
|None| 无下划线|
|Single| 单下划线|

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

### **设置删除线效果**

通过将[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)对象的[**IsStrikeout**](https://reference.aspose.com/cells/cpp/aspose.cells/font/isstrikeout/)属性设置为**true**应用删除线。

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

### **设置下标效果**

通过将[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)对象的[**IsSubScript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issubscript/)属性设置为**true**应用下标。

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

### **在字体上设置上标效果**

开发人员可以通过将[**Style.GetFont()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/)对象的[**IsSuperscript**](https://reference.aspose.com/cells/cpp/aspose.cells/font/issuperscript/)属性设置为**true**在字体上应用上标效果。

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

## **高级主题**
- [在字体上应用上标和下标效果](/cells/zh/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [获取电子表格或工作簿中使用的字体列表](/cells/zh/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="cpp" >}}
