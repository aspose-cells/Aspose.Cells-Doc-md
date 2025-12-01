---
title: Border Settings
description: How to use the Aspose.Cells for Python via .NET library in Python to set the border style and color of cells. By adjusting the width, style, and color of the border, you have more control over how cells look and appear.
keywords: Aspose.Cells for Python via .NET, Cell Border Settings, Python Border Width, Border Style, Border Color
type: docs
weight: 40
url: /python-net/cells-border-settings/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Adding Borders to Cells**

Microsoft Excel allows users to format cells by adding borders. The type of border depends on where it is added. For example, a top border is one added to the top position of a cell. Users can also modify the borders' line style and color.

With Aspose.Cells for Python via .NET, developers can add borders and customize what they look like in the same flexible way as in Microsoft Excel.

### **Adding Borders to Cells**

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class.

Aspose.Cells for Python via .NET provides the [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) method in the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class. The [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) method is used to set a cell's formatting style. The [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) class provides properties for adding borders to cells.

#### **Adding Borders to a Cell**

Developers can add borders to a cell by using the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object's [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection. The border type is passed as an index to the [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection. All border types are pre-defined in the [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) enumeration.

**Border enumeration**

|**Border Types**|**Description**|
| :- | :- |
|BOTTOM_BORDER|A bottom border line|
|DIAGONAL_DOWN|A diagonal line from top left to right bottom|
|DIAGONAL_UP|A diagonal line from bottom left to right top|
|LEFT_BORDER|A left border line|
|RIGHT_BORDER|A right border line|
|TOP_BORDER|A top border line|

The [**borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/python-net/aspose.cells/style/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) object which provides two properties, [**color**](https://reference.aspose.com/cells/python-net/aspose.cells/border/color) and [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) to set a border's line color and style respectively.

To set a border's line color, select a color using the Color enumeration (part of the .NET Framework) and assign it to the Border object's Color property.

The border's line style is set by selecting a line style from the [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype) enumeration.

**CellBorderType enumeration**

|**Line Styles**|**Description**|
| :- | :- |
|DASH_DOT|Thin dash-dotted line|
|DASH_DOT_DOT|Thin dash-dot-dotted line|
|DASHED|Dashed line|
|DOTTED|Dotted line|
|DOUBLE|Double line|
|HAIR|Hairline|
|MEDIUM_DASH_DOT|Medium dash-dotted line|
|MEDIUM_DASH_DOT_DOT|Medium dash-dot-dotted line|
|MEDIUM_DASHED|Medium dashed line|
|NONE|No line|
|MEDIUM|Medium line|
|SLANTED_DASH_DOT|Slanted medium dash-dotted line|
|THICK|Thick line|
|THIN|Thin line|
Select one of the line styles and then assign it to the [**Border**](https://reference.aspose.com/cells/python-net/aspose.cells/border) object's [**line_style**](https://reference.aspose.com/cells/python-net/aspose.cells/border/line_style) property.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBordersToCells-1.py" >}}

{{% alert color="primary" %}}

You should set both line style and color at the same time. The two diagonal border line should have the same line style and color.

{{% /alert %}}

#### **Adding Borders to a Range of Cells**

It is also possible to add borders to a range of cells rather than just a single cell. To do so, first, create a range of cells by calling the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection's [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) method. It takes the following parameters:

- First Row, the first row of the range.
- First Column, represents the first column of the range.
- Number of Rows, the number of rows in the range.
- Number of Columns, the number of columns in the range.

The [**create_range**](hhttps://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range/#str) method returns a [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) object, which contains the specified range of cells. The [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) object provides a [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border) method that takes the following parameters to add a border to the range of cells:

- **Border Type**, the border type, selected from the [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype) enumeration.
- **Line Style**, the border line style, selected from the [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype) enumeration.
- **Color**, the line color, selected from the Color enumeration.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Borders-AddingBorderstoRange-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
