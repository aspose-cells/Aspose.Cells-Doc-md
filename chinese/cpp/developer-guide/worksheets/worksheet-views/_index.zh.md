---
title: 工作表视图
type: docs
weight: 40
url: /zh/cpp/worksheet-views/
---
## **分页预览**
所有工作表都可以在两种模式下查看：

- 正常视图。
- 分页预览。

普通视图是工作表的默认视图。分页预览是一种编辑视图，显示将要打印的工作表。分页预览显示每页上将显示哪些数据，因此您可以调整打印区域和分页。使用 Aspose.Cells 开发人员可以启用普通视图或分页预览模式。
### **控制视图模式**
 Aspose.Cells提供类[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类包含一个[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)允许访问 Excel 文件中每个工作表的集合。

工作表由[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。这[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类提供了多种管理工作表的方法。要启用普通或分页预览模式，请使用[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)的方法[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)返回一个布尔值，这意味着它只能存储一个**真的**要么**错误的**价值。
#### **启用普通视图**
通过将工作表设置为普通视图[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)的方法[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类**错误的**.
#### **启用分页预览**
通过设置任何工作表以分页预览[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)的方法[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类**真的**.这样做会将工作表从普通视图切换到分页预览。

下面给出了一个完整的示例，演示了如何使用[IsPageBreakPreview](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#aa1af81cfb7635232c7f839192b442892)为 Excel 文件的第一个工作表启用分页预览模式的方法。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview.cpp" >}}
## **缩放系数**
### **使用 Microsoft Excel**
Microsoft Excel 提供了一项功能，允许用户设置工作表的缩放或比例因子。此功能可帮助用户以较小或较大的视图查看工作表内容。用户可以将缩放因子设置为任意值。
### **Aspose.Cells & 缩放系数**
Aspose.Cells 还允许开发人员设置工作表缩放系数。 Aspose.Cells提供类[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类包含一个[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)允许访问 Excel 文件中每个工作表的集合。

工作表由[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。这[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类提供了多种管理工作表的方法。要设置工作表的缩放系数，请使用[飞涨](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)的方法[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类 缩放因子是通过将数字（整数）值分配给[飞涨](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)方法。

下面给出了一个完整的示例，演示了如何使用[飞涨](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ad94669a93a4324b3a4b7f9582df5b0ec)设置Excel文件第一个工作表缩放比例的方法。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor.cpp" >}}
## **冻结窗格**
### **使用 Microsoft Excel**
冻结窗格是 Microsoft Excel 提供的一项功能。冻结窗格允许您选择在工作表中滚动时保持可见的数据。
### **Aspose.Cells & 冻结窗格**
Aspose.Cells 还允许开发人员在运行时将冻结窗格应用于工作表。 Aspose.Cells提供类[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类包含一个[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)允许访问 Excel 文件中每个工作表的集合。

工作表由[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。这[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)类提供了多种管理工作表的方法。要配置冻结窗格，请调用[冻结窗格](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)的方法[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。这[冻结窗格](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)方法采用以下参数：

- **排**，冻结将从其开始的单元格的行索引。
- **柱子**，冻结将从其开始的单元格的列索引。
- **冻结行**，顶部窗格中可见行的数量。
- **冻结列**左窗格中可见列的数量

下面给出了一个完整的示例，说明如何使用[冻结窗格](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#ac4f68dfe9ac219fb8de6d6824ec1aa22)冻结Excel文件第一个工作表的行和列（从C4开始，用第4行第3列表示，其中行和列从0索引开始）的方法。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes.cpp" >}}
## **拆分窗格**
如果您需要拆分屏幕以在同一工作表中获得两个不同的视图，请拆分窗格。 Microsoft Excel 提供了一项非常方便的功能，允许您查看工作表的多个副本，并且能够独立滚动浏览工作表的每个窗格：拆分窗格。

窗格同时工作。如果您对一个进行更改，则更改会同时出现在另一个中。 Aspose.Cells 为用户提供分割窗格功能。
### **应用和删除拆分窗格**
#### **拆分窗格**
 Aspose.Cells提供类[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)表示 Microsoft Excel 文件。这[工作簿](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)类提供了多种管理 Excel 文件的方法。要实现拆分视图，请使用[分裂](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a0e581a3a9528a767c57008521ee02b6f)的方法[工作表](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)班级。要删除拆分窗格，请使用[删除拆分](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)方法。

在示例中，我们使用加载的简单模板文件，然后将设置拆分窗格功能应用于第一个工作表中的单元格。更新的文件被保存。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes.cpp" >}}
#### **删除窗格**
使用删除拆分窗格[删除拆分](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5b554108c91f686e906400c26248eee5)方法。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes.cpp" >}}
