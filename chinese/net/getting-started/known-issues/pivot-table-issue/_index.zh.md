---
title: 数据透视表问题
type: docs
weight: 50
url: /zh/net/pivot-table-issue/
---

## **症状**
"我尝试通过IE的“打开”按钮打开生成的Excel文件。Excel是通过读取Excel模板生成的。当我点击打开按钮时，它会打开，同时还会弹出一个错误消息，说"无法打开数据透视表源文件......"。

但是，当我使用“保存”按钮保存生成的Excel文件，并从保存路径中打开文件时，它会正确打开，没有任何错误。"
### **解决方案**
Aspose.Cells设置了数据透视表数据格式，并在工作簿在MS Excel中打开时，强制MS Excel根据数据源创建数据透视表报告和其他计算任务。因此，应该使用**SaveType.OpenInBrowser**而不是**SaveType.OpenInExcel**。其中的一个原因是当您在运行时使用“打开”对话框的按钮将输出生成的文件保存到MS Excel中时使用OpenInExcel选项，MS Excel无法解析工作簿数据以生成数据透视表报告。这是由于文件名问题造成的，这是IE的例行操作，因为它会附加类似于"[1]"的内容以将原始名称变为"文件名"+"[1]"+ ".xls"，因此与Aspose.Cells无关。(即...它总是添加"[1]"以形成"文件名"+"[1]"+ "。xls"而不是像fileName.xls那样)。简而言之，如果文件包含数据透视表，那么无法使用OpenInExcel SaveType选项打开文件，这将适用于两种情况，即如果您从头开始创建文件或者使用任何模板文件来创建数据透视表报告的源数据。因此，如果文件中包含数据透视表数据，则应使用OpenInBrowser SaveType选项来创建数据透视表报告。

如果您使用Workbook.Save()方法，请更改您的代码并更新为SaveType.OpenInBrowser

或者如果您的代码中使用了"attachment"选项，请编辑您的代码以使用"inline"。即，



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
