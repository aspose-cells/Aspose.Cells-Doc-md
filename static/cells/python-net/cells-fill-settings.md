##Fill Settings
Aspose.Cells is a Python library for working with spreadsheet files. It supports setting the fill settings of cells, allowing users to customize the background and style of cells. This article will introduce how to use the Aspose.Cells for Python via .NET library to set cell fill settings.
## **Colors and Background Patterns**
Microsoft Excel can set the foreground (outline) and background (fill) colors of cells and background patterns.
Aspose.Cells for Python via .NET also supports these features in a flexible manner. In this topic, we learn to use these features using Aspose.Cells.
### **Setting Colors and Background Patterns**
Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) class.
The [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) has the [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) and [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) methods that are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) class provides properties for setting the foreground and background colors of the cells. Aspose.Cells for Python via .NET provides a [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) enumeration that contains a set of pre-defined types of background patterns which are given below.
|**Background Patterns**|**Description**|
| :- | :- |
|DIAGONAL_CROSSHATCH|Represents diagonal crosshatch pattern|
|DIAGONAL_STRIPE|Represents diagonal stripe pattern|
|GRAY6|Represents 6.25% gray pattern|
|GRAY12|Represents 12.5% gray pattern|
|GRAY25|Represents 25% gray pattern|
|GRAY50|Represents 50% gray pattern|
|GRAY75|Represents 75% gray pattern|
|HORIZONTAL_STRIPE|Represents horizontal stripe pattern|
|NONE|Represents no background|
|REVERSE_DIAGONAL_STRIPE|Represents reverse diagonal stripe pattern|
|SOLID|Represents solid pattern|
|THICK_DIAGONAL_CROSSHATCH|Represents thick diagonal crosshatch pattern|
|THIN_DIAGONAL_CROSSHATCH|Represents thin diagonal crosshatch pattern|
|THIN_DIAGONAL_STRIPE|Represents thin diagonal stripe pattern|
|THIN_HORIZONTAL_CROSSHATCH|Represents thin horizontal crosshatch pattern|
|THIN_HORIZONTAL_STRIPE|Represents thin horizontal stripe pattern|
|THIN_REVERSE_DIAGONAL_STRIPE|Represents thin reverse diagonal stripe pattern|
|THIN_VERTICAL_STRIPE|Represents thin vertical stripe pattern|
|VERTICAL_STRIPE|Represents vertical stripe pattern|
In the example below, the foreground color of the A1 cell is set but A2 is configured to have both foreground and background colors with a vertical stripe background pattern.
### **Important to Know**
- To set a cell's foreground or background color, use the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object's [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) or [**background_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_color) properties. Both properties will take effect only if the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object's [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) property is configured.
- The [**foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) property sets the cell's shade color.
The [**pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) property specifies the type of background pattern used for the foreground or background color. Aspose.Cells for Python via .NET provides an enumeration, [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype). that contains a set of pre-defined types of background patterns.
- If you select *BackgroundType.None* value from the [**BackgroundType**](https://reference.aspose.com/cells/python-net/aspose.cells/backgroundtype) enumeration, the foreground color is not applied.
Likewise, the background color is not applied if you select the *BackgroundType.None* or *BackgroundType.Solid* values.
- When retrieving cell's shading/fill color, if [**Style.pattern**](https://reference.aspose.com/cells/python-net/aspose.cells/style/pattern) is *BackgroundType.None*, [**Style.foreground_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_color) will return *Color.Empty*.
### **Applying Gradient Fill Effects**
To apply your desired Gradient Fill Effects to the cell, use the [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) object's [**set_two_color_gradient**](https://reference.aspose.com/cells/python-net/aspose.cells/style/set_two_color_gradient) method accordingly.
## **Colors and Palette**
A palette is the number of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97-2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills and lines in a chart.
With Aspose.Cells for Python via .NET it is possible not only to use the palette's existing colors but also custom colors. Before using a custom color, add it to the palette first.
This topic discusses how to add custom colors to the palette.
### **Adding Custom Colors to Palette**
Aspose.Cells for Python via .NET supports Microsoft Excel's 56 color palette. To use a custom color that is not defined in the palette, add the color to the palette.
Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class provides a [**change_palette**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/change_palette) method that takes the following parameters to add a custom color to modify the palette:
- Custom Color, the custom color to be added.
- Index, the index of the color in the palette that the custom color will replace. Should be between 0-55.
The example below adds a custom color (Orchid) to the palette before applying it on a font.
The palette only holds 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file formatted with the previous color is changed. So, when you change the palette, please be very careful. Moreover, this is the limitation in XLS (Excel 97 - 2003) file format only as there is no such limitation for XLSX or other advanced MS Excel (2007/2010 or 2013) file formats.
