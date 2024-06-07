---
title: 处理Worksheets GridWeb
type: docs
weight: 30
url: /zh/java/working-with-worksheets-gridweb/
---

## **访问工作表**

这个主题讨论了访问GridWeb控件的工作表。我们也可以称这些工作表为Web工作表，因为它们属于GridWeb并在Web应用程序中使用。

GridWeb控件中包含的所有工作表都存储在GridWeb控件的GridWorksheetCollection中。通过其表索引访问特定工作表非常简单。

开发人员可以通过在示例代码片段中指定其表索引来访问特定工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **移除工作表**

本主题提供了使用GridWeb API从Microsoft Excel文件中移除工作表的简要信息。通过指定工作表的表索引来移除工作表。

开发人员可以通过在示例代码片段中所示的方式，通过指定表索引从GridWorksheetCollection集合中删除特定工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **添加工作表**

工作表是GridWeb的重要组成部分。所有数据以工作表的形式进行管理和存储。GridWeb允许开发人员向Aspose.Cells.GridWeb控件添加一个或多个工作表。本主题展示了向GridWeb添加工作表的简单方法。

### **不指定工作表名称**

向Aspose.Cells.GridWeb添加工作表的最简单方法是调用GridWeb控件中GridWorksheetCollection类的add方法。

**输出：已将具有默认名称的工作表添加到GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **使用指定的表名称**

为了向GridWeb控件添加名称特定的工作表，而不是使用默认命名方案，调用重载版本的add方法，传入指定字符串SheetName。

**输出：已向GridWeb添加了一个具有指定名称的工作表** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

add() 方法返回新工作表的索引，可用于访问此工作表实例。

{{% /alert %}}

## **重命名工作表**

当与GridWeb中的许多工作表一起工作并决定更改它们的名称以使其更有意义时，重命名工作表非常有用。

### **重命名工作表**

所有工作表都包含一个允许开发人员访问或修改工作表名称的Name属性。

1. 从GridWorksheetCollection访问工作表。
1. 重命名所选工作表。

{{% alert color="primary" %}}

有关如何访问Aspose.Cells.GridWeb中的工作表的更多详细信息，请参阅[访问工作表](/cells/zh/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets)。

{{% /alert %}}

在执行代码之前，工作表具有默认名称，如Sheet1。

**输入文件：工作表具有默认名称Sheet1** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

运行代码后，工作表被重命名为Invoice。

**输出：工作表已重命名为Invoice** 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **复制工作表**

[添加工作表](/cells/zh/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)描述了如何向GridWeb添加新工作表。

### **使用表索引**

以下示例代码显示如何通过在GridWorksheetCollection的addCopy方法中指定工作表的索引向GridWeb控件添加工作表的副本。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **使用工作表名称**
以下示例代码显示如何通过在GridWorksheetCollection的addCopy方法中指定工作表的名称向GridWeb控件添加工作表的副本。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

addCopy方法返回新添加工作表的索引，可以用于访问工作表实例。

{{% /alert %}}

## **使用命名区域**

通常，列和行标签用于唯一地引用单元格。但你可以创建描述性名称来表示单元格、单元格范围、公式或常量值。

单词**名称**可能指代代表单元格、单元格范围、公式或常量值的一系列字符。例如，使用易于理解的名称，例如Products，来指代难以理解的范围，例如Sales!C20:C30。

标签可以用于引用同一工作表上的数据的公式；如果您想要表示另一个工作表上的范围，则可以使用名称。**命名范围** 是Microsoft Excel中最强大的功能之一。

用户可以给一个范围命名，然后在公式中使用该名称。Aspose.Cells.GridWeb支持这一功能。

### **在公式中添加/引用命名区域**

GridWeb控件提供了两个类(GridName 和 GridNameCollection) 用于处理命名范围。

以下代码片段将帮助您了解如何使用它们。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **管理工作表中的批注**

本主题讨论了如何向工作表添加、访问和移除批注。批注可用于为将使用工作表的用户添加注释或有用信息。开发人员可以灵活地向工作表的任何单元格添加批注。

### **处理批注**

#### **添加批注**

要向工作表添加批注，请按照以下步骤进行：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 表单。
1. 访问要添加批注的工作表。
1. 向单元格添加注释。
1. 为新的批注设置备注。

**已向工作表添加批注** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **访问评论**

要访问批注：

1. 访问包含批注的单元格。
1. 获取单元格的引用。
1. 将引用传递给Comment集合以访问批注。
1. 现在可以修改批注的属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **删除评论**

要移除批注：

1. 如上所述访问单元格。
1. 使用Comment集合的removeAt方法移除批注。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **在工作表中管理超链接**

本主题讨论了Aspose.Cells.GridWeb支持哪些类型的超链接以及如何通过编程方式管理它们。超链接可用于创建指向Web URL或执行服务器端回发的链接。

### **超链接类型**

Aspose.Cells.GridWeb支持以下类型的超链接：

- 文本URL超链接，应用于文本的URL超链接。
- 图像URL超链接，应用于图像的URL超链接。

#### **文本URL超链接**

下面的示例在工作表中添加了两个超链接。一个具有_blank目标，另一个设置为_parent。

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**输出：工作表中添加的文本超链接**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **图像URL超链接**

下面的示例将图像URL超链接添加到工作表中。

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**输出：工作表中添加的图像超链接**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **数据排序**

数据处理时，排序是非常有价值的功能。未排序的数据在搜索特定信息时对用户来说是一个痛点。Aspose.Cells.GridWeb支持强大的排序功能。本主题讨论使用Aspose.Cells.GridWeb API对数据进行排序。

Aspose.Cells.GridWeb允许开发人员按水平和垂直方向对数据进行排序，使开发人员可以从上到下或从左到右对数据进行排序。

### **从上到下**

要按从上到下的方向对数据进行排序：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问要进行排序的工作表。
1. 以任何顺序（升序或降序）对数据范围进行排序。确保选择从上到下的方向。

下面的示例按升序对工作表中两列（学生ID和学生姓名）的数据进行排序。仅有两列的十二行在从上到下的方向上排序。

在应用代码之前，工作表包含无序数据。

**输入：未排序数据** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

执行代码后，数据按升序排序。

**输出：数据按从上到下的方式按升序排序** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **从左到右**

要按从左到右的方向对数据进行排序：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问要进行排序的工作表。
1. 以任何顺序（升序或降序）对数据范围进行排序。确保选择从左到右的方向。

下面的示例按升序对工作表中两行（学生ID和学生姓名）的数据进行排序。仅有四列的两行按从左到右的方式排序。

在应用代码之前，工作表包含无序数据。

**输入：执行代码片段之前的未排序数据** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

执行代码后，数据按升序排序。

**输出：数据按从左到右的方式按升序排序** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **搜索和替换**

在大型电子表格中进行重复更改最快捷的方法之一是使用查找和替换功能。查找帮助您定位文本字符串或数据，并用新值替换它。Aspose.Cells.GridWeb提供此功能。它使您能够通过简单对话框在工作表客户端端搜索和替换特定文本字符串或值。它甚至允许您搜索部分数据。

### **查找/替换对话框**

打开查找/替换对话框有两种方式：

1. 当控件激活时，按 **CTRL+F** 打开对话框，或按 **CTRL+R** 键打开对话框并启用 **Replace** 按钮。
1. 将光标移到工作表的单元区域，然后右键单击。 从菜单中选择 **查找** 或 **替换**。

**选择查找**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

显示查找和替换对话框。

**查找/替换对话框**

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

**使用查找**

搜索:

1. 打开查找/替换对话框。
1. 在“查找内容”字段中键入要搜索的字符串。
1. 单击“查找下一个”进行搜索。

突出显示与您的查找条件匹配的下一个单元格。

{{% alert color="primary" %}}

如果未找到搜索条件，将显示对话框进行通知。

{{% /alert %}}

### **搜索选项**

您可以在对话框中自定义一些搜索选项。 下表列出了它们。

|**编号**|**选项名称**|**描述**|
| :- | :- | :- |
|1|匹配大小写|指示在搜索中是否区分大小写。
|2|匹配整个单词|指示在搜索中是否匹配整个单词。
|3|向上搜索|指示搜索是从底部到顶部进行的。
|4|正则表达式|选中后，控件将视Find what文本框中的字符串为正则表达式。
|5|在公式/值中查找|如果选择公式，则控件将匹配单元格的公式或未格式化值，如果存在公式或未格式化值。 如果选择值，则控件将仅匹配单元格的显示值。

### **使用替换**

要替换文本或值:

1.按 **CTRL+F** 打开查找/替换对话框，或者右键单击单元格并在单击 **替换** 之前选择 **查找**。
1. 在 **替换为** 字段中键入替换字符串。
1. 单击 **替换**。

要替换文本:

1. 打开对话框。
1. 在 **查找内容** 字段中输入要查找的文本，在 **替换为** 字段中输入要替换的文本。
1. 点击**查找下一个**，然后点击**替换** 逐一替换一次出现。
1. 如果您非常确定工作表包含的内容，请单击 **全部替换**。

{{% alert color="primary" %}}

如果工作表不在编辑模式下，**替换**按钮将不会显示。

{{% /alert %}}

## 从客户端添加/删除超链接

Aspose.Cells GridWeb 现在支持从客户端添加和删除超链接。为此，API提供了"addCelllink"和"delCelllink"函数。以下代码片段演示了如何在GridWeb中从客户端添加和删除超链接。

###示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

您还可以使用以下代码片段链接表格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## 从客户端更新字体设置

Aspose.Cells GridWeb现在支持从客户端更改字体设置。为此，API提供以下功能

- **updateCellFontStyle**：参数-r/i/b/ib用于常规/斜体/粗体/斜体＆＆粗体
- **updateCellFontSize**：参数-fontname，等等。‘系统’
- **updateCellFontName**：参数-字体大小，等等。‘12pt’
- **updateCellFontColor**：参数-无/u/l/ul/用于无/下划线/删除线/下划线&&删除线
- **updateCellFontLine**：参数-HTML颜色，如#aa22ee或绿色、红色等大家知道的颜色名称
- **updateCellBackGroundColor**：参数-HTML颜色，如#aa22ee或绿色、红色等大家知道的颜色名称

以下代码片段演示了如何在GridWeb中从客户端更改字体设置。

###示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## 从客户端添加/删除批注

Aspose.Cells GridWeb现在支持在客户端添加和删除注释。为此，API提供了"addcomments"和"delcomments"函数。以下代码片段演示了如何在GridWeb中从客户端添加和删除注释。

###示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## 显示按钮以添加/删除工作表

Aspose.Cells GridWeb现在通过在工具栏中使用按钮来添加和删除工作表。要在前端显示按钮，您需要将**GridWeb1.ShowAddButton**设置为**true**。以下代码片段演示了如何向GridWeb工具栏添加添加/删除按钮。

###示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
