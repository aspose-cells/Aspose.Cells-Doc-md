---
title: HTTP压缩
type: docs
weight: 10
url: /zh/net/http-compression/
---

## **HTTP压缩问题**
一些用户报告说，如果他们在IIS中配置了HTTP压缩，他们在将生成的文件发送到客户端浏览器时会遇到错误。
### **解释**
我们使用**"Content-disposition", "inline; filename=test.xls"**标题强制浏览器打开文件，并使用**"Content-disposition", "attachment; filename=test.xls"**标题强制浏览器打开**另存为**对话框，并使用Microsoft Excel打开文件。然而，确实存在一些例外情况。
### **例外情况**
你可以使用以下代码来验证这是否是Aspose的错误。

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **解决方案**
你可以使用以下其中一个变通方法来解决这个问题：

- 将指定的 ASP.NET 文件（包含调用Aspose.Cells的代码）移动到另一个未压缩的文件夹中。
- 为动态内容禁用HTTP压缩。
- 在服务器上保存生成的文件，并向用户提供一个链接。

如果您希望使用HTTP压缩，请在启用IIS压缩后，当您知道已启用IIS压缩时，请始终使用 *OpenInExcel* 选项而不是 *OpenInBrowser* 选项。
{{< app/cells/assistant language="csharp" >}}
