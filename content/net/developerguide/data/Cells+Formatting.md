+++
title = "Cells Formatting" 
description = "" 
weight = 12191 
+++

Aspose.Cells for .NET : Cells Formatting  

# Aspose.Cells for .NET : Cells Formatting


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Adding Borders to Cells](#CellsFormatting-AddingBorderstoCells)
    *   1.1 [Adding Borders to Cells](#CellsFormatting-AddingBorderstoCells.1)
        *   1.1.1 [Adding Borders to a Cell](#CellsFormatting-AddingBorderstoaCell)
        *   1.1.2 [Adding Borders to a Range of Cells](#CellsFormatting-AddingBorderstoaRangeofCells)
*   2 [Colors and Palette](#CellsFormatting-ColorsandPalette)
    *   2.1 [Adding Custom Colors to Palette](#CellsFormatting-AddingCustomColorstoPalette)
*   3 [Colors and Background Patterns](#CellsFormatting-ColorsandBackgroundPatterns)
    *   3.1 [Setting Colors and Background Patterns](#CellsFormatting-SettingColorsandBackgroundPatterns)
    *   3.2 [Important to Know](#CellsFormatting-ImportanttoKnow)
{{< /panel >}}
 

## Adding Borders to Cells

Microsoft Excel allows users to format cells by adding borders. The type of border depends on where it is added. For example, a top border is one added to the top position of a cell. Users can also modify the borders' line style and color.

With Aspose.Cells, developers can add borders and customize what they look like in the same flexible way as in Microsoft Excel.

### Adding Borders to Cells

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection. Each item in the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection represents an object of the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class.

Aspose.Cells provides the [GetStyle](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getstyle/index) method in the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell)class. The [SetStyle](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/setstyle/index) method is used to set a cell's formatting style. The [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) class provides properties for adding borders to cells.

#### Adding Borders to a Cell

Developers can add borders to a cell by using the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object's [Borders](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/borders) collection. The border type is passed as an index to the [Borders](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/borders) collection. All border types are pre-defined in the [BorderType](https://apireference.aspose.com/net/cells/aspose.cells/bordertype) enumeration.

**Border enumeration**

{{< table style="table-striped" >}}
|Border Types|Description|
|:----|:----|
|BottomBorder|A bottom border line|
|DiagonalDown|A diagonal line from top left to right bottom|
|DiagonalUp|A diagonal line from bottom left to right top|
|LeftBorder|A left border line|
|RightBorder|A right border line|
|TopBorder|A top border line|
{{< /table >}}

The [Borders](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/borders) collection stores all borders. Each border in the [Borders](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/borders) collection is represented by a [Border](https://apireference.aspose.com/net/cells/aspose.cells/border) object which provides two properties, [Color](https://apireference.aspose.com/net/cells/aspose.cells/border/properties/color) and [LineStyle](https://apireference.aspose.com/net/cells/aspose.cells/border/properties/linestyle) to set a border's line color and style respectively.

To set a border's line color, select a color using the `Color` enumeration (part of the .NET Framework) and assign it to the `Border` object's `Color` property.

The border's line style is set by selecting a line style from the [CellBorderType](https://apireference.aspose.com/net/cells/aspose.cells/cellbordertype) enumeration.

**CellBorderType enumeration**

{{< table style="table-striped" >}}
|Line Styles|Description|
|:----|:----|
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
{{< /table >}}

Select one of the line styles and then assign it to the [Border](https://apireference.aspose.com/net/cells/aspose.cells/border) object's [LineStyle](https://apireference.aspose.com/net/cells/aspose.cells/border/properties/linestyle) property.

You should set both line style and color at the same time. The two diagonal border line should have the same line style and color.

#### Adding Borders to a Range of Cells

It is also possible to add borders to a range of cells rather than just a single cell. To do so, first, create a range of cells by calling the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection's [CreateRange](https://apireference.aspose.com/net/cells/aspose.cells.cells/createrange/methods/1) method. It takes the following parameters:

*   First Row, the first row of the range.
*   First Column, represents the first column of the range.
*   Number of Rows, the number of rows in the range.
*   Number of Columns, the number of columns in the range.

The [CreateRange](https://apireference.aspose.com/net/cells/aspose.cells.cells/createrange/methods/1) method returns a [Range](https://apireference.aspose.com/net/cells/aspose.cells/range) object, which contains the specified range of cells. The [Range](https://apireference.aspose.com/net/cells/aspose.cells/range) object provides a [SetOutlineBorder](https://apireference.aspose.com/net/cells/aspose.cells/range/methods/setoutlineborder) method that takes the following parameters to add a border to the range of cells:

*   **Border Type**, the border type, selected from the [BorderType](https://apireference.aspose.com/net/cells/aspose.cells/bordertype) enumeration.
*   **Line Style**, the border line style, selected from the [CellBorderType](https://apireference.aspose.com/net/cells/aspose.cells/cellbordertype) enumeration.
*   **Color**, the line color, selected from the Color enumeration.

## Colors and Palette

A palette is the number of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97-2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills and lines in a chart.

With Aspose.Cells it is possible not only to use the palette's existing colors but also custom colors. Before using a custom color, add it to the palette first.

This topic discusses how to add custom colors to the palette.

### Adding Custom Colors to Palette

Aspose.Cells supports Microsoft Excel's 56 color palette. To use a custom color that is not defined in the palette, add the color to the palette.

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class provides a [ChangePalette](https://apireference.aspose.com/net/cells/aspose.cells/workbook/methods/changepalette) method that takes the following parameters to add a custom color to modify the palette:

*   Custom Color, the custom color to be added.
*   Index, the index of the color in the palette that the custom color will replace. Should be between 0-55.

The example below adds a custom color (Orchid) to the palette before applying it on a font.

Limitation in Excel 97-2003 format

The palette only holds 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file formatted with the previous color is changed. So, when you change the palette, please be very careful. Moreover, this is the limitation in XLS (Excel 97 - 2003) file format only as there is no such limitation for XLSX or other advanced MS Excel (2007/2010 or 2013) file formats.

## Colors and Background Patterns

Microsoft Excel can set the foreground (outline) and background (fill) colors of cells and background patterns.

Aspose.Cells also supports these features in a flexible manner. In this topic, we learn to use these features using Aspose.Cells.

### Setting Colors and Background Patterns

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/net/cells/aspose.cells/workbook) class contains a [Worksheets](https://apireference.aspose.com/net/cells/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class. The [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class provides a [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection. Each item in the [Cells](https://apireference.aspose.com/net/cells/aspose.cells/cells) collection represents an object of the [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) class.

The [Cell](https://apireference.aspose.com/net/cells/aspose.cells/cell) has the [GetStyle](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getstyle) and [SetStyle](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/setstyle) methods that are used to get and set a cell's formatting. The [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) class provides properties for setting the foreground and background colors of the cells. Aspose.Cells provides a [BackgroundType](https://apireference.aspose.com/net/cells/aspose.cells/backgroundtype) enumeration that contains a set of pre-defined types of background patterns which are given below.

{{< table style="table-striped" >}}
|Background Patterns|Description|
|:----|:----|
|DiagonalCrosshatch|Represents diagonal crosshatch pattern|
|DiagonalStripe|Represents diagonal stripe pattern|
|Gray6|Represents 6.25% gray pattern|
|Gray12|Represents 12.5% gray pattern|
|Gray25|Represents 25% gray pattern|
|Gray50|Represents 50% gray pattern|
|Gray75|Represents 75% gray pattern|
|HorizontalStripev|Represents horizontal stripe pattern|
|None|Represents no background|
|ReverseDiagonalStripe|Represents reverse diagonal stripe pattern|
|Solid|Represents solid pattern|
|ThickDiagonalCrosshatch|Represents thick diagonal crosshatch pattern|
|ThinDiagonalCrosshatch|Represents thin diagonal crosshatch pattern|
|ThinDiagonalStripe|Represents thin diagonal stripe pattern|
|ThinHorizontalCrosshatch|Represents thin horizontal crosshatch pattern|
|ThinHorizontalStripe|Represents thin horizontal stripe pattern|
|ThinReverseDiagonalStripe|Represents thin reverse diagonal stripe pattern|
|ThinVerticalStripe|Represents thin vertical stripe pattern|
|VerticalStripe|Represents vertical stripe pattern|
{{< /table >}}

In the example below, the foreground color of the A1 cell is set but A2 is configured to have both foreground and background colors with a vertical stripe background pattern.

### Important to Know

*   To set a cell's foreground or background color, use the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style) object's [ForegroundColor](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/foregroundcolor) or [BackgroundColor](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/backgroundcolor) properties. Both properties will take effect only if the [Style](https://apireference.aspose.com/net/cells/aspose.cells/style)object's [Pattern](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/pattern) property is configured.

*   The [ForegroundColor](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/foregroundcolor)property sets the cell's shade color.  
    The [Pattern](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/pattern)property specifies the type of background pattern used for the foreground or background color. Aspose.Cells provides an enumeration, [BackgroundType](https://apireference.aspose.com/net/cells/aspose.cells/backgroundtype). that contains a set of pre-defined types of background patterns.

*   If you select *BackgroundType.None* value from the [BackgroundType](https://apireference.aspose.com/net/cells/aspose.cells/backgroundtype)enumeration, the foreground color is not applied.  
    Likewise, the background color is not applied if you select the *BackgroundType.None* or *BackgroundType.Solid* values.
*   When retrieving cell's shading/fill color, if [Style.Pattern](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/pattern) is *BackgroundType.None*, [Style.ForegroundColor](https://apireference.aspose.com/net/cells/aspose.cells/style/properties/foregroundcolor) will return *Color.Empty*.

