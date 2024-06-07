---
title: 工作表视图
type: docs
weight: 40
url: /zh/cpp/worksheet-views/
---

## **分页预览**
所有工作表可以以两种模式查看：

- 正常视图。
- 分页预览。

正常视图是工作表的默认视图。 分页预览是一种编辑视图，显示工作表将如何打印。 分页预览显示了每个页面上将显示哪些数据，因此您可以调整打印区域和分页。使用Aspose.Cells，开发人员可以启用正常视图或分页预览模式。
### **控制视图模式**
Aspose.Cells提供了一个代表Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。

工作表由[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了许多用于管理工作表的方法。 要启用正常或分页预览模式，请使用工作表类的[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)方法。[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/)返回一个bool值，这意味着它只能存储**true**或**false**值。
#### **启用正常视图**
通过将[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)方法设置为**false**来将工作表设置为正常视图。
#### **启用分页符预览**
通过将[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)方法设置为**true**，可以将任何工作表设置为分页预览。这样做会将工作表从正常视图切换到分页预览。

以下是一个完整的示例，演示如何使用[SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)方法为Excel文件的第一个工作表启用分页预览模式。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
## **缩放因子**
### **使用Microsoft Excel**
Microsoft Excel提供了一项功能，让用户设置工作表的缩放或比例因子。此功能可帮助用户以较小或较大的视图查看工作表内容。用户可以将缩放因子设置为任何值。
### **Aspose.Cells和缩放因子**
Aspose.Cells也允许开发人员设置工作表的缩放因子。Aspose.Cells提供了一个代表Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。

工作表由[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了许多用于管理工作表的方法。要设置工作表的缩放因子，请使用[SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)方法。缩放因子通过将数值（整数）值分配给[SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)方法来设置。

以下是一个完整的示例，演示如何使用[SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)方法设置Excel文件的第一个工作表的缩放因子。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
## **冻结窗格**
### **使用Microsoft Excel**
冻结窗格是Microsoft Excel提供的一个功能。冻结窗格可以让您选择在工作表中滚动时保持可见的数据。
### **Aspose.Cells和冻结窗格**
Aspose.Cells还允许开发人员在运行时将冻结窗格应用于工作表。Aspose.Cells提供了一个代表Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。

工作表由[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了许多用于管理工作表的方法。要配置冻结窗格，请调用[FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)方法。[FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)方法接受以下参数：

- **行**，冻结将从该行开始的单元格的行索引。
- **列**，冻结将从该列开始的单元格的列索引。
- **冻结行**，顶部窗格中可见行数。
- **冻结列**，左侧窗格中可见列数

以下是一个完整的示例，展示如何使用[FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)方法冻结Excel文件的第一个工作表的行和列（从C4开始，由第4行和第3列表示，其中行和列从0索引开始）的窗格。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
## **拆分窗格**
如果您需要在同一工作表中获得两个不同视图来拆分屏幕，请使用拆分窗格。 Microsoft Excel提供了一个非常方便的功能，允许您查看工作表的多个副本，并允许您能够独立滚动工作表的每个窗格：拆分窗格。

窗格同时工作。如果您更改一个窗格中的内容，则更改将同时显示在另一个窗格中。Aspose.Cells为用户提供了拆分窗格功能。
### **应用和移除拆分窗格**
#### **拆分窗格**
Aspose.Cells提供了一个代表Microsoft Excel文件的[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类。 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类提供了一系列用于管理Excel文件的方法。要实现拆分视图，请使用[Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/)方法。要移除拆分窗格，请使用[RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)方法。

在示例中，我们使用一个简单的模板文件进行加载，然后应用了设置拆分窗格功能到第一个工作表中的单元格。然后保存更新后的文件。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
#### **移除分栏**
使用[RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)方法来移除分栏。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
