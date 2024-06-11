---
title: 数据透视表问题
type: docs
weight: 50
url: /zh/net/pivot-table-issue/
---

## **症状**
"我尝试从 IE 的 "打开" 按钮打开生成的 Excel 文件。这个 Excel 文件是通过读取一个 Excel 模板生成的。当我点击打开按钮时，它会打开并同时弹出一个错误消息，说"无法打开数据透视表源文件..."。

但是当我使用 "保存" 按钮保存生成的 Excel 文件，并从保存路径中打开它时，它会正常打开，没有任何错误。
### **Solution**
Aspose.Cells 在工作簿打开到 MS Excel 时设置了数据透视表数据格式，并强制 MS Excel 基于数据源创建数据透视表报告和其他计算任务。因此，应该使用 **SaveType.OpenInBrowser** 而不是使用 **SaveType.OpenInExcel**。其中的一个原因是，当你使用 OpenInExcel 选项将在运行时使用 "打开" 按钮从下载对话框框中保存的输出文件保存到 MS Excel 时，MS Excel 无法解析工作簿数据以生成数据透视表报告。这是由文件名问题造成的，这是 IE 的例行工作，因为它会添加类似 "[1]" 的东西来将其作为 "fileName"+ "[1]"+ ".xls" 添加到原始名称中，因此与 Aspose.Cells 无关。(也就是说...它总是添加 "[1]" 来将 "fileName"+ "[1]"+ ".xls" 添加到文件名中，而不是像 fileName.xls 这样）。简而言之，如果文件包含数据透视表，则无法使用 OpenInExcel SaveType 选项打开它，这将适用于创建文件或使用任何模板文件以创建数据透视表报告的情况。所以，如果文件中包含数据透视表数据，应该使用 OpenInBrowser SaveType 选项创建数据透视表报告。

如果你正在使用 Workbook.Save() 方法，应该更改你的代码并更新为 SaveType.OpenInBrowser

或者如果你的代码中使用了 "attachment" 选项，应该编辑你的代码来使用 "inline"。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
