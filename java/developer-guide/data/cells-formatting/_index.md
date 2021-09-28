---
title: Cells Formatting
type: docs
weight: 30
url: /java/cells-formatting/
---

## **Adding Borders to Cells**
Microsoft Excel allows users to format cells by adding borders.

**Borders settings in Microsoft Excel** 

![todo:image_alt_text](cells-formatting_1.png)

The type of border depends on where it is added. For example, a top border is one added to the top position of a cell. Users can also modify the borders' line style and color.

With Aspose.Cells, developers can add borders and customize what they look like in the same flexible way they can in Microsoft Excel.
### **Adding Borders to Cells**
Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) class contains a [WorksheetCollection](https://apireference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/cells/java/com.aspose.cells/Worksheet) class. The [Worksheet](https://apireference.aspose.com/cells/java/com.aspose.cells/Worksheet) class provides a [Cells](https://apireference.aspose.com/cells/java/com.aspose.cells/Cells) collection. Each item in the [Cells](https://apireference.aspose.com/cells/java/com.aspose.cells/Cells) collection represents an object of the [Cell](https://apireference.aspose.com/cells/java/com.aspose.cells/cell) class.

Aspose.Cells provides the [setStyle](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) method in the [Cell](https://apireference.aspose.com/cells/java/com.aspose.cells/cell) class used to set a cell's formatting style. Also, the object of the [Style](https://apireference.aspose.com/cells/java/com.aspose.cells/Style) class is used and provides properties for configuring font settings.
#### **Adding Borders to a Cell**
Add borders to a cell with the [Style](https://apireference.aspose.com/cells/java/com.aspose.cells/Style) object's [setBorder](https://apireference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) method. The border type is passed as a parameter. All border types are pre-defined in the [BorderType](https://apireference.aspose.com/cells/java/com.aspose.cells/BorderType) enumeration.

|**Border Types**|**Description**|
| :- | :- |
|[BOTTOM_BORDER](https://apireference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|The bottom border line|
|[DIAGONAL_DOWN](https://apireference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|A diagonal line from top left to right bottom|
|[DIAGONAL_UP](https://apireference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|A diagonal line from bottom left to right top|
|[LEFT_BORDER](https://apireference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|The left border line|
|[RIGHT_BORDER](https://apireference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|The right border line|
|[TOP_BORDER](https://apireference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|The top border line|
|[HORIZONTAL](https://apireference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|Only for dynamic style, such as conditional formatting.|
|[VERTICAL](https://apireference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|Only for dynamic style, such as conditional formatting.|
To set the line color, select a color using the [Color](https://apireference.aspose.com/cells/java/com.aspose.cells/Color) enumeration and pass it to the [Style](https://apireference.aspose.com/cells/java/com.aspose.cells/Style) object's [setBorder](https://apireference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) method's Color parameter. The line styles are pre-defined in the [CellBorderType](https://apireference.aspose.com/cells/java/com.aspose.cells/CellBorderType) enumeration.

|**Line Styles**|**Description**|
| :- | :- |
|[DASH_DOT](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|Represents thin dash-dotted line|
|[DASH_DOT_DOT](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|Represents thin dash-dot-dotted line|
|[DASHED](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|Represents dashed line|
|[DOTTED](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|Represents dotted line|
|[DOUBLE](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|Represents double line|
|[HAIR](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|Represents hair line|
|[MEDIUM_DASH_DOT](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|Represents medium dash-dotted line|
|[MEDIUM_DASH_DOT_DOT](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|Represents medium dash-dot-dotted line|
|[MEDIUM_DASHED](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|Represents medium dashed line|
|[NONE](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|Represents no line|
|[MEDIUM](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|Represents medium line|
|[SLANTED_DASH_DOT](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|Represents slanted medium dash-dotted line|
|[THICK](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|Represents thick line|
|[THIN](https://apireference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|Represents thin line|
Select one of the above line styles and then assign it to the [Style](https://apireference.aspose.com/cells/java/com.aspose.cells/Style) object's [setBorder](https://apireference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) method.

The following output is generated when executing the code below.

**Borders applied on all sides of a cell** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **Adding Borders to a Range of Cells**
It is possible to add borders to a range of cells rather than just a single cell. First, create a range of cells by calling the [Cells](https://apireference.aspose.com/cells/java/com.aspose.cells/Cells) collection's [createRange](https://apireference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) method, which takes the following parameters:

- **First Row**, the first row of the range.
- **First Column**, the first column of the range.
- **Number of Rows**, the number of rows in the range.
- **Number of Columns**, the number of columns in the range.

The [createRange](https://apireference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) method returns a [Range](https://apireference.aspose.com/cells/java/com.aspose.cells/Range) object, which contains the specified range. The [Range](https://apireference.aspose.com/cells/java/com.aspose.cells/Range) object provides a [setOutlineBorders](https://apireference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)) method that takes the following parameters:

- **CellBorderType**, the border line style, selected from the [CellBorderType](https://apireference.aspose.com/cells/java/com.aspose.cells/CellBorderType) enumeration.
- **Color**, the border line color, selected from the [Color](https://apireference.aspose.com/cells/java/com.aspose.cells/Color) enumeration.

The following output is generated when executing the code below.

**Borders applied on a range of cells** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **Colors and Palette**
A palette is the number of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97-2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills and lines in a chart.

**Palette settings in Microsoft Excel** 

![todo:image_alt_text](cells-formatting_4.png)

With Aspose.Cells it is not only possible to use existing colors but also custom colors. Before using a custom color, add it to the palette. This topic explains how to add custom colors to the palette.
### **Adding Custom Colors to Palette**
Aspose.Cells also supports a palette of 56 colors. A standard color palette is shown above. If you want to use a custom color that is not defined in the palette then you will need to add that color to the palette before usage.

{{% alert color="primary" %}} 

The palette only holds 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file formatted with the previous color is changed. So, when you change the palette, please be very careful. Moreover, this is the limitation in XLS (Excel 97 - 2003) file format only as there is no such limitation for XLSX or other advanced MS Excel (2007/2010) file formats.

{{% /alert %}} 

Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook), that represents a Microsoft Excel file. The class provides the [changePalette](https://apireference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)) method that takes the following parameters to add a custom color to modify the palette:

- **Custom color**, the custom color to be added to the palette.
- **Index**, the index of the color that will be replaced with the custom color. Should be between 0-55.

The example below adds a custom color to the palette before applying it on a font.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **Colors and Background Patterns**
Microsoft Excel can set the foreground (outline) and background (fill) colors of cells and background patterns as shown below.

**Setting colors and background Patterns in Microsoft Excel** 

![todo:image_alt_text](cells-formatting_5.png)

Aspose.Cells also supports these features in a flexible manner. In this topic, we learn to use these features using Aspose.Cells.
### **Setting Colors & Background Patterns**
Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) class contains a [WorksheetCollection](https://apireference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/cells/java/com.aspose.cells/Worksheet) class. The [Worksheet](https://apireference.aspose.com/cells/java/com.aspose.cells/Worksheet) class provides a [Cells](https://apireference.aspose.com/cells/java/com.aspose.cells/Cells) collection. Each item in the [Cells](https://apireference.aspose.com/cells/java/com.aspose.cells/Cells) collection represents an object of the [Cell](https://apireference.aspose.com/cells/java/com.aspose.cells/cell) class.

Aspose.Cells provides the [setStyle](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) method in the [Cell](https://apireference.aspose.com/cells/java/com.aspose.cells/cell) class that is used to set a cell's formatting. Also, the object of the [Style](https://apireference.aspose.com/cells/java/com.aspose.cells/Style) class can be used to configure font settings.

{{% alert color="primary" %}} 

To set the foreground or background color of a cell, use the [Style](https://apireference.aspose.com/cells/java/com.aspose.cells/Style)  object's [setBackgroundColor](https://apireference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) or [setForegroundColor](https://apireference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) properties. These properties only come into effect if the [Style](https://apireference.aspose.com/cells/java/com.aspose.cells/Style)  object's [setPattern](https://apireference.aspose.com/cells/java/com.aspose.cells/style#Pattern) property is configured.

{{% /alert %}} 

The [setForegroundColor](https://apireference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)  property sets the cell's shading color.

The [setPattern](https://apireference.aspose.com/cells/java/com.aspose.cells/style#Pattern)   property specifies the background pattern used for the foreground or background color. Aspose.Cells provides the [BackgroundType](https://apireference.aspose.com/cells/java/com.aspose.cells/BackgroundType) enumeration which contains a set of pre-defined types of background patterns.

|**Pattern Type**|**Description**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|Represents diagonal crosshatch pattern|
|[DIAGONAL_STRIPE](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|Represents diagonal stripe pattern|
|[GRAY_6](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|Represents 6.25% gray pattern|
|[GRAY_12](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|Represents 12.5% gray pattern|
|[GRAY_25](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|Represents 25% gray pattern|
|[GRAY_50](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|Represents 50% gray pattern|
|[GRAY_75](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|Represents 75% gray pattern|
|[HORIZONTAL_STRIPE](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|Represents horizontal stripe pattern|
|[NONE](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|Represents no background|
|[REVERSE_DIAGONAL_STRIPE](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|Represents reverse diagonal stripe pattern|
|[SOLID](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|Represents solid pattern|
|[THICK_DIAGONAL_CROSSHATCH](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|Represents thick diagonal crosshatch pattern|
|[THIN_DIAGONAL_CROSSHATCH](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|Represents thin diagonal crosshatch pattern|
|[THIN_DIAGONAL_STRIPE](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|Represents thin diagonal stripe pattern|
|[THIN_HORIZONTAL_CROSSHATCH](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|Represents thin horizontal crosshatch pattern|
|[THIN_HORIZONTAL_STRIPE](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|Represents thin horizontal stripe pattern|
|[THIN_REVERSE_DIAGONAL_STRIPE](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|Represents thin reverse diagonal stripe pattern|
|[THIN_VERTICAL_STRIPE](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|Represents thin vertical stripe pattern|
|[VERTICAL_STRIPE](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|Represents vertical stripe pattern|
In the example below, the foreground color of the A1 cell is set but A2 is configured to have both foreground and background colors with a vertical stripe background pattern.

The following output is generated when executing the code.

**Foreground and background colors applied on cells with background patterns** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **Important to Know**
{{% alert color="primary" %}} 

- To set a cell's foreground or background color, use the [Style](https://apireference.aspose.com/cells/java/com.aspose.cells/Style)  object's [ForegroundColor](https://apireference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) or [BackgroundColor](https://apireference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) properties. Both properties will take effect only if the [Style](https://apireference.aspose.com/cells/java/com.aspose.cells/Style)  object's [Pattern](https://apireference.aspose.com/cells/java/com.aspose.cells/style#Pattern) property is configured.
- The [ForegroundColor](https://apireference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) property sets the cell's shade color.
  The [Pattern](https://apireference.aspose.com/cells/java/com.aspose.cells/style#Pattern) property specifies the type of background pattern used for the foreground or background color. Aspose.Cells provides an enumeration, [BackgroundType](https://apireference.aspose.com/cells/java/com.aspose.cells/BackgroundType). that contains a set of pre-defined types of background patterns.
- If you select [BackgroundType.NONE](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) value from the [BackgroundType](https://apireference.aspose.com/cells/java/com.aspose.cells/BackgroundType) enumeration, the foreground color is not applied.
  Likewise, the background color is not applied if you select the [BackgroundType.NONE](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) or [BackgroundType.SOLID](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID) values.
- When retrieving cell's shading/fill color, if [Style.Pattern](https://apireference.aspose.com/cells/java/com.aspose.cells/style#Pattern) is [BackgroundType.NONE](https://apireference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [Style.ForegroundColor](https://apireference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) will return *Color.Empty*.

{{% /alert %}} 
## **Formatting Selected Characters in a Cell**
[Dealing with Font Settings](/cells/java/dealing-with-font-settings/) explained how to format cells but only how to format the content of the entire cells. What if you want to format only selected characters?

Aspose.Cells supports this feature. This topic explains how to use this feature.
### **Formatting Selected Characters**
Aspose.Cells provides a class, [Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook), that represents a Microsoft Excel file. The [Workbook](https://apireference.aspose.com/cells/java/com.aspose.cells/Workbook) class contains a [WorksheetCollection](https://apireference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://apireference.aspose.com/cells/java/com.aspose.cells/Worksheet) class. The [Worksheet](https://apireference.aspose.com/cells/java/com.aspose.cells/Worksheet) class provides a [Cells](https://apireference.aspose.com/cells/java/com.aspose.cells/Cells) collection. Each item in the [Cells](https://apireference.aspose.com/cells/java/com.aspose.cells/Cells) collection represents an object of the [Cell](https://apireference.aspose.com/cells/java/com.aspose.cells/cell) class.

The [Cell](https://apireference.aspose.com/cells/java/com.aspose.cells/cell) class provides [characters](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)) method that takes the following parameters to select a range of characters in a cell:

- **Start Index**, the index of the character to start the selection from.
- **Number of Characters**, the number of characters to select.

In the output file, in the A1" cell, the word 'Visit' is formatted with the default font but 'Aspose!' is bold and blue.

**Formatting selected characters** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

If you are interested in [formatting a portion of Rich Text in a cell](https://docs.aspose.com/cells/java/access-and-update-the-portions-of-rich-text-of-cell/), consider using the [Cell.getCharacters](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) & Cell.setCharacters methods. The [Cell.getCharacters](https://apireference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) method is to be used to access the portions of the text and then amendments can be done using the Cell.setCharacters method whereas the **get** method returns an array of [FontSetting](https://apireference.aspose.com/cells/java/com.aspose.cells/FontSetting) objects which can be manipulated to set various properties such as font name, font color, boldness, etc and **set** method can be used to apply the changes.

{{% /alert %}}
