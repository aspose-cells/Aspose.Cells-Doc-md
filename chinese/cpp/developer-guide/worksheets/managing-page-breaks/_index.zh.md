---
title: 管理分页符
type: docs
weight: 30
url: /zh/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

根据定义，分页符是文本流中一页结束、下一页开始的位置。 Microsoft Excel 允许用户将分页符添加到工作表的任何选定单元格中。

添加分页符的单元格位置、页面结束以及分页符后的所有其余数据在打印时打印在下一页上。简而言之，分页符根据您的规格将您的工作表分成多个页面。您还可以使用 Aspose.Cells 在运行时向工作表添加分页符。Aspose.Cells 允许开发人员添加两种分页符：

- 水平分页符
- 垂直分页符

在剩下的讨论中，我们将描述如何使用 Aspose.Cells 在工作表中添加水平或垂直分页符。

{{% /alert %}} 
##  **分页符**
 Aspose.Cells 提供类[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook)代表一个 Excel 文件。这[练习册](https://reference.aspose.com/cells/cpp/aspose.cells/workbook)类包含一个[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection)允许访问 Excel 文件中的每个工作表的集合。

工作表由以下形式表示[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。这[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了多种用于管理工作表的方法。要添加分页符，请使用[添加分页符](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks)的方法[工作表](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)班级。
###  **添加分页符**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
