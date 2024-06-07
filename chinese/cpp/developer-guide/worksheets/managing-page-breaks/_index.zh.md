---
title: 管理分页
type: docs
weight: 30
url: /zh/cpp/managing-page-breaks/
---

{{% alert color="primary" %}} 

根据定义，分页是文本流中一个页面结束并另一个页面开始的地方。Microsoft Excel允许用户将分页符添加到工作表的任何选定单元格中。

添加分页符的单元格位置，页面结束并在分页符后的所有数据打印在下一页打印。简单来说，分页符根据您的规格将您的工作表划分为多个页面。您也可以使用Aspose.Cells在运行时向工作表添加分页符。Aspose.Cells允许开发人员添加两种分页符：

- 水平分页
- 垂直分页

在下面的讨论中，我们将描述如何使用Aspose.Cells将水平或垂直分页符添加到工作表中。

{{% /alert %}} 
## **分页符**
Aspose.Cells提供了一个代表Excel文件的[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook)类。[Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook)类包含一个[Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection)集合，允许访问Excel文件中的每个工作表。

一个工作表由[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了许多用于管理工作表的方法。要添加分页符，请使用工作表类的[AddPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks)方法。
### **添加分页符**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
