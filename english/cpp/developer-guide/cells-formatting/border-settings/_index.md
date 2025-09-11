---
title: Border Settings with C++
linktitle: Border Settings
description: How to use the Aspose.Cells library in C++ to set the border style and color of cells. By adjusting the width, style, and color of the border, you have more control over how cells look and appear.
keywords: Aspose.Cells, Cell Border Settings, C++, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /cpp/cells-border-settings/
---

## **Adding Borders to Cells**

Microsoft Excel allows users to format cells by adding borders. The type of border depends on where it is added. For example, a top border is one added to the top position of a cell. Users can also modify the borders' line style and color.

With Aspose.Cells, developers can add borders and customize what they look like in the same flexible way as in Microsoft Excel.

### **Adding Borders to Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class.

Aspose.Cells provides the [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) method in the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class. The [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) method is used to set a cell's formatting style. The [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) class provides properties for adding borders to cells.

#### **Adding Borders to a Cell**

Developers can add borders to a cell by using the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) collection. The border type is passed as an index to the [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) collection. All border types are pre-defined in the [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/) enumeration.

**Border enumeration**

| **Border Types** | **Description** |
|------------------|-----------------|
| BottomBorder     | A bottom border line |
| DiagonalDown     | A diagonal line from top left to right bottom |
| DiagonalUp       | A diagonal line from bottom left to right top |
| LeftBorder       | A left border line |
| RightBorder      | A right border line |
| TopBorder        | A top border line |

The [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) collection stores all borders. Each border in the [**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/) collection is represented by a [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/) object which provides two properties, [**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/) and [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) to set a border's line color and style respectively.

To set a border's line color, select a color using the Color enumeration and assign it to the Border object's Color property.

The border's line style is set by selecting a line style from the [**CellBorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellbordertype/) enumeration.

**CellBorderType enumeration**

| **Line Styles**       | **Description**               |
|------------------------|-------------------------------|
| DashDot               | Thin dash-dotted line         |
| DashDotDot            | Thin dash-dot-dotted line     |
| Dashed                | Dashed line                  |
| Dotted                | Dotted line                  |
| Double                | Double line                  |
| Hair                  | Hairline                     |
| MediumDashDot         | Medium dash-dotted line       |
| MediumDashDotDot      | Medium dash-dot-dotted line   |
| MediumDashed          | Medium dashed line            |
| None                  | No line                      |
| Medium                | Medium line                  |
| SlantedDashDot        | Slanted medium dash-dotted line |
| Thick                 | Thick line                   |
| Thin                  | Thin line                    |

Select one of the line styles and then assign it to the [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/) object's [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) property.

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
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Visit Aspose!");

    Style style = cell.GetStyle();

    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());

    cell.SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls");
    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

You should set both line style and color at the same time. The two diagonal border lines should have the same line style and color.

{{% /alert %}}

#### **Adding Borders to a Range of Cells**

It is also possible to add borders to a range of cells rather than just a single cell. To do so, first, create a range of cells by calling the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection's [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) method. It takes the following parameters:

- First Row, the first row of the range.
- First Column, represents the first column of the range.
- Number of Rows, the number of rows in the range.
- Number of Columns, the number of columns in the range.

The [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) method returns a [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) object, which contains the specified range of cells. The [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) object provides a [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) method that takes the following parameters to add a border to the range of cells:

- **Border Type**, the border type, selected from the [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/) enumeration.
- **Line Style**, the border line style, selected from the [**CellBorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellbordertype/) enumeration.
- **Color**, the line color, selected from the Color enumeration.

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

    // Obtain the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello World From Aspose");

    // Creating a range of cells starting from "A1" cell to 3rd column in a row
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 3);

    // Adding a thick top border with blue line
    range.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick bottom border with blue line
    range.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick left border with blue line
    range.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick right border with blue line
    range.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Thick, Color::Blue());

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}