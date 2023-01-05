---
title: Cells 格式
type: docs
weight: 100
url: /zh/java/cells-formatting/
---
## **为 Cells 添加边框**
Microsoft Excel 允许用户通过添加边框来格式化单元格。

**Microsoft Excel 中的边框设置** 

![待办事项：图片_替代_文本](cells-formatting_1.png)

边框的类型取决于添加的位置。例如，顶部边框是添加到单元格顶部位置的边框。用户还可以修改边框的线条样式和颜色。

使用 Aspose.Cells，开发人员可以像在 Microsoft Excel 中一样灵活地添加边框和自定义外观。
### **为 Cells 添加边框**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。中的每一项[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合代表一个对象[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级。

Aspose.Cells 提供了[设置样式](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\) ) 中的方法[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)用于设置单元格格式样式的类。此外，对象的[风格](https://reference.aspose.com/cells/java/com.aspose.cells/Style)使用类并提供用于配置字体设置的属性。
#### **为 Cell 添加边框**
为单元格添加边框[风格](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[设置边框](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)） 方法。边框类型作为参数传递。所有边框类型都预定义在[边框类型](https://reference.aspose.com/cells/java/com.aspose.cells/BorderType)枚举。

|**边框类型**|**描述**|
|:- |:- |
|[BOTTOM_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#BOTTOM_BORDER)|底部边界线|
|[对角向下](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_DOWN)|从左上角到右下角的对角线|
|[对角向上](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#DIAGONAL_UP)|从左下角到右上角的对角线|
|[左边框](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#LEFT_BORDER)|左边界线|
|[右边框](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#RIGHT_BORDER)|右边界线|
|[TOP_BORDER](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#TOP_BORDER)|顶部边界线|
|[水平的](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#HORIZONTAL)|仅适用于动态样式，例如条件格式。|
|[垂直的](https://reference.aspose.com/cells/java/com.aspose.cells/bordertype#VERTICAL)|仅适用于动态样式，例如条件格式。|
要设置线条颜色，请使用[颜色](https://reference.aspose.com/cells/java/com.aspose.cells/Color)枚举并将其传递给[风格](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[设置边框](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\) 方法的颜色参数。线条样式在[单元格边框类型](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)枚举。

|**线型**|**描述**|
|:- |:- |
|[破折号](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT)|代表细点划线|
|[短跑_点_点](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASH_DOT_DOT)|表示细点划线|
|[虚线](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DASHED)|代表虚线|
|[点缀](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOTTED)|代表虚线|
|[双倍的](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#DOUBLE)|代表双线|
|[头发](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#HAIR)|代表发际线|
|[中等的_短跑_点](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT)|代表中点划线|
|[中等的_短跑_DOT_DOT](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASH_DOT_DOT)|表示中点划线|
|[MEDIUM_DASHED](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM_DASHED)|代表中虚线|
|[没有任何](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#NONE)|代表没有线|
|[中等的](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#MEDIUM)|代表中线|
|[倾斜的_短跑_点](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#SLANTED_DASH_DOT)|表示倾斜的中点划线|
|[厚的](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THICK)|代表粗线|
|[薄的](https://reference.aspose.com/cells/java/com.aspose.cells/cellbordertype#THIN)|代表细线|
选择上述线型之一，然后将其分配给[风格](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[设置边框](https://reference.aspose.com/cells/java/com.aspose.cells/style#setBorder\(int,%20int,%20com.aspose.cells.Color\)） 方法。

执行下面的代码时会生成以下输出。

**应用于单元格所有边的边框** 

![待办事项：图片_替代_文本](cells-formatting_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBordersToCells-AddingBordersToCells.java" >}}
#### **为 Cells 范围添加边框**
可以为一系列单元格添加边框，而不仅仅是单个单元格。首先，通过调用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏的[创建范围](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\)方法，它采用以下参数：

- **第一排**，范围的第一行。
- **第一栏**，范围的第一列。
- **行数**，范围内的行数。
- **列数**，范围内的列数。

这[创建范围](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange\(int,%20int,%20boolean\) ) 方法返回一个[范围](https://reference.aspose.com/cells/java/com.aspose.cells/Range)对象，其中包含指定的范围。这[范围](https://reference.aspose.com/cells/java/com.aspose.cells/Range)对象提供了一个[设置轮廓边框](https://reference.aspose.com/cells/java/com.aspose.cells/range#setOutlineBorders\(int,%20com.aspose.cells.Color\)采用以下参数的方法：

- **单元格边框类型**, 边框线条样式，选自[单元格边框类型](https://reference.aspose.com/cells/java/com.aspose.cells/CellBorderType)枚举。
- **颜色**边框线颜色，选自[颜色](https://reference.aspose.com/cells/java/com.aspose.cells/Color)枚举。

执行下面的代码时会生成以下输出。

**应用于一系列单元格的边框** 

![待办事项：图片_替代_文本](cells-formatting_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AddingBorderstoRange-AddingBorderstoRange.java" >}}
## **颜色和调色板**
调色板是可用于创建图像的颜色数量。在演示文稿中使用标准化调色板允许用户创建一致的外观。每个 Microsoft Excel (97-2003) 文件都有一个 56 种颜色的调色板，可应用于图表中的单元格、字体、网格线、图形对象、填充和线条。

**Microsoft Excel 中的调色板设置** 

![待办事项：图片_替代_文本](cells-formatting_4.png)

使用 Aspose.Cells 不仅可以使用现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，将其添加到调色板中。本主题说明如何将自定义颜色添加到调色板。
### **将自定义颜色添加到调色板**
Aspose.Cells 还支持 56 种颜色的调色板。标准调色板如上所示。如果您想使用未在调色板中定义的自定义颜色，则需要在使用前将该颜色添加到调色板。

{{% alert color="primary" %}} 

调色板只有 56 种颜色。当您将自定义颜色添加到调色板时，调色板会更改，文件中使用先前颜色设置格式的任何元素也会更改。所以，当你改变调色板时，请非常小心。此外，这只是 XLS (Excel 97 - 2003) 文件格式的限制，因为 XLSX 或其他高级 MS Excel (2007/2010) 文件格式没有此类限制。

{{% /alert %}} 

Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，代表一个 Microsoft Excel 文件。该类提供[改变调色板](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#changePalette\(com.aspose.cells.Color,%20int\)方法，它采用以下参数来添加自定义颜色以修改调色板：

- **自定义颜色**，要添加到调色板的自定义颜色。
- **指数**，将被自定义颜色替换的颜色的索引。应该在 0-55 之间。

下面的示例在将自定义颜色应用于字体之前将其添加到调色板。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndPalette-ColorsAndPalette.java" >}}
## **颜色和背景图案**
Microsoft Excel 可以设置单元格的前景（轮廓）和背景（填充）颜色以及背景图案，如下所示。

**在 Microsoft Excel 中设置颜色和背景图案** 

![待办事项：图片_替代_文本](cells-formatting_5.png)

Aspose.Cells 也以灵活的方式支持这些功能。在本主题中，我们通过 Aspose.Cells 学习使用这些功能。
### **设置颜色和背景图案**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，代表一个 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。中的每一项[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合代表一个对象[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级。

Aspose.Cells 提供了[设置样式](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setStyle\(com.aspose.cells.Style\)中的方法[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)用于设置单元格格式的类。此外，对象的[风格](https://reference.aspose.com/cells/java/com.aspose.cells/Style)类可用于配置字体设置。

{{% alert color="primary" %}} 

要设置单元格的前景色或背景色，请使用[风格](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[设置背景颜色](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor)要么[设置前景色](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)特性。这些属性只有在[风格](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[设置模式](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)属性已配置。

{{% /alert %}} 

这[设置前景色](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)属性设置单元格的阴影颜色。

这[设置模式](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)属性指定用于前景色或背景色的背景图案。 Aspose.Cells 提供了[背景类型](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)枚举，其中包含一组预定义类型的背景图案。

|**图案类型**|**描述**|
|:- |:- |
|[DIAGONAL_CROSSHATCH](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_CROSSHATCH)|表示对角交叉影线图案|
|[对角条纹](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#DIAGONAL_STRIPE)|代表斜条纹图案|
|[灰色_6](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_6)|代表 6.25% 灰色图案|
|[灰色_12](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_12)|代表 12.5% 灰色图案|
|[灰色_25](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_25)|代表 25% 灰色图案|
|[灰色_50](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_50)|代表 50% 灰色图案|
|[灰色_75](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#GRAY_75)|代表75%灰色图案|
|[水平条纹](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#HORIZONTAL_STRIPE)|代表横条纹图案|
|[没有任何](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)|代表没有背景|
|[撤销_对角线_条纹](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#REVERSE_DIAGONAL_STRIPE)|表示反斜条纹图案|
|[坚硬的](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)|表示实心图案|
|[厚的_对角线_十字线](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THICK_DIAGONAL_CROSSHATCH)|表示粗对角交叉影线图案|
|[薄的_对角线_十字线](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_CROSSHATCH)|表示细对角线交叉影线图案|
|[薄的_对角线_条纹](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_DIAGONAL_STRIPE)|代表细斜条纹图案|
|[薄的_水平的_十字线](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_CROSSHATCH)|表示细水平交叉影线图案|
|[薄的_水平的_条纹](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_HORIZONTAL_STRIPE)|代表细横条纹图案|
|[薄的_撤销_对角条纹](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_REVERSE_DIAGONAL_STRIPE)|代表细反斜条纹图案|
|[薄的_垂直的_条纹](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#THIN_VERTICAL_STRIPE)|代表细竖条纹图案|
|[垂直条纹](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#VERTICAL_STRIPE)|代表竖条纹图案|
在下面的示例中，设置了 A1 单元格的前景色，但 A2 配置为具有垂直条纹背景图案的前景色和背景色。

执行代码时会生成以下输出。

**应用于具有背景图案的单元格的前景色和背景色** 

![待办事项：图片_替代_文本](cells-formatting_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ColorsAndBackground-ColorsAndBackground.java" >}}
### **重要须知**
{{% alert color="primary" %}} 

- 要设置单元格的前景色或背景色，请使用[风格](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[前景色](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)要么[背景颜色](https://reference.aspose.com/cells/java/com.aspose.cells/style#BackgroundColor)特性。只有当[风格](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象的[图案](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)属性已配置。
- 这[前景色](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)属性设置单元格的阴影颜色。
这[图案](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)属性指定用于前景色或背景色的背景图案类型。 Aspose.Cells 提供枚举，[背景类型](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType).包含一组预定义类型的背景图案。
- 如果你选择[背景类型.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)价值来自[背景类型](https://reference.aspose.com/cells/java/com.aspose.cells/BackgroundType)枚举，不应用前景色。
同样，如果您选择[背景类型.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE)要么[背景类型.SOLID](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#SOLID)值。
- 检索单元格的阴影/填充颜色时，如果[样式.图案](https://reference.aspose.com/cells/java/com.aspose.cells/style#Pattern)是[背景类型.NONE](https://reference.aspose.com/cells/java/com.aspose.cells/backgroundtype#NONE), [样式.前景色](https://reference.aspose.com/cells/java/com.aspose.cells/style#ForegroundColor)将返回*颜色.空*.

{{% /alert %}} 
## **格式化 Cell 中的选定字符**
[处理字体设置](/cells/zh/java/dealing-with-font-settings/)解释了如何格式化单元格，但仅解释了如何格式化整个单元格的内容。如果您只想格式化选定的字符怎么办？

Aspose.Cells 支持此功能。本主题说明如何使用此功能。
### **格式化所选字符**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，代表一个 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类提供了[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)收藏。中的每一项[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)集合代表一个对象[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级。

这[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类提供[人物](https://reference.aspose.com/cells/java/com.aspose.cells/cell#characters\(int,%20int\)方法，它采用以下参数来选择单元格中的字符范围：

- **起始索引**开始选择的字符的索引。
- **字符数**要选择的字符数。

在输出文件的 A1" 单元格中，单词 'Visit' 的格式为默认字体，但为 'Aspose!'是粗体和蓝色。

**格式化所选字符** 

![待办事项：图片_替代_文本](cells-formatting_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}

{{% alert color="primary" %}} 

如果你有兴趣[在单元格中格式化部分富文本](/cells/zh/java/access-and-update-the-portions-of-rich-text-of-cell/)，考虑使用[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) & Cell.setCharacters 方法。这[Cell.getCharacters](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getCharacters\(\) 方法将用于访问文本的部分，然后可以使用 Cell.setCharacters 方法进行修改，而**得到**方法返回一个数组[字体设置](https://reference.aspose.com/cells/java/com.aspose.cells/FontSetting)可以操作以设置各种属性的对象，例如字体名称、字体颜色、粗体等，以及**放**方法可用于应用更改。

{{% /alert %}}

## **推进主题**
- [对齐设置](/cells/zh/java/cells-alignment-settings/)
- [条件格式](/cells/zh/java/conditional-formatting/)
- [数据格式化](/cells/zh/java/data-formatting/)
- [Excel 主题和颜色](/cells/zh/java/excel-2007-themes-and-colors/)
- [处理字体设置](/cells/zh/java/dealing-with-font-settings/)
- [在工作簿中格式化工作表 Cells](/cells/zh/java/format-worksheet-cells-in-a-workbook/)
- [实施 1904 日期系统](/cells/zh/java/implement-1904-date-system/)
- [合并和取消合并 Cells](/cells/zh/java/merging-and-unmerging-cells/)
- [号码设置](/cells/zh/java/cells-number-settings/)
- [保留 Cell 值或范围的单引号前缀](/cells/zh/java/preserve-single-quote-prefix-of-cell-value-or-range/)
- [样式和数据格式](/cells/zh/java/styling-and-data-formatting/)
