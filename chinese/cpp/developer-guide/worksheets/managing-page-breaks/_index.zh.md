---
title: 管理分页
type: docs
weight: 30
url: /zh/cpp/managing-page-breaks/
---

{{% alert color="primary" %}} 

根据定义，分页是文本流中一页结束并另一页开始的地方。 Microsoft Excel允许用户在工作表的任何选定单元格中添加分页。 

添加分页已结束并页设置断然后一页其余数据打印在下一页打印期间添加,简单来说,分页根据你的规格将你的工作表分成多页。 您还可以在运行时使用Aspose.Cells向工作表添加分页。 Aspose.Cells 允许开发人员添加两种分页:

- 水平分页
- 垂直分页

在接下来的讨论中，我们将描述如何使用Aspose.Cells向工作表添加水平或垂直分页。

{{% /alert %}} 
## **分页**
Aspose.Cells 提供一个代表Excel文件的类 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook)。 [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook) 类包含 [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection) 集合，允许访问Excel文件中的每个工作表。

工作表由 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类表示。 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类提供了广泛的方法来管理工作表。 要添加页符，请使用 [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 类的 [AddPageBreaks](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/addpagebreaks) 方法。
### **添加分页**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
