---
title: 工作表视图
type: docs
weight: 10
url: /zh/java/worksheet-views/
---
## **分页预览**
所有工作表都可以在两种模式下查看：

- 正常视图。
- 分页预览。

普通视图是工作表的默认视图。分页预览是一种编辑视图，显示将要打印的工作表。分页预览显示每页上将显示哪些数据，因此您可以调整打印区域和分页。使用 Aspose.Cells 开发人员可以启用普通视图或分页预览模式。
### **控制视图模式**
Aspose.Cells提供了[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件的类。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)允许访问 Excel 文件中的每个工作表。

工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要启用普通或分页预览模式，请使用[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[设置分页预览](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)方法。
#### **启用普通视图**
通过使用将任何工作表设置为普通视图[设置分页预览](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)的方法[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类和传递**错误的**作为参数。
#### **启用分页预览**
使用[设置分页预览](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)的方法[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类和传递**真的**作为参数。

下面给出了一个完整的示例，演示了[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[设置分页预览](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)方法为Excel文件的第一个工作表启用分页预览模式。

在下面的屏幕截图中，您可以看到 Book1.xls 文件处于普通视图中。

**Book1.xls：修改前的工作表** 

![待办事项：图片_替代_文本](worksheet-views_1.png)

Book1.xls 打开[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类，模式切换为第一个工作表的分页预览。修改后的文件保存为 output.xls。

**Ouput.xls：修改后的工作表** 

![待办事项：图片_替代_文本](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **缩放系数**
Microsoft Excel 提供了一项功能，允许用户设置工作表的缩放或比例因子。此功能可帮助用户以较小或较大的视图查看工作表内容。用户可以将缩放因子设置为任意值。

**使用 Microsoft Excel 设置缩放系数** 

![待办事项：图片_替代_文本](worksheet-views_3.png)

Aspose.Cells 还允许开发人员设置工作表缩放系数。
### **控制缩放系数**
Aspose.Cells提供了[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件的类。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)允许访问 Excel 文件中的每个工作表。

工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要设置工作表的缩放系数，请使用[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[设置缩放](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)方法。

下面给出了一个完整的示例，演示了如何使用[设置缩放](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)方法来设置 Excel 文件中第一个工作表的缩放系数。

在下面的屏幕截图中，您可以在默认视图中看到 Book1.xls 文件。

**Book1.xls：修改前的工作表** 

![待办事项：图片_替代_文本](worksheet-views_4.png)

 Book1.xls 文件用[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类，第一个工作表的缩放系数设置为75。修改后的文件保存为output.xls。

**Output.xls：修改后的工作表** 

![待办事项：图片_替代_文本](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **冻结窗格**
冻结窗格是 Microsoft Excel 提供的一项功能。冻结窗格允许您选择在工作表中滚动时保持可见的数据。

**在 Microsoft Excel 中使用冻结窗格** 

![待办事项：图片_替代_文本](worksheet-views_6.png)

Aspose.Cells 还允许开发人员在运行时将冻结窗格应用于工作表。

Aspose.Cells提供了[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件的类。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[工作表集合](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)允许访问 Excel 文件中的每个工作表。

工作表由[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。这[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要配置冻结窗格，请调用[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[冻结窗格](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)） 方法。这[冻结窗格](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)方法采用以下参数：

- **排**，冻结将从其开始的单元格的行索引。
- **柱子**，冻结将从其开始的单元格的列索引。
- **冻结行**，顶部窗格中可见行的数量。
- **冻结列**左窗格中可见列的数量

下面给出了一个完整的示例，说明如何使用[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[冻结窗格](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\))方法冻结Excel文件第一个工作表的行和列（从C4开始，用第4行第3列表示，其中行和列从0索引开始）。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


在下面的屏幕截图中，您可以看到没有冻结窗格的 Book1.xls 文件。

**Book1.xls：任何修改前的工作表视图** 

![待办事项：图片_替代_文本](worksheet-views_7.png)

 Book1.xls 文件用[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类，然后在第一个工作表上冻结了几行和几列。修改后的文件保存为 output.xls。

**Outlook.xls：修改后的工作表视图** 

![待办事项：图片_替代_文本](worksheet-views_8.png)
## **拆分窗格**
如果您需要拆分屏幕以在同一工作表中获得两个不同的视图，请拆分窗格。 Microsoft Excel 提供了一项非常方便的功能，允许您查看工作表的多个副本，并且能够独立滚动浏览工作表的每个窗格：拆分窗格。

窗格同时工作。如果您对一个进行更改，则更改会同时出现在另一个中。 Aspose.Cells 为用户提供分割窗格功能。
### **应用和删除拆分窗格**
#### **拆分窗格**
Aspose.Cells提供了[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)表示 Microsoft Excel 文件的类。这[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类提供了广泛的属性和方法来管理 Excel 文件。要实现拆分视图，请使用[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[分裂](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\)） 方法。要删除拆分窗格，请使用[删除拆分](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)） 方法。

在示例中，我们使用加载的简单模板文件，然后将设置拆分窗格功能应用于第一个工作表中的单元格。更新的文件被保存。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



运行上面的代码后，生成的文件就有了分割视图。

**在输出文件中拆分窗格** 

![待办事项：图片_替代_文本](worksheet-views_9.png)
#### **删除窗格**
开发人员可以使用[工作表](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[删除拆分](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)） 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **推进主题**
- [隐藏工作表中零值的显示](/cells/zh/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [设置工作表标签颜色](/cells/zh/java/set-worksheet-tab-color/)
- [显示和隐藏元素](/cells/zh/java/show-and-hide-elements/)
- [在工作表中显示公式而不是值](/cells/zh/java/show-formulas-instead-of-values-in-a-worksheet/)
- [使用错误检查选项](/cells/zh/java/use-error-checking-options/)
