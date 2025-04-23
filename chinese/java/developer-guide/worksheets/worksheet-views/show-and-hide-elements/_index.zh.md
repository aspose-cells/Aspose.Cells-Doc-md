---
title: 显示和隐藏元素
type: docs
weight: 60
url: /zh/java/show-and-hide-elements/
---

{{% alert color="primary" %}}

Aspose.Cells 允许用户显示和隐藏工作簿中的元素，包括工作表、行、列、选项卡、滚动条、网格线等。

{{% /alert %}}

## **显示和隐藏工作表**

Excel文件可以包含一个或多个工作表。每当我们创建一个Excel文件时，都会向其中添加工作表。Excel文件中的每个工作表都是独立的，具有自己的数据和格式设置等。有时，开发人员可能需要将一些工作表隐藏，并使其他工作表对他们的兴趣可见。因此，**Aspose.Cells**允许开发人员控制其Excel文件中工作表的可见性。

**控制工作表的可见性：**

Aspose.Cells提供一个代表Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问Excel文件中的每个工作表。

[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示一个工作表。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。但是，要控制工作表的可见性，开发人员可以使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)方法。

### **使工作表可见**

开发人员可以通过将**true**作为参数传递给[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)方法来使工作表可见。

### **隐藏工作表**

开发人员可以通过将**false**作为参数传递给[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)方法来隐藏工作表。

**示例：**

以下是一个完整的示例，演示了如何使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible)方法来隐藏Excel文件的第一个工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**修改前的工作表：**

在下面的截图中，您可以看到**Book1.xls**文件包含三个工作表：**Sheet1**、**Sheet2**和**Sheet3**。

![todo:image_alt_text](show-and-hide-elements_1.png)

**图:** 在进行任何修改之前的工作表视图

**工作表 - 执行示例代码后:**

使用[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类打开**Book1.xls**文件，然后将**Book1.xls**文件的第一个工作表设置为隐藏。修改后的文件保存为**output.xls**，其图示视图如下:

![todo:image_alt_text](show-and-hide-elements_2.png)

**图:** 修改后的工作表视图

**设置VisibilityType**

您还可以以一种特殊的方式隐藏工作表。这个功能可以隐藏工作表，以至于您唯一能够使其再次可见的方法是在代码中使用[**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType)方法的参数值为[**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY-HIDDEN)( 需要注意的是，用户不能通过MS Excel的菜单选项直接使对象可见)。用户也可以使用[**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType)方法来检查工作表是否标记为非常隐藏。

## **显示或隐藏选项卡**

如果您仔细查看Microsoft Excel文件的底部，您会看到许多控件。其中包括:

- 工作表标签。
- 选项卡滚动按钮。

工作表标签代表Excel文件中的工作表。单击任何选项卡以切换到该工作表。工作簿中有更多的工作表，也会有更多的工作表标签。如果Excel文件有大量工作表，您需要按钮来进行导航。因此，Microsoft Excel提供了选项卡滚动按钮来滚动工作表标签。

**工作表标签和选项卡滚动按钮**

![todo:image_alt_text](show-and-hide-elements_3.png)

使用Aspose.Cells，开发人员可以控制Excel文件中工作表标签和选项卡滚动按钮的可见性。

**控制选项卡的可见性:**
Aspose.Cells提供了一个代表Microsoft Excel文件的类[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类提供了一系列属性和方法来管理Excel文件。

### **隐藏选项卡**

通过设置[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类的[**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs)方法来隐藏Excel文件中的选项卡。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **使选项卡可见**

使用[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类的[**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs)方法使选项卡可见。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**完整代码示例:**

下面是一个完整的示例，打开了一个Excel文件（book1.xls），隐藏其选项卡，并将修改后的文件保存为output.xls。

您可以在下图中看到Book1.xls文件包含选项卡。在执行示例代码后，选项卡被隐藏了，可以从下图中输出的output.xls文件的屏幕截图中看到。

**book1.xls：不进行任何修改的Excel文件**

![todo:image_alt_text](show-and-hide-elements_4.png)

**output.xls: 修改后的Excel文件**

![todo:image_alt_text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **显示和隐藏行和列**

Excel文件中的所有工作表都由排列在行和列中的单元格组成。所有行和列都有用于标识它们和标识单个单元格的唯一值。例如，行是编号的 - 1、2、3、4等，而列以字母顺序排列 - A、B、C、D等。行和列的值显示在标头中。使用Aspose.Cells，开发人员可以控制这些行和列标头的可见性。

**控制工作表的可见性：**

Aspose.Cells提供了一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。Workbook类包含一个WorksheetCollection，允许在Excel文件中访问每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。Worksheet类提供了广泛的属性和方法来管理工作表。要控制行和列标头的可见性，使用Worksheet类的[**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)方法。

### **隐藏行/列标头**

使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)方法隐藏行和列标头。

### **使行/列标头可见**

使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)方法使行和列标头可见。

下面给出了一个完整的示例，演示如何使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible)方法隐藏Excel文件的第一个工作表的行和列标头。

下图显示了Book1.xls包含三个工作表：Sheet1、Sheet2和Sheet3。每个工作表显示行和列标头。

**Book1.xls：修改前的工作表**

![todo:image_alt_text](show-and-hide-elements_6.png)

使用[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类打开了Book1.xls，并且第一个工作表上的行和列标头被隐藏了。修改后的文件被保存为output.xls。

**修改后的工作表视图**

![todo:image_alt_text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **显示和隐藏滚动条**

滚动条非常适用于浏览任何文件的内容。通常有两种滚动条：

- 垂直滚动条
- 水平滚动条

Microsoft Excel还提供水平和垂直滚动条，以便用户可以滚动工作表内容。使用Aspose.Cells，开发人员可以控制Excel文件中两种类型滚动条的可见性。

**控制滚动条的可见性:**

Aspose.Cells提供了一个代表Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类提供了广泛的属性和方法来管理Excel文件。但是，为了控制Excel文件中滚动条的可见性，开发人员可以使用[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类的[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible)和[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)方法。

### **隐藏滚动条**

通过将[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类的[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible)或[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)方法设置为**false**来隐藏滚动条。

### **显示滚动条**

通过将Workbook类的[**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible)或[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible)方法设置为**true**来显示滚动条。

**完整代码示例:**

下面是一个完整的代码，打开一个Excel文件book1.xls，隐藏两个滚动条，然后将修改后的文件保存为output.xls。

下面的屏幕截图显示了包含两个滚动条的Book1.xls文件。修改后的文件保存为output.xls文件，也显示在下面。

**Book1.xls: 在做出任何修改之前的Excel文件**

![todo:image_alt_text](show-and-hide-elements_8.png)

**output.xls: 修改后的Excel文件**

![todo:image_alt_text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **显示和隐藏网格线**

所有的Microsoft Excel工作表都默认具有网格线。它们有助于划分单元格，使得在特定单元格输入数据变得容易。网格线使我们可以将工作表视为单元格集合，其中每个单元格都很容易识别。

Aspose.Cells也允许您控制网格线的可见性。

### **控制网格线的可见性**

Aspose.Cells提供了一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)，允许访问文件中的每个工作表。

工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要控制网格线的可见性，使用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible)方法。

#### **使网格线可见**

要使网格线可见，使用 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) 方法。

#### **隐藏网格线**

使用 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) 方法隐藏网格线。

{{% alert color="primary" %}}

网格线应用于整个工作表。要在工作表的某个部分“隐藏”网格线，使用 [边框格式](/cells/zh/java/create-table-by-using-border-lines-for-a-range/) 将边框设置为与工作表颜色方案融合的颜色。

{{% /alert %}}

**示例：在特定工作表上隐藏网格线**

下面的示例演示了使用 [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) 方法来隐藏 Excel 文件的第一个工作表的网格线。

下面的屏幕截图显示，Book1.xls 文件包含三个工作表：Sheet1、Sheet2 和 Sheet3。所有这些工作表都有网格线。

**修改前的工作表视图**

![todo:image_alt_text](show-and-hide-elements_10.png)

使用 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类打开 Book1.xls 文件，然后隐藏第一个工作表的网格线。修改后的文件保存为 output.xls 文件。

**修改后的工作表视图**

![todo:image_alt_text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **相关文章**

{{% alert color="primary" %}}

- [页面设置功能](/cells/zh/java/page-setup-features/).
- [向单元格添加边框以创建表格](/cells/zh/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
