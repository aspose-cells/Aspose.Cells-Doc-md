---
title: 数据格式化
type: docs
weight: 80
url: /zh/java/data-formatting/
---

## **在单元格中格式化数据的方法**
如果工作表单元格正确格式化，用户更容易阅读单元格的内容（数据）是一个常见事实。 有许多格式化单元格及其内容的方法。 最简单的方法是在Microsoft Excel中使用所见即所得环境格式化单元格，同时创建设计师电子表格。 创建设计师电子表格后，您可以使用Aspose.Cells打开电子表格，保留所有格式设置与电子表格一起保存。 格式化单元格及其内容的另一种方法是使用Aspose.Cells API。 在本主题中，我们将描述使用Aspose.Cells API格式化单元格及其内容的两种方法。
### **格式化单元格**
开发人员可以使用 Aspose.Cells 灵活的 API 格式化单元格及其内容。Aspose.Cells 提供一个代表 Microsoft Excel 文件的 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类包含一个 [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，允许访问 Excel 文件中的每个工作表。 工作表由 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类提供一个单元格集合。 单元格集合中的每个项目都代表一个 **Cell** 类的对象。

Aspose.Cells 在[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类中提供 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 属性，用于设置单元格的格式样式。此外，Aspose.Cells 还提供了一个 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 类，用于实现相同目的。应用不同类型的格式样式来设置单元格的背景或前景色，边框，字体，水平和垂直对齐，缩进级别，文本方向，旋转角度等。
#### **使用 setStyle 方法**
在为不同单元格应用不同格式样式时，最好使用 [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的 setStyle 方法。下面给出一个示例，演示如何使用 setStyle 方法在单元格上应用各种格式设置。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formatting-FormattingCellsUsingsetStyleMethod-1.java" >}}




#### **使用样式对象**
在为不同单元格应用相同格式样式时，请使用 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 对象。

1. 通过调用 Workbook 类的 createStyle 方法将 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 对象添加到 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类的样式集合中。
1. 从样式集合中访问新增的样式对象。
1. 设置样式对象的所需属性，以应用所需的格式设置。
1. 将配置的样式对象分配给任何所需单元格的 Style 属性。

这种方法可以极大地提高您的应用程序的效率，并节省内存。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingCellsUsingStyleObject-FormattingCellsUsingStyleObject.java" >}}




#### **应用渐变填充效果**
要向单元格应用所需的梯度填充效果，请相应地使用样式对象的 setTwoColorGradient 方法。
#### **代码示例**
通过执行以下代码可实现以下输出。 

**应用渐变填充效果** 

![todo:image_alt_text](data-formatting_1.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ApplyGradientFillEffects-ApplyGradientFillEffects.java" >}}




## **配置对齐设置**
任何使用Microsoft Excel格式化单元格的人都将熟悉Microsoft Excel中的对齐设置。

**Microsoft Excel中的对齐设置** 

![todo:image_alt_text](data-formatting_2.png)

如您从上图看到的，有不同种类的对齐选项：

- [文本对齐](/cells/zh/java/data-formatting/)（水平和垂直）
- [缩进](/cells/zh/java/data-formatting/)
- [方向](/cells/zh/java/data-formatting/)
- [文本控制](/cells/zh/java/data-formatting/)
- [文本方向](/cells/zh/java/data-formatting/)

Aspose.Cells完全支持所有这些对齐设置，并在下面更详细地讨论。
### **配置对齐设置**
Aspose.Cells 提供一个代表 Excel 文件的 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类。 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个允许访问 Excel 文件中每个工作表的 WorksheetCollection。 工作表由 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。

Worksheet 类提供一个单元格集合。 单元格集合中的每个项目都代表 [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 类的对象。

Aspose.Cells 在 [Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell) 类中提供了 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 类的 setStyle 方法，用于单元格的格式设置。[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 类提供了用于配置字体设置的有用属性。

使用 TextAlignmentType 枚举选择任何文本对齐类型。 TextAlignmentType 枚举中的预定义文本对齐类型有：

|**文本对齐类型**|**描述**|
| :- | :- |
|Bottom|代表底部文本对齐|
|Center|代表居中文本对齐|
|CenterAcross|代表跨越式居中文本对齐|
|Distributed|代表分布式文本对齐|
|Fill|代表填充文本对齐|
|General|代表一般文本对齐|
|Justify|代表两端对齐文本对齐|
|Left|代表左文本对齐|
|Right|代表右文本对齐|
|Top|代表顶部文本对齐|
{{% alert color="primary" %}} 

您还可以使用 Style.setJustifyDistributed() 方法应用分散对齐设置。

{{% /alert %}} 
#### **水平对齐**
使用 [Style](https://reference.aspose.com/cells/java/com.aspose.cells/style) 对象的 setHorizontalAlignment 方法将文本水平对齐。

通过执行以下示例代码，可实现以下输出：

**将文本水平对齐** 

![todo:image_alt_text](data-formatting_3.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentHorizontal-TextAlignmentHorizontal.java" >}}




#### **垂直对齐**
使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的setVerticalAlignment方法来垂直对齐文本。

当VerticalAlignment设置为居中时，可以实现以下输出。

**将文本垂直对齐** 

![todo:image_alt_text](data-formatting_4.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextAlignmentVertical-TextAlignmentVertical.java" >}}




### **缩进**
通过使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的setIndentLevel方法，可以设置单元格中文本的缩进级别。

当IndentLevel设置为2时，可以实现以下输出。

**缩进级别调整为2** 

![todo:image_alt_text](data-formatting_5.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Indentation-ImportingfromResultSet.java" >}}




### **方向**
使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的setRotationAngle方法来设置单元格中文本的方向（旋转角度）。

当旋转角度设置为25时，可以实现以下输出。

**旋转角度设置为25** 

![todo:image_alt_text](data-formatting_6.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-Orientation-Orientation.java" >}}




### **文本控制**
以下部分讨论如何通过设置文本换行、适应和其他格式设置选项来控制文本。
#### **文本换行**
在单元格中换行文本使得阅读更容易：单元格的高度会调整以适应所有的文本，而不是截断或溢出到相邻单元格。

使用[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的setTextWrapped方法来打开或关闭文本换行。

当启用文本换行时，可以实现以下输出。

**文本在单元格内换行** 

![todo:image_alt_text](data-formatting_7.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WrapText-WrapText.java" >}}




#### **缩小以适应**
在字段中换行文本的选项是缩小文本大小以适应单元格尺寸。方法是将[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的IsTextWrapped属性设置为**true**。

当将文本缩小以适应单元格时，可以实现以下输出。

**文本缩小以适应单元格边界** 

![todo:image_alt_text](data-formatting_8.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ShrinkingToFit-ShrinkingToFit.java" >}}




#### **合并单元格**
与Microsoft Excel一样，Aspose.Cells支持将多个单元格合并为一个单元格。

如果将第一行中的三个单元格合并成一个大单元格，则可以实现以下输出。

**三个单元格合并成一个大单元格** 

![todo:image_alt_text](data-formatting_9.png)

使用[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/cells)集合的Merge方法来合并单元格。Merge方法接受以下参数：

- 第一行，从哪一行开始合并。
- 第一列，从哪一列开始合并。
- 行数，要合并的行数。
- 列数，要合并的列数。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}




### **文本方向**
可以设置单元格文本的阅读顺序。阅读顺序是显示字符、单词等的视觉顺序。例如，英语是一种从左到右的语言，而阿拉伯语是一种从右到左的语言。

阅读顺序通过[Style](https://reference.aspose.com/cells/java/com.aspose.cells/style)对象的TextDirection属性设置。Aspose.Cells在TextDirectionType枚举中提供了预定义的文本方向类型。

|**文本方向类型**|**描述**|
| :- | :- |
|Context|与第一个输入字符的语言一致的阅读顺序|
|LeftToRight|从左到右的阅读顺序|
|RightToLeft|从右到左的阅读顺序|






{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ChangeTextDirection-ChangeTextDirection.java" >}}





如果将文本的阅读顺序设置为从右到左，则可以实现以下输出。

**将文本阅读顺序设置为从右到左** 

![todo:image_alt_text](data-formatting_10.png)
## **格式化单元格中的选定字符**
[处理字体设置](/cells/zh/java/dealing-with-font-settings/)解释了如何格式化单元格，但只讲解了如何格式化整个单元格的内容。如果您只想格式化选定的字符，该怎么办？

Aspose.Cells 支持此功能。本主题解释了如何使用此功能。
### **格式化选定的字符**
Aspose.Cells提供了一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个Microsoft Excel文件。Workbook类包含一个Worksheets集合，允许访问Excel文件中的每个工作表。一个工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。Worksheet类提供了一个Cells集合。Cells集合中的每个条目代表一个[Cell](https://reference.aspose.com/cells/java/com.aspose.cells/cell)类的对象。

Cell类提供了一个characters方法，该方法接受以下参数选定单元格中一系列字符的范围：

- **起始索引**，开始选择的字符的索引。
- **字符数**，要选择的字符数。

在输出文件中，A1" 单元格中，'Visit' 一词使用默认字体格式，但 'Aspose!' 是粗体且为蓝色。

**格式化选定的字符** 

![todo:image_alt_text](data-formatting_11.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingSelectedCharacters-FormattingSelectedCharacters.java" >}}







{{% alert color="primary" %}} 

如果您有兴趣[格式化单元格中的富文本的一部分](/cells/zh/java/access-and-update-the-portions-of-rich-text-of-cell/)，考虑使用Cell.getCharacters和Cell.setCharacters方法。Cell.getCharacters方法用于访问文本的各个部分，然后可以使用Cell.setCharacters方法进行修改，而**获取**方法返回一个FontSetting对象数组，可以进行设置各种属性的字体名称，字体颜色，粗体等，**设置**方法可以用于应用更改。

{{% /alert %}} 
## **激活工作表并将活动单元格或选择工作表中的单元格范围**
有时，您可能需要激活特定工作表，使其在Microsoft Excel中打开文件时首先显示。您还可能需要激活特定单元格，使滚动条滚动到活动单元格，以便它清楚可见。Aspose.Cells能够执行所有上述任务。

活动工作表是工作簿中正在处理的工作表。活动工作表的标签名称默认为粗体。而活动单元格是您选择的单元格，在开始输入数据时将数据输入其中。每次只有一个单元格是活动的。活动单元格周围有粗边框，以使其在其他单元格之间显示。Aspose.Cells还允许您在工作表中选择一系列单元格。
### **激活工作表并使单元格活动**
Aspose.Cells为这些任务提供了特定的API。例如，WorksheetCollection.setActiveSheetIndex方法用于设置活动工作表。类似地，Worksheet.setActiveCell方法用于在工作表中设置和获取活动单元格。

如果您希望在Microsoft Excel中打开文件时，水平和垂直滚动条滚动到行和列索引位置，以便查看选定数据，可以使用Worksheet.setFirstVisibleRow和Worksheet.setFirstVisibleColumn属性。

以下示例展示了如何激活工作表并使其中的一个单元格活动。滚动条被滚动到使第2行和第2列为其第一个可见行和列。

**将B2单元格设置为活动单元格** 

![todo:image_alt_text](data-formatting_12.png)





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MakeCellActive-MakeCellActive.java" >}}




#### **选择工作表中的一系列单元格**
Aspose.Cells提供了方法Worksheet.selectRange(int startRow, int startColumn, int totalRows, int totalColumns, bool removeOthers)。使用最后一个参数 - removeOthers - 为true，将删除工作表中其他单元格或单元格范围的选择。

以下示例展示了如何在活动工作表中选择一系列单元格。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SelectRangeofCellsinWorksheet-SelectRangeofCellsinWorksheet.java" >}}







{{% alert color="primary" %}} 

所有上述类和方法均适用于Aspose.Cells的许可版本。

{{% /alert %}} 
## **格式化行和列**
在电子表格中格式化行和列，以使报告具有外观，可能是Excel应用程序最广泛使用的功能。Aspose.Cells API还通过其数据模型提供此功能，通过公开处理所有样式相关功能的Style类，如字体及其属性，文本对齐，背景/前景颜色，边框，数字和日期文本的显示格式等。Aspose.Cells API提供的另一个有用类是StyleFlag，允许重复使用Style对象。 

在本文中，我们将尝试解释如何使用Aspose.Cells for Java API为行和列应用格式。 
### **格式化行和列**
Aspose.Cells提供了一个类，[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个Microsoft Excel文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。一个工作表由Worksheet类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了Cells集合。Cells集合提供了Rows集合。
#### **格式化行**
Rows集合中的每个项代表一个行对象。Row对象提供了applyStyle方法，用于将格式应用于行。

要将相同的格式应用于一行，使用Style对象：

1. 通过调用其createStyle方法将Style对象添加到Workbook类。
2. 设置Style对象属性以应用格式设置。
1. 将配置的Style对象分配给Row对象的applyStyle方法。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingARow-FormattingARow.java" >}}




#### **格式化列**
Cells集合提供了一个Columns集合。 Columns集合中的每个项目代表一个Column对象。类似于Row对象，Column对象提供了applyStyle方法，用于设置列格式。使用Column对象的applyStyle方法来为列设置格式，方法与为行格式化方式相同。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FormattingAColumn-FormattingAColumn.java" >}}




#### **设置行和列的数字和日期显示格式**
如果需要为整个行或列设置数字和日期的显示格式，则过程与上文讨论的大致相同，但是，而不是为文本内容设置参数，您将使用Style.Number或Style.Custom设置数字和日期的格式。 请注意，Style.Number属性为整数类型，指的是内置的数字和日期格式，而Style.Custom属性为字符串类型，接受有效的模式。





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingDisplayFormat-SettingDisplayFormat.java" >}}







{{% alert color="primary" %}} 

请查看关于[设置数字和日期显示格式的详细文章](/cells/zh/java/data-formatting/)

{{% /alert %}}
