---
title: 数据透视表问题
type: docs
weight: 50
url: /zh/net/pivot-table-issue/
---
## **症状**
“我试图从 IE 的“打开”按钮打开生成的 excel 文件。excel 是通过读取 excel 模板生成的。当我单击“打开”按钮时，它正在打开，同时弹出一个错误消息说“无法打开数据透视表源文件......”。

但是当我使用“保存”按钮保存生成的 excel 文件并从保存路径的文件中打开它时，它可以正确打开而没有任何错误。 “
### **解决方案**
Aspose.Cells 设置数据透视表格式并强制 MS Excel 在工作簿打开到 MS Excel 时根据数据源创建数据透视表报告和其他计算任务。所以应该使用**保存类型.OpenInBrowser**而不是使用**保存类型.OpenInExcel**.众多原因之一是当您使用 OpenInExcel 选项并在运行时使用下载对话框的“打开”按钮将生成的输出文件保存到 MS Excel 中时，MS Excel 无法解析工作簿数据以生成数据透视表报告。这是文件名的问题，IE的套路是在原文件名后加“[1]”，变成“文件名”+“[1]”+“.xls”，无所谓处理 Aspose.Cells。（即......它总是添加“[1]”来制作“fileName”+“[1]”+“.xls”而不是像 fileName.xls）。简而言之，如果文件包含数据透视表，则无法使用 OpenInExcel SaveType 选项打开它，这将适用于两者，即，如果您从头开始创建文件或使用任何源数据模板文件来创建数据透视表报告。因此，如果文件中包含数据透视表数据，您应该使用 OpenInBrowser SaveType 选项来创建数据透视表报告。

如果您使用的是 Workbook.Save() 方法，则应更改代码并更新为 SaveType.OpenInBrowser

或者，如果您在代码中使用“附件”选项，则编辑您的代码以使用“内联”。 IE



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
