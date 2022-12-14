---
title: 数据格式化
type: docs
weight: 80
url: /zh/java/data-formatting/
---
## **Cells 中格式化数据的方法**
一个普遍的事实是，如果工作表单元格的格式正确，那么用户就可以更轻松地阅读单元格的内容（数据）。有许多方法可以格式化单元格及其内容。最简单的方法是在创建 Designer 电子表格时在所见即所得环境中使用 Microsoft Excel 格式化单元格。创建设计器电子表格后，您可以使用 Aspose.Cells 打开电子表格，同时将所有格式设置保存在电子表格中。另一种格式化单元格及其内容的方法是使用 Aspose.Cells API。在本主题中，我们将介绍两种使用 Aspose.Cells API 格式化单元格及其内容的方法。
### **格式化 Cells**
开发者可以使用Aspose.Cells的灵活的API格式化单元格及其内容。Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了一个 Cells 集合。中的每一项[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)集合代表一个对象**Cell**班级。

Aspose.Cells 提供了[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)中的财产[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类，用于设置单元格的格式样式。此外，Aspose.Cells还提供了一个[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)用于服务相同目的的类。在单元格上应用不同类型的格式样式以设置它们的背景或前景色、边框、字体、水平和垂直对齐方式、缩进级别、文本方向、旋转角度等等。
#### **使用 setStyle 方法**
将不同的格式样式应用于不同的单元格时，最好使用[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级。下面给出了一个示例来演示如何使用 setStyle 方法在单元格上应用各种格式设置。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **使用样式对象**
将相同的格式样式应用于不同的单元格时，使用[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)目的。

1. 添加一个[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)的样式集合的对象[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)通过调用 Workbook 类的 createStyle 方法来创建类。
1. 从 Styles 集合访问新添加的 Style 对象。
1. 设置 Style 对象的所需属性以应用所需的格式设置。
1. 将配置的 Style 对象分配给任何所需单元格的 Style 属性。

这种方法可以大大提高应用程序的效率并节省内存。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **应用渐变填充效果**
要将所需的渐变填充效果应用到单元格，请相应地使用 Style 对象的 setTwoColorGradient 方法。
#### **代码示例**
以下输出是通过执行下面的代码实现的。

**应用渐变填充效果** 

![待办事项：图片_替代_文本](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **配置对齐设置**
用过Microsoft Excel格式化单元格的人都会熟悉Microsoft Excel中的对齐设置。

**Microsoft Excel 中的对齐设置** 

![待办事项：图片_替代_文本](data-formatting_2.png)

从上图可以看出，有不同种类的对齐选项：

- [文本对齐](/cells/zh/java/data-formatting/)（水平垂直）
- [缩进](/cells/zh/java/data-formatting/).
- [方向](/cells/zh/java/data-formatting/).
- [文本控件](/cells/zh/java/data-formatting/).
- [文字方向](/cells/zh/java/data-formatting/).

Aspose.Cells 完全支持所有这些对齐设置，并在下面进行更详细的讨论。
### **配置对齐设置**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 表示一个 Excel 文件。 Workbook 类包含一个 WorksheetCollection，它允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。

Worksheet 类提供了一个 Cells 集合。 Cells 集合中的每个项目代表[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级。

Aspose.Cells 中提供了setStyle方法[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)用于单元格格式的类。这[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)类提供用于配置字体设置的有用属性。

使用 TextAlignmentType 枚举选择任何文本对齐类型。 TextAlignmentType 枚举中的预定义文本对齐类型是：

|**文本对齐类型**|**描述**|
|:- |:- |
|底部|表示底部文本对齐|
|中心|表示居中文本对齐|
|跨中心|表示跨文本居中对齐|
|分散式|表示分布式文本对齐|
|充满|表示填充文本对齐方式|
|一般的|表示一般文本对齐方式|
|证明合法|表示对齐文本对齐|
|剩下|表示文本左对齐|
|正确的|表示文本右对齐|
|最佳|表示顶部文本对齐|
{{% alert color="primary" %}} 

您还可以使用 Style.setJustifyDistributed() 方法应用对齐分布式设置。

{{% /alert %}} 
#### **水平对齐**
使用[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的 setHorizontalAlignment 方法来水平对齐文本。

以下输出是通过执行下面的示例代码实现的：

**水平对齐文本** 

![待办事项：图片_替代_文本](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **垂直对齐**
使用[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的 setVerticalAlignment 方法来垂直对齐文本。

当 VerticalAlignment 设置为 center 时，会实现以下输出。

**垂直对齐文本** 

![待办事项：图片_替代_文本](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **缩进**
可以通过使用设置单元格中文本的缩进级别[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的 setIndentLevel 方法。

当 IndentLevel 设置为 2 时，将实现以下输出。

**缩进级别调整为 2** 

![待办事项：图片_替代_文本](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **方向**
设置单元格中文本的方向（旋转）[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的 setRotationAngle 方法。

旋转角度设置为25时实现如下输出。

**旋转角度设置为 25** 

![待办事项：图片_替代_文本](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **文字控制**
以下部分讨论如何通过设置文本换行、收缩以适合和其他格式设置选项来控制文本。
#### **环绕文字**
在单元格中环绕文本使其更易于阅读：单元格的高度会调整以适合所有文本，而不是将其切断或溢出到相邻的单元格中。

使用[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的 setTextWrapped 方法。

启用文本换行时会实现以下输出。

**文本包裹在单元格内** 

![待办事项：图片_替代_文本](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **收缩以适应**
在字段中换行文本的一个选项是缩小文本大小以适合单元格的尺寸。这是通过设置[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的 IsTextWrapped 属性为**真的**.

当文本缩小以适合单元格时，将实现以下输出。

**文本缩小以适合单元格的边界** 

![待办事项：图片_替代_文本](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **合并 Cells**
与Microsoft Excel一样，Aspose.Cells支持将多个单元格合并为一个单元格。

如果合并第一行中的三个单元格以创建一个大的单个单元格，则会实现以下输出。

**三个单元格合并成一个大单元格** 

![待办事项：图片_替代_文本](data-formatting_9.png)

使用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)collection 的 Merge 方法来合并单元格。 Merge 方法采用以下参数：

- 第一行，从哪里开始合并的第一行。
- 第一列，从哪里开始合并的第一列。
- Number of rows，要合并的行数。
- 列数，要合并的列数。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **文字方向**
可以设置单元格中文本的阅读顺序。阅读顺序是显示字符、单词等的视觉顺序。例如，英语是从左到右的语言，而阿拉伯语是从右到左的语言。

阅读顺序设置为[风格](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的 TextDirection 属性。 Aspose.Cells 在 TextDirectionType 枚举中提供预定义的文本方向类型。

|**文本方向类型**|**描述**|
|:- |:- |
|语境|与第一个输入字符的语言一致的阅读顺序|
|左到右|从左到右的阅读顺序|
|右到左|从右到左的阅读顺序|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





如果将文本的阅读顺序设置为从右到左，则会实现以下输出。

**将文本阅读顺序设置为从右到左** 

![待办事项：图片_替代_文本](data-formatting_10.png)
## **格式化 Cell 中的选定字符**
[处理字体设置](/cells/zh/java/dealing-with-font-settings/)解释了如何格式化单元格，但仅解释了如何格式化整个单元格的内容。如果您只想格式化选定的字符怎么办？

Aspose.Cells 支持此功能。本主题说明如何使用此功能。
### **格式化所选字符**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。 Workbook 类包含一个 Worksheets 集合，允许访问 Excel 文件中的每个工作表。工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。 Worksheet 类提供了一个 Cells 集合。 Cells 集合中的每个项目代表[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)班级。

Cell 类提供了字符方法，该方法采用以下参数来选择单元格中的字符范围：

- **起始索引**开始选择的字符的索引。
- **字符数**要选择的字符数。

在输出文件的 A1" 单元格中，单词 'Visit' 的格式为默认字体，但为 'Aspose!'是粗体和蓝色。

**格式化所选字符** 

![待办事项：图片_替代_文本](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

如果你有兴趣[在[单元格]中格式化部分富文本](/cells/zh/java/access-and-update-the-portions-of-rich-text-of-cell/) 考虑使用 Cell.getCharacters & Cell.setCharacters 方法。 Cell.getCharacters 方法用于访问文本部分，然后可以使用 Cell.setCharacters 方法进行修改，而**得到**方法返回一个 FontSetting 对象数组，可以对其进行操作以设置各种属性字体名称、字体颜色、粗体等，以及**放**方法可用于应用更改。

{{% /alert %}} 
## **激活工作表并激活 Cell 或在工作表中选择范围 Cells**
有时，您可能需要激活一个特定的工作表，以便当有人在 Microsoft Excel 中打开文件时首先显示它。您可能还需要以滚动条滚动到活动单元格以便清晰可见的方式激活特定单元格。 Aspose.Cells 能够完成上述所有任务。

活动工作表是您在工作簿中处理的工作表。默认情况下，活动工作表选项卡上的名称为粗体。同时，活动单元格是选中的单元格，当您开始键入时，数据会输入到该单元格中。一次只有一个细胞处于活动状态。活动单元格被粗边框包围，使其与其他单元格相对照。 Aspose.Cells 还允许您在工作表中选择一系列单元格。
### **激活工作表并激活 Cell**
Aspose.Cells 为这些任务提供了特定的 API。例如，WorksheetCollection.setActiveSheetIndex 方法对于设置活动工作表很有用。同样，Worksheet.setActiveCell 方法用于设置和获取工作表中的活动单元格。

如果您希望在 Microsoft Excel 中打开文件时将水平和垂直滚动条滚动到行和列索引位置以便更好地查看所选数据，请使用 Worksheet.setFirstVisibleRow 和 Worksheet.setFirstVisibleColumn 属性。

以下示例显示如何激活工作表并使其中的单元格处于活动状态。滚动条滚动使第 2 行和第 2 列成为它们的第一个可见行和列。

**将 B2 单元格设置为活动单元格** 

![待办事项：图片_替代_文本](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **在工作表中选择范围 Cells**
Aspose.Cells 提供方法 Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers)。使用最后一个参数 - removeOthers - 为 true，删除工作表中的其他单元格或单元格范围选择。

下面的示例演示如何在活动工作表中选择一系列单元格。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

上述所有类和方法在 Aspose.Cells 的许可版本中可用。

{{% /alert %}} 
## **格式化行和列**
格式化电子表格中的行和列以使报告看起来更美观可能是 Excel 应用程序使用最广泛的功能。 Aspose.Cells API 还通过其数据模型通过公开 Style 类提供此功能，该类主要处理所有与样式相关的功能，例如字体及其属性、文本对齐、背景/前景色、边框、数字和日期文字的显示格式等. Aspose.Cells API 提供的另一个有用的类是 StyleFlag，它允许 Style 对象的可重用性。

在本文中，我们将尝试解释如何使用 Aspose.Cells for Java API 将格式应用于行和列。
### **格式化行和列**
Aspose.Cells提供了一个类，[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个 WorksheetCollection，它允许访问 Excel 文件中的每个工作表。工作表由 Worksheet 类表示。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供 Cells 集合。 Cells 集合提供了一个 Rows 集合。
#### **格式化一行**
Rows 集合中的每一项都代表一个 Row 对象。 Row 对象提供用于将格式应用到行的 applyStyle 方法。

要对一行应用相同的格式，请使用 Style 对象：

1. 通过调用其 createStyle 方法将 Style 对象添加到 Workbook 类。
1. 设置 Style 对象属性以应用格式设置。
1. 将配置的 Style 对象分配给 Row 对象的 applyStyle 方法。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **格式化列**
Cells 集合提供了一个 Columns 集合。 Columns 集合中的每一项都代表一个 Column 对象。与 Row 对象类似，Column 对象提供了用于设置列格式的 applyStyle 方法。使用 Column 对象的 applyStyle 方法以与行相同的方式格式化列。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **设置行和列的数字和日期的显示格式**
如果要求为完整的行或列设置数字和日期的显示格式，那么该过程或多或少与上面讨论的相同，但是，不是为文本内容设置参数，而是为数字设置格式和日期使用 Style.Number 或 Style.Custom。请注意，Style.Number 属性是整数类型，指的是内置数字和日期格式，而 Style.Custom 属性是字符串类型，接受有效模式。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

请查看详细文章[设置数字和[日期]的显示格式](/cells/zh/java/data-formatting/).

{{% /alert %}}
