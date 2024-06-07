---
title: 工作表视图
type: docs
weight: 10
url: /zh/java/worksheet-views/
---

## **分页预览**
所有工作表可以以两种模式查看：

- 正常视图。
- 分页预览。

正常视图是工作表的默认视图。分页预览是一种编辑视图，显示工作表的打印效果。分页预览显示每页将显示的数据，以便您可以调整打印区域和页面分隔位置。使用Aspose.Cells，开发人员可以启用正常视图或分页预览模式。
### **控制视图模式**
Aspose.Cells 提供了代表 Microsoft Excel 文件的[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。

工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了许多用于管理工作表的属性和方法。要启用正常或分页预览模式，请使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)方法。
#### **启用正常视图**
通过使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)方法并将**false**作为参数来将任何工作表设置为正常视图。
#### **启用分页符预览**
通过使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)方法并将**true**作为参数来将任何工作表设置为分页预览。

以下是一个完整的示例，演示了如何使用 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) 方法来启用 Excel 文件的第一个工作表的分页预览模式。

在下面的截图中，您可以看到 Book1.xls 文件处于正常视图。

**Book1.xls：修改前的工作表** 

![todo:image_alt_text](worksheet-views_1.png)

使用[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类打开Book1.xls，并将模式切换为第一张工作表的分页预览。修改后的文件保存为output.xls。

**Ouput.xls：修改后的工作表** 

![todo:image_alt_text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **缩放因子**
Microsoft Excel提供了一项功能，让用户设置工作表的缩放或比例因子。此功能可帮助用户以较小或较大的视图查看工作表内容。用户可以将缩放因子设置为任何值。

**使用Microsoft Excel设置缩放比例** 

![todo:image_alt_text](worksheet-views_3.png)

Aspose.Cells还允许开发人员设置工作表的缩放比例。
### **控制缩放比例**
Aspose.Cells提供了一个表示Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。

一个工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法，用于管理工作表。要设置工作表的缩放比例，使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[setZoom ](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)方法。

下面提供了一个完整的示例，演示如何使用[setZoom ](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)方法设置Excel文件中第一个工作表的缩放比例。

在下面的屏幕截图中，您可以看到默认视图中的Book1.xls文件。

**Book1.xls：修改前的工作表** 

![todo:image_alt_text](worksheet-views_4.png)

使用[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类打开Book1.xls文件，然后将第一个工作表的缩放比例设置为75。修改后的文件保存为output.xls。

**Output.xls：修改后的工作表** 

![todo:image_alt_text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **冻结窗格**
冻结窗格是Microsoft Excel提供的一个功能。冻结窗格可以让您选择在工作表中滚动时保持可见的数据。

**在Microsoft Excel中使用冻结窗格** 

![todo:image_alt_text](worksheet-views_6.png)

Aspose.Cells还允许开发人员在运行时向工作表应用冻结窗格。

Aspose.Cells提供了一个表示Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。

一个工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法，用于管理工作表。要配置冻结窗格，请调用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\))方法。[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\))方法接受以下参数：

- **行**，冻结将从该行开始的单元格的行索引。
- **列**，冻结将从该列开始的单元格的列索引。
- **冻结行**，顶部窗格中可见行数。
- **冻结列**，左侧窗格中可见列数

下面提供了一个完整的示例，展示如何使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\))方法冻结Excel文件的第一个工作表的行和列（从C4开始，表示第4行和第3列，其中行和列从0索引开始）。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


在下面的屏幕截图中，您可以看到没有冻结窗格的Book1.xls文件。

**Book1.xls：任何修改前的工作表视图** 

![todo:image_alt_text](worksheet-views_7.png)

使用[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类打开Book1.xls文件，然后在第一个工作表上冻结了几行和列。修改后的文件保存为output.xls。

**Outlook.xls：修改后的工作表视图** 

![todo:image_alt_text](worksheet-views_8.png)
## **拆分窗格**
如果您需要在同一工作表中获得两个不同视图来拆分屏幕，请使用拆分窗格。 Microsoft Excel提供了一个非常方便的功能，允许您查看工作表的多个副本，并允许您能够独立滚动工作表的每个窗格：拆分窗格。

窗格同时工作。如果您更改一个窗格中的内容，则更改将同时显示在另一个窗格中。Aspose.Cells为用户提供了拆分窗格功能。
### **应用和移除拆分窗格**
#### **拆分窗格**
Aspose.Cells提供了一个表示Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类提供了广泛的属性和方法，用于管理Excel文件。要实现分割视图，请使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[split](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\))方法。要移除分割窗格，请使用[removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\))方法。

在示例中，我们使用一个简单的模板文件进行加载，然后应用了设置拆分窗格功能到第一个工作表中的单元格。然后保存更新后的文件。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



运行以上代码后，生成的文件具有分割视图。

**输出文件中的分割窗格** 

![todo:image_alt_text](worksheet-views_9.png)
#### **移除分栏**
开发人员可以使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\))方法来移除分割窗格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **高级主题**
- [隐藏工作表中零值的显示](/cells/zh/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [设置工作表选项卡颜色](/cells/zh/java/set-worksheet-tab-color/)
- [显示和隐藏元素](/cells/zh/java/show-and-hide-elements/)
- [在工作表中显示公式而不是值](/cells/zh/java/show-formulas-instead-of-values-in-a-worksheet/)
- [使用错误检查选项](/cells/zh/java/use-error-checking-options/)
