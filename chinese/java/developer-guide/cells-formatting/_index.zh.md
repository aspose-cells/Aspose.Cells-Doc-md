---
title: 单元格格式
type: docs
weight: 100
url: /zh/java/cells-formatting/
---

## **向单元格添加边框**
Microsoft Excel 允许用户通过添加边框来格式化单元格。

Microsoft Excel 中的边框设置 

![todo:image_alt_text](cells-formatting_1.png)

边框的类型取决于添加的位置。例如，顶部边框是添加到单元格顶部位置的边框。用户还可以修改边框的线条样式和颜色。

使用 Aspose.Cells，开发人员可以以与 Microsoft Excel 中相同灵活的方式添加边框并自定义其外观。
### **向单元格添加边框**
Aspose.Cells 提供了一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，表示 Microsoft Excel 文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) 类包含一个 [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问 Excel 文件中的每个工作表。工作表由 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类提供一个 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合中的每个项表示 [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) 类的对象。

Aspose.Cells 在 [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell) 类中提供了 [setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)) 方法，用于设置单元格的格式样式。还使用 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) 类的对象提供配置字体设置属性。
#### **向单元格添加边框**
使用 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) 对象的 [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/Style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) 方法向单元格添加边框。将边框类型作为参数传递。所有边框类型均在 [BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType) 枚举中预定义。

|**边框类型**|**描述**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|底部边框线|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|从左上到右下的对角线|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|从左下到右上的对角线|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|左边框线|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|右边框线|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|顶部边框线|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|仅适用于动态样式，如条件格式设置。|
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|仅适用于动态样式，如条件格式设置。|
要设置线条颜色，请使用[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)枚举选择颜色，并将其传递给[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\))方法的Color参数。线条样式在[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)枚举中预定义。

|**线条样式**|**描述**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|代表细虚线|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|代表细虚线点线|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|代表虚线|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|代表点线|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|代表双线|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|代表发线|
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|代表中虚线点线|
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|代表中虚线点点线|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|代表中虚线|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|代表无线|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|代表中线|
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|代表倾斜的中虚点线|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|代表粗线|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|代表细线|
选择上述线条样式之一，然后将其分配给[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) 对象的 [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) 方法。

执行下面的代码后生成以下输出。

**应用于单元格所有边的边框** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **向单元格范围添加边框**
可以向一系列单元格添加边框，而不仅仅是单个单元格。首先，通过调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合的[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\))方法创建一系列单元格，该方法接受以下参数：

- **第一行**，范围的第一行。
- **第一列**，范围的第一列。
- **行数**，范围中的行数。
- **列数**，范围中的列数。

[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\))方法返回一个[Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range)对象，该对象包含指定的范围。Range对象提供了一个[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\))方法，接受以下参数:

- **CellBorderType**，边框线样式，从[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)枚举中选择。
- **Color**，边框线颜色，从[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)枚举中选择。

执行下面的代码后生成以下输出。

**应用于单元格范围的边框** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **颜色和调色板**
调色板是用于创建图像的可用颜色数量。在演示文稿中使用标准化的调色板允许用户创建一致的外观。每个微软 Excel (97-2003) 文件有一个包含 56 种颜色的调色板，可应用于单元格、字体、网格线、图形对象、填充和图表中的线条。

**Microsoft Excel中的调色板设置** 

![todo:image_alt_text](cells-formatting_4.png)

通过Aspose.Cells不仅可以使用现有颜色，还可使用自定义颜色。在使用自定义颜色之前，将其添加到调色板中。本主题解释了如何向调色板中添加自定义颜色。
### **将自定义颜色添加到调色板**
Aspose.Cells还支持包含56种颜色的调色板。上面显示了标准颜色调色板。如果要使用未在调色板中定义的自定义颜色，则需在使用之前将该颜色添加到调色板中。

{{% alert color="primary" %}} 

调色板只能容纳56种颜色。将自定义颜色添加到调色板中后，会更改整个调色板，并更改使用先前颜色格式化的文件中的任何元素。因此，在更改调色板时，请非常小心。此外，这只是XLS（Excel 97 - 2003）文件格式中的限制，因为对于XLSX或其他高级MS Excel（2007/2010）文件格式并无此类限制。

{{% /alert %}} 

Aspose.Cells提供了一个表示Microsoft Excel文件的类[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)。该类提供了[changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\))方法，接受以下参数以添加自定义颜色来修改调色板:

- **自定义颜色**，要添加到调色板中的自定义颜色。
- **索引**，将被自定义颜色替换的颜色索引。应介于0-55之间。

下面的示例在将自定义颜色应用于字体之前将其添加到调色板中。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **颜色和背景图案**
Microsoft Excel可以设置单元格的前景（轮廓）和背景（填充）颜色以及背景图案，如下所示。

**在Microsoft Excel中设置颜色和背景图案** 

![todo:image_alt_text](cells-formatting_5.png)

Aspose.Cells还以灵活的方式支持这些功能。在这个主题中，我们将学习如何使用Aspose.Cells使用这些功能。
### **设置颜色和背景图案**
Aspose.Cells 提供了一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，表示 Microsoft Excel 文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) 类包含一个 [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问 Excel 文件中的每个工作表。工作表由 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类提供一个 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合中的每个项目都表示 [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 类的对象。

Aspose.Cells在[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类中提供了[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\))方法，用于设置单元格的格式。同时，[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)类的对象可用于配置字体设置。

{{% alert color="primary" %}} 

要设置单元格的前景色或背景色，请使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor)或[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)属性。只有在配置[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)属性后，这些属性才会生效。

{{% /alert %}} 

[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)属性设置单元格的底纹颜色。

[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)属性指定用于前景色或背景色的背景图案。Aspose.Cells提供了包含一组预定义背景图案类型的[BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)枚举。

|**图案类型**|**描述**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|代表对角交叉阴影图案|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|代表对角条纹图案|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|代表6.25%灰度图案|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|代表12.5%灰度图案|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|代表25%灰度图案|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|代表50%灰度图案|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|代表75%灰度图案|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|代表横条纹图案|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|代表无背景|
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|代表逆向对角条纹图案|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|代表实心图案|
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|代表粗对角线格涂鸦图案|
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|代表细对角线格涂鸦图案|
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|代表细对角线条纹图案|
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|代表细水平格涂鸦图案|
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|代表细水平条纹图案|
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|代表细反对角线条纹图案|
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|代表细垂直条纹图案|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|代表垂直条纹图案|
在下面的示例中，设置了A1单元格的前景色，而A2配置为具有前景色和背景色，背景模式为垂直条纹。

执行代码时生成以下输出。

**在带有背景图案的单元格上应用前景和背景颜色** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **重要知识**
{{% alert color="primary" %}} 

- 要设置单元格的前景色或背景色，请使用 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) 对象的 [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) 或 [BackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor) 属性。只有在配置 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) 对象的 [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) 属性后，这两个属性才会生效。
- [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) 属性设置单元格的阴影颜色。
  [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) 属性指定用于前景或背景颜色的背景图案类型。Aspose.Cells 提供一个枚举，[BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)。其中包含一组预定义的背景图案类型。
- 如果从 [BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType) 枚举中选择 [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) 值，则不会应用前景色。
  同样，如果选择 [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE) 或 [BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID) 值，则不会应用背景颜色。
- 当检索单元格的阴影/填充颜色时，如果 [Style.Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern) 是 [BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)，则 [Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor) 将返回 *Color.Empty*。

{{% /alert %}} 
## **格式化单元格中的选定字符**
[处理字体设置](/cells/zh/java/dealing-with-font-settings/) 解释了如何格式化单元格，但只是如何格式化整个单元格的内容。如果您只想格式化选定的字符怎么办？

Aspose.Cells 支持此功能。本主题解释了如何使用此功能。
### **格式化选定的字符**
Aspose.Cells 提供了一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，表示 Microsoft Excel 文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) 类包含一个 [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问 Excel 文件中的每个工作表。工作表由 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类提供一个 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合中的每个项目都表示 [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 类的对象。

[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 类提供 [characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)) 方法，该方法使用以下参数选择单元格中的一系列字符：

- **起始索引**，开始选择的字符的索引。
- **字符数**，要选择的字符数。

在输出文件中，A1" 单元格中，'Visit' 一词使用默认字体格式，但 'Aspose!' 是粗体且为蓝色。

**格式化选定的字符** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

如果您有兴趣 [格式化单元格中的部分富文本](/cells/zh/java/access-and-update-the-portions-of-rich-text-of-cell/)，请考虑使用 [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) 和 Cell.setCharacters 方法。[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) 方法用于访问文本的部分，然后可以使用 Cell.setCharacters 方法进行修改，而 **get** 方法返回一个 [FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting) 对象数组，可以操作以设置各种属性，如字体名称、字体颜色、加粗等，**set** 方法可用于应用更改。

{{% /alert %}}

## **高级主题**
- [对齐设置](/cells/zh/java/cells-alignment-settings/)
- [条件格式设置](/cells/zh/java/conditional-formatting/)
- [数据格式化](/cells/zh/java/data-formatting/)
- [Excel主题和颜色](/cells/zh/java/excel-2007-themes-and-colors/)
- [处理字体设置](/cells/zh/java/dealing-with-font-settings/)
- [在工作簿中格式化工作表单元格](/cells/zh/java/format-worksheet-cells-in-a-workbook/)
- [实施1904日期系统](/cells/zh/java/implement-1904-date-system/)
- [合并和取消合并单元格](/cells/zh/java/merging-and-unmerging-cells/)
- [数字设置](/cells/zh/java/cells-number-settings/)
- [保留单引号前缀的单元格值或范围](/cells/zh/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [样式和数据格式化](/cells/zh/java/styling-and-data-formatting/)
