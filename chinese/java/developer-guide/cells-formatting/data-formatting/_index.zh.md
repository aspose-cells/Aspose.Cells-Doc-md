---
title: 数据格式化
type: docs
weight: 80
url: /zh/java/data-formatting/
---

## **在单元格中格式化数据的方法**
众所周知，如果工作表单元格格式正确，用户可以更轻松地阅读单元格内容（数据）。有多种方法可以格式化单元格及其内容。最简单的方法是在创建设计者电子表格时，在一个所见即所得的环境中使用Microsoft Excel格式化单元格。创建设计者电子表格后，可以使用Aspose.Cells打开电子表格，保留电子表格中的所有格式设置。另一种格式化单元格及其内容的方法是利用Aspose.Cells API。在本主题中，我们将描述两种使用Aspose.Cells API格式化单元格及其内容的方法。
### **格式化单元格**
开发人员可以使用Aspose.Cells的灵活API对单元格及其内容进行格式化。Aspose.Cells提供了一个代表Microsoft Excel文件的类，Workbook。Workbook类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。工作表由Worksheet类表示。Worksheet类提供了一个Cells集合。Cells集合中的每个项代表Cell类的对象。

Aspose.Cells在Cell类中提供了Style属性，用于设置单元格的格式样式。此外，Aspose.Cells还提供了一个Style类，用于相同的目的。对单元格应用不同类型的格式样式以设置其背景或前景颜色，边框，字体，水平和垂直对齐，缩进级别，文本方向，旋转角度等。
#### **使用setStyle方法**
当对不同的单元格应用不同的格式样式时，最好使用Cell类的setStyle方法。下面提供了一个示例来演示如何使用setStyle方法在单元格上应用各种格式设置。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **使用Style对象**
当将相同的格式样式应用于不同的单元格时，请使用Style对象。

1.通过调用Workbook类的createStyle方法将Style对象添加到Workbook类的Styles集合中。
1.从Styles集合中访问新添加的Style对象。
1.设置Style对象的所需属性以应用所需的格式设置。
1.将配置好的Style对象分配给任何所需单元格的Style属性。

这种方法可以极大地提高您的应用程序的效率，并节省内存。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **应用梯度填充效果**
要将所需的梯度填充效果应用于单元格，请相应使用Style对象的setTwoColorGradient方法。
#### **代码示例**
通过执行以下代码实现以下输出。 

应用梯度填充效果 

![todo:image_alt_text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **配置对齐设置**
任何使用Microsoft Excel格式化单元格的人都会熟悉Microsoft Excel中的对齐设置。

Microsoft Excel中的对齐设置 

![todo:image_alt_text](data-formatting_2.png)

从上面的图中可以看出，有不同种类的对齐选项：

- 文本对齐（水平和垂直）
- [缩进](/cells/zh/java/data-formatting/).
- [方向](/cells/zh/java/data-formatting/).
- [文本控制](/cells/zh/java/data-formatting/).
- [文本方向](/cells/zh/java/data-formatting/).

Aspose.Cells完全支持所有这些对齐设置，并在下面详细讨论。
### **配置对齐设置**
Aspose.Cells提供了一个代表Excel文件的[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类。Workbook类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。

Worksheet类提供了一个Cells集合。Cells集合中的每个项代表[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的对象。

Aspose.Cells为[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类提供了setStyle方法，用于设置单元格的格式。[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)类提供了配置字体设置的实用属性。

使用TextAlignmentType枚举选择任何文本对齐类型。TextAlignmentType枚举中预定义的文本对齐类型有：

|**文本对齐类型**|**描述**|
| :- | :- |
|Bottom|表示底部文本对齐
|Center|表示居中文本对齐
|CenterAcross|表示跨列居中文本对齐
|Distributed|表示分散文本对齐
|Fill|表示填充文本对齐
|General|表示常规文本对齐
|Justify|表示两端对齐文本对齐
|Left|表示左对齐文本对齐
|Right|表示右对齐文本对齐
|Top|表示顶部文本对齐|
{{% alert color="primary" %}} 

您还可以使用Style.setJustifyDistributed()方法应用分散两端设置。

{{% /alert %}} 
#### **水平对齐**
使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 对象的setHorizontalAlignment方法来水平对齐文本。

通过执行下面的示例代码可以实现以下输出:

**文本水平对齐** 

![todo:image_alt_text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **垂直对齐**
使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 对象的setVerticalAlignment方法来垂直对齐文本。

当VerticalAlignment设置为center时，会得到以下输出。

**文本垂直对齐** 

![todo:image_alt_text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **缩进**
可以使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的setIndentLevel方法来设置单元格中文本的缩进级别。

当IndentLevel设置为2时，会得到以下输出。

**缩进级别调整为2** 

![todo:image_alt_text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **方向**
使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 对象的setRotationAngle方法设置单元格中文本的方向（旋转）。

当旋转角度设置为25时，会得到以下输出。

**旋转角度设置为25** 

![todo:image_alt_text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **文本控制**
以下部分讨论了如何通过设置文本换行、缩小以适应和其他格式设置选项来控制文本。
#### **自动换行文本**
将单元格中的文本进行换行会使其更易于阅读：单元格的高度会根据文本的长度进行调整，而不是截断文本或溢出到相邻单元格。

可使用 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 对象的 setTextWrapped 方法来设置文本是否自动换行。

启用文本自动换行后，将获得以下输出。

**单元格内的文本已自动换行** 

![todo:image_alt_text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **缩小以适应**
在单元格中将文本缩小以适应单元格的尺寸是一个选项。可以通过设置 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 对象的 IsTextWrapped 属性为 **true** 来实现此功能。

将文本缩小以适应单元格后，将获得以下输出。

**文本缩小以适应单元格的边界** 

![todo:image_alt_text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **合并单元格**
与 Microsoft Excel 一样，Aspose.Cells 支持将多个单元格合并为一个单元格。

如果将第一行中的三个单元格合并，将获得以下输出，形成一个大的单元格。

**三个单元格被合并成一个大单元格** 

![todo:image_alt_text](data-formatting_9.png)

可以使用 [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells) 集合的 Merge 方法来合并单元格。Merge 方法带有以下参数：

- 第一行，合并开始的第一行。
- 第一列，合并开始的第一列。
- 行数，要合并的行数。
- 列数，要合并的列数。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **文本方向**
可以设置单元格中文本的阅读顺序。阅读顺序是字符、单词等显示的视觉顺序。例如，英语是从左到右的语言，而阿拉伯语是从右到左的语言。

阅读顺序是使用 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 对象的 TextDirection 属性设置的。Aspose.Cells 在 TextDirectionType 列挙中提供了预定义的文本方向类型。

|**文本方向类型**|**描述**|
| :- | :- |
|Context|与第一个输入字符的语言一致的阅读顺序
|LeftToRight|从左到右的阅读顺序
|RightToLeft|从右到左的阅读顺序






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





如果将文本的阅读顺序设置为从右到左，则会实现以下输出。

**将文本阅读顺序设置为从右到左** 

![todo:image_alt_text](data-formatting_10.png)
## **在单元格中格式化所选字符**
[处理字体设置](/cells/zh/java/dealing-with-font-settings/) 解释了如何格式化单元格，但只是如何格式化整个单元格的内容。如果你只想格式化选定的字符，该怎么办呢？

Aspose.Cells 支持此功能。本主题解释了如何使用此功能。
### **格式化所选字符**
Aspose.Cells 提供了一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，用于表示 Microsoft Excel 文件。Workbook 类包含一个 Worksheets 集合，允许访问 Excel 文件中的每个工作表。工作表由 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。Worksheet 类提供了一个 Cells 集合。Cells 集合中的每个项目代表 [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 类的对象。

Cell 类提供了 characters 方法，该方法接受以下参数来选择单元格中的字符范围:

- **起始索引**，从中开始选择的字符的索引。
- **字符数**，要选择的字符数。

在输出文件中，A1单元格中，“Visit”一词使用默认字体格式，但“Aspose!”是粗体和蓝色。

**格式化所选字符** 

![todo:image_alt_text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

如果您对[格式化单元格中的部分富文本](/cells/zh/java/access-and-update-the-portions-of-rich-text-of-cell/)感兴趣，请考虑使用 Cell.getCharacters 和 Cell.setCharacters 方法。Cell.getCharacters 方法用于访问文本的部分，然后可以使用 Cell.setCharacters 方法进行修改，而 **get** 方法返回可操作的 FontSetting 对象数组，用于设置各种属性，如字体名称、字体颜色、粗体等，**set** 方法可用于应用更改。

{{% /alert %}} 
## **激活工作表并在工作表中使活动单元格或选择一系列单元格**
有时，您可能需要激活特定的工作表，以便在打开文件后首先显示。您可能还需要以一种特定的方式激活特定的单元格，以便滚动条滚动到活动单元格，以便它清晰可见。Aspose.Cells 能够执行上述所有任务。

活动工作表是工作簿中正在操作的工作表。活动工作表选项卡上的名称默认为加粗。而活动单元格是选定的单元格，键入数据时将其输入。一次只能激活一个单元格。活动单元格四周有较粗的边框，以突显其与其他单元格的区别。Aspose.Cells 还允许您在工作表中选择单元格范围。
### **激活工作表并使单元格处于活动状态**
Aspose.Cells 为这些任务提供了具体的 API。例如，WorksheetCollection.setActiveSheetIndex 方法对于设置活动工作表非常有用。同样，Worksheet.setActiveCell 方法用于在工作表中设置和获取活动单元格。

如果希望水平和垂直滚动条在打开 Microsoft Excel 文件时滚动到行和列索引位置，以便查看所选择的数据，请使用 Worksheet.setFirstVisibleRow 和 Worksheet.setFirstVisibleColumn 属性。

下面的示例显示了如何激活工作表，并使其上的一个单元格处于活动状态。滚动条被滚动以使第二行和第二列成为其首个可见行和列。

**将B2单元设置为活动单元** 

![todo:image_alt_text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **在工作表中选择单元格范围**
Aspose.Cells 提供了方法 Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers)。通过将最后一个参数 removeOthers 设置为 true，可以去除工作表中其他单元格或单元格范围的选择。

下面的示例显示了如何在活动工作表中选择单元格范围。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

上述所有类和方法都在使用许可版本的 Aspose.Cells 中可用。

{{% /alert %}} 
## **格式化行和列**
在电子表格中格式化行和列，以使报表具有良好的外观，可能是 Excel 应用程序中使用最广泛的功能。Aspose.Cells API 也通过其数据模型提供此功能，通过公开处理所有样式相关功能(如字体及其属性、文本对齐、背景/前景颜色、边框、数字和日期文本的显示格式等)的 Style 类来提供此功能。Aspose.Cells API 还提供了一个有用的类 StyleFlag，它允许重复利用 Style 对象。 

在本文中，我们将尝试解释如何使用 Aspose.Cells for Java API 对行和列应用格式。 
### **格式化行和列**
Aspose.Cells 提供了一个表示 Microsoft Excel 文件的类 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类包含一个允许访问 Excel 文件中的每个工作表的 WorksheetCollection。工作表由 Worksheet 类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类提供了 Cells 集合。Cells 集合提供了 Rows 集合。
#### **格式化行**
Rows 集合中的每个项都表示一个 Row 对象。Row 对象提供了 applyStyle 方法，用于对行应用格式。

要对行应用相同的格式，使用 Style 对象：

1. 通过调用其 createStyle 方法将一个 Style 对象添加到 Workbook 类。
1. 设置 Style 对象的属性以应用格式设置。
1. 将配置好的 Style 对象分配给 Row 对象的 applyStyle 方法。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **格式化一列**
Cells 集合提供了 Columns 集合。Columns 集合中的每个项表示一个 Column 对象。与 Row 对象类似，Column 对象提供了 applyStyle 方法用于设置列格式。使用 Column 对象的 applyStyle 方法来格式化一列，方式与格式化行相同。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **设置行和列的数字和日期显示格式**
如果要设置完整行或列的数字和日期显示格式，则步骤与上述讨论的大致相同，但是，你将会使用 Style.Number 或 Style.Custom 来设置数字和日期的格式，而不是为文本内容设置参数。请注意，Style.Number 属性的类型为整数，指的是内置的数字和日期格式，而 Style.Custom 属性的类型为字符串，接受有效的模式。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

请查看关于 [设置数字和[日期]的显示格式](/cells/zh/java/data-formatting/) 的详细文章。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
