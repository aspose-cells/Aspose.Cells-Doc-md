---
title: 工作表视图
type: docs
weight: 40
url: /zh/cpp/worksheet-views/
---
##  **分页预览**
所有工作表都可以通过两种模式查看：

- 正常视图。
- 分页预览。

普通视图是工作表的默认视图。分页预览是一种编辑视图，用于显示将要打印的工作表。分页符预览显示每页上将显示哪些数据，以便您可以调整打印区域和分页符。使用 Aspose.Cells 开发人员可以启用正常视图或分页预览模式。
###  **控制视图模式**
 Aspose.Cells 提供类[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)代表 Microsoft Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)允许访问 Excel 文件中的每个工作表的集合。

工作表由以下形式表示[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了多种管理工作表的方法。要启用正常或分页预览模式，请使用[设置为分页预览](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)的方法[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。[IsPageBreak预览](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/)返回一个bool值，这意味着它只能存储一个**真的**或者**错误的**价值。
####  **启用普通视图**
通过设置将工作表设置为普通视图[设置为分页预览](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)的方法[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类为 *false**。
####  **启用分页预览**
通过设置将任何工作表设置为分页预览[设置为分页预览](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)的方法[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类为 *true**。这样做会将工作表从正常视图切换到分页预览。

下面给出了一个完整的示例，演示了如何使用[设置为分页预览](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/)方法为 Excel 文件的第一个工作表启用分页预览模式。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
##  **变焦倍数**
###  **使用 Microsoft Excel**
Microsoft Excel 提供了一项功能，允许用户设置工作表的缩放或比例因子。此功能可帮助用户以较小或较大的视图查看工作表内容。用户可以将缩放系数设置为任意值。
###  **Aspose.Cells & 变焦倍数**
Aspose.Cells还允许开发人员设置工作表缩放系数。 Aspose.Cells 提供类[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)代表 Microsoft Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)允许访问 Excel 文件中的每个工作表的集合。

工作表由以下形式表示[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了多种管理工作表的方法。要设置工作表的缩放系数，请使用[设置缩放](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)的方法[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。缩放系数是通过将数字（整数）值分配给[设置缩放](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)方法。

下面给出了一个完整的示例，演示了如何使用[设置缩放](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/)方法设置 Excel 文件的第一个工作表的缩放系数。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
##  **冻结窗格**
###  **使用 Microsoft Excel**
冻结窗格是 Microsoft Excel 提供的一项功能。冻结窗格允许您选择在工作表中滚动时保持可见的数据。
###  **Aspose.Cells & 冻结窗格**
Aspose.Cells 还允许开发人员在运行时将冻结窗格应用于工作表。 Aspose.Cells 提供类[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)代表 Microsoft Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)允许访问 Excel 文件中的每个工作表的集合。

工作表由以下形式表示[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了多种管理工作表的方法。要配置冻结窗格，请调用[冻结窗格](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)的方法[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[冻结窗格](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)方法采用以下参数：

- *行**，冻结开始的单元格的行索引。
- *列**，冻结开始的单元格的列索引。
- *冻结行**，顶部窗格中可见的行数。
- *冻结列**，左窗格中可见列的数量

下面给出了一个完整的示例，展示了如何使用[冻结窗格](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/)方法冻结Excel文件第一个工作表的行和列（从C4开始，用第4行第3列表示，其中行和列从0索引开始）。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
##  **分割窗格**
如果您需要拆分屏幕以在同一工作表中获得两个不同的视图，请拆分窗格。 Microsoft Excel 提供了一项非常方便的功能，允许您查看工作表的多个副本，并且能够独立滚动浏览工作表的每个窗格：分割窗格。

窗格同时工作。如果您对其中一个进行更改，则该更改会同时出现在另一个中。 Aspose.Cells为用户提供了分割窗格功能。
###  **应用和删除分割窗格**
####  **分割窗格**
 Aspose.Cells 提供类[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)代表 Microsoft Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类提供了多种用于管理 Excel 文件的方法。要实现分割视图，请使用[分裂](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/)的方法[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。要删除分割窗格，请使用[删除分割](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)方法。

在示例中，我们使用加载的简单模板文件，然后将设置的拆分窗格功能应用于第一个工作表中的单元格。更新的文件已保存。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
####  **移除窗格**
使用删除分割窗格[删除分割](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/)方法。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
