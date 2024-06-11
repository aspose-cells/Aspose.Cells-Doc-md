---
title: 单元格格式
type: docs
weight: 100
url: /zh/java/cells-formatting/
---

## **向单元格添加边框**
Microsoft Excel允许用户通过添加边框来格式化单元格。

**Microsoft Excel中的边框设置** 

![todo:image_alt_text](cells-formatting_1.png)

边框的类型取决于添加的位置。例如，顶部边框是添加到单元格顶部位置的边框。用户还可以修改边框的线条样式和颜色。

使用Aspose.Cells，开发人员可以以与Microsoft Excel中相同灵活的方式添加边框并自定义其外观。
### **向单元格添加边框**
Aspose.Cells提供了代表Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了一个[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合。[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合中的每个项代表[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的对象。

Aspose.Cells在[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类中提供了[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\))方法，用于设置单元格的格式样式。同时使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)类的对象，提供用于配置字体设置的属性。
#### **向单元格添加边框**
使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)类的[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\))方法向单元格添加边框。边框类型作为参数传递。所有边框类型均在[BorderType](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)枚举中预定义。

|**边框类型**|**描述**|
| :- | :- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|底部边框线|
|[DIAGONAL_DOWN](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|从左上到右下对角线|
|[DIAGONAL_UP](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|从左下到右上对角线|
|[LEFT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|左边框线|
|[RIGHT_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|右边框线|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|顶部边框线|
|[HORIZONTAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|仅用于动态样式，例如条件格式设置。
|[VERTICAL](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|仅用于动态样式，例如条件格式设置。
要设置线条颜色，请使用[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)枚举选择颜色，并将其传递给[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)类的[setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\))方法的Color参数。线条样式在[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)枚举中预定义。

|**线条样式**|**描述**|
| :- | :- |
|[DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|表示细虚线-点线|
|[DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|表示细虚线-点-点线|
|[DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|表示虚线|
|[DOTTED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|表示点线|
|[DOUBLE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|表示双线|
|[HAIR](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|表示发际线|
|[MEDIUM_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|表示中等虚线-点线|
|[MEDIUM_DASH_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|表示中等虚线-点-点线|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|表示中等虚线|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|表示无线条|
|[MEDIUM](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|表示中等线|
|[SLANTED_DASH_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|表示倾斜中等虚线-点线|
|[THICK](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|表示粗线|
|[THIN](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|表示细线|
选择以上线条样式之一，然后将其分配给 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style) 对象的 [setBorder](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)) 方法。

执行以下代码时生成下面的输出。

**应用于单元格四周的边框** 

![todo:image_alt_text](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **向单元格范围添加边框**
可以向单元格范围添加边框，而不仅仅是单个单元格。首先，通过调用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) 集合的 [createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)) 方法创建单元格范围，该方法接受以下参数：

- **第一行**，范围的第一行。
- **第一列**，范围的第一列。
- **行数**，范围内的行数。
- **列数**，范围内的列数。

[createRange](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\))方法返回一个包含指定范围的[Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range)对象。[Range](https://reference.aspose.com/cells/java/com.aspose.cells/Range)对象提供了一个[setOutlineBorders](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\))方法，它接受以下参数：

- **CellBorderType**，边框线样式，从[CellBorderType](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)枚举中选择。
- **Color**，边框线颜色，从[Color](https://reference.aspose.com/cells/java/com.aspose.cells/Color)枚举中选择。

执行以下代码时生成下面的输出。

**应用于单元格范围的边框** 

![todo:image_alt_text](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **颜色和调色板**
调色板是在创建图像时可用的颜色数量。在演示文稿中使用标准调色板可以让用户创建一致的外观。每个Microsoft Excel（97-2003）文件都有一个包含可应用于单元格、字体、网格线、图形对象、填充和图表中的线条的56种颜色的调色板。

Microsoft Excel中的调色板设置 

![todo:image_alt_text](cells-formatting_4.png)

通过Aspose.Cells不仅可以使用现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，将其添加到调色板中。本主题解释了如何向调色板中添加自定义颜色。
### **向调色板中添加自定义颜色**
Aspose.Cells还支持56种颜色的调色板。上面显示了标准颜色调色板。如果要使用在调色板中未定义的自定义颜色，则需要在使用之前将该颜色添加到调色板中。

{{% alert color="primary" %}} 

调色板只能保存56种颜色。当向调色板中添加自定义颜色时，调色板被更改，并且文件中使用以前颜色格式化的任何元素都将被更改。因此，在更改调色板时，请非常小心。此外，在XLS（Excel 97-2003）文件格式中存在此限制，而在XLSX或其他先进的MS Excel（2007/2010）文件格式中则没有此限制。

{{% /alert %}} 

Aspose.Cells提供了一个表示Microsoft Excel文件的类，称为[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)。该类提供了[changePalette](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\))方法，它接受以下参数以添加自定义颜色并修改调色板：

- **自定义颜色**，要添加到调色板中的自定义颜色。
- **索引**，将被自定义颜色替换的颜色的索引。应该在0-55之间。

下面的示例在应用于字体之前将一个自定义颜色添加到调色板中。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **颜色和背景图案**
Microsoft Excel可以设置单元格的前景（轮廓）和背景（填充）颜色以及背景图案，如下所示。

在Microsoft Excel中设置颜色和背景图案 

![todo:image_alt_text](cells-formatting_5.png)

Aspose.Cells还以灵活的方式支持这些功能。在本主题中，我们将学习如何使用Aspose.Cells来使用这些功能。
### **设置颜色和背景图案**
Aspose.Cells 提供了一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，它表示 Microsoft Excel 文件。 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) 类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问 Excel 文件中的每个工作表。 工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类提供一个[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合。 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合中的每个项都表示[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的对象。

Aspose.Cells在[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/Cell)类中提供一个[setStyle](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\))方法，用于设置单元格的格式。同时，可以使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)类的对象来配置字体设置。

{{% alert color="primary" %}} 

要设置单元格的前景或背景颜色，使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[setBackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor)或[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)属性。只有在配置[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)属性时，这些属性才会生效。

{{% /alert %}} 

[setForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)属性设置单元格的底纹颜色。

[setPattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)属性指定单元格的前景或背景颜色所使用的背景图案。Aspose.Cells提供[BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)枚举，其中包含一组预定义的背景图案类型。

|**图案类型**|**描述**|
| :- | :- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|表示对角线交叉图案|
|[DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|表示对角线条纹图案|
|[GRAY_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|表示6.25%灰色图案|
|[GRAY_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|表示12.5%灰色图案|
|[GRAY_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|表示25%灰色图案|
|[GRAY_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|表示50%灰色图案|
|[GRAY_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|表示75%灰色图案|
|[HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|表示水平条纹图案|
|[NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|表示无背景|
|[REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|代表着反斜纹样式|
|[SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|代表着固体图案|
|[THICK_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|代表着粗对角交错图案|
|[THIN_DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|代表着细对角交错图案|
|[THIN_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|代表着细对角条纹图案|
|[THIN_HORIZONTAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|代表着细水平交错图案|
|[THIN_HORIZONTAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|代表着细水平条纹图案|
|[THIN_REVERSE_DIAGONAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|代表着细反斜纹条纹图案|
|[THIN_VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|代表着细垂直条纹图案|
|[VERTICAL_STRIPE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|代表着垂直条纹图案|
在下面的示例中，A1单元格的前景色已设置，但A2配置为具有前景色和背景色的垂直条纹背景模式。

执行代码时会生成以下输出。

**在具有背景模式的单元格上应用前景色和背景色** 

![todo:image_alt_text](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **重要知识**
{{% alert color="primary" %}} 

- 要设置单元格的前景色或背景色，请使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)或[BackgroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor)属性。只有在配置了[Style](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)属性后，这两个属性才会生效。
- [ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)属性设置单元格的阴影颜色。
  [Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)属性指定用于前景色或背景色的背景图案的类型。Aspose.Cells提供了一个包含一组预定义背景图案类型的枚举，[BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)。
- 如果从[BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)枚举中选择[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)值，将不会应用前景色。
  同样，如果从[BackgroundType](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)枚举中选择[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)或[BackgroundType.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)值，将不会应用背景色。
-当获取单元格的阴影/填充颜色时，如果[Style.Pattern](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)为[BackgroundType.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)，[Style.ForegroundColor](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)将返回*Color.Empty*。

{{% /alert %}} 
## **在单元格中格式化所选字符**
[处理字体设置](/cells/zh/java/dealing-with-font-settings/)解释了如何格式化单元格，但只是如何格式化整个单元格的内容。 如果您只想格式化所选字符该怎么办？

Aspose.Cells 支持此功能。本主题解释了如何使用此功能。
### **格式化所选字符**
Aspose.Cells 提供了一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，它表示 Microsoft Excel 文件。 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) 类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问 Excel 文件中的每个工作表。 工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) 类提供一个[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合。 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合中的每个项都表示[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的对象。

[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类提供了[characters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\))方法，接受以下参数以选择单元格中的字符范围：

- **起始索引**，从中开始选择的字符的索引。
- **字符数**，要选择的字符数。

在输出文件中，A1单元格中，“Visit”一词使用默认字体格式，但“Aspose!”是粗体和蓝色。

**格式化所选字符** 

![todo:image_alt_text](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

如果您有兴趣[格式化单元格中的富文本的一部分](/cells/zh/java/access-and-update-the-portions-of-rich-text-of-cell/)，请考虑使用 [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) 和 Cell.setCharacters 方法。 [Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\)) 方法用于访问文本的部分，然后可以使用 Cell.setCharacters 方法进行修改，而 **获得** 方法返回一个[FontSetting](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting)对象数组，可以对其进行操作以设置各种属性，例如字体名称、字体颜色、粗细等，而 **设置** 方法可用于应用更改。

{{% /alert %}}

## **高级主题**
- [对齐设置](/cells/zh/java/cells-alignment-settings/)
- [条件格式](/cells/zh/java/conditional-formatting/)
- [数据格式设置](/cells/zh/java/data-formatting/)
- [Excel 主题和颜色](/cells/zh/java/excel-2007-themes-and-colors/)
- [处理字体设置](/cells/zh/java/dealing-with-font-settings/)
- [在工作簿中格式化工作表单元格](/cells/zh/java/format-worksheet-cells-in-a-workbook/)
- [实现1904日期系统](/cells/zh/java/implement-1904-date-system/)
- [合并和取消合并单元格](/cells/zh/java/merging-and-unmerging-cells/)
- [数字设置](/cells/zh/java/cells-number-settings/)
- [保留单引号前缀的单元格值或范围](/cells/zh/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [样式和数据格式](/cells/zh/java/styling-and-data-formatting/)
