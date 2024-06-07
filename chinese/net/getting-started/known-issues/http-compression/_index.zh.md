---
title: HTTP 压缩
type: docs
weight: 10
url: /zh/net/http-compression/
---

## **HTTP 压缩问题**
一些用户报告说，如果他们在 IIS 中配置了 HTTP 压缩，当将生成的文件发送给客户端浏览器时，会发现错误。
### **解释**
我们使用 **“Content-disposition”, “inline; filename=test.xls”** 头部来强制浏览器打开文件，使用 **“Content-disposition”, “attachment; filename=test.xls”** 头部来强制浏览器打开“另存为”对话框，并使用 Microsoft Excel 打开文件。但确实存在一些异常情况。
### **异常**
您可以使用以下代码来验证这不是 Aspose 的 bug。

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **解决方案**
您可以使用以下其中一个解决方法解决这个问题:

- 将那些包含调用 Aspose.Cells 代码的指定 ASP.NET 文件移动到另一个未压缩的文件夹。
- 为动态内容禁用 HTTP 压缩。
- 将生成的文件保存在服务器上，并向用户提供一个链接。

如果您希望使用 HTTP 压缩，请在启用了 IIS 压缩并且您知道已启用 IIS 压缩时，始终使用“OpenInExcel”选项，而不是“OpenInBrowser”选项。
