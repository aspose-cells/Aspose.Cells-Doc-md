---
title: 管理分页
type: docs
weight: 30
url: /zh/go-cpp/managing-page-breaks/
---

{{% alert color="primary" %}}

根据定义，分页是文本流中一页结束并另一页开始的地方。 Microsoft Excel允许用户在工作表的任何选定单元格中添加分页。 

添加分页已结束并页设置断然后一页其余数据打印在下一页打印期间添加,简单来说,分页根据你的规格将你的工作表分成多页。 您还可以在运行时使用Aspose.Cells向工作表添加分页。 Aspose.Cells 允许开发人员添加两种分页:

- 水平分页
- 垂直分页

在接下来的讨论中，我们将描述如何使用Aspose.Cells向工作表添加水平或垂直分页。

{{% /alert %}}

## **分页**

Aspose.Cells 提供了代表Excel文件的 [Workbook](https://reference.aspose.com/cells/go-cpp/workbook) 类。该类包含一个 [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection) 集合，允许访问Excel文件中的每个工作表。

工作表由 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) 类表示。该类提供了用于管理工作表的广泛方法。要添加分页符，可使用 [AddPageBreaks](https://reference.aspose.com/cells/go-cpp/worksheet/addpagebreaks) 方法。

### **添加分页**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingPageBreaks.go" >}}
