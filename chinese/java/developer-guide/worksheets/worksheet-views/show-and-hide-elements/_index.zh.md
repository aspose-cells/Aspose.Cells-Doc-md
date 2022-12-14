---
title: 显示和隐藏元素
type: docs
weight: 60
url: /zh/java/show-and-hide-elements/
---
{{% alert color="primary" %}}

Aspose.Cells 允许用户显示和隐藏工作簿的元素，包括工作表、行、列、选项卡、滚动条、网格线、

{{% /alert %}}

## **显示和隐藏工作表**

一个 Excel 文件可以有一个或多个工作表。每当我们创建 Excel 文件时，我们都会将工作表添加到我们工作的 Excel 文件中。 Excel 文件中的每个工作表都独立于其他工作表，具有自己的数据和格式设置等。有时，开发人员可能出于自己的兴趣需要隐藏一些工作表，而其他工作表在 Excel 文件中可见。所以，**Aspose.Cells**允许开发人员控制工作表在其 Excel 文件中的可见性。

**控制工作表的可见性：**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示一个 Excel 文件。[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问 Excel 文件中的每个工作表。

工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。但是，为了控制工作表的可见性，开发人员可以使用[**设置可见**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)的方法[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。

### **使工作表可见**

开发人员可以通过传递使工作表可见**真的**作为参数[**设置可见**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)的方法[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。

### **隐藏工作表**

开发人员可以通过传递隐藏工作表**错误的**作为参数[**设置可见**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)的方法[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。

**例子：**

下面给出了一个完整的示例，演示了[**设置可见（假）**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)的方法[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类隐藏 Excel 文件的第一个工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**工作表 - 修改前：**

在下面的屏幕截图中，您可以看到**Book1.xls**文件包含三个工作表：**工作表1** , **工作表2**和**工作表3** .

![待办事项：图片_替代_文本](show-and-hide-elements_1.png)

**数字：**任何修改前的工作表视图

**工作表 - 执行示例代码后：**

**Book1.xls**使用打开文件[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类，然后是第一个工作表**Book1.xls**文件被隐藏。修改后的文件另存为**输出.xls**其图形视图如下所示的文件：

![待办事项：图片_替代_文本](show-and-hide-elements_2.png)

**数字：**修改后的工作表视图

**设置可见性类型**

您还可以以特殊方式隐藏工作表。此功能可以隐藏工作表，以便您使其再次可见的唯一方法是提供[**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN)作为参数值[**设置可见类型**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType)代码中的方法（这里需要注意的是，用户不能直接使用其菜单选项使对象在 MS Excel 中可见）。用户还可以使用[**获取可见性类型**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType)检查工作表是否标记为 VeryHidden 的方法。

## **显示或隐藏标签**

如果仔细查看 Microsoft Excel 文件的底部，您会看到许多控件。这些包括：

- 工作表标签。
- 选项卡滚动按钮。

工作表选项卡代表 Excel 文件中的工作表。单击任何选项卡以切换到该工作表。工作簿中的工作表越多，工作表标签就越多。如果 Excel 文件有大量工作表，您需要按钮来浏览它们。因此，Microsoft Excel 提供了用于滚动工作表选项卡的选项卡滚动按钮。

**工作表标签和标签滚动按钮**

![待办事项：图片_替代_文本](show-and-hide-elements_3.png)

使用 Aspose.Cells，开发人员可以控制 Excel 文件中工作表选项卡和选项卡滚动按钮的可见性。

**控制选项卡的可见性：**
Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类提供了广泛的属性和方法来管理 Excel 文件。

### **隐藏标签**

通过设置隐藏 Excel 文件中的选项卡[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)班级'[**getSettings().setShowTabs(假)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs)方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **使选项卡可见**

使选项卡可见[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)班级'[**getSettings().setShowTabs(真)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs)方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**完整的代码示例：**

下面是打开 Excel 文件 (book1.xls)、隐藏其选项卡并将修改后的文件保存为 output.xls 的完整示例。

您可以看到 Book1.xls 文件包含下图中的选项卡。示例代码执行后，选项卡被隐藏，您可以从下面的 output.xls 文件的屏幕截图中看到。

**book1.xls：修改前的Excel文件**

![待办事项：图片_替代_文本](show-and-hide-elements_4.png)

**output.xls：修改后的Excel文件**

![待办事项：图片_替代_文本](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **显示和隐藏行和列**

Excel 文件中的所有工作表均由按行和列排列的单元格组成。所有行和列都有唯一的值，用于标识它们和标识单个单元格。例如，行编号 - 1、2、3、4 等 - 列按字母顺序排序 - A、B、C、D 等。行和列值显示在标题中。使用 Aspose.Cells，开发人员可以控制这些行和列标题的可见性。

**控制工作表的可见性：**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。 Workbook 类包含一个 WorksheetCollection，它允许访问 Excel 文件中的每个工作表。

工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。 Worksheet 类提供了广泛的属性和方法来管理工作表。要控制行和列标题的可见性，请使用 Worksheet 类[**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)方法。

### **隐藏行/列标题**

使用隐藏行和列标题[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)方法。

### **使行/列标题可见**

使用[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[**setRowColumnHeadersVisible(真)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)方法。

下面给出了一个完整的示例，演示了如何使用[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)隐藏 Excel 文件第一个工作表的行和列标题的方法。

下面的屏幕截图显示 Book1.xls 包含三个工作表：Sheet1、Sheet2 和 Sheet3。每个工作表都显示行和列标题。

**Book1.xls：修改前的工作表**

![待办事项：图片_替代_文本](show-and-hide-elements_6.png)

Book1.xls 是使用[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class' 以及第一个工作表上的行标题和列标题被隐藏。修改后的文件保存为 output.xls。

**修改后的工作表视图**

![待办事项：图片_替代_文本](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **显示和隐藏滚动条**

滚动条非常适用于浏览任何文件的内容。通常，有两种滚动条：

- 垂直滚动条
- 水平滚动条

Microsoft Excel 还提供水平和垂直滚动条，以便用户可以滚动浏览工作表内容。使用 Aspose.Cells，开发人员可以控制 Excel 文件中两种滚动条的可见性。

**控制滚动条的可见性：**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示一个 Excel 文件。[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类提供了广泛的属性和方法来管理 Excel 文件。但是，为了控制 Excel 文件中滚动条的可见性，开发人员可以使用[**设置VScrollBar可见**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) & [**设置 HScrollBar 可见**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)的方法[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)班级。

### **隐藏滚动条**

通过设置隐藏滚动条[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)班级'[**设置VScrollBar可见**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible)或者[**设置 HScrollBar 可见**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)方法**错误的**.

### **使滚动条可见**

通过设置工作簿类使滚动条可见'[**设置VScrollBar可见**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible)或者[**设置 HScrollBar 可见**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)方法**真的**.

**完整的代码示例：**

下面是打开 Excel 文件 book1.xls 的完整代码，隐藏两个滚动条，然后将修改后的文件保存为 output.xls。

下面的屏幕截图显示了包含两个滚动条的 Book1.xls 文件。修改后的文件保存为output.xls文件，如下图所示。

**Book1.xls：修改前的Excel文件**

![待办事项：图片_替代_文本](show-and-hide-elements_8.png)

**output.xls：修改后的Excel文件**

![待办事项：图片_替代_文本](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **显示和隐藏网格线**

默认情况下，所有 Microsoft Excel 工作表都有网格线。它们有助于描绘单元格，因此很容易将数据输入特定单元格。网格线使我们能够将工作表视为单元格的集合，其中每个单元格都很容易识别。

Aspose.Cells 还允许您控制网格线的可见性。

### **控制网格线的可见性**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**工作表集合**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)允许访问文件中的每个工作表。

工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要控制网格线的可见性，请使用[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[**设置网格线可见**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)方法。

#### **使网格线可见**

要使网格线可见，请使用[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[**设置网格线可见（真）**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)方法。

#### **隐藏网格线**

使用 the 隐藏网格线[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[**setGridlinesVisible(假)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)方法。

{{% alert color="primary" %}}

网格线应用于整个工作表。要在工作表的某个部分“隐藏”网格线，请使用[边框格式](/cells/zh/java/create-table-by-using-border-lines-for-a-range/)将边框设置为与工作表配色方案相融合的颜色。

{{% /alert %}}

**示例：隐藏特定工作表上的网格线**

下面的例子演示了使用[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[**setGridlinesVisible(假)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)隐藏 Excel 文件第一个工作表的网格线的方法。

下面的屏幕截图显示 Book1.xls 文件包含三个工作表：Sheet1、Sheet2 和 Sheet3。所有这些工作表都有网格线。

**修改前的工作表视图**

![待办事项：图片_替代_文本](show-and-hide-elements_10.png)

Book1.xls 文件使用[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类，然后隐藏第一个工作表的网格线。修改后的文件保存为 output.xls 文件。

**修改后的工作表视图**

![待办事项：图片_替代_文本](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **相关文章**

{{% alert color="primary" %}}

- [页面设置功能](/cells/zh/java/page-setup-features/).
- [为单元格添加边框以创建表格](/cells/zh/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
