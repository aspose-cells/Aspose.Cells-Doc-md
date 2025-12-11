---
title: Border Settings
description: How to use the Aspose.Cells library in C# to set the border style and color of cells. By adjusting the width, style, and color of the border, you have more control over how cells look and appear.
keywords: Aspose.Cells, Cell Border Settings, C#, Border Width, Border Style, Border Color
type: docs
weight: 40
url: /net/cells-border-settings/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Adding Borders to Cells**

Microsoft Excel allows users to format cells by adding borders. The type of border depends on where it is added. For example, a top border is one added to the top position of a cell. Users can also modify the borders' line style and color.

With Aspose.Cells, developers can add borders and customize how they look in the same flexible way as in Microsoft Excel.

### **Adding Borders to Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) class.

Aspose.Cells provides the [**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) method in the [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) class. The [**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) method is used to set a cell's formatting style. The [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) class provides properties for adding borders to cells.

#### **Adding Borders to a Cell**

Developers can add borders to a cell by using the [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) object's [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection. The border type is passed as an index to the [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection. All border types are pre‑defined in the [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) enumeration.

**Border enumeration**

|**Border Types**|**Description**|
| :- | :- |
|BottomBorder|A bottom border line|
|DiagonalDown|A diagonal line from top‑left to bottom‑right|
|DiagonalUp|A diagonal line from bottom‑left to top‑right|
|LeftBorder|A left border line|
|RightBorder|A right border line|
|TopBorder|A top border line|

The [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [**Borders**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection is represented by a [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) object which provides two properties, [**Color**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/color) and [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

To set a border's line color, select a color using the Color enumeration (part of the .NET Framework) and assign it to the Border object's Color property.

The border's line style is set by selecting a line style from the [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype) enumeration.

**CellBorderType enumeration**

|**Line Styles**|**Description**|
| :- | :- |
|DashDot|Thin dash‑dotted line|
|DashDotDot|Thin dash‑dot‑dotted line|
|Dashed|Dashed line|
|Dotted|Dotted line|
|Double|Double line|
|Hair|Hairline|
|MediumDashDot|Medium dash‑dotted line|
|MediumDashDotDot|Medium dash‑dot‑dotted line|
|MediumDashed|Medium dashed line|
|None|No line|
|Medium|Medium line|
|SlantedDashDot|Slanted medium dash‑dotted line|
|Thick|Thick line|
|Thin|Thin line|

Select one of the line styles and then assign it to the [**Border**](https://reference.aspose.com/cells/net/aspose.cells/border) object's [**LineStyle**](https://reference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

You should set both line style and color at the same time. The two diagonal border lines should have the same line style and color.

{{% /alert %}}

#### **Adding Borders to a Range of Cells**

It is also possible to add borders to a range of cells rather than just a single cell. To do so, first create a range of cells by calling the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection's [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) method. It takes the following parameters:

- First Row – the first row of the range.  
- First Column – the first column of the range.  
- Number of Rows – the number of rows in the range.  
- Number of Columns – the number of columns in the range.

The [**CreateRange**](https://reference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) method returns a [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) object, which contains the specified range of cells. The [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) object provides a [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) method that takes the following parameters to add a border to the range of cells:

- **Border Type** – the border type, selected from the [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype) enumeration.  
- **Line Style** – the border line style, selected from the [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype) enumeration.  
- **Color** – the line color, selected from the Color enumeration.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
