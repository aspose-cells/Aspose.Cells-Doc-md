---
title: Font Settings with C++
linktitle: Font Settings
type: docs
weight: 30
url: /cpp/cells-font-settings/
description: Aspose.Cells is a C++ library for working with spreadsheet files. It supports setting the font settings of cells, allowing users to customize the font style and properties of cells. This article will introduce how to use the Aspose.Cells library to set cell font settings.
keywords: Aspose.Cells, Cells, Font Settings, Styles, Properties
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

The look and feel of a text can be controlled by changing font settings. The font settings may include the name, style, size, color, and other effects of the fonts. Just like Microsoft Excel, Aspose.Cells also supports configuring the font settings of the cells.

{{% /alert %}}

## **Configuring Font Settings**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a **GetCells()** collection. Each item in the **GetCells()** collection represents an object of the **Cell** class.

Aspose.Cells provides the **Cell** class's **GetStyle** and **SetStyle** methods which are used to get and set a cell's formatting style. The [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) class provides properties for configuring font settings.

### **Setting Font Name**

Developers can apply any font to text inside a cell by using the **Style.GetFont()** object's **SetName()** method.

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

Developers can make text bold by setting the **Style.GetFont()** object's **IsBold** property to **true**.

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

Set the font size using the **Style.GetFont()** object's **SetSize()** method.

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

Use the **Style.GetFont()** object's **SetColor()** method to set the font color. Select any color from the `Color` enumeration (part of the C++ framework) and assign it to the method.

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

Use the **Style.GetFont()** object's **SetUnderline()** method to underline text. Aspose.Cells offers various pre‑defined font underline types in the **FontUnderlineType** enumeration.

| **Font Underline Types** | **Description**                     |
| ------------------------ | ----------------------------------- |
| Accounting               | A single accounting underline       |
| Double                   | Double underline                    |
| DoubleAccounting         | Double accounting underline         |
| None                     | No underline                        |
| Single                   | A single underline                  |

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

Apply strikeout by setting the **Style.GetFont()** object's **IsStrikeout** property to **true**.

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

Apply subscript by setting the **Style.GetFont()** object's **IsSubscript** property to **true**.

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

Developers can apply the superscript effect on the font by setting the **IsSuperscript** property of the **Style.GetFont()** object to **true**.

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

## **Advanced topics**
- [Apply Superscript and Subscript Effects on Fonts](/cells/cpp/apply-superscript-and-subscript-effects-on-fonts/)
- [Get a List of Fonts used in a Spreadsheet or Workbook](/cells/cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
{{< app/cells/assistant language="cpp" >}}
