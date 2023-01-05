---
title: HTTP 压缩
type: docs
weight: 10
url: /zh/net/http-compression/
---
## **HTTP压缩问题**
一些用户报告说，如果他们在 IIS 中配置 HTTP 压缩，他们会在将生成的文件发送到客户端浏览器时发现错误。
### **解释**
我们用**"Content-disposition", "inline; filename=test.xls"**标头强制浏览器打开文件和**"Content-disposition", "attachment; filename=test.xls"**标题强制浏览器打开**另存为**对话框并使用 Microsoft Excel 打开文件。但是，确实存在一些例外情况。
### **例外情况**
您可以使用以下代码来验证它不是 Aspose 的错误。

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **解决方案**
您可以使用以下解决方法之一来解决此问题：

- 将那些指定的 ASP.NET 文件（其中包含调用 Aspose.Cells 的代码）移动到另一个未压缩的文件夹。
- 为动态内容禁用 HTTP 压缩。
- 将生成的文件保存在您的服务器中，并向您的用户提供一个链接。

如果您确实希望使用 HTTP 压缩，请始终使用*打开Excel*选项而不是*在浏览器中打开*当您知道您已启用 IIS 压缩时的选项。
