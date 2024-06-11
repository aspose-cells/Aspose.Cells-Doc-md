---
title: 工作表视图
type: docs
weight: 40
url: /zh/cpp/worksheet-views/
---

## **分页预览**
所有工作表都可以以两种模式查看：

- 普通视图。
- 分页预览。

普通视图是工作表的默认视图。分页预览是一种编辑视图，显示工作表将要打印的内容。分页预览显示数据将会出现在每一页上，因此您可以调整打印区域和分页。使用Aspose.Cells开发人员可以启用普通视图或分页预览模式。
### **控制视图模式**
Aspose.Cells提供了一个表示Microsoft Excel文件的类[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。

工作表由[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了广泛的方法来管理工作表。要启用普通或分页预览模式，请使用[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)方法。[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/)返回一个布尔值，这意味着它只能存储**true**或**false**值。
#### **启用普通视图**
通过将[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)方法设置为**false**，将工作表设置为普通视图。
#### **启用分页预览**
通过将[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)方法设置为**true**，可以将任何工作表设置为分页预览。这样可以将工作表从普通视图切换到分页预览。

下面的完整示例演示了如何使用[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)方法，将Excel文件的第一个工作表启用为分页预览模式。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
## **缩放因子**
### **使用Microsoft Excel**
Microsoft Excel提供了一个功能，允许用户设置工作表的缩放比例。此功能帮助用户以更大或更小的视图查看工作表内容。用户可以将缩放因子设置为任何值。
### **Aspose.Cells和缩放因子**
Aspose.Cells还允许开发人员设置工作表的缩放比例。Aspose.Cells提供了一个表示Microsoft Excel文件的类[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。

工作表由 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供了各种方法来管理工作表。要设置工作表的缩放比例，使用 [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) 方法的 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类。通过将一个数字（整数）值分配给[SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)方法来设置缩放比例。

下面给出了一个完整的示例，演示了如何使用 [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) 方法设置Excel文件的第一个工作表的缩放比例。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
## **冻结窗格**
### **使用Microsoft Excel**
冻结窗格是Microsoft Excel提供的一个功能。冻结窗格允许您在工作表中滚动时选择要保持可见的数据。
### **Aspose.Cells 和 冻结窗格**
Aspose.Cells 还允许开发人员在运行时将冻结窗格应用到工作表。Aspose.Cells 提供了表示Microsoft Excel文件的 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类包含一个 [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) 集合，允许访问Excel文件中的每个工作表。

工作表由 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供了各种管理工作表的方法。要配置冻结窗格，调用 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类的 [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) 方法。[FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) 方法采用以下参数：

- **行**，冻结将从该行开始。
- **列**，冻结将从该列开始。
- **冻结行**，顶部窗格中可见的行数。
- **冻结列**，左侧窗格中可见的列数

下面提供了一个完整的示例，演示了如何使用[FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) 方法来冻结Excel文件的第一个工作表的行和列（从C4开始，由第4行和第3列表示，其中行和列从0索引开始）。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
## **拆分窗格**
如果您需要拆分屏幕以在同一工作表中获得两个不同的视图，请使用拆分窗格。Microsoft Excel提供了一个非常方便的功能，允许您查看工作表的多个副本，并且您可以独立滚动工作表的每个窗格：拆分窗格。

窗格同时工作。如果您在一个窗格中进行更改，则更改将同时显示在另一个窗格中。Aspose.Cells为用户提供了拆分窗格功能。
### **应用和移除拆分窗格**
#### **拆分窗格**
Aspose.Cells提供了表示Microsoft Excel文件的 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类提供了各种管理Excel文件的方法。要实现拆分视图，使用 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类的 [Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) 方法。要删除拆分窗格，使用 [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) 方法。

在示例中，我们使用一个简单的模板文件进行加载，然后应用拆分窗格功能到第一个工作表的一个单元格上。然后保存更新后的文件。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
#### **移除窗格**
使用 [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) 方法移除分割窗格。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
