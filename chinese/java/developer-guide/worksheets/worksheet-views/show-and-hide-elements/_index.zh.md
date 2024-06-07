---
title: 显示和隐藏元素
type: docs
weight: 60
url: /zh/java/show-and-hide-elements/
---

{{% alert color="primary" %}}

Aspose.Cells允许用户显示和隐藏工作簿的各种元素，包括工作表、行、列、标签、滚动条、网格线等。

{{% /alert %}}

## **显示和隐藏工作表**

Excel 文件可以有一个或多个工作表。每当创建一个 Excel 文件时，我们向其中添加工作表。Excel 文件中的每个工作表通过具有自己的数据和格式设置等独立于其他工作表来。有时，开发人员可能需要将某些工作表隐藏，而将其他工作表对于他们自己的兴趣设为可见。因此，**Aspose.Cells** 允许开发人员控制其 Excel 文件中工作表的可见性。

**控制工作表的可见性：**

Aspose.Cells提供了一个类,[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，它代表一个Excel文件。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问Excel文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类提供了广泛的属性和方法来管理工作表。但是，为了控制工作表的可见性，开发人员可以使用 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) 方法。

### **使工作表可见**

开发人员可以通过将 **true** 作为参数传递给 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) 方法来使工作表可见。

### **隐藏工作表**

开发人员可以通过将 **false** 作为参数传递给 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) 方法来隐藏工作表。

**示例：**

下面提供了一个完整的示例，演示了如何使用 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) 方法隐藏 Excel 文件的第一个工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**修改前的工作表：**

在下面的截图中，您可以看到 **Book1.xls** 文件包含三个工作表：**Sheet1**、**Sheet2** 和 **Sheet3**。

![todo:image_alt_text](show-and-hide-elements_1.png)

**图：** 修改前的工作表视图

**执行示例代码后的工作表：**

使用 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类打开了 **Book1.xls** 文件，然后将 **Book1.xls** 文件的第一个工作表隐藏起来。修改后的文件另存为 **output.xls** 文件，其图片视图如下所示：

![todo:image_alt_text](show-and-hide-elements_2.png)

**图：** 修改后的工作表视图

**设置 VisibilityType**

您还可以以特殊方式隐藏工作表。此功能可以隐藏工作表，这样您只能通过在代码中将 [**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) 方法的参数值设为 [**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) 来再次使其可见（这里需要注意，用户不能直接通过 MS Excel 的菜单选项使对象可见）。用户还可以使用 [**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) 方法来检查工作表是否被标记为 VeryHidden。

## **显示或隐藏标签**

如果仔细查看 Microsoft Excel 文件底部，您会看到许多控件。这包括:

- 工作表选项卡。
- 选项卡滚动按钮。

工作表选项卡代表Excel文件中的工作表。单击任何选项卡切换到该工作表。工作簿中有更多工作表时，就会有更多的工作表选项卡。如果Excel文件有大量工作表，需要按钮来在它们之间进行导航。因此，Microsoft Excel提供了选项卡滚动按钮，用于滚动工作表选项卡。

**工作表标签和标签滚动按钮**

![todo:image_alt_text](show-and-hide-elements_3.png)

使用Aspose.Cells，开发人员可以控制Excel文件中的工作表选项卡的可见性和选项卡滚动按钮。

**控制标签的可见性：**
Aspose.Cells 提供了一个表示 Microsoft Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类提供了一系列广泛的属性和方法来管理 Excel 文件。

### **隐藏选项卡。**

通过设置 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类的 [**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) 方法来隐藏 Excel 文件中的标签。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **使选项卡可见。**

使用 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类的 [**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) 方法来使标签可见。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**完整代码示例:**

以下是一个完整的示例，打开一个Excel文件（book1.xls），隐藏其标签页并将修改后的文件保存为output.xls。

您可以从下面的截图中看到Book1.xls文件包含标签页。示例代码执行后，标签页被隐藏了，您可以从下面的output.xls文件的截图中看到。

**book1.xls：任何修改之前的Excel文件**

![todo:image_alt_text](show-and-hide-elements_4.png)

**output.xls：修改后的Excel文件**

![todo:image_alt_text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **显示和隐藏行和列**

Excel文件中的所有工作表都由排列在行和列中的单元格组成。所有行和列都具有用于标识它们和标识单个单元格的唯一值。例如，行编号为1、2、3、4等，列按字母顺序排列为A、B、C、D等。行和列的值显示在标题中。使用Aspose.Cells，开发人员可以控制这些行和列标题的可见性。

**控制工作表的可见性：**

Aspose.Cells 提供了一个表示 Microsoft Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。Workbook 类包含一个 WorksheetCollection，允许访问 Excel 文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。Worksheet 类提供了广泛的属性和方法来管理工作表。要控制行和列标题的可见性，请使用 Worksheet 类的 [**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) 方法。

### **隐藏行/列标题**

使用 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的方法打开了 Book1.xls 文件，然后隐藏了第一个工作表的行和列标题。修改后的文件另存为 output.xls。

### **显示行/列标题**

通过使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)方法来使行和列标头可见。

下面给出了一个完整的示例，演示了如何使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)方法将Excel文件的第一个工作表的行和列标头隐藏起来。

下面的截图显示了Book1.xls包含三个工作表：Sheet1、Sheet2和Sheet3。每个工作表都显示了行和列标头。

**Book1.xls：修改前的工作表**

![todo:image_alt_text](show-and-hide-elements_6.png)

使用[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类'打开Book1.xls，并将第一个工作表上的行和列标头隐藏。修改后的文件保存为output.xls。

**修改后的工作表视图**

![todo:image_alt_text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **显示和隐藏滚动条**

滚动条非常适用于导航任何文件的内容。通常有两种滚动条：

- 垂直滚动条
- 水平滚动条

Microsoft Excel 还提供水平和垂直滚动条，以便用户可以滚动工作表内容。使用 Aspose.Cells，开发人员可以控制 Excel 文件中两种类型滚动条的可见性。

**控制滚动条的可见性：**

Aspose.Cells 提供了一个表示 Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类提供了广泛的属性和方法来管理 Excel 文件。但是，为了控制 Excel 文件中滚动条的可见性，开发人员可以使用 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类的 [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) 和 [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) 方法。

### **隐藏滚动条**

通过将 **false** 作为参数值传递给 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类的 [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) 或 [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) 方法来隐藏滚动条。

### **使滚动条可见**

通过将Workbook类的[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible)或[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)方法设置为**true**来使滚动条可见。

**完整代码示例:**

以下是完整代码，打开一个 Excel 文件，book1.xls，隐藏两个滚动条，然后将修改后的文件保存为 output.xls。

下面的截图显示了Book1.xls文件包含两个滚动条。修改后的文件保存为output.xls文件，如下所示。

**Book1.xls：任何修改前的Excel文件**

![todo:image_alt_text](show-and-hide-elements_8.png)

**output.xls：修改后的Excel文件**

![todo:image_alt_text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **显示和隐藏网格线**

所有Microsoft Excel工作表默认具有网格线。它们有助于区分单元格，这样就可以轻松地输入数据到特定单元格。网格线使我们能够将工作表视为单元格集合，其中每个单元格都能轻松识别。

Aspose.Cells还允许您控制网格线的可见性。

### **控制网格线的可见性**

Aspose.Cells提供了一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，用于访问文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要控制网格线的可见性，使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)方法。

#### **使网格线可见**

要使网格线可见，请使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)方法。

#### **隐藏网格线**

使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)方法隐藏网格线。

{{% alert color="primary" %}}

网格线应用于整个工作表。要在工作表的某部分“隐藏”网格线，请使用[边框格式设置](/cells/zh/java/create-table-by-using-border-lines-for-a-range/)将边框设置为与工作表颜色方案融为一体的颜色。

{{% /alert %}}

**示例：在特定工作表上隐藏网格线**

下面的示例演示了使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)方法隐藏Excel文件的第一个工作表的网格线。

下面的屏幕截图显示了Book1.xls文件包含三个工作表：Sheet1、Sheet2和Sheet3。所有这些工作表都有网格线。

**修改前的工作表视图**

![todo:image_alt_text](show-and-hide-elements_10.png)

使用[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类打开Book1.xls文件，然后隐藏第一个工作表的网格线。修改后的文件保存为output.xls文件。

**修改后的工作表视图**

![todo:image_alt_text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **相关文章**

{{% alert color="primary" %}}

- [页面设置功能](/cells/zh/java/page-setup-features/)。
- [向单元格添加边框以创建表格](/cells/zh/java/create-table-by-using-border-lines-for-a-range/)。

{{% /alert %}}
