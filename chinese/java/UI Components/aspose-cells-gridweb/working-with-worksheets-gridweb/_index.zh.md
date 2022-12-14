---
title: 使用工作表 GridWeb
type: docs
weight: 30
url: /zh/java/working-with-worksheets-gridweb/
---
## **访问工作表**

本主题讨论访问 GridWeb 控件的工作表。我们也可以称这些工作表为web工作表，因为它们属于GridWeb，用于web应用。

GridWeb 控件中包含的所有工作表都存储在 GridWeb 控件的 GridWorksheetCollection 中。通过工作表索引访问特定工作表很简单。

开发人员可以通过指定工作表索引来访问特定工作表，如下面的示例代码片段所示。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingWorksheet-AccessingWorksheet.jsp" >}}

## **删除工作表**

本主题提供有关使用 GridWeb API 从 Microsoft Excel 文件中删除工作表的简要信息。通过指定工作表索引来删除工作表。

开发人员可以通过使用 GridWorksheetCollection 集合的 removeAt 方法指定工作表索引来删除特定工作表，如下面的示例代码片段所示。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingWorksheet-RemovingWorksheet.jsp" >}}

## **添加工作表**

工作表是 GridWeb 不可或缺的一部分。所有数据都以工作表的形式进行管理和存储。 GridWeb 允许开发人员向 Aspose.Cells.GridWeb 控件添加一个或多个工作表。本主题展示了将工作表添加到 GridWeb 的简单方法。

### **不指定工作表名称**

向 Aspose.Cells.GridWeb 添加工作表的最简单方法是在 GridWeb 控件中调用 GridWorksheetCollection 类的 add 方法。这将创建使用默认名称（即 Sheet1、Sheet2、Sheet3 等）的工作表并将它们添加到 GridWeb 控件。

**输出：具有默认名称的工作表已添加到 GridWeb** 

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithoutSpecificName-AddingWorksheetWithoutSpecificName.jsp" >}}

### **具有指定的工作表名称**

要将具有特定名称的工作表添加到 GridWeb 控件而不是使用默认命名方案，请调用采用指定字符串 SheetName 的 add 方法的重载版本。例如，下面的示例添加了一个名为 Invoice 的工作表。

**输出：具有指定名称的工作表已添加到 GridWeb** 

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingWorksheetWithSpecificName-AddingWorksheetWithSpecificName.jsp" >}}

{{% alert color="primary" %}}

 add() 方法返回新工作表的索引，可用于访问此工作表的实例。有关如何访问工作表的更多详细信息，请阅读[访问工作表](/cells/zh/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **重命名工作表**

在 GridWeb 中处理许多工作表并决定更改它们的名称以使它们更有意义时，重命名工作表可能非常有用。例如，可以将包含发票的工作表重命名为 Invoice 而不是 Sheet1。本主题描述了这个简单但有用的功能。

### **重命名工作表**

所有工作表都包含一个名称属性，允许开发人员访问或修改工作表的名称。要重命名工作表：

1. 从 GridWorksheetCollection 访问工作表。
1. 重命名选定的工作表。

{{% alert color="primary" %}}

 Aspose.Cells.GridWeb中工作表的访问方法请参考[访问工作表](/cells/zh/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

在执行代码之前，工作表有一个默认名称，例如 Sheet1。

**输入文件：默认名称为 Sheet1 的工作表** 

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_3.png)

运行代码后，工作表被重命名为 Invoice。

**输出：工作表重命名为 Invoice** 

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RenamingWorksheet-RenamingWorksheet.jsp" >}}

## **复制工作表**

[添加工作表](/cells/zh/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-addingworksheets)描述了如何向 GridWeb 添加新的工作表。也可以将另一个工作表的副本（或副本）添加到 Aspose.Cells.GridWeb 控件。当一个工作表中的相同或相似数据在另一个工作表中也需要时，此功能会很有用。在这种情况下，复制现有工作表并将其作为新工作表添加到 Aspose.Cells.GridWeb 比从头开始创建更容易。

### **使用工作表索引**

下面的示例代码显示了如何通过在 GridWorksheetCollection 的 addCopy 方法中指定工作表的索引来将工作表的副本添加到 GridWeb 控件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetIndex-CopyWorksheetUsingSheetIndex.jsp" >}}
### **使用工作表名称**
下面的示例代码显示了如何通过在 GridWorksheetCollection 的 addCopy 方法中指定工作表的名称来将工作表的副本添加到 GridWeb 控件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-CopyWorksheetUsingSheetName-CopyWorksheetUsingSheetName.jsp" >}}

{{% alert color="primary" %}}

 addCopy 方法返回新添加的工作表的索引，可用于访问工作表实例。有关如何访问工作表的更多详细信息，请阅读[访问工作表](/cells/zh/java/working-with-worksheets-gridweb/#workingwithworksheetsgridweb-accessingworksheets).

{{% /alert %}}

## **使用命名范围**

通常，列和行标签用于唯一引用单元格。但是您可以创建描述性名称来表示单元格、单元格区域、公式或常量值。

这个单词**姓名**可以指表示单元格、单元格范围、公式或常量值的字符串。例如，使用易于理解的名称（例如 Products）来指代难以理解的范围（例如 Sales!C20:C30）。

标签可用于引用同一工作表上数据的公式中；如果你想在另一个工作表上表示一个范围，你可以使用一个名称。**命名范围**是 Microsoft Excel 最强大的功能之一。

用户可以为范围指定一个名称并在公式中使用该名称。 Aspose.Cells.GridWeb 支持此功能。

### **在公式中添加/引用命名范围**

GridWeb 控件提供了两个类（GridName 和 GridNameCollection）用于处理命名范围。

以下代码片段将帮助您了解如何使用它们。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingNamedRangesinFormulas-AddingNamedRangesinFormulas.jsp" >}}

## **管理工作表中的评论**

本主题讨论在工作表中添加、访问和删除注释。注释对于为将使用工作表的用户添加注释或有用信息很有用。开发人员可以灵活地向工作表的任何单元格添加注释。

### **使用注释**

#### **添加评论**

要向工作表添加评论，请按照以下步骤操作：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问要添加评论的工作表。
1. 向单元格添加注释。
1. 为新评论设置注释。

**评论已添加到工作表** 

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AddingComments-AddingComments.jsp" >}}

#### **访问评论**

要访问评论：

1. 访问包含评论的单元格。
1. 获取单元格的引用。
1. 将引用传递给 Comment 集合以访问评论。
1. 现在可以修改评论的属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-AccessingComments-AccessingComments.jsp" >}}

#### **删除评论**

要删除评论：

1. 如上所述访问单元格。
1. 使用 Comment 集合的 removeAt 方法删除评论。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-RemovingComments-RemovingComments.jsp" >}}

## **管理工作表中的超链接**

本主题讨论 Aspose.Cells.GridWeb 支持哪些类型的超链接以及如何以编程方式管理它们。超链接可用于创建指向 Web URL 的链接或执行回发到服务器。

### **超链接的类型**

Aspose.Cells.GridWeb 支持以下超链接：

- 文本 URL 超链接，应用于文本的 URL 超链接。
- 图像 URL 超链接，应用于图像的 URL 超链接。

#### **文本 URL 超链接**

下面的示例将两个超链接添加到工作表。一个有一个_空白目标，而另一个设置为_父母。

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_6.png)

**输出：添加到工作表的文本超链接**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-TextURLHyperlinks-TextURLHyperlinks.jsp" >}}

#### **图片 URL 超链接**

下面的示例将图像 URL 超链接添加到工作表。

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_7.png)

**输出：添加到工作表的图像超链接**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-ImageURLHyperlinks-ImageURLHyperlinks.jsp" >}}

## **排序数据**

在数据处理方面，排序是一项非常有价值的功能。在搜索特定信息时，未排序的数据对用户来说是一种痛苦。 Aspose.Cells.GridWeb支持强大的排序功能。本主题讨论使用 Aspose.Cells.GridWeb API 对数据进行排序。

Aspose.Cells.GridWeb 允许开发者对数据进行水平和垂直排序，以便开发者可以从上到下或从左到右对数据进行排序。

### **从上到下**

要从上到下对数据进行排序：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问要排序的工作表。
1. 以任何顺序（升序或降序）对数据范围进行排序。请务必选择从上到下的方向。

下面的示例按升序对工作表的两列（学生 ID 和学生姓名）中的数据进行排序。只有十二行两列按从上到下的方向排序。

在应用代码之前，工作表包含无序数据。

**输入：未排序的数据** 

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_8.png)

执行代码后，数据按升序排序。

**输出：数据从上到下按升序排列** 

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromtoptobottomascendingorder-datasortedfromtoptobottomascendingorder.jsp" >}}

### **从左到右**

从左到右对数据进行排序：

1. 将 Aspose.Cells.GridWeb 控件添加到 Web 窗体。
1. 访问要排序的工作表。
1. 以任何顺序（升序或降序）对数据范围进行排序。一定要选择从左到右。

下面的示例按升序对两行（学生 ID 和学生姓名）中的数据进行排序。只有两行四列从左到右排序。

在应用代码之前，工作表包含无序数据。

**输入：执行代码片段前未排序的数据** 

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_10.png)

执行代码后，数据按升序排序。

**输出：数据从左到右按升序排列** 

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-datasortedfromleftrightascendingorder-datasortedfromleftrightascendingorder.jsp" >}}

## **搜索和替换**

在大型电子表格中进行重复更改的最快方法之一是使用查找和替换功能。 Find 可帮助您找到文本字符串或数据，并将其替换为新值。 Aspose.Cells.GridWeb提供了这个功能。它使您能够通过一个简单的对话框在工作表客户端中搜索并替换为特定的文本字符串或值。它甚至允许您查找部分数据。

### **查找/替换对话框**

有两种方法可以打开“查找/替换”对话框：

1. 当控件处于活动状态时，按**CTRL+F**打开对话框，或按**CTRL+R**键打开对话框**代替**按钮启用。
1. 将光标移动到工作表中的单元格区域，然后单击鼠标右键。选择**寻找**或者**代替**从菜单中。

**选择查找**

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_12.png)

将显示一个查找和替换对话框。

**查找/替换对话框**

![待办事项：图片_替代_文本](working-with-worksheets-gridweb_13.png)

**使用查找**

寻找：

1. 打开“查找/替换”对话框。
1. 在“查找内容”字段中键入要搜索的字符串。
1. 单击“查找下一个”进行搜索。

与您的查找条件相匹配的下一个单元格会突出显示。

{{% alert color="primary" %}}

如果未找到您的搜索条件，则会显示一个对话框告诉您。

{{% /alert %}}

### **搜索选项**

您可以在对话框中自定义一些搜索选项。下表列出了它们。

|**不。**|**选项名称**|**描述**|
|:- |:- |:- |
|1|相符|指示是否在搜索时区分大小写。|
|2|全字匹配|表示在搜索时是否全词匹配。|
|3|向上搜索|指示是否从下到上进行搜索。|
|4|正则表达式|选中后，控件将在查找过程中将“查找内容”文本框中的字符串视为正则表达式。|
|5|在公式/值中查找|选择公式后，如果存在公式或未格式化的值，控件将匹配单元格的公式或未格式化的值。选择值时，控件将仅匹配单元格的显示值。|

### **使用替换**

要替换文本或值：

1. 通过按打开“查找/替换”对话框**CTRL+F**，或选择右键单击一个单元格并选择**寻找**点击前**代替**.
1. 在中键入替换字符串**用。。。来代替**场地。
1. 点击**代替**.

要替换文本：

1. 打开对话框。
1. 输入要查找的文本**找什么**字段，以及要在其中替换它的文本**用。。。来代替**场地。
1. 通过单击一次替换一个事件**找下一个**其次是**代替**.
1. 如果您非常确定工作表包含的内容，请单击**全部替换**.

{{% alert color="primary" %}}

如果工作表未处于编辑模式，则**代替**按钮不显示。

{{% /alert %}}

## 从客户端添加/删除超链接

Aspose.Cells GridWeb 现在支持从客户端添加和删除超链接。为此，API 提供了“addCelllink”和“delCelllink”函数。以下代码片段演示了在 GridWeb 中从客户端添加和删除超链接。

### 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-1.jsp" >}}

您还可以使用以下代码片段链接到工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add-remove-hyperlink-from-client-side-2.jsp" >}}

## 从客户端更新字体设置

Aspose.Cells GridWeb 现在支持从客户端更改字体设置。为此，API 提供了以下功能

- **更新单元格字体样式**参数 - r/i/b/ib 用于常规/斜体/粗体/斜体&&粗体
- **更新单元格字体大小**参数 - 字体名称等 '系统'
- **更新单元格字体名称**：参数 - 字体大小等。 '12pt'
- **更新单元格字体颜色**参数 - 无/u/l/ul/ 无/下划线/删除线/下划线&&删除线
- **更新单元格字体线**Params - html 颜色如#aa22ee 或众所周知的颜色名称如绿色、红色...
- **更新单元格背景颜色**Params - html 颜色如#aa22ee 或众所周知的颜色名称如绿色、红色...

以下代码片段演示了在 GridWeb 中从客户端更改字体设置。

### 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-update_font_from_client_side-1.jsp" >}}

## 从客户端添加/删除评论

Aspose.Cells GridWeb 现在支持从客户端添加和删除评论。为此，API 提供了“addcomments”和“delcomments”功能。以下代码片段演示了在 GridWeb 中从客户端添加和删除注释。

### 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-worksheets-add_remove_comments_from_client_side.jsp" >}}

## 显示添加/删除工作表的按钮

Aspose.Cells GridWeb 现在支持使用工具栏中的按钮添加和删除工作表。为了使按钮在前端可见，您需要设置**GridWeb1.ShowAddButton**至**真的**.以下代码片段演示了向 GridWeb 工具栏添加添加/删除按钮。

### 示例代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "GridWeb-show_add_remove_worksheet_buttons.java" >}}
