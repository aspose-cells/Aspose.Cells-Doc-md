---
title: 使用Worksheets GridWeb
type: docs
weight: 30
url: /zh/java/working-with-worksheets-gridweb/
---

## **访问工作表**

本主题讨论访问GridWeb控件的工作表。我们也可以称这些工作表为Web工作表，因为它们属于GridWeb并在Web应用程序中使用。

GridWeb控件中包含的所有工作表都存储在GridWeb控件的GridWorksheetCollection中。通过其工作表索引简单访问特定工作表。

开发人员可以通过在示例代码段中如下指定其工作表索引来访问特定工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **删除工作表**

本主题提供了使用GridWeb API从Microsoft Excel文件中删除工作表的简要信息。通过指定其工作表索引来删除工作表。

开发人员可以通过在示例代码段中如下指定其工作表索引使用GridWorksheetCollection集合的removeAt方法来删除特定工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **添加工作表**

工作表是GridWeb的一个组成部分。所有数据都以工作表的形式进行管理和存储。GridWeb允许开发人员向Aspose.Cells.GridWeb控件添加一个或多个工作表。本主题展示了向GridWeb添加工作表的简单方法。

### **不指定工作表名称**

向Aspose.Cells.GridWeb添加工作表的最简单方法是在GridWeb控件中调用GridWorksheetCollection类的add方法。这将创建使用默认名称（即Sheet1、Sheet2、Sheet3等）的工作表，并将它们添加到GridWeb控件。

**输出：一个带有默认名称的工作表已添加到GridWeb** 

![todo:image_alt_text](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **使用指定的表格名称**

为了向GridWeb控件添加指定名称的工作表，而不是使用默认命名方案，可以调用重载版本的add方法，传递指定的字符串SheetName。例如，下面的示例添加了一个名为Invoice的工作表。

**输出：已向GridWeb添加了具有指定名称的工作表** 

![todo:image_alt_text](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

add()方法返回新工作表的索引，可以用于访问该工作表的实例。有关如何访问工作表的更多详细信息，请阅读[访问工作表](/cells/zh/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets)。

{{% /alert %}}

## **重命名工作表**

在处理GridWeb中的多个工作表并决定将它们更名以使其更有意义时，重命名工作表可能非常有用。例如，包含发票的工作表可以更名为Invoice，而不是Sheet1。本主题描述了这一简单但有用的功能。

### **重命名工作表**

所有工作表都包含一个Name属性，允许开发人员访问或修改工作表的名称。要重命名工作表：

1. 从GridWorksheetCollection中访问工作表。
1. 重命名选定的工作表。

{{% alert color="primary" %}}

有关如何在Aspose.Cells.GridWeb中访问工作表的更多详细信息，请参阅[访问工作表](/cells/zh/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets)。

{{% /alert %}}

在执行代码之前，工作表具有默认名称，如Sheet1。

**输入文件：具有默认名称Sheet1的工作表** 

![todo:image_alt_text](working-with-worksheets-gridweb_3.png)

运行代码后，工作表将更名为Invoice。

**输出：工作表已更名为Invoice** 

![todo:image_alt_text](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **复制工作表**

[添加工作表](/cells/zh/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)描述了如何向GridWeb添加新工作表。还可以将另一个工作表的副本或复制品添加到Aspose.Cells.GridWeb控件中。当需要在另一个工作表中使用相同或相似数据时，这个功能非常有用。在这种情况下，复制现有工作表并将其作为新工作表添加到Aspose.Cells.GridWeb要比从头开始创建更容易。

### **使用Sheet索引**

下面的示例代码显示了如何通过在GridWorksheetCollection的addCopy方法中指定工作表的索引来向GridWeb控件添加一个工作表的副本。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **使用工作表名称**
下面的示例代码显示了如何通过在GridWorksheetCollection的addCopy方法中指定工作表的名称来向GridWeb控件添加一个工作表的副本。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

addCopy方法返回新添加的工作表的索引，可以用于访问工作表实例。有关如何访问工作表的更多详细信息，请阅读[访问工作表](/cells/zh/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets)。

{{% /alert %}}

## **使用命名范围**

通常使用列和行标签来唯一地引用单元格。但是，您可以创建描述性名称来表示单元格、单元格范围、公式或常量值。

单词**名称**可能指代代表单元格、单元格范围、公式或常量值的一串字符。例如，使用易于理解的名称，如Products，来引用难以理解的范围，如Sales!C20:C30。

标签可以用于引用同一工作表上的数据的公式；如果要表示另一个工作表上的范围，可以使用名称。**命名范围**是Microsoft Excel最强大的功能之一。

用户可以为范围分配一个名称，并在公式中使用该名称。Aspose.Cells.GridWeb支持此功能。

### **在公式中添加/引用命名范围**

GridWeb控件提供了两个类（GridName和GridNameCollection），用于处理命名范围。

下面的代码片段将帮助您了解如何使用它们。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **在工作表中管理评论**

本主题讨论了如何在工作表中添加、访问和移除评论。评论可用于为将要使用工作表的用户添加注释或有用信息。开发人员可以灵活地向工作表的任何单元格添加评论。

### **处理评论**

#### **添加评论**

要向工作表添加评论，请按照以下步骤进行：

1. 将Aspose.Cells.GridWeb控件添加到Web表单。
1. 访问要添加评论的工作表。
1. 向单元格添加评论。
1. 为新评论设置注释。

**已向工作表添加了评论** 

![todo:image_alt_text](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **访问评论**

要访问评论：

1. 访问包含评论的单元格。
1. 获取单元格的引用。
1. 将引用传递给评论集合以访问评论。
1. 现在可以修改评论的属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **移除评论**

要移除评论：

1. 如上所述访问单元格。
1. 使用评论集合的removeAt方法来删除评论。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **在工作表中管理超链接**

本主题讨论 Aspose.Cells.GridWeb 支持的超链接类型以及如何以编程方式管理它们。超链接可用于创建指向 Web URL 或执行服务器端回发的链接。

### **超链接类型**

Aspose.Cells.GridWeb支持以下超链接：

- 文本URL超链接，应用于文本的URL超链接。
- 图像URL超链接，应用于图像的URL超链接。

#### **文本URL超链接**

下面的示例在工作表中添加了两个超链接。其中一个具有_blank目标，而另一个设置为_parent。

![todo:image_alt_text](working-with-worksheets-gridweb_6.png)

**输出：向工作表添加文本超链接**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **图像URL超链接**

下面的示例向工作表添加图像URL超链接。

![todo:image_alt_text](working-with-worksheets-gridweb_7.png)

**输出：工作表中添加了图像超链接**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **排序数据**

排序是数据处理时非常宝贵的功能。未经排序的数据在用户搜索特定信息时非常痛苦。Aspose.Cells.GridWeb支持强大的排序功能。本主题讨论使用Aspose.Cells.GridWeb API排序数据。

Aspose.Cells.GridWeb允许开发人员水平和垂直排序数据，以便开发人员可以从上到下或从左到右排序数据。

### **从上到下**

要从上到下方向排序数据：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问您要排序的工作表。
1. 以任意顺序（升序或降序）对数据范围进行排序。确保选择从上到下的方向。

下面的示例按升序排序工作表中两列数据（学生ID和学生姓名）。只有两列十二行数据按从上到下的方式排序。

应用代码之前，工作表包含无序数据。

**输入：未排序的数据** 

![todo:image_alt_text](working-with-worksheets-gridweb_8.png)

执行代码后，数据按升序排序。

**输出：数据按从上到下的方式升序排序** 

![todo:image_alt_text](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **从左到右**

要从左到右排序数据：

1. 将Aspose.Cells.GridWeb控件添加到您的Web表单中。
1. 访问您要排序的工作表。
1. 以任意顺序（升序或降序）对数据范围进行排序。确保选择从左到右的方向。

下面的示例按升序排序工作表中两行数据（学生ID和学生姓名）。只有四列两行数据按从左到右的方式排序。

应用代码之前，工作表包含无序数据。

**执行代码片段前的未排序数据** 

![todo:image_alt_text](working-with-worksheets-gridweb_10.png)

执行代码后，数据按升序排序。

**输出：数据按从左到右的方式升序排序** 

![todo:image_alt_text](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **搜索和替换**

在大型电子表格中执行重复更改的最快方法之一是使用查找和替换功能。查找通过定位文本字符串或数据并替换为新值来帮助您。Aspose.Cells.GridWeb提供了此功能。它使您可以通过简单的对话框在工作表客户端端搜索和替换特定的文本字符串或值。它甚至允许您查找部分数据。

### **查找/替换对话框**

打开查找/替换对话框有两种方法：

1. 当控件处于活动状态时，按下**CTRL+F**以打开对话框，或者按下**CTRL+R**键以启用**替换**按钮打开对话框。
1. 将光标移动到工作表的单元格区域，然后右键单击。在菜单中选择**查找**或**替换**。

**选择查找**

![todo:image_alt_text](working-with-worksheets-gridweb_12.png)

显示查找和替换对话框。

**查找/替换对话框**

![todo:image_alt_text](working-with-worksheets-gridweb_13.png)

**使用查找**

要搜索：

1. 打开查找/替换对话框。
1. 在“查找内容”字段中键入要搜索的字符串。
1. 单击“查找下一个”进行搜索。

会突出显示满足查找条件的下一个单元格。

{{% alert color="primary" %}}

如果未找到符合条件的搜索结果，则会显示一个对话框告知您。

{{% /alert %}}

### **搜索选项**

对话框中有一些搜索选项可供自定义。下表列出了这些选项。

|**序号**|**选项名称**|**描述**|
| :- | :- | :- |
|1|区分大小写|指示是否在搜索中区分大小写。
|2|全字匹配|指示是否在搜索中匹配整个单词。
|3|向上搜索|指示搜索将从下到上进行。
|4|正则表达式|勾选后，控件将在搜索过程中将“查找内容”文本框中的字符串视为正则表达式。
|5|在公式/数值中查找|当选择“公式”时，控件将匹配单元格的公式或未格式化值（如果存在公式或未格式化值）。当选择“数值”时，控件将仅匹配单元格的显示值。

### **使用替换**

替换文本或值：

1. 通过按下**CTRL+F**或选择右击单元格并选择**查找**，然后再单击**替换**，打开查找/替换对话框。
1. 在**替换为**字段中键入替换字符串。
1. 单击**替换**。

替换文本：

1. 打开对话框。
1. 在**查找**字段中输入要查找的文本，然后在**替换为**字段中输入要替换的文本。
1. 通过单击**查找下一个**，然后单击**替换**，一次替换一个出现的实例。
1. 如果您非常确定工作表包含的内容，请单击**全部替换**。

{{% alert color="primary" %}}

如果工作表不处于编辑模式，则**替换**按钮不会显示。

{{% /alert %}}

## 在客户端添加/删除超链接

Aspose.Cells GridWeb 现在支持在客户端添加和删除超链接。为此，API 提供了"addCelllink"和"delCelllink"函数。以下代码片段演示了在 GridWeb 中在客户端添加和删除超链接。

### 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

您也可以使用以下代码片段链接到工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## 在客户端更新字体设置

Aspose.Cells GridWeb 现在支持从客户端更改字体设置。为此，API 提供了以下函数

- **updateCellFontStyle**：参数 - r/i/b/ib 分别代表正常/斜体/粗体/斜体和粗体
- **updateCellFontSize**：参数 - fontname 等，'System'
- **updateCellFontName**：参数 - fontsize 等，'12pt'
- **updateCellFontColor**：参数 - none/u/l/ul 代表无/下划线/删除线/下划线和删除线
- **updateCellFontLine**：参数 - html 颜色，如 #aa22ee 或绿色、红色等
- **updateCellBackGroundColor**：参数 - html 颜色，如 #aa22ee 或绿色、红色等

以下代码片段演示了在 GridWeb 中在客户端更改字体设置。

### 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## 在客户端添加/删除注释

Aspose.Cells GridWeb 现在支持在客户端添加和删除注释。为此，API 提供了"addcomments"和"delcomments"函数。以下代码片段演示了在 GridWeb 中在客户端添加和删除注释。

### 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## 显示添加/删除工作表的按钮

Aspose.Cells GridWeb现在支持通过工具栏中的按钮添加和删除工作表。要在前端显示按钮，需要将**GridWeb1.ShowAddButton**设置为**true**。以下代码片段演示了将添加/删除按钮添加到GridWeb工具栏。

### 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
