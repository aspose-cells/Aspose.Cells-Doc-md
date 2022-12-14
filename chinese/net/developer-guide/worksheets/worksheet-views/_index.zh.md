---
title: 工作表视图
type: docs
weight: 40
url: /zh/net/worksheet-views/
---
## **分页预览**

所有工作表都可以在两种模式下查看：

- 正常视图。
- 分页预览。

普通视图是工作表的默认视图。分页预览是一种编辑视图，显示将要打印的工作表。分页预览显示每页上将显示哪些数据，因此您可以调整打印区域和分页。使用 Aspose.Cells 开发人员可以启用普通视图或分页预览模式。

### **控制视图模式**

Aspose.Cells提供了[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件的类。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要启用普通或分页预览模式，请使用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)财产。[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)是一个布尔属性，这意味着它只能存储一个**真的**或**错误的**价值。

#### **启用普通视图**

通过将工作表设置为普通视图[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)财产给**错误的**.

#### **启用分页预览**

通过设置任何工作表以分页预览[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)财产给**真的**.这样做会将工作表从普通视图切换到分页预览。

下面给出了一个完整的示例，演示了如何使用[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)属性为 Excel 文件的第一个工作表启用分页预览模式。

book1.xls 文件是通过创建一个实例来打开的[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级。通过将视图切换到第一个工作表的分页预览[**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview)财产给**真的**.修改后的文件保存为 output.xls。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **缩放系数**

### **使用 Microsoft Excel**

Microsoft Excel 提供了一项功能，允许用户设置工作表的缩放或比例因子。此功能可帮助用户以较小或较大的视图查看工作表内容。用户可以将缩放因子设置为任意值。

### **Aspose.Cells & 缩放系数**

Aspose.Cells 允许开发人员设置工作表缩放系数。
Aspose.Cells提供了[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件的类。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要设置工作表的缩放系数，请使用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级'[**飞涨**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)财产。缩放系数是通过将数字（整数）值分配给[**飞涨**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)财产。

下面给出了一个完整的示例，演示了如何使用[**飞涨**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom)属性设置 Excel 文件第一个工作表的缩放系数。

book1.xls 文件是通过创建一个实例来打开的[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)班级。第一个工作表的缩放系数设置为 75，修改后的文件保存为 output.xls。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **冻结窗格**

### **使用 Microsoft Excel**

冻结窗格是 Microsoft Excel 提供的一项功能。冻结窗格允许您选择在工作表中滚动时保持可见的数据。

### **Aspose.Cells & 冻结窗格**

Aspose.Cells 允许开发人员在运行时将冻结窗格应用于工作表。

Aspose.Cells提供了[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件的类。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要配置冻结窗格，请调用 Worksheet 类'[**冻结窗格**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)方法。这[**冻结窗格**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)方法采用以下参数：

- **排**，冻结将从其开始的单元格的行索引。
- **柱子**，冻结将从其开始的单元格的列索引。
- **冻结行**，顶部窗格中可见行的数量。
- **冻结列**左窗格中可见列的数量

book1.xls 文件通过调用打开[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的构造函数，同时实例化它，一些行和列在第一个工作表中被冻结。修改后的文件保存为 output.xls。

下面给出了一个完整的示例，说明如何使用[**冻结窗格**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index)冻结Excel文件第一个工作表的行和列（从C4开始，用第4行第3列表示，其中行和列从0索引开始）的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **拆分窗格**

如果您需要拆分屏幕以在同一工作表中获得两个不同的视图，请拆分窗格。 Microsoft Excel 提供了一项非常方便的功能，允许您查看工作表的多个副本，并且能够独立滚动浏览工作表的每个窗格：拆分窗格。

窗格同时工作。如果您对一个进行更改，则更改会同时出现在另一个中。 Aspose.Cells 为用户提供分割窗格功能。

### **应用和删除拆分窗格**

#### **拆分窗格**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类提供了广泛的属性和方法来管理 Excel 文件。要实现拆分视图，请使用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级'[**分裂**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split).要删除拆分窗格，请使用[**删除拆分**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)方法。

在示例中，我们使用加载的简单模板文件，然后将设置拆分窗格功能应用于第一个工作表中的单元格。更新的文件被保存。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

运行上述代码后，生成的文件将具有拆分视图。

#### **删除窗格**

使用删除拆分窗格[**删除拆分**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **推进主题**
- [隐藏工作表中零值的显示](/cells/zh/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [设置工作表标签颜色](/cells/zh/net/set-worksheet-tab-color/)
- [显示和隐藏网格线和行列标题](/cells/zh/net/show-and-hide-gridlines-and-row-column-headers/)
- [显示和隐藏行列和滚动条](/cells/zh/net/show-and-hide-rows-columns-and-scroll-bars/)
- [显示和隐藏工作表和选项卡](/cells/zh/net/show-and-hide-worksheets-and-tabs/)
- [在工作表中显示公式而不是值](/cells/zh/net/show-formulas-instead-of-values-in-a-worksheet/)
- [使用错误检查选项](/cells/zh/net/use-error-checking-options/)

