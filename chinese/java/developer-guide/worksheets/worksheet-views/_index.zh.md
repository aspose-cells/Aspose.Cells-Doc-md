---
title: 工作表视图
type: docs
weight: 10
url: /zh/java/worksheet-views/
---

## **分页预览**
所有工作表都可以以两种模式查看：

- 普通视图。
- 分页预览。

普通视图是工作表的默认视图。分页预览是一种编辑视图，显示工作表的打印效果。分页预览显示每页的数据，以便调整打印区域和分页线路。使用Aspose.Cells，开发者可以启用普通视图或分页预览模式。
### **控制视图模式**
Aspose.Cells提供了一个[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类，表示Microsoft Excel文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。

工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要启用普通或分页预览模式，使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)方法。
#### **启用普通视图**
使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)方法将任何工作表设置为普通视图，并传递**false**作为参数。
#### **启用分页预览**
使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)方法将任何工作表设置为分页预览，并传递**true**作为参数。

下面给出一个完整的示例，演示了如何使用[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)方法为Excel文件的第一个工作表启用分页预览模式。

在下面的截图中，您可以看到Book1.xls文件处于普通视图。

**Book1.xls：修改前的工作表** 

![todo:image_alt_text](worksheet-views_1.png)

使用[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类打开Book1.xls，并将模式切换为第一个工作表的分页预览。修改后的文件保存为output.xls。

**Ouput.xls：修改后的工作表** 

![todo:image_alt_text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **缩放因子**
Microsoft Excel提供了一个功能，允许用户设置工作表的缩放比例。此功能帮助用户以更大或更小的视图查看工作表内容。用户可以将缩放因子设置为任何值。

**使用Microsoft Excel设置缩放因子** 

![todo:image_alt_text](worksheet-views_3.png)

Aspose.Cells还允许开发人员设置工作表的缩放因子。
### **控制缩放因子**
Aspose.Cells提供了一个[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类，表示Microsoft Excel文件。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类包含一个[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。

工作表由 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类提供了广泛的属性和方法用于管理工作表。要设置工作表的缩放比例，使用 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) 方法。

下面提供一个完整示例，演示如何使用 [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) 方法设置Excel文件中第一个工作表的缩放比例。

在下面的截图中，您可以看到Book1.xls文件处于默认视图。

**Book1.xls：修改前的工作表** 

![todo:image_alt_text](worksheet-views_4.png)

使用 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类 打开 Book1.xls 文件，并将第一个工作表的缩放系数设置为 75。修改后的文件保存为 output.xls。

**Output.xls: 修改后的工作表** 

![todo:image_alt_text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **冻结窗格**
冻结窗格是Microsoft Excel提供的一个功能。冻结窗格允许您在工作表中滚动时选择要保持可见的数据。

**在 Microsoft Excel 中使用冻结窗格** 

![todo:image_alt_text](worksheet-views_6.png)

Aspose.Cells 还允许开发人员在运行时将冻结窗格应用于工作表。

Aspose.Cells 提供一个代表 Microsoft Excel 文件的 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类。[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类包含一个 [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)，允许访问 Excel 文件中的每个工作表。

工作表由 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类表示。[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类提供了广泛的属性和方法用于管理工作表。要配置冻结窗格，调用 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) 方法。 [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) 方法的参数如下：

- **行**，冻结将从该行开始。
- **列**，冻结将从该列开始。
- **冻结行**，顶部窗格中可见的行数。
- **冻结列**，左侧窗格中可见的列数

下面提供一个完整示例，展示如何使用 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) 方法冻结Excel文件第一个工作表中从C4开始的行和列（以第4行和第3列表示，索引从0开始）。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


在下面的屏幕截图中，您可以看到没有冻结窗格的 Book1.xls 文件。

**Book1.xls: 任何修改之前的工作表视图** 

![todo:image_alt_text](worksheet-views_7.png)

使用 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类打开 Book1.xls 文件，然后在第一个工作表上冻结了几行和列。修改后的文件保存为 output.xls。

**Outlook.xls: 修改后的工作表视图** 

![todo:image_alt_text](worksheet-views_8.png)
## **拆分窗格**
如果您需要拆分屏幕以在同一工作表中获得两个不同的视图，请使用拆分窗格。Microsoft Excel提供了一个非常方便的功能，允许您查看工作表的多个副本，并且您可以独立滚动工作表的每个窗格：拆分窗格。

窗格同时工作。如果您在一个窗格中进行更改，则更改将同时显示在另一个窗格中。Aspose.Cells为用户提供了拆分窗格功能。
### **应用和移除拆分窗格**
#### **拆分窗格**
Aspose.Cells 提供了一个 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类，用于表示Microsoft Excel 文件。 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类提供了丰富的属性和方法用于管理Excel文件。要实现拆分视图，使用 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [split](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split--) 方法。要移除拆分窗格，使用 [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit--) 方法。

在示例中，我们使用一个简单的模板文件进行加载，然后应用拆分窗格功能到第一个工作表的一个单元格上。然后保存更新后的文件。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



运行以上代码后，生成的文件具有分割视图。

**输出文件中的分割窗格** 

![todo:image_alt_text](worksheet-views_9.png)
#### **移除窗格**
开发者可以使用 [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) 类的 [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit--) 方法移除拆分窗格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **高级主题**
- [隐藏工作表中零值的显示](/cells/zh/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [设置工作表标签颜色](/cells/zh/java/set-worksheet-tab-color/)
- [显示和隐藏元素](/cells/zh/java/show-and-hide-elements/)
- [显示工作表中的公式而不是值](/cells/zh/java/show-formulas-instead-of-values-in-a-worksheet/)
- [使用错误检查选项](/cells/zh/java/use-error-checking-options/)
{{< app/cells/assistant language="java" >}}
