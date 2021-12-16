---
title: Border Settings
type: docs
weight: 30
url: /net/cells-border-settings/
---

## **Adding Borders to Cells**

Microsoft Excel allows users to format cells by adding borders. The type of border depends on where it is added. For example, a top border is one added to the top position of a cell. Users can also modify the borders' line style and color.

With Aspose.Cells, developers can add borders and customize what they look like in the same flexible way as in Microsoft Excel.

### **Adding Borders to Cells**

Aspose.Cells provides a class, [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class. The [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) class provides the [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/cells) collection. Each item in the [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/cells) collection represents an object of the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class.

Aspose.Cells provides the [**GetStyle**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) method in the [**Cell**](https://apireference.aspose.com/cells/net/aspose.cells/cell) class. The [**SetStyle**](https://apireference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) method is used to set a cell's formatting style. The [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) class provides properties for adding borders to cells.

#### **Adding Borders to a Cell**

Developers can add borders to a cell by using the [**Style**](https://apireference.aspose.com/cells/net/aspose.cells/style) object's [**Borders**](https://apireference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection. The border type is passed as an index to the [**Borders**](https://apireference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection. All border types are pre-defined in the [**BorderType**](https://apireference.aspose.com/cells/net/aspose.cells/bordertype) enumeration.

**Border enumeration**

|**Border Types**|**Description**|
| :- | :- |
|BottomBorder|A bottom border line|
|DiagonalDown|A diagonal line from top left to right bottom|
|DiagonalUp|A diagonal line from bottom left to right top|
|LeftBorder|A left border line|
|RightBorder|A right border line|
|TopBorder|A top border line|

The [**Borders**](https://apireference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [**Borders**](https://apireference.aspose.com/cells/net/aspose.cells/style/properties/borders) collection is represented by a [**Border**](https://apireference.aspose.com/cells/net/aspose.cells/border) object which provides two properties, [**Color**](https://apireference.aspose.com/cells/net/aspose.cells/border/properties/color) and [**LineStyle**](https://apireference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

To set a border's line color, select a color using the Color enumeration (part of the .NET Framework) and assign it to the Border object's Color property.

The border's line style is set by selecting a line style from the [**CellBorderType**](https://apireference.aspose.com/cells/net/aspose.cells/cellbordertype) enumeration.

**CellBorderType enumeration**

|**Line Styles**|**Description**|
| :- | :- |
|DashDot|Thin dash-dotted line|
|DashDotDot|Thin dash-dot-dotted line|
|Dashed|Dashed line|
|Dotted|Dotted line|
|Double|Double line|
|Hair|Hairline|
|MediumDashDot|Medium dash-dotted line|
|MediumDashDotDot|Medium dash-dot-dotted line|
|MediumDashed|Medium dashed line|
|None|No line|
|Medium|Medium line|
|SlantedDashDot|Slanted medium dash-dotted line|
|Thick|Thick line|
|Thin|Thin line|
Select one of the line styles and then assign it to the [**Border**](https://apireference.aspose.com/cells/net/aspose.cells/border) object's [**LineStyle**](https://apireference.aspose.com/cells/net/aspose.cells/border/properties/linestyle) property.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBordersToCells-1.cs" >}}

{{% alert color="primary" %}}

You should set both line style and color at the same time. The two diagonal border line should have the same line style and color.

{{% /alert %}}

#### **Adding Borders to a Range of Cells**

It is also possible to add borders to a range of cells rather than just a single cell. To do so, first, create a range of cells by calling the [**Cells**](https://apireference.aspose.com/cells/net/aspose.cells/cells) collection's [**CreateRange**](https://apireference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) method. It takes the following parameters:

- First Row, the first row of the range.
- First Column, represents the first column of the range.
- Number of Rows, the number of rows in the range.
- Number of Columns, the number of columns in the range.

The [**CreateRange**](https://apireference.aspose.com/cells/net/aspose.cells.cells/createrange/methods/1) method returns a [**Range**](https://apireference.aspose.com/cells/net/aspose.cells/range) object, which contains the specified range of cells. The [**Range**](https://apireference.aspose.com/cells/net/aspose.cells/range) object provides a [**SetOutlineBorder**](https://apireference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder) method that takes the following parameters to add a border to the range of cells:

- **Border Type**, the border type, selected from the [**BorderType**](https://apireference.aspose.com/cells/net/aspose.cells/bordertype) enumeration.
- **Line Style**, the border line style, selected from the [**CellBorderType**](https://apireference.aspose.com/cells/net/aspose.cells/cellbordertype) enumeration.
- **Color**, the line color, selected from the Color enumeration.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Borders-AddingBorderstoRange-1.cs" >}}

## **Colors and Palette**

A palette is the number of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97-2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills and lines in a chart.

With Aspose.Cells it is possible not only to use the palette's existing colors but also custom colors. Before using a custom color, add it to the palette first.

This topic discusses how to add custom colors to the palette.

### **Adding Custom Colors to Palette**

Aspose.Cells supports Microsoft Excel's 56 color palette. To use a custom color that is not defined in the palette, add the color to the palette.

Aspose.Cells provides a class, [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://apireference.aspose.com/cells/net/aspose.cells/workbook) class provides a [**ChangePalette**](https://apireference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) method that takes the following parameters to add a custom color to modify the palette:

- Custom Color, the custom color to be added.
- Index, the index of the color in the palette that the custom color will replace. Should be between 0-55.

The example below adds a custom color (Orchid) to the palette before applying it on a font.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

The palette only holds 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file formatted with the previous color is changed. So, when you change the palette, please be very careful. Moreover, this is the limitation in XLS (Excel 97 - 2003) file format only as there is no such limitation for XLSX or other advanced MS Excel (2007/2010 or 2013) file formats.

{{% /alert %}}


